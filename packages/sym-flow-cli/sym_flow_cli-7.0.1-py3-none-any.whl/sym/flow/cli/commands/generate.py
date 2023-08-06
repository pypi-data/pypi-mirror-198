from pathlib import Path
from typing import Optional

import click

import sym.flow.cli.helpers.output as cli_output
from sym.flow.cli.errors import NotLoggedInError
from sym.flow.cli.helpers.code_generation.approval_only import ApprovalFlowGeneration
from sym.flow.cli.helpers.code_generation.core import get_valid_slug
from sym.flow.cli.helpers.code_generation.okta import OktaFlowGeneration
from sym.flow.cli.helpers.config import Config
from sym.flow.cli.helpers.global_options import GlobalOptions
from sym.flow.cli.helpers.tracked_command import TrackedCommand
from sym.flow.cli.helpers.utils import get_or_prompt

FLOW_TYPE_OPTIONS = ["okta", "approval-only"]


@click.command(cls=TrackedCommand, short_help="Generate Terraform to configure a Sym Flow.")
@click.make_pass_decorator(GlobalOptions, ensure=True)
@click.option(
    "--type",
    "type_",
    type=click.Choice(FLOW_TYPE_OPTIONS, case_sensitive=False),
    help="What type of Sym Flow to create.",
)
@click.option(
    "--flow-name",
    help="A unique name for this Sym Flow.",
)
def generate(options: GlobalOptions, type_: str, flow_name: Optional[str] = None) -> None:
    """Generates all Terraform required to configure a Sym Flow.

    This command should be run inside the directory created by `symflow init`.
    """
    if not Config.is_logged_in() or not Config.get_org():
        raise NotLoggedInError()

    # If environment.tf and versions.tf are not both present, we can relatively safely assume that
    # the user isn't inside a directory created by `symflow init` because it would have generated them.
    if not Path("./environment.tf").is_file() or not Path("./versions.tf").is_file():
        cli_output.fail(
            "This command must be run inside a directory created by `symflow init`. Please run that command first.",
            hint="Hint: The current directory must have `environment.tf` and `versions.tf` files.",
        )

    cli_output.info(
        "\nWelcome to Sym! This command will generate new files in the current directory required to configure a Sym Flow.\n",
    )

    # Prompt for any values that weren't already passed in.
    type_ = get_or_prompt(
        type_,
        click.style("Please select the type of Flow you would like to create", bold=True),
        FLOW_TYPE_OPTIONS,
    )

    # If the user used --flow-name to pass in a name, we need to do the same validation we'd do
    # if we were prompting for it.
    if flow_name:
        # This may set the flow_name back to None, if we need to re-prompt.
        flow_name = get_valid_slug(label="Flow name", slug_candidate=flow_name)

    while not flow_name:
        flow_name_candidate = click.prompt(
            f"{click.style('What would you like to name this Flow?', bold=True)} {click.style('This name should be unique', dim=True, italic=True)}",
            type=str,
        )

        flow_name = get_valid_slug(label="Flow name", slug_candidate=flow_name_candidate)

    cli_output.info(f'\nGenerating a Sym Flow of type "{type_}" named "{flow_name}"...\n')

    if type_ == "okta":
        generator = OktaFlowGeneration(flow_name=flow_name)
    elif type_ == "approval-only":
        generator = ApprovalFlowGeneration(flow_name=flow_name)
    else:
        # This should never happen, because the user chooses from a given list.
        # If we get here, we've done something wrong.
        cli_output.fail(
            f'Unknown Flow type: "{type_}". Please use `symflow generate --help` to see the list of available Flow types.'
        )

    generator.generate()

    cli_output.info(
        f"\nSuccessfully generated your Terraform configuration! Run the following to check the configuration:"
    )
    cli_output.actionable(f"terraform init && terraform plan")
    cli_output.info("\nWhen you are ready to apply your configuration, run the following:")
    cli_output.actionable("terraform apply")

    generator.final_instructions()
