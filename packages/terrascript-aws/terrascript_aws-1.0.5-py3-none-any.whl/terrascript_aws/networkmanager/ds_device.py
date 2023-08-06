import terrascript.core as core


@core.schema
class Location(core.Schema):

    address: str | core.StringOut = core.attr(str, computed=True)

    latitude: str | core.StringOut = core.attr(str, computed=True)

    longitude: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        latitude: str | core.StringOut,
        longitude: str | core.StringOut,
    ):
        super().__init__(
            args=Location.Args(
                address=address,
                latitude=latitude,
                longitude=longitude,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut = core.arg()

        latitude: str | core.StringOut = core.arg()

        longitude: str | core.StringOut = core.arg()


@core.schema
class AwsLocation(core.Schema):

    subnet_arn: str | core.StringOut = core.attr(str, computed=True)

    zone: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        subnet_arn: str | core.StringOut,
        zone: str | core.StringOut,
    ):
        super().__init__(
            args=AwsLocation.Args(
                subnet_arn=subnet_arn,
                zone=zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_arn: str | core.StringOut = core.arg()

        zone: str | core.StringOut = core.arg()


@core.data(type="aws_networkmanager_device", namespace="networkmanager")
class DsDevice(core.Data):
    """
    The Amazon Resource Name (ARN) of the device.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS location of the device. Documented below.
    """
    aws_location: list[AwsLocation] | core.ArrayOut[AwsLocation] = core.attr(
        AwsLocation, computed=True, kind=core.Kind.array
    )

    """
    A description of the device.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the device.
    """
    device_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the global network.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The location of the device. Documented below.
    """
    location: list[Location] | core.ArrayOut[Location] = core.attr(
        Location, computed=True, kind=core.Kind.array
    )

    """
    The model of device.
    """
    model: str | core.StringOut = core.attr(str, computed=True)

    """
    The serial number of the device.
    """
    serial_number: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the site.
    """
    site_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value tags for the device.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The type of device.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    """
    The vendor of the device.
    """
    vendor: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        device_id: str | core.StringOut,
        global_network_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDevice.Args(
                device_id=device_id,
                global_network_id=global_network_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_id: str | core.StringOut = core.arg()

        global_network_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
