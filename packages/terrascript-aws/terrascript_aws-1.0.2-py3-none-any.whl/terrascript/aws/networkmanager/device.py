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


@core.resource(type="aws_networkmanager_device", namespace="aws_networkmanager")
class Device(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    aws_location: AwsLocation | None = core.attr(AwsLocation, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    location: Location | None = core.attr(Location, default=None)

    model: str | core.StringOut | None = core.attr(str, default=None)

    serial_number: str | core.StringOut | None = core.attr(str, default=None)

    site_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

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
