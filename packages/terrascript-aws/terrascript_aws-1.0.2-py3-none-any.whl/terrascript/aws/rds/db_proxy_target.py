import terrascript.core as core


@core.resource(type="aws_db_proxy_target", namespace="aws_rds")
class DbProxyTarget(core.Resource):

    db_cluster_identifier: str | core.StringOut | None = core.attr(str, default=None)

    db_instance_identifier: str | core.StringOut | None = core.attr(str, default=None)

    db_proxy_name: str | core.StringOut = core.attr(str)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    rds_resource_id: str | core.StringOut = core.attr(str, computed=True)

    target_arn: str | core.StringOut = core.attr(str, computed=True)

    target_group_name: str | core.StringOut = core.attr(str)

    tracked_cluster_id: str | core.StringOut = core.attr(str, computed=True)

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
