import importlib.resources as pkg_resources

from sym.flow.cli.code_generation_templates import (  # import the *package* containing the tf files
    flows,
)

from .core import FlowGeneration


class ApprovalFlowGeneration(FlowGeneration):
    @property
    def impl_filepath(self) -> str:
        return f"{self.working_directory}/impls/approval_{self.flow_resource_name}_impl.py"

    @classmethod
    def get_flow_tf_filepath(cls, flow_name: str, working_directory: str = ".") -> str:
        return f"{working_directory}/approval_{cls._get_flow_resource_name(flow_name)}.tf"

    def generate(self) -> None:
        """Generate the impl and Terraform files required to configure an Approval-Only Flow."""
        # Generate any core requirements that don't already exist in this directory.
        self._create_impls_directory()

        # Generate the Approval-Only-specific files.
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
            approval_tf = pkg_resources.read_text(flows, "approval_only.tf")

            approval_tf = approval_tf.replace("SYM_TEMPLATE_VAR_SYMFLOW_VERSION", self.symflow_version)
            approval_tf = approval_tf.replace(
                "SYM_TEMPLATE_VAR_GENERATION_TIME", self.generation_time.strftime("%Y-%m-%d %H:%M")
            )
            approval_tf = approval_tf.replace("SYM_TEMPLATE_VAR_FLOW_RESOURCE_NAME", self.flow_resource_name)
            approval_tf = approval_tf.replace("SYM_TEMPLATE_VAR_FLOW_NAME", self.flow_name)
            f.write(approval_tf)
