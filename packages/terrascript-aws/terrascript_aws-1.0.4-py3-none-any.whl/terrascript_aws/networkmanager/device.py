import terrascript.core as core


@core.schema
class AwsLocation(core.Schema):

    subnet_arn: str | core.StringOut | None = core.attr(str, default=None)

    zone: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        subnet_arn: str | core.StringOut | None = None,
        zone: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AwsLocation.Args(
                subnet_arn=subnet_arn,
                zone=zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_arn: str | core.StringOut | None = core.arg(default=None)

        zone: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Location(core.Schema):

    address: str | core.StringOut | None = core.attr(str, default=None)

    latitude: str | core.StringOut | None = core.attr(str, default=None)

    longitude: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        address: str | core.StringOut | None = None,
        latitude: str | core.StringOut | None = None,
        longitude: str | core.StringOut | None = None,
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
        address: str | core.StringOut | None = core.arg(default=None)

        latitude: str | core.StringOut | None = core.arg(default=None)

        longitude: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_networkmanager_device", namespace="networkmanager")
class Device(core.Resource):
    """
    The Amazon Resource Name (ARN) of the device.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The AWS location of the device. Documented below.
    """
    aws_location: AwsLocation | None = core.attr(AwsLocation, default=None)

    """
    (Optional) A description of the device.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the global network.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The location of the device. Documented below.
    """
    location: Location | None = core.attr(Location, default=None)

    """
    (Optional) The model of device.
    """
    model: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The serial number of the device.
    """
    serial_number: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ID of the site.
    """
    site_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value tags for the device. If configured with a provider [`default_tags` configuratio
    n block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuratio
    n-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) The type of device.
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The vendor of the device.
    """
    vendor: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        global_network_id: str | core.StringOut,
        aws_location: AwsLocation | None = None,
        description: str | core.StringOut | None = None,
        location: Location | None = None,
        model: str | core.StringOut | None = None,
        serial_number: str | core.StringOut | None = None,
        site_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        vendor: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Device.Args(
                global_network_id=global_network_id,
                aws_location=aws_location,
                description=description,
                location=location,
                model=model,
                serial_number=serial_number,
                site_id=site_id,
                tags=tags,
                tags_all=tags_all,
                type=type,
                vendor=vendor,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_location: AwsLocation | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        global_network_id: str | core.StringOut = core.arg()

        location: Location | None = core.arg(default=None)

        model: str | core.StringOut | None = core.arg(default=None)

        serial_number: str | core.StringOut | None = core.arg(default=None)

        site_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        vendor: str | core.StringOut | None = core.arg(default=None)
