import terrascript.core as core


@core.schema
class GlobalSecondaryIndex(core.Schema):

    hash_key: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    non_key_attributes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    projection_type: str | core.StringOut = core.attr(str, computed=True)

    range_key: str | core.StringOut = core.attr(str, computed=True)

    read_capacity: int | core.IntOut = core.attr(int, computed=True)

    write_capacity: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        hash_key: str | core.StringOut,
        name: str | core.StringOut,
        non_key_attributes: list[str] | core.ArrayOut[core.StringOut],
        projection_type: str | core.StringOut,
        range_key: str | core.StringOut,
        read_capacity: int | core.IntOut,
        write_capacity: int | core.IntOut,
    ):
        super().__init__(
            args=GlobalSecondaryIndex.Args(
                hash_key=hash_key,
                name=name,
                non_key_attributes=non_key_attributes,
                projection_type=projection_type,
                range_key=range_key,
                read_capacity=read_capacity,
                write_capacity=write_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hash_key: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        non_key_attributes: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        projection_type: str | core.StringOut = core.arg()

        range_key: str | core.StringOut = core.arg()

        read_capacity: int | core.IntOut = core.arg()

        write_capacity: int | core.IntOut = core.arg()


@core.schema
class Ttl(core.Schema):

    attribute_name: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        attribute_name: str | core.StringOut,
        enabled: bool | core.BoolOut,
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

        enabled: bool | core.BoolOut = core.arg()


@core.schema
class Attribute(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

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
class LocalSecondaryIndex(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    non_key_attributes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    projection_type: str | core.StringOut = core.attr(str, computed=True)

    range_key: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        non_key_attributes: list[str] | core.ArrayOut[core.StringOut],
        projection_type: str | core.StringOut,
        range_key: str | core.StringOut,
    ):
        super().__init__(
            args=LocalSecondaryIndex.Args(
                name=name,
                non_key_attributes=non_key_attributes,
                projection_type=projection_type,
                range_key=range_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        non_key_attributes: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        projection_type: str | core.StringOut = core.arg()

        range_key: str | core.StringOut = core.arg()


@core.schema
class Replica(core.Schema):

    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    region_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        kms_key_arn: str | core.StringOut,
        region_name: str | core.StringOut,
    ):
        super().__init__(
            args=Replica.Args(
                kms_key_arn=kms_key_arn,
                region_name=region_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_arn: str | core.StringOut = core.arg()

        region_name: str | core.StringOut = core.arg()


@core.schema
class ServerSideEncryption(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        kms_key_arn: str | core.StringOut,
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

        kms_key_arn: str | core.StringOut = core.arg()


@core.schema
class PointInTimeRecovery(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

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


@core.data(type="aws_dynamodb_table", namespace="dynamodb")
class DsTable(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    attribute: list[Attribute] | core.ArrayOut[Attribute] = core.attr(
        Attribute, computed=True, kind=core.Kind.array
    )

    billing_mode: str | core.StringOut = core.attr(str, computed=True)

    global_secondary_index: list[GlobalSecondaryIndex] | core.ArrayOut[
        GlobalSecondaryIndex
    ] = core.attr(GlobalSecondaryIndex, computed=True, kind=core.Kind.array)

    hash_key: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    local_secondary_index: list[LocalSecondaryIndex] | core.ArrayOut[
        LocalSecondaryIndex
    ] = core.attr(LocalSecondaryIndex, computed=True, kind=core.Kind.array)

    """
    (Required) The name of the DynamoDB table.
    """
    name: str | core.StringOut = core.attr(str)

    point_in_time_recovery: list[PointInTimeRecovery] | core.ArrayOut[
        PointInTimeRecovery
    ] = core.attr(PointInTimeRecovery, computed=True, kind=core.Kind.array)

    range_key: str | core.StringOut = core.attr(str, computed=True)

    read_capacity: int | core.IntOut = core.attr(int, computed=True)

    replica: list[Replica] | core.ArrayOut[Replica] = core.attr(
        Replica, computed=True, kind=core.Kind.array
    )

    server_side_encryption: ServerSideEncryption | None = core.attr(
        ServerSideEncryption, default=None, computed=True
    )

    stream_arn: str | core.StringOut = core.attr(str, computed=True)

    stream_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    stream_label: str | core.StringOut = core.attr(str, computed=True)

    stream_view_type: str | core.StringOut = core.attr(str, computed=True)

    table_class: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    ttl: list[Ttl] | core.ArrayOut[Ttl] = core.attr(Ttl, computed=True, kind=core.Kind.array)

    write_capacity: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        server_side_encryption: ServerSideEncryption | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsTable.Args(
                name=name,
                server_side_encryption=server_side_encryption,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        server_side_encryption: ServerSideEncryption | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
