import terrascript.core as core


@core.schema
class CanarySettings(core.Schema):

    percent_traffic: float | core.FloatOut | None = core.attr(float, default=None)

    stage_variable_overrides: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    use_stage_cache: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        percent_traffic: float | core.FloatOut | None = None,
        stage_variable_overrides: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        use_stage_cache: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=CanarySettings.Args(
                percent_traffic=percent_traffic,
                stage_variable_overrides=stage_variable_overrides,
                use_stage_cache=use_stage_cache,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        percent_traffic: float | core.FloatOut | None = core.arg(default=None)

        stage_variable_overrides: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        use_stage_cache: bool | core.BoolOut | None = core.arg(default=None)


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


@core.resource(type="aws_api_gateway_stage", namespace="aws_api_gateway")
class Stage(core.Resource):

    access_log_settings: AccessLogSettings | None = core.attr(AccessLogSettings, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    cache_cluster_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    cache_cluster_size: str | core.StringOut | None = core.attr(str, default=None)

    canary_settings: CanarySettings | None = core.attr(CanarySettings, default=None)

    client_certificate_id: str | core.StringOut | None = core.attr(str, default=None)

    deployment_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    documentation_version: str | core.StringOut | None = core.attr(str, default=None)

    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    invoke_url: str | core.StringOut = core.attr(str, computed=True)

    rest_api_id: str | core.StringOut = core.attr(str)

    stage_name: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    web_acl_arn: str | core.StringOut = core.attr(str, computed=True)

    xray_tracing_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        deployment_id: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        stage_name: str | core.StringOut,
        access_log_settings: AccessLogSettings | None = None,
        cache_cluster_enabled: bool | core.BoolOut | None = None,
        cache_cluster_size: str | core.StringOut | None = None,
        canary_settings: CanarySettings | None = None,
        client_certificate_id: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        documentation_version: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        xray_tracing_enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stage.Args(
                deployment_id=deployment_id,
                rest_api_id=rest_api_id,
                stage_name=stage_name,
                access_log_settings=access_log_settings,
                cache_cluster_enabled=cache_cluster_enabled,
                cache_cluster_size=cache_cluster_size,
                canary_settings=canary_settings,
                client_certificate_id=client_certificate_id,
                description=description,
                documentation_version=documentation_version,
                tags=tags,
                tags_all=tags_all,
                variables=variables,
                xray_tracing_enabled=xray_tracing_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_log_settings: AccessLogSettings | None = core.arg(default=None)

        cache_cluster_enabled: bool | core.BoolOut | None = core.arg(default=None)

        cache_cluster_size: str | core.StringOut | None = core.arg(default=None)

        canary_settings: CanarySettings | None = core.arg(default=None)

        client_certificate_id: str | core.StringOut | None = core.arg(default=None)

        deployment_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        documentation_version: str | core.StringOut | None = core.arg(default=None)

        rest_api_id: str | core.StringOut = core.arg()

        stage_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        xray_tracing_enabled: bool | core.BoolOut | None = core.arg(default=None)
