import terrascript.core as core


@core.resource(type="aws_transcribe_vocabulary", namespace="transcribe")
class Vocabulary(core.Resource):
    """
    ARN of the Vocabulary.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Generated download URI.
    """
    download_uri: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the Vocabulary.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The language code you selected for your vocabulary.
    """
    language_code: str | core.StringOut = core.attr(str)

    """
    (Optional) - A list of terms to include in the vocabulary. Conflicts with `vocabulary_file_uri`
    """
    phrases: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the Vocabulary. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-l
    evel.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The Amazon S3 location (URI) of the text file that contains your custom vocabulary.
    """
    vocabulary_file_uri: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name of the Vocabulary.
    """
    vocabulary_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        language_code: str | core.StringOut,
        vocabulary_name: str | core.StringOut,
        phrases: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vocabulary_file_uri: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Vocabulary.Args(
                language_code=language_code,
                vocabulary_name=vocabulary_name,
                phrases=phrases,
                tags=tags,
                tags_all=tags_all,
                vocabulary_file_uri=vocabulary_file_uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        language_code: str | core.StringOut = core.arg()

        phrases: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vocabulary_file_uri: str | core.StringOut | None = core.arg(default=None)

        vocabulary_name: str | core.StringOut = core.arg()
