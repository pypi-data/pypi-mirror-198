import terrascript.core as core


@core.resource(type="aws_db_proxy_target", namespace="rds")
class DbProxyTarget(core.Resource):
    """
    (Optional, Forces new resource) DB cluster identifier.
    """

    db_cluster_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Forces new resource) DB instance identifier.
    """
    db_instance_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required, Forces new resource) The name of the DB proxy.
    """
    db_proxy_name: str | core.StringOut = core.attr(str)

    """
    Hostname for the target RDS DB Instance. Only returned for `RDS_INSTANCE` type.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of  `db_proxy_name`, `target_group_name`, target type (e.g., `RDS_INSTANCE` or `TRACKED_C
    LUSTER`), and resource identifier separated by forward slashes (`/`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Port for the target RDS DB Instance or Aurora DB Cluster.
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    """
    Identifier representing the DB Instance or DB Cluster target.
    """
    rds_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) for the DB instance or DB cluster. Currently not returned by the RDS API.
    """
    target_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The name of the target group.
    """
    target_group_name: str | core.StringOut = core.attr(str)

    """
    DB Cluster identifier for the DB Instance target. Not returned unless manually importing an `RDS_INS
    TANCE` target that is part of a DB Cluster.
    """
    tracked_cluster_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Type of targetE.g., `RDS_INSTANCE` or `TRACKED_CLUSTER`
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_proxy_name: str | core.StringOut,
        target_group_name: str | core.StringOut,
        db_cluster_identifier: str | core.StringOut | None = None,
        db_instance_identifier: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbProxyTarget.Args(
                db_proxy_name=db_proxy_name,
                target_group_name=target_group_name,
                db_cluster_identifier=db_cluster_identifier,
                db_instance_identifier=db_instance_identifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        db_instance_identifier: str | core.StringOut | None = core.arg(default=None)

        db_proxy_name: str | core.StringOut = core.arg()

        target_group_name: str | core.StringOut = core.arg()
