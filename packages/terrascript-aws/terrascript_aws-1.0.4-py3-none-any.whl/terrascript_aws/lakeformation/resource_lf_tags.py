import terrascript.core as core


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


@core.schema
class LfTag(core.Schema):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LfTag.Args(
                key=key,
                value=value,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_lakeformation_resource_lf_tags", namespace="lakeformation")
class ResourceLfTags(core.Resource):
    """
    (Optional) Identifier for the Data Catalog. By default, it is the account ID of the caller.
    """

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block for a database resource. See below.
    """
    database: Database | None = core.attr(Database, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    lf_tag: list[LfTag] | core.ArrayOut[LfTag] = core.attr(LfTag, kind=core.Kind.array)

    """
    (Optional) Configuration block for a table resource. See below.
    """
    table: Table | None = core.attr(Table, default=None, computed=True)

    """
    (Optional) Configuration block for a table with columns resource. See below.
    """
    table_with_columns: TableWithColumns | None = core.attr(
        TableWithColumns, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        lf_tag: list[LfTag] | core.ArrayOut[LfTag],
        catalog_id: str | core.StringOut | None = None,
        database: Database | None = None,
        table: Table | None = None,
        table_with_columns: TableWithColumns | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceLfTags.Args(
                lf_tag=lf_tag,
                catalog_id=catalog_id,
                database=database,
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

        database: Database | None = core.arg(default=None)

        lf_tag: list[LfTag] | core.ArrayOut[LfTag] = core.arg()

        table: Table | None = core.arg(default=None)

        table_with_columns: TableWithColumns | None = core.arg(default=None)
