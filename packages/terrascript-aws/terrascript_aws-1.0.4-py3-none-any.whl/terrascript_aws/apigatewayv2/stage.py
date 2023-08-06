import terrascript.core as core


@core.schema
class DefaultRouteSettings(core.Schema):

    data_trace_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    detailed_metrics_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    logging_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    throttling_burst_limit: int | core.IntOut | None = core.attr(int, default=None)

    throttling_rate_limit: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        data_trace_enabled: bool | core.BoolOut | None = None,
        detailed_metrics_enabled: bool | core.BoolOut | None = None,
        logging_level: str | core.StringOut | None = None,
        throttling_burst_limit: int | core.IntOut | None = None,
        throttling_rate_limit: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=DefaultRouteSettings.Args(
                data_trace_enabled=data_trace_enabled,
                detailed_metrics_enabled=detailed_metrics_enabled,
                logging_level=logging_level,
                throttling_burst_limit=throttling_burst_limit,
                throttling_rate_limit=throttling_rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_trace_enabled: bool | core.BoolOut | None = core.arg(default=None)

        detailed_metrics_enabled: bool | core.BoolOut | None = core.arg(default=None)

        logging_level: str | core.StringOut | None = core.arg(default=None)

        throttling_burst_limit: int | core.IntOut | None = core.arg(default=None)

        throttling_rate_limit: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class AccessLogSettings(core.Schema):

    destination_arn: str | core.StringOut = core.attr(str)

    format: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        destination_arn: str | core.StringOut,
        format: str | core.StringOut,
    ):
        super().__init__(
            args=AccessLogSettings.Args(
                destination_arn=destination_arn,
                format=format,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_arn: str | core.StringOut = core.arg()

        format: str | core.StringOut = core.arg()


@core.schema
class RouteSettings(core.Schema):

    data_trace_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    detailed_metrics_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    logging_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    route_key: str | core.StringOut = core.attr(str)

    throttling_burst_limit: int | core.IntOut | None = core.attr(int, default=None)

    throttling_rate_limit: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        route_key: str | core.StringOut,
        data_trace_enabled: bool | core.BoolOut | None = None,
        detailed_metrics_enabled: bool | core.BoolOut | None = None,
        logging_level: str | core.StringOut | None = None,
        throttling_burst_limit: int | core.IntOut | None = None,
        throttling_rate_limit: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=RouteSettings.Args(
                route_key=route_key,
                data_trace_enabled=data_trace_enabled,
                detailed_metrics_enabled=detailed_metrics_enabled,
                logging_level=logging_level,
                throttling_burst_limit=throttling_burst_limit,
                throttling_rate_limit=throttling_rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_trace_enabled: bool | core.BoolOut | None = core.arg(default=None)

        detailed_metrics_enabled: bool | core.BoolOut | None = core.arg(default=None)

        logging_level: str | core.StringOut | None = core.arg(default=None)

        route_key: str | core.StringOut = core.arg()

        throttling_burst_limit: int | core.IntOut | None = core.arg(default=None)

        throttling_rate_limit: float | core.FloatOut | None = core.arg(default=None)


@core.resource(type="aws_apigatewayv2_stage", namespace="apigatewayv2")
class Stage(core.Resource):
    """
    (Optional) Settings for logging access in this stage.
    """

    access_log_settings: AccessLogSettings | None = core.attr(AccessLogSettings, default=None)

    """
    (Required) The API identifier.
    """
    api_id: str | core.StringOut = core.attr(str)

    """
    The ARN of the stage.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether updates to an API automatically trigger a new deployment. Defaults to `false`. Ap
    plicable for HTTP APIs.
    """
    auto_deploy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The identifier of a client certificate for the stage. Use the [`aws_api_gateway_client_ce
    rtificate`](/docs/providers/aws/r/api_gateway_client_certificate.html) resource to configure a clien
    t certificate.
    """
    client_certificate_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The default route settings for the stage.
    """
    default_route_settings: DefaultRouteSettings | None = core.attr(
        DefaultRouteSettings, default=None
    )

    """
    (Optional) The deployment identifier of the stage. Use the [`aws_apigatewayv2_deployment`](/docs/pro
    viders/aws/r/apigatewayv2_deployment.html) resource to configure a deployment.
    """
    deployment_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The description for the stage. Must be less than or equal to 1024 characters in length.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN prefix to be used in an [`aws_lambda_permission`](/docs/providers/aws/r/lambda_permission.ht
    ml)'s `source_arn` attribute.
    """
    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The stage identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The URL to invoke the API pointing to the stage,
    """
    invoke_url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the stage. Must be between 1 and 128 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Route settings for the stage.
    """
    route_settings: list[RouteSettings] | core.ArrayOut[RouteSettings] | None = core.attr(
        RouteSettings, default=None, kind=core.Kind.array
    )

    """
    (Optional) A map that defines the stage variables for the stage.
    """
    stage_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) A map of tags to assign to the stage. If configured with a provider [`default_tags` confi
    guration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-confi
    guration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        api_id: str | core.StringOut,
        name: str | core.StringOut,
        access_log_settings: AccessLogSettings | None = None,
        auto_deploy: bool | core.BoolOut | None = None,
        client_certificate_id: str | core.StringOut | None = None,
        default_route_settings: DefaultRouteSettings | None = None,
        deployment_id: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        route_settings: list[RouteSettings] | core.ArrayOut[RouteSettings] | None = None,
        stage_variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stage.Args(
                api_id=api_id,
                name=name,
                access_log_settings=access_log_settings,
                auto_deploy=auto_deploy,
                client_certificate_id=client_certificate_id,
                default_route_settings=default_route_settings,
                deployment_id=deployment_id,
                description=description,
                route_settings=route_settings,
                stage_variables=stage_variables,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_log_settings: AccessLogSettings | None = core.arg(default=None)

        api_id: str | core.StringOut = core.arg()

        auto_deploy: bool | core.BoolOut | None = core.arg(default=None)

        client_certificate_id: str | core.StringOut | None = core.arg(default=None)

        default_route_settings: DefaultRouteSettings | None = core.arg(default=None)

        deployment_id: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        route_settings: list[RouteSettings] | core.ArrayOut[RouteSettings] | None = core.arg(
            default=None
        )

        stage_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
