import terrascript.core as core


@core.schema
class PortInfo(core.Schema):

    cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    from_port: int | core.IntOut = core.attr(int)

    protocol: str | core.StringOut = core.attr(str)

    to_port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut,
        protocol: str | core.StringOut,
        to_port: int | core.IntOut,
        cidrs: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=PortInfo.Args(
                from_port=from_port,
                protocol=protocol,
                to_port=to_port,
                cidrs=cidrs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        from_port: int | core.IntOut = core.arg()

        protocol: str | core.StringOut = core.arg()

        to_port: int | core.IntOut = core.arg()


@core.resource(type="aws_lightsail_instance_public_ports", namespace="lightsail")
class InstancePublicPorts(core.Resource):
    """
    ID of the resource.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the Lightsail Instance.
    """
    instance_name: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block with port information. AWS closes all currently open ports that are n
    ot included in the `port_info`. Detailed below.
    """
    port_info: list[PortInfo] | core.ArrayOut[PortInfo] = core.attr(PortInfo, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_name: str | core.StringOut,
        port_info: list[PortInfo] | core.ArrayOut[PortInfo],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstancePublicPorts.Args(
                instance_name=instance_name,
                port_info=port_info,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_name: str | core.StringOut = core.arg()

        port_info: list[PortInfo] | core.ArrayOut[PortInfo] = core.arg()
