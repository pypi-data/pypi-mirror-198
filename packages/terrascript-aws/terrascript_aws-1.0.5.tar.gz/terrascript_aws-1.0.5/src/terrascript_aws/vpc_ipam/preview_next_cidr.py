import terrascript.core as core


@core.resource(type="aws_vpc_ipam_preview_next_cidr", namespace="vpc_ipam")
class PreviewNextCidr(core.Resource):
    """
    The previewed CIDR from the pool.
    """

    cidr: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Exclude a particular CIDR range from being returned by the pool.
    """
    disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The ID of the preview.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the pool to which you want to assign a CIDR.
    """
    ipam_pool_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The netmask length of the CIDR you would like to preview from the IPAM pool.
    """
    netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        ipam_pool_id: str | core.StringOut,
        disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = None,
        netmask_length: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PreviewNextCidr.Args(
                ipam_pool_id=ipam_pool_id,
                disallowed_cidrs=disallowed_cidrs,
                netmask_length=netmask_length,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipam_pool_id: str | core.StringOut = core.arg()

        netmask_length: int | core.IntOut | None = core.arg(default=None)
