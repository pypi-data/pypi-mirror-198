import terrascript.core as core


@core.resource(type="aws_neptune_cluster_endpoint", namespace="aws_neptune")
class ClusterEndpoint(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_endpoint_identifier: str | core.StringOut = core.attr(str)

    cluster_identifier: str | core.StringOut = core.attr(str)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    endpoint_type: str | core.StringOut = core.attr(str)

    excluded_members: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    static_members: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

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
        cluster_endpoint_identifier: str | core.StringOut,
        cluster_identifier: str | core.StringOut,
        endpoint_type: str | core.StringOut,
        excluded_members: list[str] | core.ArrayOut[core.StringOut] | None = None,
        static_members: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterEndpoint.Args(
                cluster_endpoint_identifier=cluster_endpoint_identifier,
                cluster_identifier=cluster_identifier,
                endpoint_type=endpoint_type,
                excluded_members=excluded_members,
                static_members=static_members,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_endpoint_identifier: str | core.StringOut = core.arg()

        cluster_identifier: str | core.StringOut = core.arg()

        endpoint_type: str | core.StringOut = core.arg()

        excluded_members: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        static_members: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
