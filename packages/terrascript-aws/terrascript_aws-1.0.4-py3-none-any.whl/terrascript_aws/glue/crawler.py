import terrascript.core as core


@core.schema
class SchemaChangePolicy(core.Schema):

    delete_behavior: str | core.StringOut | None = core.attr(str, default=None)

    update_behavior: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        delete_behavior: str | core.StringOut | None = None,
        update_behavior: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SchemaChangePolicy.Args(
                delete_behavior=delete_behavior,
                update_behavior=update_behavior,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_behavior: str | core.StringOut | None = core.arg(default=None)

        update_behavior: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LineageConfiguration(core.Schema):

    crawler_lineage_settings: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        crawler_lineage_settings: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LineageConfiguration.Args(
                crawler_lineage_settings=crawler_lineage_settings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        crawler_lineage_settings: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RecrawlPolicy(core.Schema):

    recrawl_behavior: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        recrawl_behavior: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RecrawlPolicy.Args(
                recrawl_behavior=recrawl_behavior,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        recrawl_behavior: str | core.StringOut | None = core.arg(default=None)


@core.schema
class S3Target(core.Schema):

    connection_name: str | core.StringOut | None = core.attr(str, default=None)

    dlq_event_queue_arn: str | core.StringOut | None = core.attr(str, default=None)

    event_queue_arn: str | core.StringOut | None = core.attr(str, default=None)

    exclusions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    path: str | core.StringOut = core.attr(str)

    sample_size: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        path: str | core.StringOut,
        connection_name: str | core.StringOut | None = None,
        dlq_event_queue_arn: str | core.StringOut | None = None,
        event_queue_arn: str | core.StringOut | None = None,
        exclusions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        sample_size: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=S3Target.Args(
                path=path,
                connection_name=connection_name,
                dlq_event_queue_arn=dlq_event_queue_arn,
                event_queue_arn=event_queue_arn,
                exclusions=exclusions,
                sample_size=sample_size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_name: str | core.StringOut | None = core.arg(default=None)

        dlq_event_queue_arn: str | core.StringOut | None = core.arg(default=None)

        event_queue_arn: str | core.StringOut | None = core.arg(default=None)

        exclusions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        path: str | core.StringOut = core.arg()

        sample_size: int | core.IntOut | None = core.arg(default=None)


@core.schema
class DynamodbTarget(core.Schema):

    path: str | core.StringOut = core.attr(str)

    scan_all: bool | core.BoolOut | None = core.attr(bool, default=None)

    scan_rate: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        path: str | core.StringOut,
        scan_all: bool | core.BoolOut | None = None,
        scan_rate: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=DynamodbTarget.Args(
                path=path,
                scan_all=scan_all,
                scan_rate=scan_rate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: str | core.StringOut = core.arg()

        scan_all: bool | core.BoolOut | None = core.arg(default=None)

        scan_rate: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class CatalogTarget(core.Schema):

    database_name: str | core.StringOut = core.attr(str)

    tables: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        database_name: str | core.StringOut,
        tables: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=CatalogTarget.Args(
                database_name=database_name,
                tables=tables,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database_name: str | core.StringOut = core.arg()

        tables: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class MongodbTarget(core.Schema):

    connection_name: str | core.StringOut = core.attr(str)

    path: str | core.StringOut = core.attr(str)

    scan_all: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        connection_name: str | core.StringOut,
        path: str | core.StringOut,
        scan_all: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=MongodbTarget.Args(
                connection_name=connection_name,
                path=path,
                scan_all=scan_all,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_name: str | core.StringOut = core.arg()

        path: str | core.StringOut = core.arg()

        scan_all: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class DeltaTarget(core.Schema):

    connection_name: str | core.StringOut = core.attr(str)

    delta_tables: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    write_manifest: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        connection_name: str | core.StringOut,
        delta_tables: list[str] | core.ArrayOut[core.StringOut],
        write_manifest: bool | core.BoolOut,
    ):
        super().__init__(
            args=DeltaTarget.Args(
                connection_name=connection_name,
                delta_tables=delta_tables,
                write_manifest=write_manifest,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_name: str | core.StringOut = core.arg()

        delta_tables: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        write_manifest: bool | core.BoolOut = core.arg()


@core.schema
class JdbcTarget(core.Schema):

    connection_name: str | core.StringOut = core.attr(str)

    exclusions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        connection_name: str | core.StringOut,
        path: str | core.StringOut,
        exclusions: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=JdbcTarget.Args(
                connection_name=connection_name,
                path=path,
                exclusions=exclusions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_name: str | core.StringOut = core.arg()

        exclusions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        path: str | core.StringOut = core.arg()


@core.resource(type="aws_glue_crawler", namespace="glue")
class Crawler(core.Resource):
    """
    The ARN of the crawler
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    catalog_target: list[CatalogTarget] | core.ArrayOut[CatalogTarget] | None = core.attr(
        CatalogTarget, default=None, kind=core.Kind.array
    )

    classifiers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    configuration: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the Glue database to be synchronized.
    """
    database_name: str | core.StringOut = core.attr(str)

    delta_target: list[DeltaTarget] | core.ArrayOut[DeltaTarget] | None = core.attr(
        DeltaTarget, default=None, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    dynamodb_target: list[DynamodbTarget] | core.ArrayOut[DynamodbTarget] | None = core.attr(
        DynamodbTarget, default=None, kind=core.Kind.array
    )

    """
    Crawler name
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    jdbc_target: list[JdbcTarget] | core.ArrayOut[JdbcTarget] | None = core.attr(
        JdbcTarget, default=None, kind=core.Kind.array
    )

    lineage_configuration: LineageConfiguration | None = core.attr(
        LineageConfiguration, default=None
    )

    mongodb_target: list[MongodbTarget] | core.ArrayOut[MongodbTarget] | None = core.attr(
        MongodbTarget, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    recrawl_policy: RecrawlPolicy | None = core.attr(RecrawlPolicy, default=None)

    role: str | core.StringOut = core.attr(str)

    s3_target: list[S3Target] | core.ArrayOut[S3Target] | None = core.attr(
        S3Target, default=None, kind=core.Kind.array
    )

    schedule: str | core.StringOut | None = core.attr(str, default=None)

    schema_change_policy: SchemaChangePolicy | None = core.attr(SchemaChangePolicy, default=None)

    security_configuration: str | core.StringOut | None = core.attr(str, default=None)

    table_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        name: str | core.StringOut,
        role: str | core.StringOut,
        catalog_target: list[CatalogTarget] | core.ArrayOut[CatalogTarget] | None = None,
        classifiers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        configuration: str | core.StringOut | None = None,
        delta_target: list[DeltaTarget] | core.ArrayOut[DeltaTarget] | None = None,
        description: str | core.StringOut | None = None,
        dynamodb_target: list[DynamodbTarget] | core.ArrayOut[DynamodbTarget] | None = None,
        jdbc_target: list[JdbcTarget] | core.ArrayOut[JdbcTarget] | None = None,
        lineage_configuration: LineageConfiguration | None = None,
        mongodb_target: list[MongodbTarget] | core.ArrayOut[MongodbTarget] | None = None,
        recrawl_policy: RecrawlPolicy | None = None,
        s3_target: list[S3Target] | core.ArrayOut[S3Target] | None = None,
        schedule: str | core.StringOut | None = None,
        schema_change_policy: SchemaChangePolicy | None = None,
        security_configuration: str | core.StringOut | None = None,
        table_prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Crawler.Args(
                database_name=database_name,
                name=name,
                role=role,
                catalog_target=catalog_target,
                classifiers=classifiers,
                configuration=configuration,
                delta_target=delta_target,
                description=description,
                dynamodb_target=dynamodb_target,
                jdbc_target=jdbc_target,
                lineage_configuration=lineage_configuration,
                mongodb_target=mongodb_target,
                recrawl_policy=recrawl_policy,
                s3_target=s3_target,
                schedule=schedule,
                schema_change_policy=schema_change_policy,
                security_configuration=security_configuration,
                table_prefix=table_prefix,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_target: list[CatalogTarget] | core.ArrayOut[CatalogTarget] | None = core.arg(
            default=None
        )

        classifiers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        configuration: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut = core.arg()

        delta_target: list[DeltaTarget] | core.ArrayOut[DeltaTarget] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        dynamodb_target: list[DynamodbTarget] | core.ArrayOut[DynamodbTarget] | None = core.arg(
            default=None
        )

        jdbc_target: list[JdbcTarget] | core.ArrayOut[JdbcTarget] | None = core.arg(default=None)

        lineage_configuration: LineageConfiguration | None = core.arg(default=None)

        mongodb_target: list[MongodbTarget] | core.ArrayOut[MongodbTarget] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        recrawl_policy: RecrawlPolicy | None = core.arg(default=None)

        role: str | core.StringOut = core.arg()

        s3_target: list[S3Target] | core.ArrayOut[S3Target] | None = core.arg(default=None)

        schedule: str | core.StringOut | None = core.arg(default=None)

        schema_change_policy: SchemaChangePolicy | None = core.arg(default=None)

        security_configuration: str | core.StringOut | None = core.arg(default=None)

        table_prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
