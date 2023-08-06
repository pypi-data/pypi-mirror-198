import terrascript.core as core


@core.schema
class DeviceBlk(core.Schema):

    description: str | core.StringOut | None = core.attr(str, default=None)

    device_name: str | core.StringOut = core.attr(str)

    iot_thing_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        iot_thing_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DeviceBlk.Args(
                device_name=device_name,
                description=description,
                iot_thing_name=iot_thing_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut | None = core.arg(default=None)

        device_name: str | core.StringOut = core.arg()

        iot_thing_name: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_sagemaker_device", namespace="aws_sagemaker")
class Device(core.Resource):

    agent_version: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    device: DeviceBlk = core.attr(DeviceBlk)

    device_fleet_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        device: DeviceBlk,
        device_fleet_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Device.Args(
                device=device,
                device_fleet_name=device_fleet_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device: DeviceBlk = core.arg()

        device_fleet_name: str | core.StringOut = core.arg()
