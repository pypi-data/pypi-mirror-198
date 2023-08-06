import terrascript.core as core


@core.resource(type="aws_ssm_patch_group", namespace="aws_ssm")
class PatchGroup(core.Resource):

    baseline_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
