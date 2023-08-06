import terrascript.core as core


@core.schema
class AppMonitorConfiguration(core.Schema):

    allow_cookies: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_xray: bool | core.BoolOut | None = core.attr(bool, default=None)

    excluded_pages: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    favorite_pages: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    guest_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    identity_pool_id: str | core.StringOut | None = core.attr(str, default=None)

    included_pages: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    session_sample_rate: float | core.FloatOut | None = core.attr(float, default=None)

    telemetries: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        allow_cookies: bool | core.BoolOut | None = None,
        enable_xray: bool | core.BoolOut | None = None,
        excluded_pages: list[str] | core.ArrayOut[core.StringOut] | None = None,
        favorite_pages: list[str] | core.ArrayOut[core.StringOut] | None = None,
        guest_role_arn: str | core.StringOut | None = None,
        identity_pool_id: str | core.StringOut | None = None,
        included_pages: list[str] | core.ArrayOut[core.StringOut] | None = None,
        session_sample_rate: float | core.FloatOut | None = None,
        telemetries: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AppMonitorConfiguration.Args(
                allow_cookies=allow_cookies,
                enable_xray=enable_xray,
                excluded_pages=excluded_pages,
                favorite_pages=favorite_pages,
                guest_role_arn=guest_role_arn,
                identity_pool_id=identity_pool_id,
                included_pages=included_pages,
                session_sample_rate=session_sample_rate,
                telemetries=telemetries,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_cookies: bool | core.BoolOut | None = core.arg(default=None)

        enable_xray: bool | core.BoolOut | None = core.arg(default=None)

        excluded_pages: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        favorite_pages: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        guest_role_arn: str | core.StringOut | None = core.arg(default=None)

        identity_pool_id: str | core.StringOut | None = core.arg(default=None)

        included_pages: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        session_sample_rate: float | core.FloatOut | None = core.arg(default=None)

        telemetries: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_rum_app_monitor", namespace="rum")
class AppMonitor(core.Resource):

    app_monitor_configuration: AppMonitorConfiguration | None = core.attr(
        AppMonitorConfiguration, default=None, computed=True
    )

    """
    The Amazon Resource Name (ARN) specifying the app monitor.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter  specif
    ies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This
    enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Lo
    gs charges. Default value is `false`.
    """
    cw_log_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The name of the log group where the copies are stored.
    """
    cw_log_group: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The top-level internet domain name for which your application has administrative authorit
    y.
    """
    domain: str | core.StringOut = core.attr(str)

    """
    TThe Amazon Resource Name (ARN) specifying the app monitor.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the log stream.
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

    def __init__(
        self,
        resource_name: str,
        *,
        domain: str | core.StringOut,
        name: str | core.StringOut,
        app_monitor_configuration: AppMonitorConfiguration | None = None,
        cw_log_enabled: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppMonitor.Args(
                domain=domain,
                name=name,
                app_monitor_configuration=app_monitor_configuration,
                cw_log_enabled=cw_log_enabled,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_monitor_configuration: AppMonitorConfiguration | None = core.arg(default=None)

        cw_log_enabled: bool | core.BoolOut | None = core.arg(default=None)

        domain: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
