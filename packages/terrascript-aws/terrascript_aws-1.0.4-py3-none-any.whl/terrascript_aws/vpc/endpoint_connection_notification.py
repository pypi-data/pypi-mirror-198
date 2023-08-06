import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_connection_notification", namespace="vpc")
class EndpointConnectionNotification(core.Resource):
    """
    (Required) One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_
    CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestPara
    meters) for which to receive notifications.
    """

    connection_events: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) The ARN of the SNS topic for the notifications.
    """
    connection_notification_arn: str | core.StringOut = core.attr(str)

    """
    The ID of the VPC connection notification.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of notification.
    """
    notification_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the notification.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the VPC Endpoint to receive notifications for.
    """
    vpc_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ID of the VPC Endpoint Service to receive notifications for.
    """
    vpc_endpoint_service_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_events: list[str] | core.ArrayOut[core.StringOut],
        connection_notification_arn: str | core.StringOut,
        vpc_endpoint_id: str | core.StringOut | None = None,
        vpc_endpoint_service_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointConnectionNotification.Args(
                connection_events=connection_events,
                connection_notification_arn=connection_notification_arn,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_endpoint_service_id=vpc_endpoint_service_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        connection_notification_arn: str | core.StringOut = core.arg()

        vpc_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        vpc_endpoint_service_id: str | core.StringOut | None = core.arg(default=None)
