import terrascript.core as core


@core.schema
class CapacityUnits(core.Schema):

    query_capacity_units: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    storage_capacity_units: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        query_capacity_units: int | core.IntOut | None = None,
        storage_capacity_units: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CapacityUnits.Args(
                query_capacity_units=query_capacity_units,
                storage_capacity_units=storage_capacity_units,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        query_capacity_units: int | core.IntOut | None = core.arg(default=None)

        storage_capacity_units: int | core.IntOut | None = core.arg(default=None)


@core.schema
class JsonTokenTypeConfiguration(core.Schema):

    group_attribute_field: str | core.StringOut = core.attr(str)

    user_name_attribute_field: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        group_attribute_field: str | core.StringOut,
        user_name_attribute_field: str | core.StringOut,
    ):
        super().__init__(
            args=JsonTokenTypeConfiguration.Args(
                group_attribute_field=group_attribute_field,
                user_name_attribute_field=user_name_attribute_field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_attribute_field: str | core.StringOut = core.arg()

        user_name_attribute_field: str | core.StringOut = core.arg()


@core.schema
class JwtTokenTypeConfiguration(core.Schema):

    claim_regex: str | core.StringOut | None = core.attr(str, default=None)

    group_attribute_field: str | core.StringOut | None = core.attr(str, default=None)

    issuer: str | core.StringOut | None = core.attr(str, default=None)

    key_location: str | core.StringOut = core.attr(str)

    secrets_manager_arn: str | core.StringOut | None = core.attr(str, default=None)

    url: str | core.StringOut | None = core.attr(str, default=None)

    user_name_attribute_field: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key_location: str | core.StringOut,
        claim_regex: str | core.StringOut | None = None,
        group_attribute_field: str | core.StringOut | None = None,
        issuer: str | core.StringOut | None = None,
        secrets_manager_arn: str | core.StringOut | None = None,
        url: str | core.StringOut | None = None,
        user_name_attribute_field: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=JwtTokenTypeConfiguration.Args(
                key_location=key_location,
                claim_regex=claim_regex,
                group_attribute_field=group_attribute_field,
                issuer=issuer,
                secrets_manager_arn=secrets_manager_arn,
                url=url,
                user_name_attribute_field=user_name_attribute_field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        claim_regex: str | core.StringOut | None = core.arg(default=None)

        group_attribute_field: str | core.StringOut | None = core.arg(default=None)

        issuer: str | core.StringOut | None = core.arg(default=None)

        key_location: str | core.StringOut = core.arg()

        secrets_manager_arn: str | core.StringOut | None = core.arg(default=None)

        url: str | core.StringOut | None = core.arg(default=None)

        user_name_attribute_field: str | core.StringOut | None = core.arg(default=None)


@core.schema
class UserTokenConfigurations(core.Schema):

    json_token_type_configuration: JsonTokenTypeConfiguration | None = core.attr(
        JsonTokenTypeConfiguration, default=None
    )

    jwt_token_type_configuration: JwtTokenTypeConfiguration | None = core.attr(
        JwtTokenTypeConfiguration, default=None
    )

    def __init__(
        self,
        *,
        json_token_type_configuration: JsonTokenTypeConfiguration | None = None,
        jwt_token_type_configuration: JwtTokenTypeConfiguration | None = None,
    ):
        super().__init__(
            args=UserTokenConfigurations.Args(
                json_token_type_configuration=json_token_type_configuration,
                jwt_token_type_configuration=jwt_token_type_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        json_token_type_configuration: JsonTokenTypeConfiguration | None = core.arg(default=None)

        jwt_token_type_configuration: JwtTokenTypeConfiguration | None = core.arg(default=None)


@core.schema
class ServerSideEncryptionConfiguration(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ServerSideEncryptionConfiguration.Args(
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class UserGroupResolutionConfiguration(core.Schema):

    user_group_resolution_mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        user_group_resolution_mode: str | core.StringOut,
    ):
        super().__init__(
            args=UserGroupResolutionConfiguration.Args(
                user_group_resolution_mode=user_group_resolution_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        user_group_resolution_mode: str | core.StringOut = core.arg()


@core.schema
class FaqStatistics(core.Schema):

    indexed_question_answers_count: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        indexed_question_answers_count: int | core.IntOut,
    ):
        super().__init__(
            args=FaqStatistics.Args(
                indexed_question_answers_count=indexed_question_answers_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        indexed_question_answers_count: int | core.IntOut = core.arg()


@core.schema
class TextDocumentStatistics(core.Schema):

    indexed_text_bytes: int | core.IntOut = core.attr(int, computed=True)

    indexed_text_documents_count: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        indexed_text_bytes: int | core.IntOut,
        indexed_text_documents_count: int | core.IntOut,
    ):
        super().__init__(
            args=TextDocumentStatistics.Args(
                indexed_text_bytes=indexed_text_bytes,
                indexed_text_documents_count=indexed_text_documents_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        indexed_text_bytes: int | core.IntOut = core.arg()

        indexed_text_documents_count: int | core.IntOut = core.arg()


@core.schema
class IndexStatistics(core.Schema):

    faq_statistics: list[FaqStatistics] | core.ArrayOut[FaqStatistics] = core.attr(
        FaqStatistics, computed=True, kind=core.Kind.array
    )

    text_document_statistics: list[TextDocumentStatistics] | core.ArrayOut[
        TextDocumentStatistics
    ] = core.attr(TextDocumentStatistics, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        faq_statistics: list[FaqStatistics] | core.ArrayOut[FaqStatistics],
        text_document_statistics: list[TextDocumentStatistics]
        | core.ArrayOut[TextDocumentStatistics],
    ):
        super().__init__(
            args=IndexStatistics.Args(
                faq_statistics=faq_statistics,
                text_document_statistics=text_document_statistics,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        faq_statistics: list[FaqStatistics] | core.ArrayOut[FaqStatistics] = core.arg()

        text_document_statistics: list[TextDocumentStatistics] | core.ArrayOut[
            TextDocumentStatistics
        ] = core.arg()


@core.schema
class Search(core.Schema):

    displayable: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    facetable: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    searchable: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    sortable: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        displayable: bool | core.BoolOut | None = None,
        facetable: bool | core.BoolOut | None = None,
        searchable: bool | core.BoolOut | None = None,
        sortable: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Search.Args(
                displayable=displayable,
                facetable=facetable,
                searchable=searchable,
                sortable=sortable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        displayable: bool | core.BoolOut | None = core.arg(default=None)

        facetable: bool | core.BoolOut | None = core.arg(default=None)

        searchable: bool | core.BoolOut | None = core.arg(default=None)

        sortable: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Relevance(core.Schema):

    duration: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    freshness: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    importance: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    rank_order: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    values_importance_map: dict[str, int] | core.MapOut[core.IntOut] | None = core.attr(
        int, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        duration: str | core.StringOut | None = None,
        freshness: bool | core.BoolOut | None = None,
        importance: int | core.IntOut | None = None,
        rank_order: str | core.StringOut | None = None,
        values_importance_map: dict[str, int] | core.MapOut[core.IntOut] | None = None,
    ):
        super().__init__(
            args=Relevance.Args(
                duration=duration,
                freshness=freshness,
                importance=importance,
                rank_order=rank_order,
                values_importance_map=values_importance_map,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration: str | core.StringOut | None = core.arg(default=None)

        freshness: bool | core.BoolOut | None = core.arg(default=None)

        importance: int | core.IntOut | None = core.arg(default=None)

        rank_order: str | core.StringOut | None = core.arg(default=None)

        values_importance_map: dict[str, int] | core.MapOut[core.IntOut] | None = core.arg(
            default=None
        )


@core.schema
class DocumentMetadataConfigurationUpdates(core.Schema):

    name: str | core.StringOut = core.attr(str)

    relevance: Relevance | None = core.attr(Relevance, default=None, computed=True)

    search: Search | None = core.attr(Search, default=None, computed=True)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
        relevance: Relevance | None = None,
        search: Search | None = None,
    ):
        super().__init__(
            args=DocumentMetadataConfigurationUpdates.Args(
                name=name,
                type=type,
                relevance=relevance,
                search=search,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        relevance: Relevance | None = core.arg(default=None)

        search: Search | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_kendra_index", namespace="aws_kendra")
class Index(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    capacity_units: CapacityUnits | None = core.attr(CapacityUnits, default=None, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    document_metadata_configuration_updates: list[
        DocumentMetadataConfigurationUpdates
    ] | core.ArrayOut[DocumentMetadataConfigurationUpdates] | None = core.attr(
        DocumentMetadataConfigurationUpdates, default=None, computed=True, kind=core.Kind.array
    )

    edition: str | core.StringOut | None = core.attr(str, default=None)

    error_message: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    index_statistics: list[IndexStatistics] | core.ArrayOut[IndexStatistics] = core.attr(
        IndexStatistics, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    server_side_encryption_configuration: ServerSideEncryptionConfiguration | None = core.attr(
        ServerSideEncryptionConfiguration, default=None
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    updated_at: str | core.StringOut = core.attr(str, computed=True)

    user_context_policy: str | core.StringOut | None = core.attr(str, default=None)

    user_group_resolution_configuration: UserGroupResolutionConfiguration | None = core.attr(
        UserGroupResolutionConfiguration, default=None
    )

    user_token_configurations: UserTokenConfigurations | None = core.attr(
        UserTokenConfigurations, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        capacity_units: CapacityUnits | None = None,
        description: str | core.StringOut | None = None,
        document_metadata_configuration_updates: list[DocumentMetadataConfigurationUpdates]
        | core.ArrayOut[DocumentMetadataConfigurationUpdates]
        | None = None,
        edition: str | core.StringOut | None = None,
        server_side_encryption_configuration: ServerSideEncryptionConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_context_policy: str | core.StringOut | None = None,
        user_group_resolution_configuration: UserGroupResolutionConfiguration | None = None,
        user_token_configurations: UserTokenConfigurations | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Index.Args(
                name=name,
                role_arn=role_arn,
                capacity_units=capacity_units,
                description=description,
                document_metadata_configuration_updates=document_metadata_configuration_updates,
                edition=edition,
                server_side_encryption_configuration=server_side_encryption_configuration,
                tags=tags,
                tags_all=tags_all,
                user_context_policy=user_context_policy,
                user_group_resolution_configuration=user_group_resolution_configuration,
                user_token_configurations=user_token_configurations,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_units: CapacityUnits | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        document_metadata_configuration_updates: list[
            DocumentMetadataConfigurationUpdates
        ] | core.ArrayOut[DocumentMetadataConfigurationUpdates] | None = core.arg(default=None)

        edition: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        server_side_encryption_configuration: ServerSideEncryptionConfiguration | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_context_policy: str | core.StringOut | None = core.arg(default=None)

        user_group_resolution_configuration: UserGroupResolutionConfiguration | None = core.arg(
            default=None
        )

        user_token_configurations: UserTokenConfigurations | None = core.arg(default=None)
