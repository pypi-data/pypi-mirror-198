import terrascript.core as core


@core.schema
class Ttl(core.Schema):

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=Ttl.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut = core.arg()


@core.schema
class Comment(core.Schema):

    message: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        message: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Comment.Args(
                message=message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CapacitySpecification(core.Schema):

    read_capacity_units: int | core.IntOut | None = core.attr(int, default=None)

    throughput_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    write_capacity_units: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        read_capacity_units: int | core.IntOut | None = None,
        throughput_mode: str | core.StringOut | None = None,
        write_capacity_units: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CapacitySpecification.Args(
                read_capacity_units=read_capacity_units,
                throughput_mode=throughput_mode,
                write_capacity_units=write_capacity_units,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        read_capacity_units: int | core.IntOut | None = core.arg(default=None)

        throughput_mode: str | core.StringOut | None = core.arg(default=None)

        write_capacity_units: int | core.IntOut | None = core.arg(default=None)


@core.schema
class ClusteringKey(core.Schema):

    name: str | core.StringOut = core.attr(str)

    order_by: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        order_by: str | core.StringOut,
    ):
        super().__init__(
            args=ClusteringKey.Args(
                name=name,
                order_by=order_by,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        order_by: str | core.StringOut = core.arg()


@core.schema
class Column(core.Schema):

    name: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Column.Args(
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class PartitionKey(core.Schema):

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=PartitionKey.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class StaticColumn(core.Schema):

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=StaticColumn.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class SchemaDefinition(core.Schema):

    clustering_key: list[ClusteringKey] | core.ArrayOut[ClusteringKey] | None = core.attr(
        ClusteringKey, default=None, kind=core.Kind.array
    )

    column: list[Column] | core.ArrayOut[Column] = core.attr(Column, kind=core.Kind.array)

    partition_key: list[PartitionKey] | core.ArrayOut[PartitionKey] = core.attr(
        PartitionKey, kind=core.Kind.array
    )

    static_column: list[StaticColumn] | core.ArrayOut[StaticColumn] | None = core.attr(
        StaticColumn, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        column: list[Column] | core.ArrayOut[Column],
        partition_key: list[PartitionKey] | core.ArrayOut[PartitionKey],
        clustering_key: list[ClusteringKey] | core.ArrayOut[ClusteringKey] | None = None,
        static_column: list[StaticColumn] | core.ArrayOut[StaticColumn] | None = None,
    ):
        super().__init__(
            args=SchemaDefinition.Args(
                column=column,
                partition_key=partition_key,
                clustering_key=clustering_key,
                static_column=static_column,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        clustering_key: list[ClusteringKey] | core.ArrayOut[ClusteringKey] | None = core.arg(
            default=None
        )

        column: list[Column] | core.ArrayOut[Column] = core.arg()

        partition_key: list[PartitionKey] | core.ArrayOut[PartitionKey] = core.arg()

        static_column: list[StaticColumn] | core.ArrayOut[StaticColumn] | None = core.arg(
            default=None
        )


@core.schema
class PointInTimeRecovery(core.Schema):

    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        status: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PointInTimeRecovery.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EncryptionSpecification(core.Schema):

    kms_key_identifier: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        kms_key_identifier: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EncryptionSpecification.Args(
                kms_key_identifier=kms_key_identifier,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_identifier: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_keyspaces_table", namespace="keyspaces")
class Table(core.Resource):
    """
    The ARN of the table.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the read/write throughput capacity mode for the table.
    """
    capacity_specification: CapacitySpecification | None = core.attr(
        CapacitySpecification, default=None, computed=True
    )

    """
    (Optional) A description of the table.
    """
    comment: Comment | None = core.attr(Comment, default=None, computed=True)

    """
    (Optional) The default Time to Live setting in seconds for the table. More information can be found
    in the [Developer Guide](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html
    #ttl-howitworks_default_ttl).
    """
    default_time_to_live: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Specifies how the encryption key for encryption at rest is managed for the table. More in
    formation can be found in the [Developer Guide](https://docs.aws.amazon.com/keyspaces/latest/devguid
    e/EncryptionAtRest.html).
    """
    encryption_specification: EncryptionSpecification | None = core.attr(
        EncryptionSpecification, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the keyspace that the table is going to be created in.
    """
    keyspace_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies if point-in-time recovery is enabled or disabled for the table. More informatio
    n can be found in the [Developer Guide](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointI
    nTimeRecovery.html).
    """
    point_in_time_recovery: PointInTimeRecovery | None = core.attr(
        PointInTimeRecovery, default=None, computed=True
    )

    """
    (Optional) Describes the schema of the table.
    """
    schema_definition: SchemaDefinition = core.attr(SchemaDefinition)

    """
    (Required) The name of the table.
    """
    table_name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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

    """
    (Optional) Enables Time to Live custom settings for the table. More information can be found in the
    [Developer Guide](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL.html).
    """
    ttl: Ttl | None = core.attr(Ttl, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        keyspace_name: str | core.StringOut,
        schema_definition: SchemaDefinition,
        table_name: str | core.StringOut,
        capacity_specification: CapacitySpecification | None = None,
        comment: Comment | None = None,
        default_time_to_live: int | core.IntOut | None = None,
        encryption_specification: EncryptionSpecification | None = None,
        point_in_time_recovery: PointInTimeRecovery | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        ttl: Ttl | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Table.Args(
                keyspace_name=keyspace_name,
                schema_definition=schema_definition,
                table_name=table_name,
                capacity_specification=capacity_specification,
                comment=comment,
                default_time_to_live=default_time_to_live,
                encryption_specification=encryption_specification,
                point_in_time_recovery=point_in_time_recovery,
                tags=tags,
                tags_all=tags_all,
                ttl=ttl,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_specification: CapacitySpecification | None = core.arg(default=None)

        comment: Comment | None = core.arg(default=None)

        default_time_to_live: int | core.IntOut | None = core.arg(default=None)

        encryption_specification: EncryptionSpecification | None = core.arg(default=None)

        keyspace_name: str | core.StringOut = core.arg()

        point_in_time_recovery: PointInTimeRecovery | None = core.arg(default=None)

        schema_definition: SchemaDefinition = core.arg()

        table_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        ttl: Ttl | None = core.arg(default=None)
