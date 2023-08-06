import terrascript.core as core


@core.resource(type="aws_ce_cost_allocation_tag", namespace="aws_ce")
class CostAllocationTag(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str)

    tag_key: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        status: str | core.StringOut,
        tag_key: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CostAllocationTag.Args(
                status=status,
                tag_key=tag_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        status: str | core.StringOut = core.arg()

        tag_key: str | core.StringOut = core.arg()
