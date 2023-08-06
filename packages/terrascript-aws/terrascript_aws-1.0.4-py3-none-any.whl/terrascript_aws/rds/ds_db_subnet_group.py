import terrascript.core as core


@core.data(type="aws_db_subnet_group", namespace="rds")
class DsDbSubnetGroup(core.Data):
    """
    The Amazon Resource Name (ARN) for the DB subnet group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides the description of the DB subnet group.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the RDS database subnet group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Provides the status of the DB subnet group.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Contains a list of subnet identifiers.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The network type of the DB subnet group.
    """
    supported_network_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Provides the VPC ID of the DB subnet group.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDbSubnetGroup.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
