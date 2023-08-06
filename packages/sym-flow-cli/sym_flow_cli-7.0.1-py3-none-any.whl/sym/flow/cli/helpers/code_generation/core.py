import importlib.resources as pkg_resources
import os
import re
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Optional

import click

import sym.flow.cli.helpers.output as cli_output
from sym.flow.cli.code_generation_templates import (  # import the *package* containing the tf files
    core,
)
from sym.flow.cli.errors import CliError
from sym.flow.cli.helpers.version import get_current_version

# Slugs are only allowed to have letters, numbers, and dashes. This regex matches
# all character that are NOT those.
slug_disallowed_pattern = re.compile(r"[^a-zA-Z\d-]+")


class CodeGenerationError(CliError):
    """Generic class for code generation errors."""


class MissingConfig(CodeGenerationError):
    def __init__(self, file_name: str, name: str) -> None:
        super().__init__(f"Could not generate {file_name}. A value for {name} is required, but was not given.")


class FlowGeneration(ABC):
    """Core logic for generating Flow configuration with `symflow generate`."""

    def __init__(self, flow_name: str) -> None:
        self.flow_name = flow_name
        self.generation_time = datetime.utcnow()
        self.symflow_version = str(get_current_version())

        # Subclasses will choose whether they need runtime.tf or not, so we may
        # not need aws_region. Set to None here so it's never undefined.
        self.aws_region: Optional[str] = None

    @property
    def flow_resource_name(self) -> str:
        """The name of the Flow used as a slug may have dashes, but used as a
        file name or Terraform resource should have underscores.
        """
        return self.flow_name.replace("-", "_").lower()

    @property
    def working_directory(self):
        return "."

    @abstractmethod
    def generate(self) -> None:
        """Generate all files required to configure this particular type of
        Flow.
        """

    def final_instructions(self) -> None:
        """Optionally output instructions after code generation is complete for
        for the user to follow now or after `terraform apply` (e.g. instructions
        on how to set the value for a new AWS Secretsmanager Secret).
        """

    def _get_aws_region(self) -> Optional[str]:
        """If a runtime.tf file would need to be generated, prompt the user for
        the AWS region to use.
        """

        if not Path("./runtime.tf").is_file():
            return click.prompt(
                click.style("What AWS region are your resources in?", bold=True), type=str, default="us-east-1"
            )

    def _generate_runtime_tf(self) -> None:
        """Generate runtime.tf if it does not already exist."""

        if not Path("./runtime.tf").is_file():
            if not self.aws_region:
                raise MissingConfig(file_name="runtime.tf", name="aws_region")

            runtime_tf = pkg_resources.read_text(core, "runtime.tf")

            with open("./runtime.tf", "w") as f:
                runtime_tf = runtime_tf.replace("SYM_TEMPLATE_VAR_SYMFLOW_VERSION", self.symflow_version)
                runtime_tf = runtime_tf.replace(
                    "SYM_TEMPLATE_VAR_GENERATION_TIME", self.generation_time.strftime("%Y-%m-%d %H:%M")
                )
                runtime_tf = runtime_tf.replace("SYM_TEMPLATE_VAR_AWS_REGION", self.aws_region)
                f.write(runtime_tf)

    def _generate_secrets_tf(self) -> None:
        """Generate secrets.tf if it does not already exist."""

        if not Path("./secrets.tf").is_file():
            secrets_tf = pkg_resources.read_text(core, "secrets.tf")

            with open("./secrets.tf", "w") as f:
                secrets_tf = secrets_tf.replace("SYM_TEMPLATE_VAR_SYMFLOW_VERSION", self.symflow_version)
                secrets_tf = secrets_tf.replace(
                    "SYM_TEMPLATE_VAR_GENERATION_TIME", self.generation_time.strftime("%Y-%m-%d %H:%M")
                )
                f.write(secrets_tf)

    def _create_impls_directory(self) -> None:
        """Create the impls directory to contain all Flow impls if it does not
        already exist.
        """

        if not Path("./impls").is_dir():
            os.makedirs("impls")


def get_valid_slug(label: str, slug_candidate: str) -> Optional[str]:
    """Interactively validate that a given string could be used as a slug and/or as a Terraform
    resource name. Outputs an error mesasge to the command line if not.

    Args:
        label: How to refer to the value the `slug_candidate` will be used for.
        slug_candidate: The string to validate.

    Returns:
        The `slug_candidate` if it's valid or the user confirmed a valid suggestion.
        None otherwise.
    """

    # Look for any disallowed characters in the given slug_candidate.
    if slug_disallowed_pattern.search(slug_candidate):
        # Replace any disallowed characters with dashes and remove any from the start or end.
        formatted_slug_candidate = slug_disallowed_pattern.sub("-", slug_candidate).strip("-")

        # It's possible there was nothing valid to work with, in which case just reject the name outright.
        if not formatted_slug_candidate:
            return None

        # Give the user a chance to accept the newly formatted slug. If they accept, great. If not, return None
        # so we can prompt again for a totally new name.
        if click.confirm(
            click.style(
                f'{label} can only contain letters, numbers, and dashes. Use "{formatted_slug_candidate}" instead?',
                fg="red",
            )
        ):
            return formatted_slug_candidate

        # Trigger a re-prompt for the slug
        return None

    # The slug will often be used in combination with some other identifying text (e.g. "SLUG-okta-group").
    # Resources like Targets have a slug limit of 55 characters (and -okta-group is 11), so 32 should give us a
    # little bit of wiggle room.
    if len(slug_candidate) > 32:
        cli_output.error(f"{label} cannot be longer than 32 characters. Please enter a shorter name.")

        # Trigger a re-prompt for the Flow name
        return None

    return slug_candidate
