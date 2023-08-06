import terrascript.core as core


@core.schema
class CampaignHook(core.Schema):

    lambda_function_name: str | core.StringOut | None = core.attr(str, default=None)

    mode: str | core.StringOut | None = core.attr(str, default=None)

    web_url: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        lambda_function_name: str | core.StringOut | None = None,
        mode: str | core.StringOut | None = None,
        web_url: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CampaignHook.Args(
                lambda_function_name=lambda_function_name,
                mode=mode,
                web_url=web_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_function_name: str | core.StringOut | None = core.arg(default=None)

        mode: str | core.StringOut | None = core.arg(default=None)

        web_url: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Limits(core.Schema):

    daily: int | core.IntOut | None = core.attr(int, default=None)

    maximum_duration: int | core.IntOut | None = core.attr(int, default=None)

    messages_per_second: int | core.IntOut | None = core.attr(int, default=None)

    total: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        daily: int | core.IntOut | None = None,
        maximum_duration: int | core.IntOut | None = None,
        messages_per_second: int | core.IntOut | None = None,
        total: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Limits.Args(
                daily=daily,
                maximum_duration=maximum_duration,
                messages_per_second=messages_per_second,
                total=total,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        daily: int | core.IntOut | None = core.arg(default=None)

        maximum_duration: int | core.IntOut | None = core.arg(default=None)

        messages_per_second: int | core.IntOut | None = core.arg(default=None)

        total: int | core.IntOut | None = core.arg(default=None)


@core.schema
class QuietTime(core.Schema):

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=QuietTime.Args(
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_pinpoint_app", namespace="pinpoint")
class App(core.Resource):

    application_id: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    campaign_hook: CampaignHook | None = core.attr(CampaignHook, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    limits: Limits | None = core.attr(Limits, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    quiet_time: QuietTime | None = core.attr(QuietTime, default=None)

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
        campaign_hook: CampaignHook | None = None,
        limits: Limits | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        quiet_time: QuietTime | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=App.Args(
                campaign_hook=campaign_hook,
                limits=limits,
                name=name,
                name_prefix=name_prefix,
                quiet_time=quiet_time,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        campaign_hook: CampaignHook | None = core.arg(default=None)

        limits: Limits | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        quiet_time: QuietTime | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
