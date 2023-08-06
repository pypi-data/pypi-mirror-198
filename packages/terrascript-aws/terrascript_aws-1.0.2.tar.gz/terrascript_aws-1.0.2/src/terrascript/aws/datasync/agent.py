import terrascript.core as core


@core.resource(type="aws_datasync_agent", namespace="aws_datasync")
class Agent(core.Resource):

    activation_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None)

    private_link_endpoint: str | core.StringOut | None = core.attr(str, default=None)

    security_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        activation_key: str | core.StringOut | None = None,
        ip_address: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        private_link_endpoint: str | core.StringOut | None = None,
        security_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_endpoint_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Agent.Args(
                activation_key=activation_key,
                ip_address=ip_address,
                name=name,
                private_link_endpoint=private_link_endpoint,
                security_group_arns=security_group_arns,
                subnet_arns=subnet_arns,
                tags=tags,
                tags_all=tags_all,
                vpc_endpoint_id=vpc_endpoint_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activation_key: str | core.StringOut | None = core.arg(default=None)

        ip_address: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        private_link_endpoint: str | core.StringOut | None = core.arg(default=None)

        security_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_endpoint_id: str | core.StringOut | None = core.arg(default=None)
