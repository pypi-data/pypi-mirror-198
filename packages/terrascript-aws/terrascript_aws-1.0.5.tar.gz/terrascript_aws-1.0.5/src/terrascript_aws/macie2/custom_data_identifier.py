import terrascript.core as core


@core.resource(type="aws_macie2_custom_data_identifier", namespace="macie2")
class CustomDataIdentifier(core.Resource):
    """
    The Amazon Resource Name (ARN) of the custom data identifier.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time, in UTC and extended RFC 3339 format, when the Amazon Macie account was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A custom description of the custom data identifier. The description can contain as many a
    s 512 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The unique identifier (ID) of the macie custom data identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An array that lists specific character sequences (ignore words) to exclude from the resul
    ts. If the text matched by the regular expression is the same as any string in this array, Amazon Ma
    cie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 9
    0 characters. Ignore words are case sensitive.
    """
    ignore_words: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) An array that lists specific character sequences (keywords), one of which must be within
    proximity (`maximum_match_distance`) of the regular expression to match. The array can contain as m
    any as 50 keywords. Each keyword can contain 3 - 90 characters. Keywords aren't case sensitive.
    """
    keywords: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The maximum number of characters that can exist between text that matches the regex patte
    rn and the character sequences specified by the keywords array. Macie includes or excludes a result
    based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 -
    300 characters. The default value is 50.
    """
    maximum_match_distance: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) A custom name for the custom data identifier. The name can contain as many as 128 charact
    ers. If omitted, Terraform will assign a random, unique name. Conflicts with `name_prefix`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The regular expression (regex) that defines the pattern to match. The expression can cont
    ain as many as 512 characters.
    """
    regex: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of key-value pairs that specifies the tags to associate with the custom data identi
    fier.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut | None = None,
        ignore_words: list[str] | core.ArrayOut[core.StringOut] | None = None,
        keywords: list[str] | core.ArrayOut[core.StringOut] | None = None,
        maximum_match_distance: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        regex: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CustomDataIdentifier.Args(
                description=description,
                ignore_words=ignore_words,
                keywords=keywords,
                maximum_match_distance=maximum_match_distance,
                name=name,
                name_prefix=name_prefix,
                regex=regex,
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

        ignore_words: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        keywords: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        maximum_match_distance: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        regex: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
