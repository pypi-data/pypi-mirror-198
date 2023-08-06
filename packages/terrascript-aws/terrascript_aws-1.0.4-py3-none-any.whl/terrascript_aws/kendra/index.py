import terrascript.core as core


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


@core.resource(type="aws_kendra_index", namespace="kendra")
class Index(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Index.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A block that sets the number of additional document storage and query capacity units that
    should be used by the index. [Detailed below](#capacity_units).
    """
    capacity_units: CapacityUnits | None = core.attr(CapacityUnits, default=None, computed=True)

    """
    The Unix datetime that the index was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the Index.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) One or more blocks that specify the configuration settings for any metadata applied to th
    e documents in the index. Minimum number of 0 items. Maximum number of 500 items. If specified, you
    must define all elements, including those that are provided by default. These index fields are docum
    ented at [Amazon Kendra Index documentation](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index.
    html). For an example resource that defines these default index fields, refer to the [default exampl
    e above](#specifying-the-predefined-elements). For an example resource that appends additional index
    fields, refer to the [append example above](#appending-additional-elements). All arguments for each
    block must be specified. Note that blocks cannot be removed since index fields cannot be deleted. T
    his argument is [detailed below](#document_metadata_configuration_updates).
    """
    document_metadata_configuration_updates: list[
        DocumentMetadataConfigurationUpdates
    ] | core.ArrayOut[DocumentMetadataConfigurationUpdates] | None = core.attr(
        DocumentMetadataConfigurationUpdates, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The Amazon Kendra edition to use for the index. Choose `DEVELOPER_EDITION` for indexes in
    tended for development, testing, or proof of concept. Use `ENTERPRISE_EDITION` for your production d
    atabases. Once you set the edition for an index, it can't be changed. Defaults to `ENTERPRISE_EDITIO
    N`
    """
    edition: str | core.StringOut | None = core.attr(str, default=None)

    """
    When the Status field value is `FAILED`, this contains a message that explains why.
    """
    error_message: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the Index.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A block that provides information about the number of FAQ questions and answers and the number of te
    xt documents indexed. [Detailed below](#index_statistics).
    """
    index_statistics: list[IndexStatistics] | core.ArrayOut[IndexStatistics] = core.attr(
        IndexStatistics, computed=True, kind=core.Kind.array
    )

    """
    (Required) Specifies the name of the Index.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) An AWS Identity and Access Management (IAM) role that gives Amazon Kendra permissions to
    access your Amazon CloudWatch logs and metrics. This is also the role you use when you call the `Bat
    chPutDocument` API to index documents from an Amazon S3 bucket.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) A block that specifies the identifier of the AWS KMS customer managed key (CMK) that's us
    ed to encrypt data indexed by Amazon Kendra. Amazon Kendra doesn't support asymmetric CMKs. [Detaile
    d below](#server_side_encryption_configuration).
    """
    server_side_encryption_configuration: ServerSideEncryptionConfiguration | None = core.attr(
        ServerSideEncryptionConfiguration, default=None
    )

    """
    The current status of the index. When the value is `ACTIVE`, the index is ready for use. If the Stat
    us field value is `FAILED`, the `error_message` field contains a message that explains why.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Tags to apply to the Index. If configured with a provider
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
    The Unix datetime that the index was last updated.
    """
    updated_at: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The user context policy. Valid values are `ATTRIBUTE_FILTER` or `USER_TOKEN`. For more in
    formation, refer to [UserContextPolicy](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateIndex
    .html#Kendra-CreateIndex-request-UserContextPolicy). Defaults to `ATTRIBUTE_FILTER`.
    """
    user_context_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A block that enables fetching access levels of groups and users from an AWS Single Sign-O
    n identity source. To configure this, see [UserGroupResolutionConfiguration](https://docs.aws.amazon
    .com/kendra/latest/dg/API_UserGroupResolutionConfiguration.html). [Detailed below](#user_group_resol
    ution_configuration).
    """
    user_group_resolution_configuration: UserGroupResolutionConfiguration | None = core.attr(
        UserGroupResolutionConfiguration, default=None
    )

    """
    (Optional) A block that specifies the user token configuration. [Detailed below](#user_token_configu
    rations).
    """
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
