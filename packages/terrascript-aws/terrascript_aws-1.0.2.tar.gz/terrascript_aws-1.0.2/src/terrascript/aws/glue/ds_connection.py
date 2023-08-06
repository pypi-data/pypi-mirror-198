import terrascript.core as core


@core.schema
class PhysicalConnectionRequirements(core.Schema):

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    security_group_id_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zone: str | core.StringOut,
        security_group_id_list: list[str] | core.ArrayOut[core.StringOut],
        subnet_id: str | core.StringOut,
    ):
        super().__init__(
            args=PhysicalConnectionRequirements.Args(
                availability_zone=availability_zone,
                security_group_id_list=security_group_id_list,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut = core.arg()

        security_group_id_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_id: str | core.StringOut = core.arg()


@core.data(type="aws_glue_connection", namespace="aws_glue")
class DsConnection(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    catalog_id: str | core.StringOut = core.attr(str, computed=True)

    connection_properties: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    connection_type: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str)

    match_criteria: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    physical_connection_requirements: list[PhysicalConnectionRequirements] | core.ArrayOut[
        PhysicalConnectionRequirements
    ] = core.attr(PhysicalConnectionRequirements, computed=True, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsConnection.Args(
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
