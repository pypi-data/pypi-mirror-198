import terrascript.core as core


@core.schema
class GrokClassifier(core.Schema):

    classification: str | core.StringOut = core.attr(str)

    custom_patterns: str | core.StringOut | None = core.attr(str, default=None)

    grok_pattern: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        classification: str | core.StringOut,
        grok_pattern: str | core.StringOut,
        custom_patterns: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=GrokClassifier.Args(
                classification=classification,
                grok_pattern=grok_pattern,
                custom_patterns=custom_patterns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classification: str | core.StringOut = core.arg()

        custom_patterns: str | core.StringOut | None = core.arg(default=None)

        grok_pattern: str | core.StringOut = core.arg()


@core.schema
class JsonClassifier(core.Schema):

    json_path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        json_path: str | core.StringOut,
    ):
        super().__init__(
            args=JsonClassifier.Args(
                json_path=json_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        json_path: str | core.StringOut = core.arg()


@core.schema
class XmlClassifier(core.Schema):

    classification: str | core.StringOut = core.attr(str)

    row_tag: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        classification: str | core.StringOut,
        row_tag: str | core.StringOut,
    ):
        super().__init__(
            args=XmlClassifier.Args(
                classification=classification,
                row_tag=row_tag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classification: str | core.StringOut = core.arg()

        row_tag: str | core.StringOut = core.arg()


@core.schema
class CsvClassifier(core.Schema):

    allow_single_column: bool | core.BoolOut | None = core.attr(bool, default=None)

    contains_header: str | core.StringOut | None = core.attr(str, default=None)

    delimiter: str | core.StringOut | None = core.attr(str, default=None)

    disable_value_trimming: bool | core.BoolOut | None = core.attr(bool, default=None)

    header: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    quote_symbol: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        allow_single_column: bool | core.BoolOut | None = None,
        contains_header: str | core.StringOut | None = None,
        delimiter: str | core.StringOut | None = None,
        disable_value_trimming: bool | core.BoolOut | None = None,
        header: list[str] | core.ArrayOut[core.StringOut] | None = None,
        quote_symbol: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CsvClassifier.Args(
                allow_single_column=allow_single_column,
                contains_header=contains_header,
                delimiter=delimiter,
                disable_value_trimming=disable_value_trimming,
                header=header,
                quote_symbol=quote_symbol,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_single_column: bool | core.BoolOut | None = core.arg(default=None)

        contains_header: str | core.StringOut | None = core.arg(default=None)

        delimiter: str | core.StringOut | None = core.arg(default=None)

        disable_value_trimming: bool | core.BoolOut | None = core.arg(default=None)

        header: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        quote_symbol: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_glue_classifier", namespace="glue")
class Classifier(core.Resource):
    """
    (Optional) A classifier for Csv content. Defined below.
    """

    csv_classifier: CsvClassifier | None = core.attr(CsvClassifier, default=None)

    grok_classifier: GrokClassifier | None = core.attr(GrokClassifier, default=None)

    """
    Name of the classifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    json_classifier: JsonClassifier | None = core.attr(JsonClassifier, default=None)

    name: str | core.StringOut = core.attr(str)

    xml_classifier: XmlClassifier | None = core.attr(XmlClassifier, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        csv_classifier: CsvClassifier | None = None,
        grok_classifier: GrokClassifier | None = None,
        json_classifier: JsonClassifier | None = None,
        xml_classifier: XmlClassifier | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Classifier.Args(
                name=name,
                csv_classifier=csv_classifier,
                grok_classifier=grok_classifier,
                json_classifier=json_classifier,
                xml_classifier=xml_classifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        csv_classifier: CsvClassifier | None = core.arg(default=None)

        grok_classifier: GrokClassifier | None = core.arg(default=None)

        json_classifier: JsonClassifier | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        xml_classifier: XmlClassifier | None = core.arg(default=None)
