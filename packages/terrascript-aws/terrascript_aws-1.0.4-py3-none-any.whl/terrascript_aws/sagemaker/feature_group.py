import terrascript.core as core


@core.schema
class SecurityConfig(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SecurityConfig.Args(
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class OnlineStoreConfig(core.Schema):

    enable_online_store: bool | core.BoolOut | None = core.attr(bool, default=None)

    security_config: SecurityConfig | None = core.attr(SecurityConfig, default=None)

    def __init__(
        self,
        *,
        enable_online_store: bool | core.BoolOut | None = None,
        security_config: SecurityConfig | None = None,
    ):
        super().__init__(
            args=OnlineStoreConfig.Args(
                enable_online_store=enable_online_store,
                security_config=security_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_online_store: bool | core.BoolOut | None = core.arg(default=None)

        security_config: SecurityConfig | None = core.arg(default=None)


@core.schema
class FeatureDefinition(core.Schema):

    feature_name: str | core.StringOut | None = core.attr(str, default=None)

    feature_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        feature_name: str | core.StringOut | None = None,
        feature_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FeatureDefinition.Args(
                feature_name=feature_name,
                feature_type=feature_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        feature_name: str | core.StringOut | None = core.arg(default=None)

        feature_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DataCatalogConfig(core.Schema):

    catalog: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    database: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    table_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        catalog: str | core.StringOut | None = None,
        database: str | core.StringOut | None = None,
        table_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DataCatalogConfig.Args(
                catalog=catalog,
                database=database,
                table_name=table_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog: str | core.StringOut | None = core.arg(default=None)

        database: str | core.StringOut | None = core.arg(default=None)

        table_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class S3StorageConfig(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    s3_uri: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        s3_uri: str | core.StringOut,
        kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3StorageConfig.Args(
                s3_uri=s3_uri,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        s3_uri: str | core.StringOut = core.arg()


@core.schema
class OfflineStoreConfig(core.Schema):

    data_catalog_config: DataCatalogConfig | None = core.attr(
        DataCatalogConfig, default=None, computed=True
    )

    disable_glue_table_creation: bool | core.BoolOut | None = core.attr(bool, default=None)

    s3_storage_config: S3StorageConfig = core.attr(S3StorageConfig)

    def __init__(
        self,
        *,
        s3_storage_config: S3StorageConfig,
        data_catalog_config: DataCatalogConfig | None = None,
        disable_glue_table_creation: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=OfflineStoreConfig.Args(
                s3_storage_config=s3_storage_config,
                data_catalog_config=data_catalog_config,
                disable_glue_table_creation=disable_glue_table_creation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_catalog_config: DataCatalogConfig | None = core.arg(default=None)

        disable_glue_table_creation: bool | core.BoolOut | None = core.arg(default=None)

        s3_storage_config: S3StorageConfig = core.arg()


@core.resource(type="aws_sagemaker_feature_group", namespace="sagemaker")
class FeatureGroup(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this feature_group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the feature that stores the EventTime of a Record in a Feature Group.
    """
    event_time_feature_name: str | core.StringOut = core.attr(str)

    feature_definition: list[FeatureDefinition] | core.ArrayOut[FeatureDefinition] = core.attr(
        FeatureDefinition, kind=core.Kind.array
    )

    """
    (Required) The name of the Feature Group. The name must be unique within an AWS Region in an AWS acc
    ount.
    """
    feature_group_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    offline_store_config: OfflineStoreConfig | None = core.attr(OfflineStoreConfig, default=None)

    online_store_config: OnlineStoreConfig | None = core.attr(OnlineStoreConfig, default=None)

    """
    (Required) The name of the Feature whose value uniquely identifies a Record defined in the Feature S
    tore. Only the latest record per identifier value will be stored in the Online Store.
    """
    record_identifier_feature_name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Map of resource tags for the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
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
        event_time_feature_name: str | core.StringOut,
        feature_definition: list[FeatureDefinition] | core.ArrayOut[FeatureDefinition],
        feature_group_name: str | core.StringOut,
        record_identifier_feature_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        description: str | core.StringOut | None = None,
        offline_store_config: OfflineStoreConfig | None = None,
        online_store_config: OnlineStoreConfig | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FeatureGroup.Args(
                event_time_feature_name=event_time_feature_name,
                feature_definition=feature_definition,
                feature_group_name=feature_group_name,
                record_identifier_feature_name=record_identifier_feature_name,
                role_arn=role_arn,
                description=description,
                offline_store_config=offline_store_config,
                online_store_config=online_store_config,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        event_time_feature_name: str | core.StringOut = core.arg()

        feature_definition: list[FeatureDefinition] | core.ArrayOut[FeatureDefinition] = core.arg()

        feature_group_name: str | core.StringOut = core.arg()

        offline_store_config: OfflineStoreConfig | None = core.arg(default=None)

        online_store_config: OnlineStoreConfig | None = core.arg(default=None)

        record_identifier_feature_name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
