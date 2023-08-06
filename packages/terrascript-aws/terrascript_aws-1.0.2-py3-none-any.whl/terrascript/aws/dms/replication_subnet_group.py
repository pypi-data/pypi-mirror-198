import terrascript.core as core


@core.resource(type="aws_dms_replication_subnet_group", namespace="aws_dms")
class ReplicationSubnetGroup(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    replication_subnet_group_arn: str | core.StringOut = core.attr(str, computed=True)

    replication_subnet_group_description: str | core.StringOut = core.attr(str)

    replication_subnet_group_id: str | core.StringOut = core.attr(str)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        replication_subnet_group_description: str | core.StringOut,
        replication_subnet_group_id: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationSubnetGroup.Args(
                replication_subnet_group_description=replication_subnet_group_description,
                replication_subnet_group_id=replication_subnet_group_id,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        replication_subnet_group_description: str | core.StringOut = core.arg()

        replication_subnet_group_id: str | core.StringOut = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
