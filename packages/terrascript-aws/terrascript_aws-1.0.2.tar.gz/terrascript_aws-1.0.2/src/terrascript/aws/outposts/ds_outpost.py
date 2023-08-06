import terrascript.core as core


@core.data(type="aws_outposts_outpost", namespace="aws_outposts")
class DsOutpost(core.Data):

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    owner_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    site_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        owner_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOutpost.Args(
                arn=arn,
                id=id,
                name=name,
                owner_id=owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        owner_id: str | core.StringOut | None = core.arg(default=None)
