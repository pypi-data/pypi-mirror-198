import terrascript.core as core


@core.resource(type="aws_dynamodb_table_replica", namespace="aws_dynamodb")
class TableReplica(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    global_table_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    point_in_time_recovery: bool | core.BoolOut | None = core.attr(bool, default=None)

    table_class_override: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        global_table_arn: str | core.StringOut,
        kms_key_arn: str | core.StringOut | None = None,
        point_in_time_recovery: bool | core.BoolOut | None = None,
        table_class_override: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TableReplica.Args(
                global_table_arn=global_table_arn,
                kms_key_arn=kms_key_arn,
                point_in_time_recovery=point_in_time_recovery,
                table_class_override=table_class_override,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        global_table_arn: str | core.StringOut = core.arg()

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        point_in_time_recovery: bool | core.BoolOut | None = core.arg(default=None)

        table_class_override: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
