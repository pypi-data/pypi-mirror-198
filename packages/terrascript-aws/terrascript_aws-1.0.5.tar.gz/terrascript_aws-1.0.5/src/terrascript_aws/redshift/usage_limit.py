import terrascript.core as core


@core.resource(type="aws_redshift_usage_limit", namespace="redshift")
class UsageLimit(core.Resource):
    """
    (Required) The limit amount. If time-based, this amount is in minutes. If data-based, this amount is
    in terabytes (TB). The value must be a positive number.
    """

    amount: int | core.IntOut = core.attr(int)

    """
    Amazon Resource Name (ARN) of the Redshift Usage Limit.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The action that Amazon Redshift takes when the limit is reached. The default is `log`. Va
    lid values are `log`, `emit-metric`, and `disable`.
    """
    breach_action: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The identifier of the cluster that you want to limit usage.
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Redshift feature that you want to limit. Valid values are `spectrum`, `concurr
    ency-scaling`, and `cross-region-datasharing`.
    """
    feature_type: str | core.StringOut = core.attr(str)

    """
    The Redshift Usage Limit ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of limit. Depending on the feature type, this can be based on a time duration or
    data size. If FeatureType is `spectrum`, then LimitType must be `data-scanned`. If FeatureType is `
    concurrency-scaling`, then LimitType must be `time`. If FeatureType is `cross-region-datasharing`, t
    hen LimitType must be `data-scanned`. Valid values are `data-scanned`, and `time`.
    """
    limit_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The time period that the amount applies to. A weekly period begins on Sunday. The default
    is `monthly`. Valid values are `daily`, `weekly`, and `monthly`.
    """
    period: str | core.StringOut | None = core.attr(str, default=None)

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
        amount: int | core.IntOut,
        cluster_identifier: str | core.StringOut,
        feature_type: str | core.StringOut,
        limit_type: str | core.StringOut,
        breach_action: str | core.StringOut | None = None,
        period: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UsageLimit.Args(
                amount=amount,
                cluster_identifier=cluster_identifier,
                feature_type=feature_type,
                limit_type=limit_type,
                breach_action=breach_action,
                period=period,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        amount: int | core.IntOut = core.arg()

        breach_action: str | core.StringOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut = core.arg()

        feature_type: str | core.StringOut = core.arg()

        limit_type: str | core.StringOut = core.arg()

        period: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
