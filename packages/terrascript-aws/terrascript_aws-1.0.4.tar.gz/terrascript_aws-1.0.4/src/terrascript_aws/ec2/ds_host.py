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


@core.data(type="aws_ec2_host", namespace="ec2")
class DsHost(core.Data):
    """
    The ARN of the Dedicated Host.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether auto-placement is on or off.
    """
    auto_placement: str | core.StringOut = core.attr(str, computed=True)

    """
    The Availability Zone of the Dedicated Host.
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of cores on the Dedicated Host.
    """
    cores: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Configuration block. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) The ID of the Dedicated Host.
    """
    host_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Indicates whether host recovery is enabled or disabled for the Dedicated Host.
    """
    host_recovery: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the Dedicated Host.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The instance family supported by the Dedicated Host. For example, "m5".
    """
    instance_family: str | core.StringOut = core.attr(str, computed=True)

    """
    The instance type supported by the Dedicated Host. For example, "m5.large". If the host supports mul
    tiple instance types, no instanceType is returned.
    """
    instance_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the AWS Outpost on which the Dedicated Host is allocated.
    """
    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS account that owns the Dedicated Host.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of sockets on the Dedicated Host.
    """
    sockets: int | core.IntOut = core.attr(int, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The total number of vCPUs on the Dedicated Host.
    """
    total_vcpus: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        host_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsHost.Args(
                filter=filter,
                host_id=host_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        host_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
