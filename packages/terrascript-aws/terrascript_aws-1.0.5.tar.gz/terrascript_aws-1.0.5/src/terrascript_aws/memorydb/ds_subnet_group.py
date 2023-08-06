import terrascript.core as core


@core.data(type="aws_memorydb_subnet_group", namespace="memorydb")
class DsSubnetGroup(core.Data):
    """
    ARN of the subnet group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the subnet group.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the subnet group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the subnet group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Set of VPC Subnet ID-s of the subnet group.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    A map of tags assigned to the subnet group.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The VPC in which the subnet group exists.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSubnetGroup.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
