import terrascript.core as core


@core.resource(type="aws_codestarconnections_connection", namespace="aws_codestarconnections")
class Connection(core.Resource):
    """
    The codestar connection ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The codestar connection status. Possible values are `PENDING`, `AVAILABLE` and `ERROR`.
    """
    connection_status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) of the host associated with the connection. Conflicts with
    provider_type`
    """
    host_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The codestar connection ARN.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the connection to be created. The name must be unique in the calling AWS acco
    unt. Changing `name` will create a new resource.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of the external provider where your third-party code repository is configured. V
    alid values are `Bitbucket`, `GitHub` or `GitHubEnterpriseServer`. Changing `provider_type` will cre
    ate a new resource. Conflicts with `host_arn`
    """
    provider_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of key-value resource tags to associate with the resource. If configured with a provi
    der [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/lates
    t/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those defin
    ed at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        host_arn: str | core.StringOut | None = None,
        provider_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Connection.Args(
                name=name,
                host_arn=host_arn,
                provider_type=provider_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        host_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        provider_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
