import terrascript.core as core


@core.resource(type="aws_redshift_usage_limit", namespace="aws_redshift")
class UsageLimit(core.Resource):

    amount: int | core.IntOut = core.attr(int)

    arn: str | core.StringOut = core.attr(str, computed=True)

    breach_action: str | core.StringOut | None = core.attr(str, default=None)

    cluster_identifier: str | core.StringOut = core.attr(str)

    feature_type: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    limit_type: str | core.StringOut = core.attr(str)

    period: str | core.StringOut | None = core.attr(str, default=None)

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
