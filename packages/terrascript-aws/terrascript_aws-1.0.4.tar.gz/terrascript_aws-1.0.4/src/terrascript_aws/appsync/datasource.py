import terrascript.core as core


@core.schema
class AwsIamConfig(core.Schema):

    signing_region: str | core.StringOut | None = core.attr(str, default=None)

    signing_service_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        signing_region: str | core.StringOut | None = None,
        signing_service_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AwsIamConfig.Args(
                signing_region=signing_region,
                signing_service_name=signing_service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        signing_region: str | core.StringOut | None = core.arg(default=None)

        signing_service_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AuthorizationConfig(core.Schema):

    authorization_type: str | core.StringOut | None = core.attr(str, default=None)

    aws_iam_config: AwsIamConfig | None = core.attr(AwsIamConfig, default=None)

    def __init__(
        self,
        *,
        authorization_type: str | core.StringOut | None = None,
        aws_iam_config: AwsIamConfig | None = None,
    ):
        super().__init__(
            args=AuthorizationConfig.Args(
                authorization_type=authorization_type,
                aws_iam_config=aws_iam_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_type: str | core.StringOut | None = core.arg(default=None)

        aws_iam_config: AwsIamConfig | None = core.arg(default=None)


@core.schema
class HttpConfig(core.Schema):

    authorization_config: AuthorizationConfig | None = core.attr(AuthorizationConfig, default=None)

    endpoint: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        endpoint: str | core.StringOut,
        authorization_config: AuthorizationConfig | None = None,
    ):
        super().__init__(
            args=HttpConfig.Args(
                endpoint=endpoint,
                authorization_config=authorization_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_config: AuthorizationConfig | None = core.arg(default=None)

        endpoint: str | core.StringOut = core.arg()


@core.schema
class DeltaSyncConfig(core.Schema):

    base_table_ttl: int | core.IntOut | None = core.attr(int, default=None)

    delta_sync_table_name: str | core.StringOut = core.attr(str)

    delta_sync_table_ttl: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        delta_sync_table_name: str | core.StringOut,
        base_table_ttl: int | core.IntOut | None = None,
        delta_sync_table_ttl: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DeltaSyncConfig.Args(
                delta_sync_table_name=delta_sync_table_name,
                base_table_ttl=base_table_ttl,
                delta_sync_table_ttl=delta_sync_table_ttl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base_table_ttl: int | core.IntOut | None = core.arg(default=None)

        delta_sync_table_name: str | core.StringOut = core.arg()

        delta_sync_table_ttl: int | core.IntOut | None = core.arg(default=None)


@core.schema
class DynamodbConfig(core.Schema):

    delta_sync_config: DeltaSyncConfig | None = core.attr(DeltaSyncConfig, default=None)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    table_name: str | core.StringOut = core.attr(str)

    use_caller_credentials: bool | core.BoolOut | None = core.attr(bool, default=None)

    versioned: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        table_name: str | core.StringOut,
        delta_sync_config: DeltaSyncConfig | None = None,
        region: str | core.StringOut | None = None,
        use_caller_credentials: bool | core.BoolOut | None = None,
        versioned: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=DynamodbConfig.Args(
                table_name=table_name,
                delta_sync_config=delta_sync_config,
                region=region,
                use_caller_credentials=use_caller_credentials,
                versioned=versioned,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delta_sync_config: DeltaSyncConfig | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        table_name: str | core.StringOut = core.arg()

        use_caller_credentials: bool | core.BoolOut | None = core.arg(default=None)

        versioned: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class LambdaConfig(core.Schema):

    function_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        function_arn: str | core.StringOut,
    ):
        super().__init__(
            args=LambdaConfig.Args(
                function_arn=function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: str | core.StringOut = core.arg()


@core.schema
class ElasticsearchConfig(core.Schema):

    endpoint: str | core.StringOut = core.attr(str)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        endpoint: str | core.StringOut,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ElasticsearchConfig.Args(
                endpoint=endpoint,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: str | core.StringOut = core.arg()

        region: str | core.StringOut | None = core.arg(default=None)


@core.schema
class HttpEndpointConfig(core.Schema):

    aws_secret_store_arn: str | core.StringOut = core.attr(str)

    database_name: str | core.StringOut | None = core.attr(str, default=None)

    db_cluster_identifier: str | core.StringOut = core.attr(str)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    schema: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        aws_secret_store_arn: str | core.StringOut,
        db_cluster_identifier: str | core.StringOut,
        database_name: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
        schema: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=HttpEndpointConfig.Args(
                aws_secret_store_arn=aws_secret_store_arn,
                db_cluster_identifier=db_cluster_identifier,
                database_name=database_name,
                region=region,
                schema=schema,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_secret_store_arn: str | core.StringOut = core.arg()

        database_name: str | core.StringOut | None = core.arg(default=None)

        db_cluster_identifier: str | core.StringOut = core.arg()

        region: str | core.StringOut | None = core.arg(default=None)

        schema: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RelationalDatabaseConfig(core.Schema):

    http_endpoint_config: HttpEndpointConfig | None = core.attr(HttpEndpointConfig, default=None)

    source_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_endpoint_config: HttpEndpointConfig | None = None,
        source_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RelationalDatabaseConfig.Args(
                http_endpoint_config=http_endpoint_config,
                source_type=source_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint_config: HttpEndpointConfig | None = core.arg(default=None)

        source_type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_appsync_datasource", namespace="appsync")
class Datasource(core.Resource):
    """
    (Required) The API ID for the GraphQL API for the data source.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    The ARN
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description of the data source.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) DynamoDB settings. See [below](#dynamodb_config)
    """
    dynamodb_config: DynamodbConfig | None = core.attr(DynamodbConfig, default=None)

    """
    (Optional) Amazon Elasticsearch settings. See [below](#elasticsearch_config)
    """
    elasticsearch_config: ElasticsearchConfig | None = core.attr(ElasticsearchConfig, default=None)

    """
    (Optional) HTTP settings. See [below](#http_config)
    """
    http_config: HttpConfig | None = core.attr(HttpConfig, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) AWS Lambda settings. See [below](#lambda_config)
    """
    lambda_config: LambdaConfig | None = core.attr(LambdaConfig, default=None)

    """
    (Required) A user-supplied name for the data source.
    """
    name: str | core.StringOut = core.attr(str)

    relational_database_config: RelationalDatabaseConfig | None = core.attr(
        RelationalDatabaseConfig, default=None
    )

    """
    (Optional) The IAM service role ARN for the data source.
    """
    service_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The type of the Data Source. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELAST
    ICSEARCH`, `HTTP`, `NONE`, `RELATIONAL_DATABASE`.
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        name: str | core.StringOut,
        type: str | core.StringOut,
        description: str | core.StringOut | None = None,
        dynamodb_config: DynamodbConfig | None = None,
        elasticsearch_config: ElasticsearchConfig | None = None,
        http_config: HttpConfig | None = None,
        lambda_config: LambdaConfig | None = None,
        relational_database_config: RelationalDatabaseConfig | None = None,
        service_role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Datasource.Args(
                api_id=api_id,
                name=name,
                type=type,
                description=description,
                dynamodb_config=dynamodb_config,
                elasticsearch_config=elasticsearch_config,
                http_config=http_config,
                lambda_config=lambda_config,
                relational_database_config=relational_database_config,
                service_role_arn=service_role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        dynamodb_config: DynamodbConfig | None = core.arg(default=None)

        elasticsearch_config: ElasticsearchConfig | None = core.arg(default=None)

        http_config: HttpConfig | None = core.arg(default=None)

        lambda_config: LambdaConfig | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        relational_database_config: RelationalDatabaseConfig | None = core.arg(default=None)

        service_role_arn: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
