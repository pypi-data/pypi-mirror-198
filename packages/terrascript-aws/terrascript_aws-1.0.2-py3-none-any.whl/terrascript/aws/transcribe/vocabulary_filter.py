import terrascript.core as core


@core.resource(type="aws_transcribe_vocabulary_filter", namespace="aws_transcribe")
class VocabularyFilter(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    download_uri: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    language_code: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vocabulary_filter_file_uri: str | core.StringOut | None = core.attr(str, default=None)

    vocabulary_filter_name: str | core.StringOut = core.attr(str)

    words: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        language_code: str | core.StringOut,
        vocabulary_filter_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vocabulary_filter_file_uri: str | core.StringOut | None = None,
        words: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VocabularyFilter.Args(
                language_code=language_code,
                vocabulary_filter_name=vocabulary_filter_name,
                tags=tags,
                tags_all=tags_all,
                vocabulary_filter_file_uri=vocabulary_filter_file_uri,
                words=words,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        language_code: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vocabulary_filter_file_uri: str | core.StringOut | None = core.arg(default=None)

        vocabulary_filter_name: str | core.StringOut = core.arg()

        words: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
