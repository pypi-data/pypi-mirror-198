import terrascript.core as core


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
class Columns(core.Schema):

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
            args=Columns.Args(
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
class StorageDescriptor(core.Schema):

    bucket_columns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    columns: list[Columns] | core.ArrayOut[Columns] | None = core.attr(
        Columns, default=None, kind=core.Kind.array
    )

    compressed: bool | core.BoolOut | None = core.attr(bool, default=None)

    input_format: str | core.StringOut | None = core.attr(str, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    number_of_buckets: int | core.IntOut | None = core.attr(int, default=None)

    output_format: str | core.StringOut | None = core.attr(str, default=None)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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

        ser_de_info: SerDeInfo | None = core.arg(default=None)

        skewed_info: SkewedInfo | None = core.arg(default=None)

        sort_columns: list[SortColumns] | core.ArrayOut[SortColumns] | None = core.arg(default=None)

        stored_as_sub_directories: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_glue_partition", namespace="glue")
class Partition(core.Resource):
    """
    (Optional) ID of the Glue Catalog and database to create the table in. If omitted, this defaults to
    the AWS Account ID plus the database name.
    """

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The time at which the partition was created.
    """
    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the metadata database where the table metadata resides. For Hive compatibility, t
    his must be all lowercase.
    """
    database_name: str | core.StringOut = core.attr(str)

    """
    partition id.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last time at which the partition was accessed.
    """
    last_accessed_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The last time at which column statistics were computed for this partition.
    """
    last_analyzed_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Properties associated with this table, as a list of key-value pairs.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Required) The values that define the partition.
    """
    partition_values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) A [storage descriptor](#storage_descriptor) object containing information about the physi
    cal storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/g
    lue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a
    full explanation of this object.
    """
    storage_descriptor: StorageDescriptor | None = core.attr(StorageDescriptor, default=None)

    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        database_name: str | core.StringOut,
        partition_values: list[str] | core.ArrayOut[core.StringOut],
        table_name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        storage_descriptor: StorageDescriptor | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Partition.Args(
                database_name=database_name,
                partition_values=partition_values,
                table_name=table_name,
                catalog_id=catalog_id,
                parameters=parameters,
                storage_descriptor=storage_descriptor,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut = core.arg()

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        partition_values: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        storage_descriptor: StorageDescriptor | None = core.arg(default=None)

        table_name: str | core.StringOut = core.arg()
