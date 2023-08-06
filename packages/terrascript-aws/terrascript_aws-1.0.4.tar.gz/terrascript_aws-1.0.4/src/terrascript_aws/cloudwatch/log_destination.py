import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_destination", namespace="cloudwatch")
class LogDestination(core.Resource):
    """
    The Amazon Resource Name (ARN) specifying the log destination.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A name for the log destination
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into th
    e target
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The ARN of the target Amazon Kinesis stream resource for the destination
    """
    target_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        target_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogDestination.Args(
                name=name,
                role_arn=role_arn,
                target_arn=target_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        target_arn: str | core.StringOut = core.arg()
