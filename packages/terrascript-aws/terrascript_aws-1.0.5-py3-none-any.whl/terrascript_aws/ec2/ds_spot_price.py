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


@core.data(type="aws_ec2_spot_price", namespace="ec2")
class DsSpotPrice(core.Data):
    """
    (Optional) The availability zone in which to query Spot price information.
    """

    availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) One or more configuration blocks containing name-values filters. See the [EC2 API Referen
    ce](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotPriceHistory.html) for su
    pported filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    AWS Region.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The type of instance for which to query Spot Price information.
    """
    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    The most recent Spot Price value for the given instance type and AZ.
    """
    spot_price: str | core.StringOut = core.attr(str, computed=True)

    """
    The timestamp at which the Spot Price value was published.
    """
    spot_price_timestamp: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        availability_zone: str | core.StringOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        instance_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSpotPrice.Args(
                availability_zone=availability_zone,
                filter=filter,
                instance_type=instance_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)
