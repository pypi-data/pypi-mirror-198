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


@core.resource(type="aws_globalaccelerator_endpoint_group", namespace="aws_globalaccelerator")
class EndpointGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    endpoint_configuration: list[EndpointConfiguration] | core.ArrayOut[
        EndpointConfiguration
    ] | None = core.attr(EndpointConfiguration, default=None, kind=core.Kind.array)

    endpoint_group_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    health_check_interval_seconds: int | core.IntOut | None = core.attr(int, default=None)

    health_check_path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    health_check_port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    health_check_protocol: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    listener_arn: str | core.StringOut = core.attr(str)

    port_override: list[PortOverride] | core.ArrayOut[PortOverride] | None = core.attr(
        PortOverride, default=None, kind=core.Kind.array
    )

    threshold_count: int | core.IntOut | None = core.attr(int, default=None)

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
