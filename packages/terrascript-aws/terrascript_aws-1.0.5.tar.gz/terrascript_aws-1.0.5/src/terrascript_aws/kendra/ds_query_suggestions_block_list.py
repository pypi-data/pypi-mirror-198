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


@core.data(type="aws_kendra_query_suggestions_block_list", namespace="kendra")
class DsQuerySuggestionsBlockList(core.Data):
    """
    The Amazon Resource Name (ARN) of the block list.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date-time a block list was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    The description for the block list.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The error message containing details if there are issues processing the block list.
    """
    error_message: str | core.StringOut = core.attr(str, computed=True)

    """
    The current size of the block list text file in S3.
    """
    file_size_bytes: int | core.IntOut = core.attr(int, computed=True)

    """
    The unique identifiers of the block list and index separated by a slash (`/`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identifier of the index that contains the block list.
    """
    index_id: str | core.StringOut = core.attr(str)

    """
    The current number of valid, non-empty words or phrases in the block list text file.
    """
    item_count: int | core.IntOut = core.attr(int, computed=True)

    """
    The name of the block list.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identifier of the block list.
    """
    query_suggestions_block_list_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of a role with permission to access the S3 bucket that contains the b
    lock list. For more information, see [IAM Roles for Amazon Kendra](https://docs.aws.amazon.com/kendr
    a/latest/dg/iam-roles.html).
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The S3 location of the block list input data. Detailed below.
    """
    source_s3_path: list[SourceS3Path] | core.ArrayOut[SourceS3Path] = core.attr(
        SourceS3Path, computed=True, kind=core.Kind.array
    )

    """
    The current status of the block list. When the value is `ACTIVE`, the block list is ready for use.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Metadata that helps organize the block list you create.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The date and time that the block list was last updated.
    """
    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        index_id: str | core.StringOut,
        query_suggestions_block_list_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsQuerySuggestionsBlockList.Args(
                index_id=index_id,
                query_suggestions_block_list_id=query_suggestions_block_list_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_id: str | core.StringOut = core.arg()

        query_suggestions_block_list_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
