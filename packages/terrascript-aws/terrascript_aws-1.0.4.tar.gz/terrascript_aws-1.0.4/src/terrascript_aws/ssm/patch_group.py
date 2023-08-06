import terrascript.core as core


@core.resource(type="aws_ssm_patch_group", namespace="ssm")
class PatchGroup(core.Resource):
    """
    (Required) The ID of the patch baseline to register the patch group with.
    """

    baseline_id: str | core.StringOut = core.attr(str)

    """
    The name of the patch group and ID of the patch baseline separated by a comma (`,`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the patch group that should be registered with the patch baseline.
    """
    patch_group: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        baseline_id: str | core.StringOut,
        patch_group: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PatchGroup.Args(
                baseline_id=baseline_id,
                patch_group=patch_group,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        baseline_id: str | core.StringOut = core.arg()

        patch_group: str | core.StringOut = core.arg()
