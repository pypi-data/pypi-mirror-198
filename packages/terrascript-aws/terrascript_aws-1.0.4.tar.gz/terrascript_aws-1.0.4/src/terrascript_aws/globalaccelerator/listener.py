import terrascript.core as core


@core.schema
class PortRange(core.Schema):

    from_port: int | core.IntOut | None = core.attr(int, default=None)

    to_port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut | None = None,
        to_port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=PortRange.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: int | core.IntOut | None = core.arg(default=None)

        to_port: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_globalaccelerator_listener", namespace="globalaccelerator")
class Listener(core.Resource):
    """
    (Required) The Amazon Resource Name (ARN) of your accelerator.
    """

    accelerator_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP
    . Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP addr
    ess, source port, destination IP address, destination port, and protocol to select the hash value. I
    f `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and
    destination IP address to select the hash value.
    """
    client_affinity: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name (ARN) of the listener.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The list of port ranges for the connections from clients to the accelerator. Fields docum
    ented below.
    """
    port_range: list[PortRange] | core.ArrayOut[PortRange] = core.attr(
        PortRange, kind=core.Kind.array
    )

    """
    (Optional) The protocol for the connections from clients to the accelerator. Valid values are `TCP`,
    UDP`.
    """
    protocol: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        accelerator_arn: str | core.StringOut,
        port_range: list[PortRange] | core.ArrayOut[PortRange],
        protocol: str | core.StringOut,
        client_affinity: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Listener.Args(
                accelerator_arn=accelerator_arn,
                port_range=port_range,
                protocol=protocol,
                client_affinity=client_affinity,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accelerator_arn: str | core.StringOut = core.arg()

        client_affinity: str | core.StringOut | None = core.arg(default=None)

        port_range: list[PortRange] | core.ArrayOut[PortRange] = core.arg()

        protocol: str | core.StringOut = core.arg()
