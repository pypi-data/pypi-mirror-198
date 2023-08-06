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


@core.resource(type="aws_globalaccelerator_listener", namespace="aws_globalaccelerator")
class Listener(core.Resource):

    accelerator_arn: str | core.StringOut = core.attr(str)

    client_affinity: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    port_range: list[PortRange] | core.ArrayOut[PortRange] = core.attr(
        PortRange, kind=core.Kind.array
    )

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
