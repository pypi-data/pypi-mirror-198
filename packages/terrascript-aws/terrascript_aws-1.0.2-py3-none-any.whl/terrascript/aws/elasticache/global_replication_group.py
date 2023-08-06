import terrascript.core as core


@core.resource(type="aws_elasticache_global_replication_group", namespace="aws_elasticache")
class GlobalReplicationGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    at_rest_encryption_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    auth_token_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    cache_node_type: str | core.StringOut = core.attr(str, computed=True)

    cluster_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    engine: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    global_replication_group_description: str | core.StringOut | None = core.attr(str, default=None)

    global_replication_group_id: str | core.StringOut = core.attr(str, computed=True)

    global_replication_group_id_suffix: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None)

    primary_replication_group_id: str | core.StringOut = core.attr(str)

    transit_encryption_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        global_replication_group_id_suffix: str | core.StringOut,
        primary_replication_group_id: str | core.StringOut,
        engine_version: str | core.StringOut | None = None,
        global_replication_group_description: str | core.StringOut | None = None,
        parameter_group_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GlobalReplicationGroup.Args(
                global_replication_group_id_suffix=global_replication_group_id_suffix,
                primary_replication_group_id=primary_replication_group_id,
                engine_version=engine_version,
                global_replication_group_description=global_replication_group_description,
                parameter_group_name=parameter_group_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        engine_version: str | core.StringOut | None = core.arg(default=None)

        global_replication_group_description: str | core.StringOut | None = core.arg(default=None)

        global_replication_group_id_suffix: str | core.StringOut = core.arg()

        parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        primary_replication_group_id: str | core.StringOut = core.arg()
