import terrascript.core as core


@core.resource(type="aws_elasticache_global_replication_group", namespace="elasticache")
class GlobalReplicationGroup(core.Resource):
    """
    The ARN of the ElastiCache Global Replication Group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A flag that indicate whether the encryption at rest is enabled.
    """
    at_rest_encryption_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    A flag that indicate whether AuthToken (password) is enabled.
    """
    auth_token_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The instance class used. See AWS documentation for information on [supported node types](https://doc
    s.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html) and [guidance on se
    lecting node types](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/nodes-select-size.ht
    ml).
    """
    cache_node_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether the Global Datastore is cluster enabled.
    """
    cluster_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The name of the cache engine to be used for the clusters in this global replication group.
    """
    engine: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Redis version to use for the Global Replication Group.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The full version number of the cache engine running on the members of this global replication group.
    """
    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    global_replication_group_description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The full ID of the global replication group.
    """
    global_replication_group_id: str | core.StringOut = core.attr(str, computed=True)

    global_replication_group_id_suffix: str | core.StringOut = core.attr(str)

    """
    The ID of the ElastiCache Global Replication Group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An ElastiCache Parameter Group to use for the Global Replication Group.
    """
    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None)

    primary_replication_group_id: str | core.StringOut = core.attr(str)

    """
    A flag that indicates whether the encryption in transit is enabled.
    """
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
