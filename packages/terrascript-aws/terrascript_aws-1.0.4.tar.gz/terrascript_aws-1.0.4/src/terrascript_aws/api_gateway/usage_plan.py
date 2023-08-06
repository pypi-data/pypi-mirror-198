import terrascript.core as core


@core.schema
class QuotaSettings(core.Schema):

    limit: int | core.IntOut = core.attr(int)

    offset: int | core.IntOut | None = core.attr(int, default=None)

    period: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        limit: int | core.IntOut,
        period: str | core.StringOut,
        offset: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=QuotaSettings.Args(
                limit=limit,
                period=period,
                offset=offset,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        limit: int | core.IntOut = core.arg()

        offset: int | core.IntOut | None = core.arg(default=None)

        period: str | core.StringOut = core.arg()


@core.schema
class ThrottleSettings(core.Schema):

    burst_limit: int | core.IntOut | None = core.attr(int, default=None)

    rate_limit: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        burst_limit: int | core.IntOut | None = None,
        rate_limit: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=ThrottleSettings.Args(
                burst_limit=burst_limit,
                rate_limit=rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        burst_limit: int | core.IntOut | None = core.arg(default=None)

        rate_limit: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class Throttle(core.Schema):

    burst_limit: int | core.IntOut | None = core.attr(int, default=None)

    path: str | core.StringOut = core.attr(str)

    rate_limit: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        path: str | core.StringOut,
        burst_limit: int | core.IntOut | None = None,
        rate_limit: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=Throttle.Args(
                path=path,
                burst_limit=burst_limit,
                rate_limit=rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        burst_limit: int | core.IntOut | None = core.arg(default=None)

        path: str | core.StringOut = core.arg()

        rate_limit: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class ApiStages(core.Schema):

    api_id: str | core.StringOut = core.attr(str)

    stage: str | core.StringOut = core.attr(str)

    throttle: list[Throttle] | core.ArrayOut[Throttle] | None = core.attr(
        Throttle, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        api_id: str | core.StringOut,
        stage: str | core.StringOut,
        throttle: list[Throttle] | core.ArrayOut[Throttle] | None = None,
    ):
        super().__init__(
            args=ApiStages.Args(
                api_id=api_id,
                stage=stage,
                throttle=throttle,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_id: str | core.StringOut = core.arg()

        stage: str | core.StringOut = core.arg()

        throttle: list[Throttle] | core.ArrayOut[Throttle] | None = core.arg(default=None)


@core.resource(type="aws_api_gateway_usage_plan", namespace="api_gateway")
class UsagePlan(core.Resource):
    """
    (Optional) The associated [API stages](#api-stages-arguments) of the usage plan.
    """

    api_stages: list[ApiStages] | core.ArrayOut[ApiStages] | None = core.attr(
        ApiStages, default=None, kind=core.Kind.array
    )

    """
    Amazon Resource Name (ARN)
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of a usage plan.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the API resource
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the usage plan.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The AWS Marketplace product identifier to associate with the usage plan as a SaaS product
    on AWS Marketplace.
    """
    product_code: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The [quota settings](#quota-settings-arguments) of the usage plan.
    """
    quota_settings: QuotaSettings | None = core.attr(QuotaSettings, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) The [throttling limits](#throttling-settings-arguments) of the usage plan.
    """
    throttle_settings: ThrottleSettings | None = core.attr(ThrottleSettings, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        api_stages: list[ApiStages] | core.ArrayOut[ApiStages] | None = None,
        description: str | core.StringOut | None = None,
        product_code: str | core.StringOut | None = None,
        quota_settings: QuotaSettings | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        throttle_settings: ThrottleSettings | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UsagePlan.Args(
                name=name,
                api_stages=api_stages,
                description=description,
                product_code=product_code,
                quota_settings=quota_settings,
                tags=tags,
                tags_all=tags_all,
                throttle_settings=throttle_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_stages: list[ApiStages] | core.ArrayOut[ApiStages] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        product_code: str | core.StringOut | None = core.arg(default=None)

        quota_settings: QuotaSettings | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throttle_settings: ThrottleSettings | None = core.arg(default=None)
