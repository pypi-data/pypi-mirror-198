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


@core.resource(type="aws_codepipeline_webhook", namespace="aws_codepipeline")
class Webhook(core.Resource):
    """
    The CodePipeline webhook's ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
    """
    authentication: str | core.StringOut = core.attr(str)

    """
    (Optional) An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
    """
    authentication_configuration: AuthenticationConfiguration | None = core.attr(
        AuthenticationConfiguration, default=None
    )

    filter: list[Filter] | core.ArrayOut[Filter] = core.attr(Filter, kind=core.Kind.array)

    """
    The CodePipeline webhook's ARN.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the webhook.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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

    """
    (Required) The name of the action in a pipeline you want to connect to the webhook. The action must
    be from the source (first) stage of the pipeline.
    """
    target_action: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the pipeline.
    """
    target_pipeline: str | core.StringOut = core.attr(str)

    """
    The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.
    """
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
