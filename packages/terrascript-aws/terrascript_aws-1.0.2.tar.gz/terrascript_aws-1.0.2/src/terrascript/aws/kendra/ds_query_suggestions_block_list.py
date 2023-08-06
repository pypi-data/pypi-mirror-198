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


@core.data(type="aws_kendra_query_suggestions_block_list", namespace="aws_kendra")
class DsQuerySuggestionsBlockList(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    error_message: str | core.StringOut = core.attr(str, computed=True)

    file_size_bytes: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    index_id: str | core.StringOut = core.attr(str)

    item_count: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    query_suggestions_block_list_id: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    source_s3_path: list[SourceS3Path] | core.ArrayOut[SourceS3Path] = core.attr(
        SourceS3Path, computed=True, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
