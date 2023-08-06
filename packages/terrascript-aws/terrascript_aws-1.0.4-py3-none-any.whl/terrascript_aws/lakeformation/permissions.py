import terrascript.core as core


@core.schema
class DataLocation(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DataLocation.Args(
                arn=arn,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        catalog_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TableWithColumns(core.Schema):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    column_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    database_name: str | core.StringOut = core.attr(str)

    excluded_column_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    wildcard: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        database_name: str | core.StringOut,
        name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        column_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        excluded_column_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        wildcard: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=TableWithColumns.Args(
                database_name=database_name,
                name=name,
                catalog_id=catalog_id,
                column_names=column_names,
                excluded_column_names=excluded_column_names,
                wildcard=wildcard,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        column_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        database_name: str | core.StringOut = core.arg()

        excluded_column_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        wildcard: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Expression(core.Schema):

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Expression.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class LfTagPolicy(core.Schema):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    expression: list[Expression] | core.ArrayOut[Expression] = core.attr(
        Expression, kind=core.Kind.array
    )

    resource_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        expression: list[Expression] | core.ArrayOut[Expression],
        resource_type: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LfTagPolicy.Args(
                expression=expression,
                resource_type=resource_type,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        expression: list[Expression] | core.ArrayOut[Expression] = core.arg()

        resource_type: str | core.StringOut = core.arg()


@core.schema
class Table(core.Schema):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    database_name: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    wildcard: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        database_name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        wildcard: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Table.Args(
                database_name=database_name,
                catalog_id=catalog_id,
                name=name,
                wildcard=wildcard,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        wildcard: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class LfTag(core.Schema):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
        catalog_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LfTag.Args(
                key=key,
                values=values,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Database(core.Schema):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Database.Args(
                name=name,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()


@core.resource(type="aws_lakeformation_permissions", namespace="lakeformation")
class Permissions(core.Resource):
    """
    (Optional) Identifier for the Data Catalog where the location is registered with Lake Formation. By
    default, it is the account ID of the caller.
    """

    catalog_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether the permissions are to be granted for the Data Catalog. Defaults to `false`.
    """
    catalog_resource: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Configuration block for a data location resource. Detailed below.
    """
    data_location: DataLocation | None = core.attr(DataLocation, default=None, computed=True)

    """
    (Optional) Configuration block for a database resource. Detailed below.
    """
    database: Database | None = core.attr(Database, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for an LF-tag resource. Detailed below.
    """
    lf_tag: LfTag | None = core.attr(LfTag, default=None, computed=True)

    """
    (Optional) Configuration block for an LF-tag policy resource. Detailed below.
    """
    lf_tag_policy: LfTagPolicy | None = core.attr(LfTagPolicy, default=None, computed=True)

    permissions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) Subset of `permissions` which the principal can pass.
    """
    permissions_with_grant_option: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    principal: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block for a table resource. Detailed below.
    """
    table: Table | None = core.attr(Table, default=None, computed=True)

    """
    (Optional) Configuration block for a table with columns resource. Detailed below.
    """
    table_with_columns: TableWithColumns | None = core.attr(
        TableWithColumns, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        permissions: list[str] | core.ArrayOut[core.StringOut],
        principal: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        catalog_resource: bool | core.BoolOut | None = None,
        data_location: DataLocation | None = None,
        database: Database | None = None,
        lf_tag: LfTag | None = None,
        lf_tag_policy: LfTagPolicy | None = None,
        permissions_with_grant_option: list[str] | core.ArrayOut[core.StringOut] | None = None,
        table: Table | None = None,
        table_with_columns: TableWithColumns | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permissions.Args(
                permissions=permissions,
                principal=principal,
                catalog_id=catalog_id,
                catalog_resource=catalog_resource,
                data_location=data_location,
                database=database,
                lf_tag=lf_tag,
                lf_tag_policy=lf_tag_policy,
                permissions_with_grant_option=permissions_with_grant_option,
                table=table,
                table_with_columns=table_with_columns,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        catalog_resource: bool | core.BoolOut | None = core.arg(default=None)

        data_location: DataLocation | None = core.arg(default=None)

        database: Database | None = core.arg(default=None)

        lf_tag: LfTag | None = core.arg(default=None)

        lf_tag_policy: LfTagPolicy | None = core.arg(default=None)

        permissions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        permissions_with_grant_option: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        principal: str | core.StringOut = core.arg()

        table: Table | None = core.arg(default=None)

        table_with_columns: TableWithColumns | None = core.arg(default=None)
