import terrascript.core as core


@core.schema
class ClusterEndpoints(core.Schema):

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        endpoint: str | core.StringOut,
        region: str | core.StringOut,
    ):
        super().__init__(
            args=ClusterEndpoints.Args(
                endpoint=endpoint,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: str | core.StringOut = core.arg()

        region: str | core.StringOut = core.arg()


@core.resource(
    type="aws_route53recoverycontrolconfig_cluster", namespace="route53recoverycontrolconfig"
)
class Cluster(core.Resource):
    """
    ARN of the cluster
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    List of 5 endpoints in 5 regions that can be used to talk to the cluster. See below.
    """
    cluster_endpoints: list[ClusterEndpoints] | core.ArrayOut[ClusterEndpoints] = core.attr(
        ClusterEndpoints, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Unique name describing the cluster.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Status of cluster. `PENDING` when it is being created, `PENDING_DELETION` when it is being deleted a
    nd `DEPLOYED` otherwise.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()
