import terrascript.core as core


@core.data(type="aws_outposts_outposts", namespace="aws_outposts")
class DsOutposts(core.Data):

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    availability_zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    site_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        availability_zone: str | core.StringOut | None = None,
        availability_zone_id: str | core.StringOut | None = None,
        owner_id: str | core.StringOut | None = None,
        site_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOutposts.Args(
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                owner_id=owner_id,
                site_id=site_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        availability_zone_id: str | core.StringOut | None = core.arg(default=None)

        owner_id: str | core.StringOut | None = core.arg(default=None)

        site_id: str | core.StringOut | None = core.arg(default=None)
