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


@core.data(type="aws_ec2_instance_type_offering", namespace="ec2")
class DsInstanceTypeOffering(core.Data):
    """
    (Optional) One or more configuration blocks containing name-values filters. See the [EC2 API Referen
    ce](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypeOfferings.html) f
    or supported filters. Detailed below.
    """

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    EC2 Instance Type.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    EC2 Instance Type.
    """
    instance_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Location type. Defaults to `region`. Valid values: `availability-zone`, `availability-zon
    e-id`, and `region`.
    """
    location_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Ordered list of preferred EC2 Instance Types. The first match in this list will be return
    ed. If no preferred matches are found and the original search returned more than one result, an erro
    r is returned.
    """
    preferred_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        location_type: str | core.StringOut | None = None,
        preferred_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInstanceTypeOffering.Args(
                filter=filter,
                location_type=location_type,
                preferred_instance_types=preferred_instance_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        location_type: str | core.StringOut | None = core.arg(default=None)

        preferred_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
