import terrascript.core as core


@core.resource(type="aws_transcribe_medical_vocabulary", namespace="transcribe")
class MedicalVocabulary(core.Resource):
    """
    ARN of the MedicalVocabulary.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Generated download URI.
    """
    download_uri: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the MedicalVocabulary.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The language code you selected for your medical vocabulary. US English (en-US) is the onl
    y language supported with Amazon Transcribe Medical.
    """
    language_code: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the MedicalVocabulary. If configured with a provider [`default
    _tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#defaul
    t_tags-configuration-block) present, tags with matching keys will overwrite those defined at the pro
    vider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The Amazon S3 location (URI) of the text file that contains your custom medical vocabular
    y.
    """
    vocabulary_file_uri: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the Medical Vocabulary.
    """
    vocabulary_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        language_code: str | core.StringOut,
        vocabulary_file_uri: str | core.StringOut,
        vocabulary_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MedicalVocabulary.Args(
                language_code=language_code,
                vocabulary_file_uri=vocabulary_file_uri,
                vocabulary_name=vocabulary_name,
                tags=tags,
                tags_all=tags_all,
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

        vocabulary_file_uri: str | core.StringOut = core.arg()

        vocabulary_name: str | core.StringOut = core.arg()
