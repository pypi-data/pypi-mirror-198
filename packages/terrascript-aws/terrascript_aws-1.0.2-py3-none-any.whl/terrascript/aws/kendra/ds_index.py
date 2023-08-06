import terrascript.core as core


@core.schema
class Search(core.Schema):

    displayable: bool | core.BoolOut = core.attr(bool, computed=True)

    facetable: bool | core.BoolOut = core.attr(bool, computed=True)

    searchable: bool | core.BoolOut = core.attr(bool, computed=True)

    sortable: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        displayable: bool | core.BoolOut,
        facetable: bool | core.BoolOut,
        searchable: bool | core.BoolOut,
        sortable: bool | core.BoolOut,
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
        displayable: bool | core.BoolOut = core.arg()

        facetable: bool | core.BoolOut = core.arg()

        searchable: bool | core.BoolOut = core.arg()

        sortable: bool | core.BoolOut = core.arg()


@core.schema
class Relevance(core.Schema):

    duration: str | core.StringOut = core.attr(str, computed=True)

    freshness: bool | core.BoolOut = core.attr(bool, computed=True)

    importance: int | core.IntOut = core.attr(int, computed=True)

    rank_order: str | core.StringOut = core.attr(str, computed=True)

    values_importance_map: dict[str, int] | core.MapOut[core.IntOut] = core.attr(
        int, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        duration: str | core.StringOut,
        freshness: bool | core.BoolOut,
        importance: int | core.IntOut,
        rank_order: str | core.StringOut,
        values_importance_map: dict[str, int] | core.MapOut[core.IntOut],
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
        duration: str | core.StringOut = core.arg()

        freshness: bool | core.BoolOut = core.arg()

        importance: int | core.IntOut = core.arg()

        rank_order: str | core.StringOut = core.arg()

        values_importance_map: dict[str, int] | core.MapOut[core.IntOut] = core.arg()


@core.schema
class DocumentMetadataConfigurationUpdates(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    relevance: list[Relevance] | core.ArrayOut[Relevance] = core.attr(
        Relevance, computed=True, kind=core.Kind.array
    )

    search: list[Search] | core.ArrayOut[Search] = core.attr(
        Search, computed=True, kind=core.Kind.array
    )

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        relevance: list[Relevance] | core.ArrayOut[Relevance],
        search: list[Search] | core.ArrayOut[Search],
        type: str | core.StringOut,
    ):
        super().__init__(
            args=DocumentMetadataConfigurationUpdates.Args(
                name=name,
                relevance=relevance,
                search=search,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        relevance: list[Relevance] | core.ArrayOut[Relevance] = core.arg()

        search: list[Search] | core.ArrayOut[Search] = core.arg()

        type: str | core.StringOut = core.arg()


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
class UserGroupResolutionConfiguration(core.Schema):

    user_group_resolution_mode: str | core.StringOut = core.attr(str, computed=True)

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
class JsonTokenTypeConfiguration(core.Schema):

    group_attribute_field: str | core.StringOut = core.attr(str, computed=True)

    user_name_attribute_field: str | core.StringOut = core.attr(str, computed=True)

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

    claim_regex: str | core.StringOut = core.attr(str, computed=True)

    group_attribute_field: str | core.StringOut = core.attr(str, computed=True)

    issuer: str | core.StringOut = core.attr(str, computed=True)

    key_location: str | core.StringOut = core.attr(str, computed=True)

    secrets_manager_arn: str | core.StringOut = core.attr(str, computed=True)

    url: str | core.StringOut = core.attr(str, computed=True)

    user_name_attribute_field: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        claim_regex: str | core.StringOut,
        group_attribute_field: str | core.StringOut,
        issuer: str | core.StringOut,
        key_location: str | core.StringOut,
        secrets_manager_arn: str | core.StringOut,
        url: str | core.StringOut,
        user_name_attribute_field: str | core.StringOut,
    ):
        super().__init__(
            args=JwtTokenTypeConfiguration.Args(
                claim_regex=claim_regex,
                group_attribute_field=group_attribute_field,
                issuer=issuer,
                key_location=key_location,
                secrets_manager_arn=secrets_manager_arn,
                url=url,
                user_name_attribute_field=user_name_attribute_field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        claim_regex: str | core.StringOut = core.arg()

        group_attribute_field: str | core.StringOut = core.arg()

        issuer: str | core.StringOut = core.arg()

        key_location: str | core.StringOut = core.arg()

        secrets_manager_arn: str | core.StringOut = core.arg()

        url: str | core.StringOut = core.arg()

        user_name_attribute_field: str | core.StringOut = core.arg()


@core.schema
class UserTokenConfigurations(core.Schema):

    json_token_type_configuration: list[JsonTokenTypeConfiguration] | core.ArrayOut[
        JsonTokenTypeConfiguration
    ] = core.attr(JsonTokenTypeConfiguration, computed=True, kind=core.Kind.array)

    jwt_token_type_configuration: list[JwtTokenTypeConfiguration] | core.ArrayOut[
        JwtTokenTypeConfiguration
    ] = core.attr(JwtTokenTypeConfiguration, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        json_token_type_configuration: list[JsonTokenTypeConfiguration]
        | core.ArrayOut[JsonTokenTypeConfiguration],
        jwt_token_type_configuration: list[JwtTokenTypeConfiguration]
        | core.ArrayOut[JwtTokenTypeConfiguration],
    ):
        super().__init__(
            args=UserTokenConfigurations.Args(
                json_token_type_configuration=json_token_type_configuration,
                jwt_token_type_configuration=jwt_token_type_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        json_token_type_configuration: list[JsonTokenTypeConfiguration] | core.ArrayOut[
            JsonTokenTypeConfiguration
        ] = core.arg()

        jwt_token_type_configuration: list[JwtTokenTypeConfiguration] | core.ArrayOut[
            JwtTokenTypeConfiguration
        ] = core.arg()


@core.schema
class CapacityUnits(core.Schema):

    query_capacity_units: int | core.IntOut = core.attr(int, computed=True)

    storage_capacity_units: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        query_capacity_units: int | core.IntOut,
        storage_capacity_units: int | core.IntOut,
    ):
        super().__init__(
            args=CapacityUnits.Args(
                query_capacity_units=query_capacity_units,
                storage_capacity_units=storage_capacity_units,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        query_capacity_units: int | core.IntOut = core.arg()

        storage_capacity_units: int | core.IntOut = core.arg()


@core.schema
class ServerSideEncryptionConfiguration(core.Schema):

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        kms_key_id: str | core.StringOut,
    ):
        super().__init__(
            args=ServerSideEncryptionConfiguration.Args(
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut = core.arg()


@core.data(type="aws_kendra_index", namespace="aws_kendra")
class DsIndex(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    capacity_units: list[CapacityUnits] | core.ArrayOut[CapacityUnits] = core.attr(
        CapacityUnits, computed=True, kind=core.Kind.array
    )

    created_at: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    document_metadata_configuration_updates: list[
        DocumentMetadataConfigurationUpdates
    ] | core.ArrayOut[DocumentMetadataConfigurationUpdates] = core.attr(
        DocumentMetadataConfigurationUpdates, computed=True, kind=core.Kind.array
    )

    edition: str | core.StringOut = core.attr(str, computed=True)

    error_message: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str)

    index_statistics: list[IndexStatistics] | core.ArrayOut[IndexStatistics] = core.attr(
        IndexStatistics, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    server_side_encryption_configuration: list[ServerSideEncryptionConfiguration] | core.ArrayOut[
        ServerSideEncryptionConfiguration
    ] = core.attr(ServerSideEncryptionConfiguration, computed=True, kind=core.Kind.array)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    updated_at: str | core.StringOut = core.attr(str, computed=True)

    user_context_policy: str | core.StringOut = core.attr(str, computed=True)

    user_group_resolution_configuration: list[UserGroupResolutionConfiguration] | core.ArrayOut[
        UserGroupResolutionConfiguration
    ] = core.attr(UserGroupResolutionConfiguration, computed=True, kind=core.Kind.array)

    user_token_configurations: list[UserTokenConfigurations] | core.ArrayOut[
        UserTokenConfigurations
    ] = core.attr(UserTokenConfigurations, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsIndex.Args(
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
