import terrascript.core as core


@core.schema
class S3Configuration(core.Schema):

    bucket_name: str | core.StringOut | None = core.attr(str, default=None)

    encryption_option: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    object_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut | None = None,
        encryption_option: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        object_key_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Configuration.Args(
                bucket_name=bucket_name,
                encryption_option=encryption_option,
                kms_key_id=kms_key_id,
                object_key_prefix=object_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut | None = core.arg(default=None)

        encryption_option: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        object_key_prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MagneticStoreRejectedDataLocation(core.Schema):

    s3_configuration: S3Configuration | None = core.attr(S3Configuration, default=None)

    def __init__(
        self,
        *,
        s3_configuration: S3Configuration | None = None,
    ):
        super().__init__(
            args=MagneticStoreRejectedDataLocation.Args(
                s3_configuration=s3_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_configuration: S3Configuration | None = core.arg(default=None)


@core.schema
class MagneticStoreWriteProperties(core.Schema):

    enable_magnetic_store_writes: bool | core.BoolOut | None = core.attr(bool, default=None)

    magnetic_store_rejected_data_location: MagneticStoreRejectedDataLocation | None = core.attr(
        MagneticStoreRejectedDataLocation, default=None
    )

    def __init__(
        self,
        *,
        enable_magnetic_store_writes: bool | core.BoolOut | None = None,
        magnetic_store_rejected_data_location: MagneticStoreRejectedDataLocation | None = None,
    ):
        super().__init__(
            args=MagneticStoreWriteProperties.Args(
                enable_magnetic_store_writes=enable_magnetic_store_writes,
                magnetic_store_rejected_data_location=magnetic_store_rejected_data_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_magnetic_store_writes: bool | core.BoolOut | None = core.arg(default=None)

        magnetic_store_rejected_data_location: MagneticStoreRejectedDataLocation | None = core.arg(
            default=None
        )


@core.schema
class RetentionProperties(core.Schema):

    magnetic_store_retention_period_in_days: int | core.IntOut = core.attr(int)

    memory_store_retention_period_in_hours: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        magnetic_store_retention_period_in_days: int | core.IntOut,
        memory_store_retention_period_in_hours: int | core.IntOut,
    ):
        super().__init__(
            args=RetentionProperties.Args(
                magnetic_store_retention_period_in_days=magnetic_store_retention_period_in_days,
                memory_store_retention_period_in_hours=memory_store_retention_period_in_hours,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        magnetic_store_retention_period_in_days: int | core.IntOut = core.arg()

        memory_store_retention_period_in_hours: int | core.IntOut = core.arg()


@core.resource(type="aws_timestreamwrite_table", namespace="timestreamwrite")
class Table(core.Resource):
    """
    The ARN that uniquely identifies this table.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    database_name: str | core.StringOut = core.attr(str)

    """
    The `table_name` and `database_name` separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Contains properties to set on the table when enabling magnetic store writes. See [Magneti
    c Store Write Properties](#magnetic-store-write-properties) below for more details.
    """
    magnetic_store_write_properties: MagneticStoreWriteProperties | None = core.attr(
        MagneticStoreWriteProperties, default=None, computed=True
    )

    """
    (Optional) The retention duration for the memory store and magnetic store. See [Retention Properties
    ](#retention-properties) below for more details. If not provided, `magnetic_store_retention_period_i
    n_days` default to 73000 and `memory_store_retention_period_in_hours` defaults to 6.
    """
    retention_properties: RetentionProperties | None = core.attr(
        RetentionProperties, default=None, computed=True
    )

    """
    (Required) The name of the Timestream table.
    """
    table_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Map of tags to assign to this resource. If configured with a provider [`default_tags` con
    figuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-con
    figuration-block) present, tags with matching keys will overwrite those defined at the provider-leve
    l.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        database_name: str | core.StringOut,
        table_name: str | core.StringOut,
        magnetic_store_write_properties: MagneticStoreWriteProperties | None = None,
        retention_properties: RetentionProperties | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Table.Args(
                database_name=database_name,
                table_name=table_name,
                magnetic_store_write_properties=magnetic_store_write_properties,
                retention_properties=retention_properties,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        database_name: str | core.StringOut = core.arg()

        magnetic_store_write_properties: MagneticStoreWriteProperties | None = core.arg(
            default=None
        )

        retention_properties: RetentionProperties | None = core.arg(default=None)

        table_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
