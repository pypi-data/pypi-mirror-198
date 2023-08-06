import terrascript.core as core


@core.schema
class S3Path(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
    ):
        super().__init__(
            args=S3Path.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()


@core.resource(type="aws_kendra_faq", namespace="kendra")
class Faq(core.Resource):
    """
    ARN of the FAQ.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Unix datetime that the FAQ was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The description for a FAQ.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    When the Status field value is `FAILED`, this contains a message that explains why.
    """
    error_message: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the FAQ.
    """
    faq_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The file format used by the input files for the FAQ. Valid Values ar
    e `CSV`, `CSV_WITH_HEADER`, `JSON`.
    """
    file_format: str | core.StringOut | None = core.attr(str, default=None)

    """
    The unique identifiers of the FAQ and index separated by a slash (`/`)
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    index_id: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) The code for a language. This shows a supported language for the FAQ
    document. English is supported by default. For more information on supported languages, including t
    heir codes, see [Adding documents in languages other than English](https://docs.aws.amazon.com/kendr
    a/latest/dg/in-adding-languages.html).
    """
    language_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required, Forces new resource) The name that should be associated with the FAQ.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of a role with permission to access t
    he S3 bucket that contains the FAQs. For more information, see [IAM Roles for Amazon Kendra](https:/
    /docs.aws.amazon.com/kendra/latest/dg/iam-roles.html).
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The S3 location of the FAQ input data. Detailed below.
    """
    s3_path: S3Path = core.attr(S3Path)

    """
    The status of the FAQ. It is ready to use when the status is ACTIVE.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

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
    The date and time that the FAQ was last updated.
    """
    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        index_id: str | core.StringOut,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        s3_path: S3Path,
        description: str | core.StringOut | None = None,
        file_format: str | core.StringOut | None = None,
        language_code: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Faq.Args(
                index_id=index_id,
                name=name,
                role_arn=role_arn,
                s3_path=s3_path,
                description=description,
                file_format=file_format,
                language_code=language_code,
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

        file_format: str | core.StringOut | None = core.arg(default=None)

        index_id: str | core.StringOut = core.arg()

        language_code: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        s3_path: S3Path = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
