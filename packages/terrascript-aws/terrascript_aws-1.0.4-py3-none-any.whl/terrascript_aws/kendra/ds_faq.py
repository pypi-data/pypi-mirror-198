import terrascript.core as core


@core.schema
class S3Path(core.Schema):

    bucket: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str, computed=True)

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


@core.data(type="aws_kendra_faq", namespace="kendra")
class DsFaq(core.Data):
    """
    The Amazon Resource Name (ARN) of the FAQ.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Unix datetime that the faq was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the FAQ.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    When the `status` field value is `FAILED`, this contains a message that explains why.
    """
    error_message: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identifier of the FAQ.
    """
    faq_id: str | core.StringOut = core.attr(str)

    """
    The file format used by the input files for the FAQ. Valid Values are `CSV`, `CSV_WITH_HEADER`, `JSO
    N`.
    """
    file_format: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifiers of the FAQ and index separated by a slash (`/`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identifier of the index that contains the FAQ.
    """
    index_id: str | core.StringOut = core.attr(str)

    """
    The code for a language. This shows a supported language for the FAQ document. For more information
    on supported languages, including their codes, see [Adding documents in languages other than English
    ](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html).
    """
    language_code: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the name of the FAQ.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of a role with permission to access the S3 bucket that contains the F
    AQs. For more information, see [IAM Roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/late
    st/dg/iam-roles.html).
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The S3 location of the FAQ input data. Detailed below.
    """
    s3_path: list[S3Path] | core.ArrayOut[S3Path] = core.attr(
        S3Path, computed=True, kind=core.Kind.array
    )

    """
    The status of the FAQ. It is ready to use when the status is ACTIVE.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Metadata that helps organize the FAQs you create.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The date and time that the FAQ was last updated.
    """
    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        faq_id: str | core.StringOut,
        index_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFaq.Args(
                faq_id=faq_id,
                index_id=index_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        faq_id: str | core.StringOut = core.arg()

        index_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
