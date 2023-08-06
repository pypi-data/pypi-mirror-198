import terrascript.core as core


@core.schema
class SslProperties(core.Schema):

    disable_ssl: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        disable_ssl: bool | core.BoolOut,
    ):
        super().__init__(
            args=SslProperties.Args(
                disable_ssl=disable_ssl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        disable_ssl: bool | core.BoolOut = core.arg()


@core.schema
class VpcConnectionProperties(core.Schema):

    vpc_connection_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        vpc_connection_arn: str | core.StringOut,
    ):
        super().__init__(
            args=VpcConnectionProperties.Args(
                vpc_connection_arn=vpc_connection_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vpc_connection_arn: str | core.StringOut = core.arg()


@core.schema
class Permission(core.Schema):

    actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    principal: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        actions: list[str] | core.ArrayOut[core.StringOut],
        principal: str | core.StringOut,
    ):
        super().__init__(
            args=Permission.Args(
                actions=actions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        principal: str | core.StringOut = core.arg()


@core.schema
class Twitter(core.Schema):

    max_rows: int | core.IntOut = core.attr(int)

    query: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        max_rows: int | core.IntOut,
        query: str | core.StringOut,
    ):
        super().__init__(
            args=Twitter.Args(
                max_rows=max_rows,
                query=query,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_rows: int | core.IntOut = core.arg()

        query: str | core.StringOut = core.arg()


@core.schema
class AmazonElasticsearch(core.Schema):

    domain: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        domain: str | core.StringOut,
    ):
        super().__init__(
            args=AmazonElasticsearch.Args(
                domain=domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: str | core.StringOut = core.arg()


@core.schema
class Postgresql(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Postgresql.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class Presto(core.Schema):

    catalog: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        catalog: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Presto.Args(
                catalog=catalog,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class SqlServer(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=SqlServer.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class Redshift(core.Schema):

    cluster_id: str | core.StringOut | None = core.attr(str, default=None)

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut | None = core.attr(str, default=None)

    port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        cluster_id: str | core.StringOut | None = None,
        host: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Redshift.Args(
                database=database,
                cluster_id=cluster_id,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_id: str | core.StringOut | None = core.arg(default=None)

        database: str | core.StringOut = core.arg()

        host: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Mysql(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Mysql.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class Snowflake(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    warehouse: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        warehouse: str | core.StringOut,
    ):
        super().__init__(
            args=Snowflake.Args(
                database=database,
                host=host,
                warehouse=warehouse,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        warehouse: str | core.StringOut = core.arg()


@core.schema
class AuroraPostgresql(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=AuroraPostgresql.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class ManifestFileLocation(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
    ):
        super().__init__(
            args=ManifestFileLocation.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()


@core.schema
class S3(core.Schema):

    manifest_file_location: ManifestFileLocation = core.attr(ManifestFileLocation)

    def __init__(
        self,
        *,
        manifest_file_location: ManifestFileLocation,
    ):
        super().__init__(
            args=S3.Args(
                manifest_file_location=manifest_file_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        manifest_file_location: ManifestFileLocation = core.arg()


@core.schema
class Teradata(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Teradata.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class Aurora(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Aurora.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class Rds(core.Schema):

    database: str | core.StringOut = core.attr(str)

    instance_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        instance_id: str | core.StringOut,
    ):
        super().__init__(
            args=Rds.Args(
                database=database,
                instance_id=instance_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        instance_id: str | core.StringOut = core.arg()


@core.schema
class MariaDb(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=MariaDb.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class AwsIotAnalytics(core.Schema):

    data_set_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        data_set_name: str | core.StringOut,
    ):
        super().__init__(
            args=AwsIotAnalytics.Args(
                data_set_name=data_set_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_set_name: str | core.StringOut = core.arg()


@core.schema
class Jira(core.Schema):

    site_base_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        site_base_url: str | core.StringOut,
    ):
        super().__init__(
            args=Jira.Args(
                site_base_url=site_base_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        site_base_url: str | core.StringOut = core.arg()


@core.schema
class Spark(core.Schema):

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Spark.Args(
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class ServiceNow(core.Schema):

    site_base_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        site_base_url: str | core.StringOut,
    ):
        super().__init__(
            args=ServiceNow.Args(
                site_base_url=site_base_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        site_base_url: str | core.StringOut = core.arg()


@core.schema
class Oracle(core.Schema):

    database: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Oracle.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class Athena(core.Schema):

    work_group: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        work_group: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Athena.Args(
                work_group=work_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        work_group: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Parameters(core.Schema):

    amazon_elasticsearch: AmazonElasticsearch | None = core.attr(AmazonElasticsearch, default=None)

    athena: Athena | None = core.attr(Athena, default=None)

    aurora: Aurora | None = core.attr(Aurora, default=None)

    aurora_postgresql: AuroraPostgresql | None = core.attr(AuroraPostgresql, default=None)

    aws_iot_analytics: AwsIotAnalytics | None = core.attr(AwsIotAnalytics, default=None)

    jira: Jira | None = core.attr(Jira, default=None)

    maria_db: MariaDb | None = core.attr(MariaDb, default=None)

    mysql: Mysql | None = core.attr(Mysql, default=None)

    oracle: Oracle | None = core.attr(Oracle, default=None)

    postgresql: Postgresql | None = core.attr(Postgresql, default=None)

    presto: Presto | None = core.attr(Presto, default=None)

    rds: Rds | None = core.attr(Rds, default=None)

    redshift: Redshift | None = core.attr(Redshift, default=None)

    s3: S3 | None = core.attr(S3, default=None)

    service_now: ServiceNow | None = core.attr(ServiceNow, default=None)

    snowflake: Snowflake | None = core.attr(Snowflake, default=None)

    spark: Spark | None = core.attr(Spark, default=None)

    sql_server: SqlServer | None = core.attr(SqlServer, default=None)

    teradata: Teradata | None = core.attr(Teradata, default=None)

    twitter: Twitter | None = core.attr(Twitter, default=None)

    def __init__(
        self,
        *,
        amazon_elasticsearch: AmazonElasticsearch | None = None,
        athena: Athena | None = None,
        aurora: Aurora | None = None,
        aurora_postgresql: AuroraPostgresql | None = None,
        aws_iot_analytics: AwsIotAnalytics | None = None,
        jira: Jira | None = None,
        maria_db: MariaDb | None = None,
        mysql: Mysql | None = None,
        oracle: Oracle | None = None,
        postgresql: Postgresql | None = None,
        presto: Presto | None = None,
        rds: Rds | None = None,
        redshift: Redshift | None = None,
        s3: S3 | None = None,
        service_now: ServiceNow | None = None,
        snowflake: Snowflake | None = None,
        spark: Spark | None = None,
        sql_server: SqlServer | None = None,
        teradata: Teradata | None = None,
        twitter: Twitter | None = None,
    ):
        super().__init__(
            args=Parameters.Args(
                amazon_elasticsearch=amazon_elasticsearch,
                athena=athena,
                aurora=aurora,
                aurora_postgresql=aurora_postgresql,
                aws_iot_analytics=aws_iot_analytics,
                jira=jira,
                maria_db=maria_db,
                mysql=mysql,
                oracle=oracle,
                postgresql=postgresql,
                presto=presto,
                rds=rds,
                redshift=redshift,
                s3=s3,
                service_now=service_now,
                snowflake=snowflake,
                spark=spark,
                sql_server=sql_server,
                teradata=teradata,
                twitter=twitter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amazon_elasticsearch: AmazonElasticsearch | None = core.arg(default=None)

        athena: Athena | None = core.arg(default=None)

        aurora: Aurora | None = core.arg(default=None)

        aurora_postgresql: AuroraPostgresql | None = core.arg(default=None)

        aws_iot_analytics: AwsIotAnalytics | None = core.arg(default=None)

        jira: Jira | None = core.arg(default=None)

        maria_db: MariaDb | None = core.arg(default=None)

        mysql: Mysql | None = core.arg(default=None)

        oracle: Oracle | None = core.arg(default=None)

        postgresql: Postgresql | None = core.arg(default=None)

        presto: Presto | None = core.arg(default=None)

        rds: Rds | None = core.arg(default=None)

        redshift: Redshift | None = core.arg(default=None)

        s3: S3 | None = core.arg(default=None)

        service_now: ServiceNow | None = core.arg(default=None)

        snowflake: Snowflake | None = core.arg(default=None)

        spark: Spark | None = core.arg(default=None)

        sql_server: SqlServer | None = core.arg(default=None)

        teradata: Teradata | None = core.arg(default=None)

        twitter: Twitter | None = core.arg(default=None)


@core.schema
class CredentialPair(core.Schema):

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=CredentialPair.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class Credentials(core.Schema):

    copy_source_arn: str | core.StringOut | None = core.attr(str, default=None)

    credential_pair: CredentialPair | None = core.attr(CredentialPair, default=None)

    def __init__(
        self,
        *,
        copy_source_arn: str | core.StringOut | None = None,
        credential_pair: CredentialPair | None = None,
    ):
        super().__init__(
            args=Credentials.Args(
                copy_source_arn=copy_source_arn,
                credential_pair=credential_pair,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_source_arn: str | core.StringOut | None = core.arg(default=None)

        credential_pair: CredentialPair | None = core.arg(default=None)


@core.resource(type="aws_quicksight_data_source", namespace="quicksight")
class DataSource(core.Resource):
    """
    Amazon Resource Name (ARN) of the data source
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The ID for the AWS account that the data source is in. Currently, yo
    u use the ID for the AWS account that contains your Amazon QuickSight account.
    """
    aws_account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The credentials Amazon QuickSight uses to connect to your underlying source. Currently, o
    nly credentials based on user name and password are supported. See [Credentials](#credentials-argume
    nt-reference) below for more details.
    """
    credentials: Credentials | None = core.attr(Credentials, default=None)

    """
    (Required, Forces new resource) An identifier for the data source.
    """
    data_source_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A name for the data source, maximum of 128 characters.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The [parameters](#parameters-argument-reference) used to connect to this data source (exa
    ctly one).
    """
    parameters: Parameters = core.attr(Parameters)

    """
    (Optional) A set of resource permissions on the data source. Maximum of 64 items. See [Permission](#
    permission-argument-reference) below for more details.
    """
    permission: list[Permission] | core.ArrayOut[Permission] | None = core.attr(
        Permission, default=None, kind=core.Kind.array
    )

    """
    (Optional) Secure Socket Layer (SSL) properties that apply when Amazon QuickSight connects to your u
    nderlying source. See [SSL Properties](#ssl_properties-argument-reference) below for more details.
    """
    ssl_properties: SslProperties | None = core.attr(SslProperties, default=None)

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

    """
    (Required) The type of the data source. See the [AWS Documentation](https://docs.aws.amazon.com/quic
    ksight/latest/APIReference/API_CreateDataSource.html#QS-CreateDataSource-request-Type) for the compl
    ete list of valid values.
    """
    type: str | core.StringOut = core.attr(str)

    vpc_connection_properties: VpcConnectionProperties | None = core.attr(
        VpcConnectionProperties, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        data_source_id: str | core.StringOut,
        name: str | core.StringOut,
        parameters: Parameters,
        type: str | core.StringOut,
        aws_account_id: str | core.StringOut | None = None,
        credentials: Credentials | None = None,
        permission: list[Permission] | core.ArrayOut[Permission] | None = None,
        ssl_properties: SslProperties | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_connection_properties: VpcConnectionProperties | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataSource.Args(
                data_source_id=data_source_id,
                name=name,
                parameters=parameters,
                type=type,
                aws_account_id=aws_account_id,
                credentials=credentials,
                permission=permission,
                ssl_properties=ssl_properties,
                tags=tags,
                tags_all=tags_all,
                vpc_connection_properties=vpc_connection_properties,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_account_id: str | core.StringOut | None = core.arg(default=None)

        credentials: Credentials | None = core.arg(default=None)

        data_source_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        parameters: Parameters = core.arg()

        permission: list[Permission] | core.ArrayOut[Permission] | None = core.arg(default=None)

        ssl_properties: SslProperties | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        vpc_connection_properties: VpcConnectionProperties | None = core.arg(default=None)
