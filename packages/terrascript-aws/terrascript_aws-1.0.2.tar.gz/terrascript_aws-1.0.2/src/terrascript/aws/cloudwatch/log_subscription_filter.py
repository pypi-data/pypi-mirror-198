import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_subscription_filter", namespace="aws_cloudwatch")
class LogSubscriptionFilter(core.Resource):

    destination_arn: str | core.StringOut = core.attr(str)

    distribution: str | core.StringOut | None = core.attr(str, default=None)

    filter_pattern: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    log_group_name: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_arn: str | core.StringOut,
        filter_pattern: str | core.StringOut,
        log_group_name: str | core.StringOut,
        name: str | core.StringOut,
        distribution: str | core.StringOut | None = None,
        role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogSubscriptionFilter.Args(
                destination_arn=destination_arn,
                filter_pattern=filter_pattern,
                log_group_name=log_group_name,
                name=name,
                distribution=distribution,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_arn: str | core.StringOut = core.arg()

        distribution: str | core.StringOut | None = core.arg(default=None)

        filter_pattern: str | core.StringOut = core.arg()

        log_group_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)
