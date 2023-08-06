import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_ec2_instance_type_offerings", namespace="ec2")
class DsInstanceTypeOfferings(core.Data):
    """
    (Optional) One or more configuration blocks containing name-values filters. See the [EC2 API Referen
    ce](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypeOfferings.html) f
    or supported filters. Detailed below.
    """

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    AWS Region.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of EC2 Instance Types.
    """
    instance_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Location type. Defaults to `region`. Valid values: `availability-zone`, `availability-zon
    e-id`, and `region`.
    """
    location_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    List of location types.
    """
    location_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    List of locations.
    """
    locations: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        location_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInstanceTypeOfferings.Args(
                filter=filter,
                location_type=location_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        location_type: str | core.StringOut | None = core.arg(default=None)
