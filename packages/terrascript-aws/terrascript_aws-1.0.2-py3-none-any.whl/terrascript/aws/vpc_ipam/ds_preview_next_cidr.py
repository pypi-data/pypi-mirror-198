import terrascript.core as core


@core.data(type="aws_vpc_ipam_preview_next_cidr", namespace="aws_vpc_ipam")
class DsPreviewNextCidr(core.Data):

    cidr: str | core.StringOut = core.attr(str, computed=True)

    disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    ipam_pool_id: str | core.StringOut = core.attr(str)

    netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        ipam_pool_id: str | core.StringOut,
        disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = None,
        netmask_length: int | core.IntOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPreviewNextCidr.Args(
                ipam_pool_id=ipam_pool_id,
                disallowed_cidrs=disallowed_cidrs,
                netmask_length=netmask_length,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipam_pool_id: str | core.StringOut = core.arg()

        netmask_length: int | core.IntOut | None = core.arg(default=None)
