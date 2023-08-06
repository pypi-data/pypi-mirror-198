import terrascript.core as core


@core.schema
class LocalSecondaryIndex(core.Schema):

    name: str | core.StringOut = core.attr(str)

    non_key_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    projection_type: str | core.StringOut = core.attr(str)

    range_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        projection_type: str | core.StringOut,
        range_key: str | core.StringOut,
        non_key_attributes: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=LocalSecondaryIndex.Args(
                name=name,
                projection_type=projection_type,
                range_key=range_key,
                non_key_attributes=non_key_attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        non_key_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        projection_type: str | core.StringOut = core.arg()

        range_key: str | core.StringOut = core.arg()


@core.schema
class PointInTimeRecovery(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=PointInTimeRecovery.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class Replica(core.Schema):

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    point_in_time_recovery: bool | core.BoolOut | None = core.attr(bool, default=None)

    propagate_tags: bool | core.BoolOut | None = core.attr(bool, default=None)

    region_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        region_name: str | core.StringOut,
        kms_key_arn: str | core.StringOut | None = None,
        point_in_time_recovery: bool | core.BoolOut | None = None,
        propagate_tags: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Replica.Args(
                region_name=region_name,
                kms_key_arn=kms_key_arn,
                point_in_time_recovery=point_in_time_recovery,
                propagate_tags=propagate_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        point_in_time_recovery: bool | core.BoolOut | None = core.arg(default=None)

        propagate_tags: bool | core.BoolOut | None = core.arg(default=None)

        region_name: str | core.StringOut = core.arg()


@core.schema
class ServerSideEncryption(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        kms_key_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ServerSideEncryption.Args(
                enabled=enabled,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class GlobalSecondaryIndex(core.Schema):

    hash_key: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    non_key_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    projection_type: str | core.StringOut = core.attr(str)

    range_key: str | core.StringOut | None = core.attr(str, default=None)

    read_capacity: int | core.IntOut | None = core.attr(int, default=None)

    write_capacity: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        hash_key: str | core.StringOut,
        name: str | core.StringOut,
        projection_type: str | core.StringOut,
        non_key_attributes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        range_key: str | core.StringOut | None = None,
        read_capacity: int | core.IntOut | None = None,
        write_capacity: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=GlobalSecondaryIndex.Args(
                hash_key=hash_key,
                name=name,
                projection_type=projection_type,
                non_key_attributes=non_key_attributes,
                range_key=range_key,
                read_capacity=read_capacity,
                write_capacity=write_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hash_key: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        non_key_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        projection_type: str | core.StringOut = core.arg()

        range_key: str | core.StringOut | None = core.arg(default=None)

        read_capacity: int | core.IntOut | None = core.arg(default=None)

        write_capacity: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Attribute(core.Schema):

    name: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Attribute.Args(
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class Ttl(core.Schema):

    attribute_name: str | core.StringOut = core.attr(str)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        attribute_name: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Ttl.Args(
                attribute_name=attribute_name,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute_name: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_dynamodb_table", namespace="dynamodb")
class Table(core.Resource):
    """
    ARN of the table
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Set of nested attribute definitions. Only required for `hash_key` and `range_key` attribu
    tes. See below.
    """
    attribute: list[Attribute] | core.ArrayOut[Attribute] | None = core.attr(
        Attribute, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Controls how you are charged for read and write throughput and how you manage capacity. T
    he valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
    """
    billing_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Describe a GSI for the table; subject to the normal limits on the number of GSIs, project
    ed attributes, etc. See below.
    """
    global_secondary_index: list[GlobalSecondaryIndex] | core.ArrayOut[
        GlobalSecondaryIndex
    ] | None = core.attr(GlobalSecondaryIndex, default=None, kind=core.Kind.array)

    """
    (Required, Forces new resource) Attribute to use as the hash (partition) key. Must also be defined a
    s an `attribute`. See below.
    """
    hash_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Name of the table
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) Describe an LSI on the table; these can only be allocated *at creati
    on* so you cannot change this definition after you have created the resource. See below.
    """
    local_secondary_index: list[LocalSecondaryIndex] | core.ArrayOut[
        LocalSecondaryIndex
    ] | None = core.attr(LocalSecondaryIndex, default=None, kind=core.Kind.array)

    """
    (Required) Unique within a region name of the table.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Enable point-in-time recovery options. See below.
    """
    point_in_time_recovery: PointInTimeRecovery | None = core.attr(
        PointInTimeRecovery, default=None, computed=True
    )

    """
    (Optional, Forces new resource) Attribute to use as the range (sort) key. Must also be defined as an
    attribute`, see below.
    """
    range_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Number of read units for this table. If the `billing_mode` is `PROVISIONED`, this field i
    s required.
    """
    read_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Configuration block(s) with [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs
    .aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) replication configuration
    s. See below.
    """
    replica: list[Replica] | core.ArrayOut[Replica] | None = core.attr(
        Replica, default=None, kind=core.Kind.array
    )

    """
    (Optional) Time of the point-in-time recovery point to restore.
    """
    restore_date_time: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the table to restore. Must match the name of an existing table.
    """
    restore_source_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) If set, restores table to the most recent point-in-time recovery point.
    """
    restore_to_latest_time: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with
    an AWS-owned Customer Master Key if this argument isn't specified. See below.
    """
    server_side_encryption: ServerSideEncryption | None = core.attr(
        ServerSideEncryption, default=None, computed=True
    )

    """
    ARN of the Table Stream. Only available when `stream_enabled = true`
    """
    stream_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether Streams are enabled.
    """
    stream_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not a unique identifier
    for the stream on its own. However, the combination of AWS customer ID, table name and this field is
    guaranteed to be unique. It can be used for creating CloudWatch Alarms. Only available when `stream
    _enabled = true`
    """
    stream_label: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) When an item in the table is modified, StreamViewType determines what information is writ
    ten to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAG
    ES`.
    """
    stream_view_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Storage class of the table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`.
    """
    table_class: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to populate on the created table. If configured with a provider [`default_t
    ags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_
    tags-configuration-block) present, tags with matching keys will overwrite those defined at the provi
    der-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Configuration block for TTL. See below.
    """
    ttl: Ttl | None = core.attr(Ttl, default=None, computed=True)

    """
    (Optional) Number of write units for this table. If the `billing_mode` is `PROVISIONED`, this field
    is required.
    """
    write_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        attribute: list[Attribute] | core.ArrayOut[Attribute] | None = None,
        billing_mode: str | core.StringOut | None = None,
        global_secondary_index: list[GlobalSecondaryIndex]
        | core.ArrayOut[GlobalSecondaryIndex]
        | None = None,
        hash_key: str | core.StringOut | None = None,
        local_secondary_index: list[LocalSecondaryIndex]
        | core.ArrayOut[LocalSecondaryIndex]
        | None = None,
        point_in_time_recovery: PointInTimeRecovery | None = None,
        range_key: str | core.StringOut | None = None,
        read_capacity: int | core.IntOut | None = None,
        replica: list[Replica] | core.ArrayOut[Replica] | None = None,
        restore_date_time: str | core.StringOut | None = None,
        restore_source_name: str | core.StringOut | None = None,
        restore_to_latest_time: bool | core.BoolOut | None = None,
        server_side_encryption: ServerSideEncryption | None = None,
        stream_enabled: bool | core.BoolOut | None = None,
        stream_view_type: str | core.StringOut | None = None,
        table_class: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        ttl: Ttl | None = None,
        write_capacity: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Table.Args(
                name=name,
                attribute=attribute,
                billing_mode=billing_mode,
                global_secondary_index=global_secondary_index,
                hash_key=hash_key,
                local_secondary_index=local_secondary_index,
                point_in_time_recovery=point_in_time_recovery,
                range_key=range_key,
                read_capacity=read_capacity,
                replica=replica,
                restore_date_time=restore_date_time,
                restore_source_name=restore_source_name,
                restore_to_latest_time=restore_to_latest_time,
                server_side_encryption=server_side_encryption,
                stream_enabled=stream_enabled,
                stream_view_type=stream_view_type,
                table_class=table_class,
                tags=tags,
                tags_all=tags_all,
                ttl=ttl,
                write_capacity=write_capacity,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attribute: list[Attribute] | core.ArrayOut[Attribute] | None = core.arg(default=None)

        billing_mode: str | core.StringOut | None = core.arg(default=None)

        global_secondary_index: list[GlobalSecondaryIndex] | core.ArrayOut[
            GlobalSecondaryIndex
        ] | None = core.arg(default=None)

        hash_key: str | core.StringOut | None = core.arg(default=None)

        local_secondary_index: list[LocalSecondaryIndex] | core.ArrayOut[
            LocalSecondaryIndex
        ] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        point_in_time_recovery: PointInTimeRecovery | None = core.arg(default=None)

        range_key: str | core.StringOut | None = core.arg(default=None)

        read_capacity: int | core.IntOut | None = core.arg(default=None)

        replica: list[Replica] | core.ArrayOut[Replica] | None = core.arg(default=None)

        restore_date_time: str | core.StringOut | None = core.arg(default=None)

        restore_source_name: str | core.StringOut | None = core.arg(default=None)

        restore_to_latest_time: bool | core.BoolOut | None = core.arg(default=None)

        server_side_encryption: ServerSideEncryption | None = core.arg(default=None)

        stream_enabled: bool | core.BoolOut | None = core.arg(default=None)

        stream_view_type: str | core.StringOut | None = core.arg(default=None)

        table_class: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        ttl: Ttl | None = core.arg(default=None)

        write_capacity: int | core.IntOut | None = core.arg(default=None)
