import terrascript.core as core


@core.schema
class PartitionIndexBlk(core.Schema):

    index_name: str | core.StringOut | None = core.attr(str, default=None)

    index_status: str | core.StringOut = core.attr(str, computed=True)

    keys: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        index_status: str | core.StringOut,
        index_name: str | core.StringOut | None = None,
        keys: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=PartitionIndexBlk.Args(
                index_status=index_status,
                index_name=index_name,
                keys=keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_name: str | core.StringOut | None = core.arg(default=None)

        index_status: str | core.StringOut = core.arg()

        keys: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_glue_partition_index", namespace="glue")
class PartitionIndex(core.Resource):
    """
    (Optional) The catalog ID where the table resides.
    """

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Name of the metadata database where the table metadata resides. For Hive compatibility, t
    his must be all lowercase.
    """
    database_name: str | core.StringOut = core.attr(str)

    """
    Catalog ID, Database name, table name, and index name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block for a partition index. See [`partition_index`](#partition_index) belo
    w.
    """
    partition_index: PartitionIndexBlk = core.attr(PartitionIndexBlk)

    """
    (Required) Name of the table. For Hive compatibility, this must be entirely lowercase.
    """
    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        database_name: str | core.StringOut,
        partition_index: PartitionIndexBlk,
        table_name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PartitionIndex.Args(
                database_name=database_name,
                partition_index=partition_index,
                table_name=table_name,
                catalog_id=catalog_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut = core.arg()

        partition_index: PartitionIndexBlk = core.arg()

        table_name: str | core.StringOut = core.arg()
