import terrascript.core as core


@core.resource(type="aws_ce_cost_allocation_tag", namespace="ce")
class CostAllocationTag(core.Resource):
    """
    The key for the cost allocation tag.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The status of a cost allocation tag. Valid values are `Active` and `Inactive`.
    """
    status: str | core.StringOut = core.attr(str)

    """
    (Required) The key for the cost allocation tag.
    """
    tag_key: str | core.StringOut = core.attr(str)

    """
    The type of cost allocation tag.
    """
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
