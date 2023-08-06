import terrascript.core as core


@core.schema
class Children(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Children.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.data(type="aws_organizations_organizational_units", namespace="organizations")
class DsOrganizationalUnits(core.Data):
    """
    List of child organizational units, which have the following attributes:
    """

    children: list[Children] | core.ArrayOut[Children] = core.attr(
        Children, computed=True, kind=core.Kind.array
    )

    """
    ID of the organizational unit
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The parent ID of the organizational unit.
    """
    parent_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        parent_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsOrganizationalUnits.Args(
                parent_id=parent_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parent_id: str | core.StringOut = core.arg()
