import terrascript.core as core


@core.resource(type="aws_lb_target_group_attachment", namespace="aws_elb")
class LbTargetGroupAttachment(core.Resource):

    availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut | None = core.attr(int, default=None)

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
