import terrascript.core as core


@core.data(type="aws_redshift_subnet_group", namespace="redshift")
class DsSubnetGroup(core.Data):
    """
    Amazon Resource Name (ARN) of the Redshift Subnet Group name.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the Redshift Subnet group.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The Redshift Subnet group Name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the cluster subnet group for which information is requested.
    """
    name: str | core.StringOut = core.attr(str)

    """
    An array of VPC subnet IDs.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The tags associated to the Subnet Group
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
