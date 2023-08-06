import terrascript.core as core


@core.resource(type="aws_transcribe_vocabulary_filter", namespace="transcribe")
class VocabularyFilter(core.Resource):
    """
    ARN of the VocabularyFilter.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Generated download URI.
    """
    download_uri: str | core.StringOut = core.attr(str, computed=True)

    """
    VocabularyFilter name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The language code you selected for your vocabulary filter. Refer to the [supported langua
    ges](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) page for accepted co
    des.
    """
    language_code: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the VocabularyFilter. If configured with a provider [`default_
    tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default
    _tags-configuration-block) present, tags with matching keys will overwrite those defined at the prov
    ider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The Amazon S3 location (URI) of the text file that contains your custom VocabularyFilter.
    Conflicts with `words`.
    """
    vocabulary_filter_file_uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the VocabularyFilter.
    """
    vocabulary_filter_name: str | core.StringOut = core.attr(str)

    """
    (Required) - A list of terms to include in the vocabulary. Conflicts with `vocabulary_file_uri`
    """
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
