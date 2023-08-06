import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_subscription_filter", namespace="cloudwatch")
class LogSubscriptionFilter(core.Resource):
    """
    (Required) The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda fu
    nction ARN.
    """

    destination_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) The method used to distribute log data to the destination. By default log data is grouped
    by log stream, but the grouping can be set to random for a more even distribution. This property is
    only applicable when the destination is an Amazon Kinesis stream. Valid values are "Random" and "By
    LogStream".
    """
    distribution: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events
    . Use empty string `""` to match everything. For more information, see the [Amazon CloudWatch Logs U
    ser Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).
    """
    filter_pattern: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the log group to associate the subscription filter with
    """
    log_group_name: str | core.StringOut = core.attr(str)

    """
    (Required) A name for the subscription filter
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested
    log events to the destination. If you use Lambda as a destination, you should skip this argument an
    d use `aws_lambda_permission` resource for granting access from CloudWatch logs to the destination L
    ambda function.
    """
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
