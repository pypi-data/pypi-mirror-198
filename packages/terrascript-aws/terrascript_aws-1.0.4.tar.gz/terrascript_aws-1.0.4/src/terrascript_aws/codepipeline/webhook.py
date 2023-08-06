import terrascript.core as core


@core.schema
class AuthenticationConfiguration(core.Schema):

    allowed_ip_range: str | core.StringOut | None = core.attr(str, default=None)

    secret_token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        allowed_ip_range: str | core.StringOut | None = None,
        secret_token: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AuthenticationConfiguration.Args(
                allowed_ip_range=allowed_ip_range,
                secret_token=secret_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_ip_range: str | core.StringOut | None = core.arg(default=None)

        secret_token: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    json_path: str | core.StringOut = core.attr(str)

    match_equals: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        json_path: str | core.StringOut,
        match_equals: str | core.StringOut,
    ):
        super().__init__(
            args=Filter.Args(
                json_path=json_path,
                match_equals=match_equals,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        json_path: str | core.StringOut = core.arg()

        match_equals: str | core.StringOut = core.arg()


@core.resource(type="aws_codepipeline_webhook", namespace="codepipeline")
class Webhook(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication: str | core.StringOut = core.attr(str)

    authentication_configuration: AuthenticationConfiguration | None = core.attr(
        AuthenticationConfiguration, default=None
    )

    filter: list[Filter] | core.ArrayOut[Filter] = core.attr(Filter, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_action: str | core.StringOut = core.attr(str)

    target_pipeline: str | core.StringOut = core.attr(str)

    url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication: str | core.StringOut,
        filter: list[Filter] | core.ArrayOut[Filter],
        name: str | core.StringOut,
        target_action: str | core.StringOut,
        target_pipeline: str | core.StringOut,
        authentication_configuration: AuthenticationConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Webhook.Args(
                authentication=authentication,
                filter=filter,
                name=name,
                target_action=target_action,
                target_pipeline=target_pipeline,
                authentication_configuration=authentication_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication: str | core.StringOut = core.arg()

        authentication_configuration: AuthenticationConfiguration | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_action: str | core.StringOut = core.arg()

        target_pipeline: str | core.StringOut = core.arg()
