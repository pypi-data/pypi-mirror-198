import terrascript.core as core


@core.schema
class SeedUrlConfiguration(core.Schema):

    seed_urls: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    web_crawler_mode: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        seed_urls: list[str] | core.ArrayOut[core.StringOut],
        web_crawler_mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SeedUrlConfiguration.Args(
                seed_urls=seed_urls,
                web_crawler_mode=web_crawler_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        seed_urls: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        web_crawler_mode: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SiteMapsConfiguration(core.Schema):

    site_maps: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        site_maps: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=SiteMapsConfiguration.Args(
                site_maps=site_maps,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        site_maps: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Urls(core.Schema):

    seed_url_configuration: SeedUrlConfiguration | None = core.attr(
        SeedUrlConfiguration, default=None
    )

    site_maps_configuration: SiteMapsConfiguration | None = core.attr(
        SiteMapsConfiguration, default=None
    )

    def __init__(
        self,
        *,
        seed_url_configuration: SeedUrlConfiguration | None = None,
        site_maps_configuration: SiteMapsConfiguration | None = None,
    ):
        super().__init__(
            args=Urls.Args(
                seed_url_configuration=seed_url_configuration,
                site_maps_configuration=site_maps_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        seed_url_configuration: SeedUrlConfiguration | None = core.arg(default=None)

        site_maps_configuration: SiteMapsConfiguration | None = core.arg(default=None)


@core.schema
class ProxyConfiguration(core.Schema):

    credentials: str | core.StringOut | None = core.attr(str, default=None)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        host: str | core.StringOut,
        port: int | core.IntOut,
        credentials: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProxyConfiguration.Args(
                host=host,
                port=port,
                credentials=credentials,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credentials: str | core.StringOut | None = core.arg(default=None)

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class BasicAuthentication(core.Schema):

    credentials: str | core.StringOut = core.attr(str)

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        credentials: str | core.StringOut,
        host: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=BasicAuthentication.Args(
                credentials=credentials,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credentials: str | core.StringOut = core.arg()

        host: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class AuthenticationConfiguration(core.Schema):

    basic_authentication: list[BasicAuthentication] | core.ArrayOut[
        BasicAuthentication
    ] | None = core.attr(BasicAuthentication, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        basic_authentication: list[BasicAuthentication]
        | core.ArrayOut[BasicAuthentication]
        | None = None,
    ):
        super().__init__(
            args=AuthenticationConfiguration.Args(
                basic_authentication=basic_authentication,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        basic_authentication: list[BasicAuthentication] | core.ArrayOut[
            BasicAuthentication
        ] | None = core.arg(default=None)


@core.schema
class WebCrawlerConfiguration(core.Schema):

    authentication_configuration: AuthenticationConfiguration | None = core.attr(
        AuthenticationConfiguration, default=None
    )

    crawl_depth: int | core.IntOut | None = core.attr(int, default=None)

    max_content_size_per_page_in_mega_bytes: float | core.FloatOut | None = core.attr(
        float, default=None
    )

    max_links_per_page: int | core.IntOut | None = core.attr(int, default=None)

    max_urls_per_minute_crawl_rate: int | core.IntOut | None = core.attr(int, default=None)

    proxy_configuration: ProxyConfiguration | None = core.attr(ProxyConfiguration, default=None)

    url_exclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    url_inclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    urls: Urls = core.attr(Urls)

    def __init__(
        self,
        *,
        urls: Urls,
        authentication_configuration: AuthenticationConfiguration | None = None,
        crawl_depth: int | core.IntOut | None = None,
        max_content_size_per_page_in_mega_bytes: float | core.FloatOut | None = None,
        max_links_per_page: int | core.IntOut | None = None,
        max_urls_per_minute_crawl_rate: int | core.IntOut | None = None,
        proxy_configuration: ProxyConfiguration | None = None,
        url_exclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        url_inclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=WebCrawlerConfiguration.Args(
                urls=urls,
                authentication_configuration=authentication_configuration,
                crawl_depth=crawl_depth,
                max_content_size_per_page_in_mega_bytes=max_content_size_per_page_in_mega_bytes,
                max_links_per_page=max_links_per_page,
                max_urls_per_minute_crawl_rate=max_urls_per_minute_crawl_rate,
                proxy_configuration=proxy_configuration,
                url_exclusion_patterns=url_exclusion_patterns,
                url_inclusion_patterns=url_inclusion_patterns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_configuration: AuthenticationConfiguration | None = core.arg(default=None)

        crawl_depth: int | core.IntOut | None = core.arg(default=None)

        max_content_size_per_page_in_mega_bytes: float | core.FloatOut | None = core.arg(
            default=None
        )

        max_links_per_page: int | core.IntOut | None = core.arg(default=None)

        max_urls_per_minute_crawl_rate: int | core.IntOut | None = core.arg(default=None)

        proxy_configuration: ProxyConfiguration | None = core.arg(default=None)

        url_exclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        url_inclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        urls: Urls = core.arg()


@core.schema
class DocumentsMetadataConfiguration(core.Schema):

    s3_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DocumentsMetadataConfiguration.Args(
                s3_prefix=s3_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AccessControlListConfiguration(core.Schema):

    key_path: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key_path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AccessControlListConfiguration.Args(
                key_path=key_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_path: str | core.StringOut | None = core.arg(default=None)


@core.schema
class S3Configuration(core.Schema):

    access_control_list_configuration: AccessControlListConfiguration | None = core.attr(
        AccessControlListConfiguration, default=None
    )

    bucket_name: str | core.StringOut = core.attr(str)

    documents_metadata_configuration: DocumentsMetadataConfiguration | None = core.attr(
        DocumentsMetadataConfiguration, default=None
    )

    exclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    inclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    inclusion_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        access_control_list_configuration: AccessControlListConfiguration | None = None,
        documents_metadata_configuration: DocumentsMetadataConfiguration | None = None,
        exclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        inclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        inclusion_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=S3Configuration.Args(
                bucket_name=bucket_name,
                access_control_list_configuration=access_control_list_configuration,
                documents_metadata_configuration=documents_metadata_configuration,
                exclusion_patterns=exclusion_patterns,
                inclusion_patterns=inclusion_patterns,
                inclusion_prefixes=inclusion_prefixes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_list_configuration: AccessControlListConfiguration | None = core.arg(
            default=None
        )

        bucket_name: str | core.StringOut = core.arg()

        documents_metadata_configuration: DocumentsMetadataConfiguration | None = core.arg(
            default=None
        )

        exclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        inclusion_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        inclusion_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class Configuration(core.Schema):

    s3_configuration: S3Configuration | None = core.attr(S3Configuration, default=None)

    web_crawler_configuration: WebCrawlerConfiguration | None = core.attr(
        WebCrawlerConfiguration, default=None
    )

    def __init__(
        self,
        *,
        s3_configuration: S3Configuration | None = None,
        web_crawler_configuration: WebCrawlerConfiguration | None = None,
    ):
        super().__init__(
            args=Configuration.Args(
                s3_configuration=s3_configuration,
                web_crawler_configuration=web_crawler_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_configuration: S3Configuration | None = core.arg(default=None)

        web_crawler_configuration: WebCrawlerConfiguration | None = core.arg(default=None)


@core.schema
class ConditionOnValue(core.Schema):

    date_value: str | core.StringOut | None = core.attr(str, default=None)

    long_value: int | core.IntOut | None = core.attr(int, default=None)

    string_list_value: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    string_value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_value: str | core.StringOut | None = None,
        long_value: int | core.IntOut | None = None,
        string_list_value: list[str] | core.ArrayOut[core.StringOut] | None = None,
        string_value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConditionOnValue.Args(
                date_value=date_value,
                long_value=long_value,
                string_list_value=string_list_value,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_value: str | core.StringOut | None = core.arg(default=None)

        long_value: int | core.IntOut | None = core.arg(default=None)

        string_list_value: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        string_value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InvocationCondition(core.Schema):

    condition_document_attribute_key: str | core.StringOut = core.attr(str)

    condition_on_value: ConditionOnValue | None = core.attr(ConditionOnValue, default=None)

    operator: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        condition_document_attribute_key: str | core.StringOut,
        operator: str | core.StringOut,
        condition_on_value: ConditionOnValue | None = None,
    ):
        super().__init__(
            args=InvocationCondition.Args(
                condition_document_attribute_key=condition_document_attribute_key,
                operator=operator,
                condition_on_value=condition_on_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition_document_attribute_key: str | core.StringOut = core.arg()

        condition_on_value: ConditionOnValue | None = core.arg(default=None)

        operator: str | core.StringOut = core.arg()


@core.schema
class PostExtractionHookConfiguration(core.Schema):

    invocation_condition: InvocationCondition | None = core.attr(InvocationCondition, default=None)

    lambda_arn: str | core.StringOut = core.attr(str)

    s3_bucket: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        lambda_arn: str | core.StringOut,
        s3_bucket: str | core.StringOut,
        invocation_condition: InvocationCondition | None = None,
    ):
        super().__init__(
            args=PostExtractionHookConfiguration.Args(
                lambda_arn=lambda_arn,
                s3_bucket=s3_bucket,
                invocation_condition=invocation_condition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        invocation_condition: InvocationCondition | None = core.arg(default=None)

        lambda_arn: str | core.StringOut = core.arg()

        s3_bucket: str | core.StringOut = core.arg()


@core.schema
class PreExtractionHookConfiguration(core.Schema):

    invocation_condition: InvocationCondition | None = core.attr(InvocationCondition, default=None)

    lambda_arn: str | core.StringOut = core.attr(str)

    s3_bucket: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        lambda_arn: str | core.StringOut,
        s3_bucket: str | core.StringOut,
        invocation_condition: InvocationCondition | None = None,
    ):
        super().__init__(
            args=PreExtractionHookConfiguration.Args(
                lambda_arn=lambda_arn,
                s3_bucket=s3_bucket,
                invocation_condition=invocation_condition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        invocation_condition: InvocationCondition | None = core.arg(default=None)

        lambda_arn: str | core.StringOut = core.arg()

        s3_bucket: str | core.StringOut = core.arg()


@core.schema
class Condition(core.Schema):

    condition_document_attribute_key: str | core.StringOut = core.attr(str)

    condition_on_value: ConditionOnValue | None = core.attr(ConditionOnValue, default=None)

    operator: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        condition_document_attribute_key: str | core.StringOut,
        operator: str | core.StringOut,
        condition_on_value: ConditionOnValue | None = None,
    ):
        super().__init__(
            args=Condition.Args(
                condition_document_attribute_key=condition_document_attribute_key,
                operator=operator,
                condition_on_value=condition_on_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition_document_attribute_key: str | core.StringOut = core.arg()

        condition_on_value: ConditionOnValue | None = core.arg(default=None)

        operator: str | core.StringOut = core.arg()


@core.schema
class TargetDocumentAttributeValue(core.Schema):

    date_value: str | core.StringOut | None = core.attr(str, default=None)

    long_value: int | core.IntOut | None = core.attr(int, default=None)

    string_list_value: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    string_value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_value: str | core.StringOut | None = None,
        long_value: int | core.IntOut | None = None,
        string_list_value: list[str] | core.ArrayOut[core.StringOut] | None = None,
        string_value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TargetDocumentAttributeValue.Args(
                date_value=date_value,
                long_value=long_value,
                string_list_value=string_list_value,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_value: str | core.StringOut | None = core.arg(default=None)

        long_value: int | core.IntOut | None = core.arg(default=None)

        string_list_value: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        string_value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Target(core.Schema):

    target_document_attribute_key: str | core.StringOut | None = core.attr(str, default=None)

    target_document_attribute_value: TargetDocumentAttributeValue | None = core.attr(
        TargetDocumentAttributeValue, default=None
    )

    target_document_attribute_value_deletion: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        target_document_attribute_key: str | core.StringOut | None = None,
        target_document_attribute_value: TargetDocumentAttributeValue | None = None,
        target_document_attribute_value_deletion: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Target.Args(
                target_document_attribute_key=target_document_attribute_key,
                target_document_attribute_value=target_document_attribute_value,
                target_document_attribute_value_deletion=target_document_attribute_value_deletion,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_document_attribute_key: str | core.StringOut | None = core.arg(default=None)

        target_document_attribute_value: TargetDocumentAttributeValue | None = core.arg(
            default=None
        )

        target_document_attribute_value_deletion: bool | core.BoolOut | None = core.arg(
            default=None
        )


@core.schema
class InlineConfigurations(core.Schema):

    condition: Condition | None = core.attr(Condition, default=None)

    document_content_deletion: bool | core.BoolOut | None = core.attr(bool, default=None)

    target: Target | None = core.attr(Target, default=None)

    def __init__(
        self,
        *,
        condition: Condition | None = None,
        document_content_deletion: bool | core.BoolOut | None = None,
        target: Target | None = None,
    ):
        super().__init__(
            args=InlineConfigurations.Args(
                condition=condition,
                document_content_deletion=document_content_deletion,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition: Condition | None = core.arg(default=None)

        document_content_deletion: bool | core.BoolOut | None = core.arg(default=None)

        target: Target | None = core.arg(default=None)


@core.schema
class CustomDocumentEnrichmentConfiguration(core.Schema):

    inline_configurations: list[InlineConfigurations] | core.ArrayOut[
        InlineConfigurations
    ] | None = core.attr(InlineConfigurations, default=None, kind=core.Kind.array)

    post_extraction_hook_configuration: PostExtractionHookConfiguration | None = core.attr(
        PostExtractionHookConfiguration, default=None
    )

    pre_extraction_hook_configuration: PreExtractionHookConfiguration | None = core.attr(
        PreExtractionHookConfiguration, default=None
    )

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        inline_configurations: list[InlineConfigurations]
        | core.ArrayOut[InlineConfigurations]
        | None = None,
        post_extraction_hook_configuration: PostExtractionHookConfiguration | None = None,
        pre_extraction_hook_configuration: PreExtractionHookConfiguration | None = None,
        role_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomDocumentEnrichmentConfiguration.Args(
                inline_configurations=inline_configurations,
                post_extraction_hook_configuration=post_extraction_hook_configuration,
                pre_extraction_hook_configuration=pre_extraction_hook_configuration,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        inline_configurations: list[InlineConfigurations] | core.ArrayOut[
            InlineConfigurations
        ] | None = core.arg(default=None)

        post_extraction_hook_configuration: PostExtractionHookConfiguration | None = core.arg(
            default=None
        )

        pre_extraction_hook_configuration: PreExtractionHookConfiguration | None = core.arg(
            default=None
        )

        role_arn: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_kendra_data_source", namespace="aws_kendra")
class DataSource(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    configuration: Configuration | None = core.attr(Configuration, default=None)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    custom_document_enrichment_configuration: CustomDocumentEnrichmentConfiguration | None = (
        core.attr(CustomDocumentEnrichmentConfiguration, default=None)
    )

    data_source_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    error_message: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    index_id: str | core.StringOut = core.attr(str)

    language_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    schedule: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str)

    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        index_id: str | core.StringOut,
        name: str | core.StringOut,
        type: str | core.StringOut,
        configuration: Configuration | None = None,
        custom_document_enrichment_configuration: CustomDocumentEnrichmentConfiguration
        | None = None,
        description: str | core.StringOut | None = None,
        language_code: str | core.StringOut | None = None,
        role_arn: str | core.StringOut | None = None,
        schedule: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataSource.Args(
                index_id=index_id,
                name=name,
                type=type,
                configuration=configuration,
                custom_document_enrichment_configuration=custom_document_enrichment_configuration,
                description=description,
                language_code=language_code,
                role_arn=role_arn,
                schedule=schedule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        configuration: Configuration | None = core.arg(default=None)

        custom_document_enrichment_configuration: CustomDocumentEnrichmentConfiguration | None = (
            core.arg(default=None)
        )

        description: str | core.StringOut | None = core.arg(default=None)

        index_id: str | core.StringOut = core.arg()

        language_code: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)

        schedule: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
