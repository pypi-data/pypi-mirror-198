import terrascript.core as core


@core.resource(type="aws_lb_target_group_attachment", namespace="elb")
class LbTargetGroupAttachment(core.Resource):
    """
    (Optional) The Availability Zone where the IP address of the target is to be registered. If the priv
    ate ip address is outside of the VPC scope, this value must be set to 'all'.
    """

    availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    """
    A unique identifier for the attachment
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The port on which targets receive traffic.
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The ARN of the target group with which to register targets
    """
    target_group_arn: str | core.StringOut = core.attr(str)

    target_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        target_group_arn: str | core.StringOut,
        target_id: str | core.StringOut,
        availability_zone: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbTargetGroupAttachment.Args(
                target_group_arn=target_group_arn,
                target_id=target_id,
                availability_zone=availability_zone,
                port=port,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        target_group_arn: str | core.StringOut = core.arg()

        target_id: str | core.StringOut = core.arg()
