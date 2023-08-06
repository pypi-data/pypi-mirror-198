import terrascript.core as core


@core.schema
class SortColumns(core.Schema):

    column: str | core.StringOut = core.attr(str)

    sort_order: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        column: str | core.StringOut,
        sort_order: int | core.IntOut,
    ):
        super().__init__(
            args=SortColumns.Args(
                column=column,
                sort_order=sort_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        column: str | core.StringOut = core.arg()

        sort_order: int | core.IntOut = core.arg()


@core.schema
class Columns(core.Schema):

    comment: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Columns.Args(
                name=name,
                comment=comment,
                parameters=parameters,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comment: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SkewedInfo(core.Schema):

    skewed_column_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    skewed_column_value_location_maps: dict[str, str] | core.MapOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.map)

    skewed_column_values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        skewed_column_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        skewed_column_value_location_maps: dict[str, str]
        | core.MapOut[core.StringOut]
        | None = None,
        skewed_column_values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=SkewedInfo.Args(
                skewed_column_names=skewed_column_names,
                skewed_column_value_location_maps=skewed_column_value_location_maps,
                skewed_column_values=skewed_column_values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        skewed_column_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        skewed_column_value_location_maps: dict[str, str] | core.MapOut[
            core.StringOut
        ] | None = core.arg(default=None)

        skewed_column_values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class SerDeInfo(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    serialization_library: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        serialization_library: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SerDeInfo.Args(
                name=name,
                parameters=parameters,
                serialization_library=serialization_library,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        serialization_library: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SchemaId(core.Schema):

    registry_name: str | core.StringOut | None = core.attr(str, default=None)

    schema_arn: str | core.StringOut | None = core.attr(str, default=None)

    schema_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        registry_name: str | core.StringOut | None = None,
        schema_arn: str | core.StringOut | None = None,
        schema_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SchemaId.Args(
                registry_name=registry_name,
                schema_arn=schema_arn,
                schema_name=schema_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        registry_name: str | core.StringOut | None = core.arg(default=None)

        schema_arn: str | core.StringOut | None = core.arg(default=None)

        schema_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SchemaReference(core.Schema):

    schema_id: SchemaId | None = core.attr(SchemaId, default=None)

    schema_version_id: str | core.StringOut | None = core.attr(str, default=None)

    schema_version_number: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        schema_version_number: int | core.IntOut,
        schema_id: SchemaId | None = None,
        schema_version_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SchemaReference.Args(
                schema_version_number=schema_version_number,
                schema_id=schema_id,
                schema_version_id=schema_version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        schema_id: SchemaId | None = core.arg(default=None)

        schema_version_id: str | core.StringOut | None = core.arg(default=None)

        schema_version_number: int | core.IntOut = core.arg()


@core.schema
class StorageDescriptor(core.Schema):

    bucket_columns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    columns: list[Columns] | core.ArrayOut[Columns] | None = core.attr(
        Columns, default=None, computed=True, kind=core.Kind.array
    )

    compressed: bool | core.BoolOut | None = core.attr(bool, default=None)

    input_format: str | core.StringOut | None = core.attr(str, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    number_of_buckets: int | core.IntOut | None = core.attr(int, default=None)

    output_format: str | core.StringOut | None = core.attr(str, default=None)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    schema_reference: SchemaReference | None = core.attr(SchemaReference, default=None)

    ser_de_info: SerDeInfo | None = core.attr(SerDeInfo, default=None)

    skewed_info: SkewedInfo | None = core.attr(SkewedInfo, default=None)

    sort_columns: list[SortColumns] | core.ArrayOut[SortColumns] | None = core.attr(
        SortColumns, default=None, kind=core.Kind.array
    )

    stored_as_sub_directories: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        bucket_columns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        columns: list[Columns] | core.ArrayOut[Columns] | None = None,
        compressed: bool | core.BoolOut | None = None,
        input_format: str | core.StringOut | None = None,
        location: str | core.StringOut | None = None,
        number_of_buckets: int | core.IntOut | None = None,
        output_format: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        schema_reference: SchemaReference | None = None,
        ser_de_info: SerDeInfo | None = None,
        skewed_info: SkewedInfo | None = None,
        sort_columns: list[SortColumns] | core.ArrayOut[SortColumns] | None = None,
        stored_as_sub_directories: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=StorageDescriptor.Args(
                bucket_columns=bucket_columns,
                columns=columns,
                compressed=compressed,
                input_format=input_format,
                location=location,
                number_of_buckets=number_of_buckets,
                output_format=output_format,
                parameters=parameters,
                schema_reference=schema_reference,
                ser_de_info=ser_de_info,
                skewed_info=skewed_info,
                sort_columns=sort_columns,
                stored_as_sub_directories=stored_as_sub_directories,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_columns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        columns: list[Columns] | core.ArrayOut[Columns] | None = core.arg(default=None)

        compressed: bool | core.BoolOut | None = core.arg(default=None)

        input_format: str | core.StringOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        number_of_buckets: int | core.IntOut | None = core.arg(default=None)

        output_format: str | core.StringOut | None = core.arg(default=None)

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        schema_reference: SchemaReference | None = core.arg(default=None)

        ser_de_info: SerDeInfo | None = core.arg(default=None)

        skewed_info: SkewedInfo | None = core.arg(default=None)

        sort_columns: list[SortColumns] | core.ArrayOut[SortColumns] | None = core.arg(default=None)

        stored_as_sub_directories: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class TargetTable(core.Schema):

    catalog_id: str | core.StringOut = core.attr(str)

    database_name: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        catalog_id: str | core.StringOut,
        database_name: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=TargetTable.Args(
                catalog_id=catalog_id,
                database_name=database_name,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut = core.arg()

        database_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class PartitionIndex(core.Schema):

    index_name: str | core.StringOut = core.attr(str)

    index_status: str | core.StringOut = core.attr(str, computed=True)

    keys: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        index_name: str | core.StringOut,
        index_status: str | core.StringOut,
        keys: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=PartitionIndex.Args(
                index_name=index_name,
                index_status=index_status,
                keys=keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_name: str | core.StringOut = core.arg()

        index_status: str | core.StringOut = core.arg()

        keys: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class PartitionKeys(core.Schema):

    comment: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PartitionKeys.Args(
                name=name,
                comment=comment,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comment: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_glue_catalog_table", namespace="glue")
class CatalogTable(core.Resource):
    """
    The ARN of the Glue Table.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ID of the Glue Catalog and database to create the table in. If omitted, this defaults to
    the AWS Account ID plus the database name.
    """
    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Name of the metadata database where the table metadata resides. For Hive compatibility, t
    his must be all lowercase.
    """
    database_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Description of the table.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Catalog ID, Database name and of the name table.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the table. For Hive compatibility, this must be entirely lowercase.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Owner of the table.
    """
    owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Properties associated with this table, as a list of key-value pairs.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Configuration block for a maximum of 3 partition indexes. See [`partition_index`](#partit
    ion_index) below.
    """
    partition_index: list[PartitionIndex] | core.ArrayOut[PartitionIndex] | None = core.attr(
        PartitionIndex, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block of columns by which the table is partitioned. Only primitive types ar
    e supported as partition keys. See [`partition_keys`](#partition_keys) below.
    """
    partition_keys: list[PartitionKeys] | core.ArrayOut[PartitionKeys] | None = core.attr(
        PartitionKeys, default=None, kind=core.Kind.array
    )

    """
    (Optional) Retention time for this table.
    """
    retention: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Configuration block for information about the physical storage of this table. For more in
    formation, refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-a
    pi-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor). See [`storage_descriptor`](#s
    torage_descriptor) below.
    """
    storage_descriptor: StorageDescriptor | None = core.attr(StorageDescriptor, default=None)

    """
    (Optional) Type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.). While optional, some Athena DDL
    queries such as `ALTER TABLE` and `SHOW CREATE TABLE` will fail if this argument is empty.
    """
    table_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block of a target table for resource linking. See [`target_table`](#target_
    table) below.
    """
    target_table: TargetTable | None = core.attr(TargetTable, default=None)

    """
    (Optional) If the table is a view, the expanded text of the view; otherwise null.
    """
    view_expanded_text: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) If the table is a view, the original text of the view; otherwise null.
    """
    view_original_text: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        database_name: str | core.StringOut,
        name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        owner: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        partition_index: list[PartitionIndex] | core.ArrayOut[PartitionIndex] | None = None,
        partition_keys: list[PartitionKeys] | core.ArrayOut[PartitionKeys] | None = None,
        retention: int | core.IntOut | None = None,
        storage_descriptor: StorageDescriptor | None = None,
        table_type: str | core.StringOut | None = None,
        target_table: TargetTable | None = None,
        view_expanded_text: str | core.StringOut | None = None,
        view_original_text: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CatalogTable.Args(
                database_name=database_name,
                name=name,
                catalog_id=catalog_id,
                description=description,
                owner=owner,
                parameters=parameters,
                partition_index=partition_index,
                partition_keys=partition_keys,
                retention=retention,
                storage_descriptor=storage_descriptor,
                table_type=table_type,
                target_table=target_table,
                view_expanded_text=view_expanded_text,
                view_original_text=view_original_text,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        owner: str | core.StringOut | None = core.arg(default=None)

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        partition_index: list[PartitionIndex] | core.ArrayOut[PartitionIndex] | None = core.arg(
            default=None
        )

        partition_keys: list[PartitionKeys] | core.ArrayOut[PartitionKeys] | None = core.arg(
            default=None
        )

        retention: int | core.IntOut | None = core.arg(default=None)

        storage_descriptor: StorageDescriptor | None = core.arg(default=None)

        table_type: str | core.StringOut | None = core.arg(default=None)

        target_table: TargetTable | None = core.arg(default=None)

        view_expanded_text: str | core.StringOut | None = core.arg(default=None)

        view_original_text: str | core.StringOut | None = core.arg(default=None)
