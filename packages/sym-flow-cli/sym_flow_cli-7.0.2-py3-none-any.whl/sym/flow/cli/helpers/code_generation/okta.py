import importlib.resources as pkg_resources
from typing import Optional

import click

import sym.flow.cli.helpers.output as cli_output
from sym.flow.cli.code_generation_templates import (  # import the *package* containing the tf files
    flows,
)

from .core import FlowGeneration


class OktaFlowGeneration(FlowGeneration):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.domain_name: str = click.prompt(
            click.style("What is your Okta domain?", bold=True), type=str, prompt_suffix=""
        )
        self.group_id: str = click.prompt(
            click.style("What is the Okta group ID you would like to manage with Sym?", bold=True),
            type=str,
            prompt_suffix="",
        )
        self.aws_region: Optional[str] = self._get_aws_region()

    @property
    def impl_filepath(self) -> str:
        return f"{self.working_directory}/impls/okta_{self.flow_resource_name}_impl.py"

    @property
    def flow_tf_filepath(self) -> str:
        return f"{self.working_directory}/okta_{self.flow_resource_name}.tf"

    def generate(self) -> None:
        """Generate the impl and Terraform files required to configure an Okta Flow."""
        # Generate any core requirements that don't already exist in this directory.
        self._generate_runtime_tf()
        self._generate_secrets_tf()
        self._create_impls_directory()

        # Generate the Okta-specific files.
        with open(self.impl_filepath, "w") as f:
            # Note: The impl file is stored as a `.txt` resource because PyOxidizer (the tool used to package symflow CLI)
            # Does NOT support reading `.py` files with `importlib.resources`
            # https://github.com/indygreg/PyOxidizer/issues/237
            #
            # However, we don't care about reading the source code, we simply need to pull the text file and write it
            # to the filesystem with a `.py` extension. As a workaround, we have stored `impl.py` as `impl.txt` in the
            # code_generation_templates.flows package so that we can read it with importlib.resources.
            impl_txt = pkg_resources.read_text(flows, "impl.txt")
            f.write(impl_txt)

        with open(self.flow_tf_filepath, "w") as f:
            okta_tf = pkg_resources.read_text(flows, "okta.tf")

            okta_tf = okta_tf.replace("SYM_TEMPLATE_VAR_SYMFLOW_VERSION", self.symflow_version)
            okta_tf = okta_tf.replace(
                "SYM_TEMPLATE_VAR_GENERATION_TIME", self.generation_time.strftime("%Y-%m-%d %H:%M")
            )
            okta_tf = okta_tf.replace("SYM_TEMPLATE_VAR_FLOW_RESOURCE_NAME", self.flow_resource_name)
            okta_tf = okta_tf.replace("SYM_TEMPLATE_VAR_FLOW_NAME", self.flow_name)
            okta_tf = okta_tf.replace("SYM_TEMPLATE_VAR_OKTA_DOMAIN", self.domain_name)
            okta_tf = okta_tf.replace("SYM_TEMPLATE_VAR_OKTA_GROUP_ID", self.group_id)
            f.write(okta_tf)

    def final_instructions(self) -> None:
        cli_output.info(
            "\nAfter running `terraform apply`, set your Okta API Key using the AWS CLI and the following command:"
        )
        cli_output.actionable(
            f'aws secretsmanager put-secret-value --secret-id "sym/{self.flow_name}/okta-api-key" --secret-string "YOUR-OKTA-API-KEY"'
        )
