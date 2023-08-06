import terrascript.core as core


@core.resource(type="aws_connect_vocabulary", namespace="connect")
class Vocabulary(core.Resource):
    """
    The Amazon Resource Name (ARN) of the vocabulary.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The content of the custom vocabulary in plain-text format with a table of values. Each ro
    w in the table represents a word or a phrase, described with Phrase, IPA, SoundsLike, and DisplayAs
    fields. Separate the fields with TAB characters. For more information, see [Create a custom vocabula
    ry using a table](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html#create-voc
    abulary-table). Minimum length of `1`. Maximum length of `60000`.
    """
    content: str | core.StringOut = core.attr(str)

    """
    The reason why the custom vocabulary was not created.
    """
    failure_reason: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the vocabulary
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) The language code of the vocabulary entries. For a list of languages and their correspond
    ing language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/d
    g/transcribe-whatis.html). Valid Values are `ar-AE`, `de-CH`, `de-DE`, `en-AB`, `en-AU`, `en-GB`, `e
    n-IE`, `en-IN`, `en-US`, `en-WL`, `es-ES`, `es-US`, `fr-CA`, `fr-FR`, `hi-IN`, `it-IT`, `ja-JP`, `ko
    KR`, `pt-BR`, `pt-PT`, `zh-CN`.
    """
    language_code: str | core.StringOut = core.attr(str)

    """
    The timestamp when the custom vocabulary was last modified.
    """
    last_modified_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A unique name of the custom vocabulary. Must not be more than 140 characters.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The current state of the custom vocabulary. Valid values are `CREATION_IN_PROGRESS`, `ACTIVE`, `CREA
    TION_FAILED`, `DELETE_IN_PROGRESS`.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Tags to apply to the vocabulary. If configured with a provider
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
    The identifier of the custom vocabulary.
    """
    vocabulary_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        content: str | core.StringOut,
        instance_id: str | core.StringOut,
        language_code: str | core.StringOut,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Vocabulary.Args(
                content=content,
                instance_id=instance_id,
                language_code=language_code,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content: str | core.StringOut = core.arg()

        instance_id: str | core.StringOut = core.arg()

        language_code: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
