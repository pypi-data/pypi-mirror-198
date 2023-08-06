import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    default_value: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        default_value: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Parameter.Args(
                default_value=default_value,
                description=description,
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_value: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AttachmentsSource(core.Schema):

    key: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AttachmentsSource.Args(
                key=key,
                values=values,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_ssm_document", namespace="ssm")
class Document(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more configuration blocks describing attachments sources to a version of a documen
    t. Defined below.
    """
    attachments_source: list[AttachmentsSource] | core.ArrayOut[
        AttachmentsSource
    ] | None = core.attr(AttachmentsSource, default=None, kind=core.Kind.array)

    """
    (Required) The JSON or YAML content of the document.
    """
    content: str | core.StringOut = core.attr(str)

    """
    The date the document was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The default version of the document.
    """
    default_version: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the document.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, defaults to JSON) The format of the document. Valid document types include: `JSON` and `Y
    AML`
    """
    document_format: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The type of the document. Valid document types include: `Automation`, `Command`, `Package
    , `Policy`, and `Session`
    """
    document_type: str | core.StringOut = core.attr(str)

    """
    The document version.
    """
    document_version: str | core.StringOut = core.attr(str, computed=True)

    """
    The sha1 or sha256 of the document content
    """
    hash: str | core.StringOut = core.attr(str, computed=True)

    """
    "Sha1" "Sha256". The hashing algorithm used when hashing the content.
    """
    hash_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The latest version of the document.
    """
    latest_version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the document.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The AWS user account of the person who created the document.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    The parameters that are available to this document.
    """
    parameter: list[Parameter] | core.ArrayOut[Parameter] = core.attr(
        Parameter, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Additional Permissions to attach to the document. See [Permissions](#permissions) below f
    or details.
    """
    permissions: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A list of OS platforms compatible with this SSM document, either "Windows" or "Linux".
    """
    platform_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The schema version of the document.
    """
    schema_version: str | core.StringOut = core.attr(str, computed=True)

    """
    "Creating", "Active" or "Deleting". The current status of the document.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the object. If configured with a provider [`default_tags` conf
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

    """
    (Optional) The target type which defines the kinds of resources the document can run on. For example
    , /AWS::EC2::Instance. For a list of valid resource types, see AWS Resource Types Reference (http://
    docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)
    """
    target_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A field specifying the version of the artifact you are creating with the document. For ex
    ample, "Release 12, Update 6". This value is unique across all versions of a document and cannot be
    changed for an existing document version.
    """
    version_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        content: str | core.StringOut,
        document_type: str | core.StringOut,
        name: str | core.StringOut,
        attachments_source: list[AttachmentsSource]
        | core.ArrayOut[AttachmentsSource]
        | None = None,
        document_format: str | core.StringOut | None = None,
        permissions: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_type: str | core.StringOut | None = None,
        version_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Document.Args(
                content=content,
                document_type=document_type,
                name=name,
                attachments_source=attachments_source,
                document_format=document_format,
                permissions=permissions,
                tags=tags,
                tags_all=tags_all,
                target_type=target_type,
                version_name=version_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attachments_source: list[AttachmentsSource] | core.ArrayOut[
            AttachmentsSource
        ] | None = core.arg(default=None)

        content: str | core.StringOut = core.arg()

        document_format: str | core.StringOut | None = core.arg(default=None)

        document_type: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        permissions: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_type: str | core.StringOut | None = core.arg(default=None)

        version_name: str | core.StringOut | None = core.arg(default=None)
