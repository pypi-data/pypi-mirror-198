import terrascript.core as core


@core.schema
class SourceS3Path(core.Schema):

    bucket: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
    ):
        super().__init__(
            args=SourceS3Path.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()


@core.data(type="aws_kendra_thesaurus", namespace="kendra")
class DsThesaurus(core.Data):
    """
    The Amazon Resource Name (ARN) of the Thesaurus.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Unix datetime that the Thesaurus was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the Thesaurus.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    When the `status` field value is `FAILED`, this contains a message that explains why.
    """
    error_message: str | core.StringOut = core.attr(str, computed=True)

    """
    The size of the Thesaurus file in bytes.
    """
    file_size_bytes: int | core.IntOut = core.attr(int, computed=True)

    """
    The unique identifiers of the Thesaurus and index separated by a slash (`/`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identifier of the index that contains the Thesaurus.
    """
    index_id: str | core.StringOut = core.attr(str)

    """
    Specifies the name of the Thesaurus.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of a role with permission to access the S3 bucket that contains the T
    hesaurus. For more information, see [IAM Roles for Amazon Kendra](https://docs.aws.amazon.com/kendra
    /latest/dg/iam-roles.html).
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The S3 location of the Thesaurus input data. Detailed below.
    """
    source_s3_path: list[SourceS3Path] | core.ArrayOut[SourceS3Path] = core.attr(
        SourceS3Path, computed=True, kind=core.Kind.array
    )

    """
    The status of the Thesaurus. It is ready to use when the status is `ACTIVE`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of synonym rules in the Thesaurus file.
    """
    synonym_rule_count: int | core.IntOut = core.attr(int, computed=True)

    """
    Metadata that helps organize the Thesaurus you create.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The number of unique terms in the Thesaurus file. For example, the synonyms `a,b,c` and `a=>d`, the
    term count would be 4.
    """
    term_count: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The identifier of the Thesaurus.
    """
    thesaurus_id: str | core.StringOut = core.attr(str)

    """
    The date and time that the Thesaurus was last updated.
    """
    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        index_id: str | core.StringOut,
        thesaurus_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsThesaurus.Args(
                index_id=index_id,
                thesaurus_id=thesaurus_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        thesaurus_id: str | core.StringOut = core.arg()
