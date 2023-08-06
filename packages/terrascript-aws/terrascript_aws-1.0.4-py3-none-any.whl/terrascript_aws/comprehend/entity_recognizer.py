import terrascript.core as core


@core.schema
class Documents(core.Schema):

    input_format: str | core.StringOut | None = core.attr(str, default=None)

    s3_uri: str | core.StringOut = core.attr(str)

    test_s3_uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_uri: str | core.StringOut,
        input_format: str | core.StringOut | None = None,
        test_s3_uri: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Documents.Args(
                s3_uri=s3_uri,
                input_format=input_format,
                test_s3_uri=test_s3_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_format: str | core.StringOut | None = core.arg(default=None)

        s3_uri: str | core.StringOut = core.arg()

        test_s3_uri: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EntityList(core.Schema):

    s3_uri: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        s3_uri: str | core.StringOut,
    ):
        super().__init__(
            args=EntityList.Args(
                s3_uri=s3_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_uri: str | core.StringOut = core.arg()


@core.schema
class EntityTypes(core.Schema):

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=EntityTypes.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


@core.schema
class Annotations(core.Schema):

    s3_uri: str | core.StringOut = core.attr(str)

    test_s3_uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_uri: str | core.StringOut,
        test_s3_uri: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Annotations.Args(
                s3_uri=s3_uri,
                test_s3_uri=test_s3_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_uri: str | core.StringOut = core.arg()

        test_s3_uri: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AugmentedManifests(core.Schema):

    annotation_data_s3_uri: str | core.StringOut | None = core.attr(str, default=None)

    attribute_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    document_type: str | core.StringOut | None = core.attr(str, default=None)

    s3_uri: str | core.StringOut = core.attr(str)

    source_documents_s3_uri: str | core.StringOut | None = core.attr(str, default=None)

    split: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        attribute_names: list[str] | core.ArrayOut[core.StringOut],
        s3_uri: str | core.StringOut,
        annotation_data_s3_uri: str | core.StringOut | None = None,
        document_type: str | core.StringOut | None = None,
        source_documents_s3_uri: str | core.StringOut | None = None,
        split: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AugmentedManifests.Args(
                attribute_names=attribute_names,
                s3_uri=s3_uri,
                annotation_data_s3_uri=annotation_data_s3_uri,
                document_type=document_type,
                source_documents_s3_uri=source_documents_s3_uri,
                split=split,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        annotation_data_s3_uri: str | core.StringOut | None = core.arg(default=None)

        attribute_names: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        document_type: str | core.StringOut | None = core.arg(default=None)

        s3_uri: str | core.StringOut = core.arg()

        source_documents_s3_uri: str | core.StringOut | None = core.arg(default=None)

        split: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InputDataConfig(core.Schema):

    annotations: Annotations | None = core.attr(Annotations, default=None)

    augmented_manifests: list[AugmentedManifests] | core.ArrayOut[
        AugmentedManifests
    ] | None = core.attr(AugmentedManifests, default=None, kind=core.Kind.array)

    data_format: str | core.StringOut | None = core.attr(str, default=None)

    documents: Documents | None = core.attr(Documents, default=None)

    entity_list: EntityList | None = core.attr(EntityList, default=None)

    entity_types: list[EntityTypes] | core.ArrayOut[EntityTypes] = core.attr(
        EntityTypes, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        entity_types: list[EntityTypes] | core.ArrayOut[EntityTypes],
        annotations: Annotations | None = None,
        augmented_manifests: list[AugmentedManifests]
        | core.ArrayOut[AugmentedManifests]
        | None = None,
        data_format: str | core.StringOut | None = None,
        documents: Documents | None = None,
        entity_list: EntityList | None = None,
    ):
        super().__init__(
            args=InputDataConfig.Args(
                entity_types=entity_types,
                annotations=annotations,
                augmented_manifests=augmented_manifests,
                data_format=data_format,
                documents=documents,
                entity_list=entity_list,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        annotations: Annotations | None = core.arg(default=None)

        augmented_manifests: list[AugmentedManifests] | core.ArrayOut[
            AugmentedManifests
        ] | None = core.arg(default=None)

        data_format: str | core.StringOut | None = core.arg(default=None)

        documents: Documents | None = core.arg(default=None)

        entity_list: EntityList | None = core.arg(default=None)

        entity_types: list[EntityTypes] | core.ArrayOut[EntityTypes] = core.arg()


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnets: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnets=subnets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_comprehend_entity_recognizer", namespace="comprehend")
class EntityRecognizer(core.Resource):
    """
    ARN of the Entity Recognizer version.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN for an IAM Role which allows Comprehend to read the training and testing data.
    """
    data_access_role_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration for the training and testing data.
    """
    input_data_config: InputDataConfig = core.attr(InputDataConfig)

    """
    (Required) Two-letter language code for the language.
    """
    language_code: str | core.StringOut = core.attr(str)

    """
    (Optional) The ID or ARN of a KMS Key used to encrypt trained Entity Recognizers.
    """
    model_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name for the Entity Recognizer.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` Co
    nfiguration Block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags wi
    th matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](/docs/providers/aws/index.html#default_tags-configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Name for the version of the Entity Recognizer.
    """
    version_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique version name beginning with the specified prefix.
    """
    version_name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) ID or ARN of a KMS Key used to encrypt storage volumes during job processing.
    """
    volume_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration parameters for VPC to contain Entity Recognizer resources.
    """
    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        data_access_role_arn: str | core.StringOut,
        input_data_config: InputDataConfig,
        language_code: str | core.StringOut,
        name: str | core.StringOut,
        model_kms_key_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        version_name: str | core.StringOut | None = None,
        version_name_prefix: str | core.StringOut | None = None,
        volume_kms_key_id: str | core.StringOut | None = None,
        vpc_config: VpcConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EntityRecognizer.Args(
                data_access_role_arn=data_access_role_arn,
                input_data_config=input_data_config,
                language_code=language_code,
                name=name,
                model_kms_key_id=model_kms_key_id,
                tags=tags,
                tags_all=tags_all,
                version_name=version_name,
                version_name_prefix=version_name_prefix,
                volume_kms_key_id=volume_kms_key_id,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        data_access_role_arn: str | core.StringOut = core.arg()

        input_data_config: InputDataConfig = core.arg()

        language_code: str | core.StringOut = core.arg()

        model_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        version_name: str | core.StringOut | None = core.arg(default=None)

        version_name_prefix: str | core.StringOut | None = core.arg(default=None)

        volume_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)
