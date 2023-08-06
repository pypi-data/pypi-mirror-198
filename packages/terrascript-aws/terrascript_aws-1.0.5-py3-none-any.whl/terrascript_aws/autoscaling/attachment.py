import terrascript.core as core


@core.resource(type="aws_autoscaling_attachment", namespace="autoscaling")
class Attachment(core.Resource):
    """
    (Optional, **Deprecated** use `lb_target_group_arn` instead) The ARN of an ALB Target Group.
    """

    alb_target_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name of ASG to associate with the ELB.
    """
    autoscaling_group_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of the ELB.
    """
    elb: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN of a load balancer target group.
    """
    lb_target_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: str | core.StringOut,
        alb_target_group_arn: str | core.StringOut | None = None,
        elb: str | core.StringOut | None = None,
        lb_target_group_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Attachment.Args(
                autoscaling_group_name=autoscaling_group_name,
                alb_target_group_arn=alb_target_group_arn,
                elb=elb,
                lb_target_group_arn=lb_target_group_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alb_target_group_arn: str | core.StringOut | None = core.arg(default=None)

        autoscaling_group_name: str | core.StringOut = core.arg()

        elb: str | core.StringOut | None = core.arg(default=None)

        lb_target_group_arn: str | core.StringOut | None = core.arg(default=None)
