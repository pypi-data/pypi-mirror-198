import terrascript.core as core


@core.resource(type="aws_detective_graph", namespace="detective")
class Graph(core.Resource):
    """
    Date and time, in UTC and extended RFC 3339 format, when the Amazon Detective Graph was created.
    """

    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the Detective Graph.
    """
    graph_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the Detective Graph.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the instance. If configured with a provider [`default_tags` c
    onfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-c
    onfiguration-block) present, tags with matching keys will overwrite those defined at the provider-le
    vel.
    """
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
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Graph.Args(
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
