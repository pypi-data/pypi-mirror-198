import importlib.resources as pkg_resources
import re
from typing import Optional

import click
import hcl2

import sym.flow.cli.helpers.output as cli_output
from sym.flow.cli.code_generation_templates import (  # import the *package* containing the tf files
    core,
    flows,
)
from sym.flow.cli.helpers.config import Config

from .core import FlowGeneration


class AWSIAMFlowGeneration(FlowGeneration):
    REQUIRES_AWS: bool = True

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.role_name: str = ""

        while not self.role_name:
            role_name = click.prompt(
                click.style("\nWhat is the AWS managed role you would like to provision?", bold=True),
                type=str,
                default="PowerUserAccess",
                prompt_suffix=click.style(
                    "\nYou can specify any AWS Managed Policy, but we’d suggest starting with one of the job "
                    "function-aligned policies listed at "
                    "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html",
                    fg="cyan",
                ),
            )
            if not self.is_valid_AWS_role_name(role_name):
                cli_output.warn(
                    f"The role name must only contain letters, numbers, or underscores, and must "
                    f"start with a capital letter. For example, AmazonElasticMapReduceforEC2Role"
                )
            else:
                self.role_name = role_name

        self.aws_region: Optional[str] = self._get_aws_region()

    @property
    def impl_filepath(self):
        return f"{self.working_directory}/impls/aws_iam_{self.flow_resource_name}_impl.py"

    @classmethod
    def get_flow_tf_filepath(cls, flow_name: str, working_directory: str = ".") -> str:
        return f"{working_directory}/aws_iam_{cls._get_flow_resource_name(flow_name)}.tf"

    def is_valid_AWS_role_name(self, string):
        # Matches PascalCase, plus underscores b/c of AWS role naming
        return bool(re.match(r"([A-Z]+[a-z0-9_]+)+", string))

    def generate(self) -> None:
        """Generate the impl and Terraform files required to configure an AWS IAM Flow."""
        # Generate any core requirements that don't already exist in this directory.
        self._generate_runtime_tf()
        self._create_impls_directory()

        # Parse the environment.tf file to see if we need to append a sym_runtime
        with open(self.environment_tf_filepath, "r") as f:
            environment_tf = hcl2.load(f)
            resources = environment_tf.get("resource", [])

            sym_environment = next((r["sym_environment"] for r in resources if r.get("sym_environment")), None)

            if not sym_environment:
                cli_output.fail(
                    "The sym_environment resource is missing in environment.tf",
                    hint=None,  # TODO(SYM-4669) Add docs for manual configuration
                )

            # Parse `locals` block to get environment_name
            local_tf_vars = environment_tf.get("locals", [{}])
            environment_name = local_tf_vars[0].get("environment_name")
            if not environment_name:
                cli_output.fail(
                    "The environment_name local variable is missing in environment.tf",
                    hint=None,
                )
            # Parse integrations to get slack integration workspace ID
            slack_integration = next(
                (r["sym_integration"].get("slack") for r in resources if r.get("sym_integration")), None
            )
            if not slack_integration:
                cli_output.fail(
                    'The sym_integration resource of type "slack" is missing in environment.tf',
                    hint=None,
                )
            slack_workspace_id = slack_integration["external_id"]
            # Parse sym_error_logger to get the destination
            slack_error_logger = next(
                (r["sym_error_logger"].get("slack") for r in resources if r.get("sym_error_logger")), None
            )
            if not slack_error_logger:
                error_logger_destination = "#sym-errors"
            else:
                error_logger_destination = slack_error_logger["destination"]

        if "this" not in sym_environment:
            cli_output.fail(
                "Could not locate the 'sym_environment.this' resource in environment.tf",
                hint=None,
            )

        if "runtime_id" not in sym_environment["this"]:
            # Add a sym_runtime resource
            self._append_sym_runtime(environment_name)

            # Add the runtime_id to the sym_environment
            with open(self.environment_tf_filepath, "w") as f:
                # replace `environment.tf` with `environment_with_runtime.tf`, which contains runtime_id line
                new_env = pkg_resources.read_text(core, "environment_with_runtime.tf")
                # Fill in all the `SYM_TEMPLATE_VAR_*` with values pulled from parsed sym_environment
                new_env = new_env.replace("SYM_TEMPLATE_VAR_ENVIRONMENT_NAME", environment_name)
                new_env = new_env.replace("SYM_TEMPLATE_VAR_SYM_ORG_SLUG", Config.get_org().slug)
                new_env = new_env.replace("SYM_TEMPLATE_VAR_SLACK_WORKSPACE_ID", slack_workspace_id)
                new_env = new_env.replace("SYM_TEMPLATE_VAR_ERROR_LOGGER_DESTINATION_ID", error_logger_destination)
                new_env = new_env.replace("SYM_TEMPLATE_VAR_SYMFLOW_VERSION", self.symflow_version)
                new_env = new_env.replace(
                    "SYM_TEMPLATE_VAR_GENERATION_TIME", self.generation_time.strftime("%Y-%m-%d at %H:%M")
                )
                f.write(new_env)

        # Generate the AWS IAM specific files.
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
            aws_iam_tf = pkg_resources.read_text(flows, "aws_iam.tf")
            aws_iam_tf = aws_iam_tf.replace("SYM_TEMPLATE_VAR_SYMFLOW_VERSION", self.symflow_version)
            aws_iam_tf = aws_iam_tf.replace(
                "SYM_TEMPLATE_VAR_GENERATION_TIME", self.generation_time.strftime("%Y-%m-%d at %H:%M")
            )
            aws_iam_tf = aws_iam_tf.replace("SYM_TEMPLATE_VAR_FLOW_RESOURCE_NAME", self.flow_resource_name)
            aws_iam_tf = aws_iam_tf.replace("SYM_TEMPLATE_VAR_FLOW_NAME", self.flow_name)
            role_arn = f"arn:aws:iam::aws:policy/{self.role_name}"
            aws_iam_tf = aws_iam_tf.replace("SYM_TEMPLATE_VAR_IAM_ROLE_NAME", self.role_name)
            aws_iam_tf = aws_iam_tf.replace("SYM_TEMPLATE_VAR_IAM_ROLE_ARN", role_arn)
            f.write(aws_iam_tf)

    def _append_sym_runtime(self, environment_name):
        """Parses the runtime.tf file and adds a sym_runtime resource to the end if it does not yet exist."""
        sym_runtime = (
            f'\n\nresource "sym_runtime" "{environment_name}" {{\n'
            f'  name = "{environment_name}"\n\n'
            "  # This tells the Sym Runtime to assume the IAM Role declared in runtime.tf\n"
            "  # when executing AWS-related Access Strategies. It will be passed into the sym_environment\n"
            "  # declared in the environment.tf file.\n"
            "  context_id = sym_integration.runtime_context.id\n"
            "}"
        )

        # Open the file in Read + Append mode
        with open(self.runtime_tf_filepath, "a+") as f:
            # Parse the existing runtime.tf file into a dict
            runtime_tf = hcl2.load(f)

            # Check to see if a sym_runtime resource is already defined
            resources = runtime_tf.get("resource", [])
            existing_sym_runtime = any((r for r in resources if r.get("sym_runtime")))

            if not existing_sym_runtime:
                # Append a sym_runtime resource
                f.write(sym_runtime)
