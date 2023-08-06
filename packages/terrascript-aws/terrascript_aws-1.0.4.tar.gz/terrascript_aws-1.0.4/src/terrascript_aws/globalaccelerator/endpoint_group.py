import terrascript.core as core


@core.schema
class PortOverride(core.Schema):

    endpoint_port: int | core.IntOut = core.attr(int)

    listener_port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        endpoint_port: int | core.IntOut,
        listener_port: int | core.IntOut,
    ):
        super().__init__(
            args=PortOverride.Args(
                endpoint_port=endpoint_port,
                listener_port=listener_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_port: int | core.IntOut = core.arg()

        listener_port: int | core.IntOut = core.arg()


@core.schema
class EndpointConfiguration(core.Schema):

    client_ip_preservation_enabled: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    weight: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        client_ip_preservation_enabled: bool | core.BoolOut | None = None,
        endpoint_id: str | core.StringOut | None = None,
        weight: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=EndpointConfiguration.Args(
                client_ip_preservation_enabled=client_ip_preservation_enabled,
                endpoint_id=endpoint_id,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_ip_preservation_enabled: bool | core.BoolOut | None = core.arg(default=None)

        endpoint_id: str | core.StringOut | None = core.arg(default=None)

        weight: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_globalaccelerator_endpoint_group", namespace="globalaccelerator")
class EndpointGroup(core.Resource):
    """
    The Amazon Resource Name (ARN) of the endpoint group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The list of endpoint objects. Fields documented below.
    """
    endpoint_configuration: list[EndpointConfiguration] | core.ArrayOut[
        EndpointConfiguration
    ] | None = core.attr(EndpointConfiguration, default=None, kind=core.Kind.array)

    endpoint_group_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The time—10 seconds or 30 seconds—between each health check for an endpoint. The default
    value is 30.
    """
    health_check_interval_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) If the protocol is HTTP/S, then this specifies the path that is the destination for healt
    h check targets. The default value is slash (`/`). Terraform will only perform drift detection of it
    s value when present in a configuration.
    """
    health_check_path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The port that AWS Global Accelerator uses to check the health of endpoints that are part
    of this endpoint group. The default port is the listener port that this endpoint group is associated
    with. If listener port is a list of ports, Global Accelerator uses the first port in the list.
    """
    health_check_port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The protocol that AWS Global Accelerator uses to check the health of endpoints that are p
    art of this endpoint group. The default value is TCP.
    """
    health_check_protocol: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name (ARN) of the endpoint group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) of the listener.
    """
    listener_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Override specific listener ports used to route traffic to endpoints that are part of this
    endpoint group. Fields documented below.
    """
    port_override: list[PortOverride] | core.ArrayOut[PortOverride] | None = core.attr(
        PortOverride, default=None, kind=core.Kind.array
    )

    """
    (Optional) The number of consecutive health checks required to set the state of a healthy endpoint t
    o unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """
    threshold_count: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
    other endpoint groups for this listener. The default value is 100.
    """
    traffic_dial_percentage: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        listener_arn: str | core.StringOut,
        endpoint_configuration: list[EndpointConfiguration]
        | core.ArrayOut[EndpointConfiguration]
        | None = None,
        endpoint_group_region: str | core.StringOut | None = None,
        health_check_interval_seconds: int | core.IntOut | None = None,
        health_check_path: str | core.StringOut | None = None,
        health_check_port: int | core.IntOut | None = None,
        health_check_protocol: str | core.StringOut | None = None,
        port_override: list[PortOverride] | core.ArrayOut[PortOverride] | None = None,
        threshold_count: int | core.IntOut | None = None,
        traffic_dial_percentage: float | core.FloatOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointGroup.Args(
                listener_arn=listener_arn,
                endpoint_configuration=endpoint_configuration,
                endpoint_group_region=endpoint_group_region,
                health_check_interval_seconds=health_check_interval_seconds,
                health_check_path=health_check_path,
                health_check_port=health_check_port,
                health_check_protocol=health_check_protocol,
                port_override=port_override,
                threshold_count=threshold_count,
                traffic_dial_percentage=traffic_dial_percentage,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        endpoint_configuration: list[EndpointConfiguration] | core.ArrayOut[
            EndpointConfiguration
        ] | None = core.arg(default=None)

        endpoint_group_region: str | core.StringOut | None = core.arg(default=None)

        health_check_interval_seconds: int | core.IntOut | None = core.arg(default=None)

        health_check_path: str | core.StringOut | None = core.arg(default=None)

        health_check_port: int | core.IntOut | None = core.arg(default=None)

        health_check_protocol: str | core.StringOut | None = core.arg(default=None)

        listener_arn: str | core.StringOut = core.arg()

        port_override: list[PortOverride] | core.ArrayOut[PortOverride] | None = core.arg(
            default=None
        )

        threshold_count: int | core.IntOut | None = core.arg(default=None)

        traffic_dial_percentage: float | core.FloatOut | None = core.arg(default=None)
