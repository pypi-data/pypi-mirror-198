import terrascript.core as core


@core.data(type="aws_lb_hosted_zone_id", namespace="elb")
class DsLbHostedZoneId(core.Data):
    """
    The ID of the AWS ELB HostedZoneId in the selected region.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The type of load balancer to create. Possible values are `application` or `network`. The
    default value is `application`.
    """
    load_balancer_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the region whose AWS ELB HostedZoneId is desired.
    """
    region: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        load_balancer_type: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLbHostedZoneId.Args(
                load_balancer_type=load_balancer_type,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        load_balancer_type: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)
