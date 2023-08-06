import terrascript.core as core


@core.resource(type="aws_route53_query_log", namespace="route53")
class QueryLog(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Query Logging Config.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) CloudWatch log group ARN to send query logs.
    """
    cloudwatch_log_group_arn: str | core.StringOut = core.attr(str)

    """
    The query logging configuration ID
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Route53 hosted zone ID to enable query logs.
    """
    zone_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cloudwatch_log_group_arn: str | core.StringOut,
        zone_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=QueryLog.Args(
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                zone_id=zone_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_log_group_arn: str | core.StringOut = core.arg()

        zone_id: str | core.StringOut = core.arg()
