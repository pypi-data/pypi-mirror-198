import terrascript.core as core


@core.schema
class VisibilityConfig(core.Schema):

    cloudwatch_metrics_enabled: bool | core.BoolOut = core.attr(bool)

    metric_name: str | core.StringOut = core.attr(str)

    sampled_requests_enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        cloudwatch_metrics_enabled: bool | core.BoolOut,
        metric_name: str | core.StringOut,
        sampled_requests_enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=VisibilityConfig.Args(
                cloudwatch_metrics_enabled=cloudwatch_metrics_enabled,
                metric_name=metric_name,
                sampled_requests_enabled=sampled_requests_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_metrics_enabled: bool | core.BoolOut = core.arg()

        metric_name: str | core.StringOut = core.arg()

        sampled_requests_enabled: bool | core.BoolOut = core.arg()


@core.schema
class ForwardedIpConfig(core.Schema):

    fallback_behavior: str | core.StringOut = core.attr(str)

    header_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        fallback_behavior: str | core.StringOut,
        header_name: str | core.StringOut,
    ):
        super().__init__(
            args=ForwardedIpConfig.Args(
                fallback_behavior=fallback_behavior,
                header_name=header_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        fallback_behavior: str | core.StringOut = core.arg()

        header_name: str | core.StringOut = core.arg()


@core.schema
class GeoMatchStatement(core.Schema):

    country_codes: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    forwarded_ip_config: ForwardedIpConfig | None = core.attr(ForwardedIpConfig, default=None)

    def __init__(
        self,
        *,
        country_codes: list[str] | core.ArrayOut[core.StringOut],
        forwarded_ip_config: ForwardedIpConfig | None = None,
    ):
        super().__init__(
            args=GeoMatchStatement.Args(
                country_codes=country_codes,
                forwarded_ip_config=forwarded_ip_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        country_codes: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        forwarded_ip_config: ForwardedIpConfig | None = core.arg(default=None)


@core.schema
class LabelMatchStatement(core.Schema):

    key: str | core.StringOut = core.attr(str)

    scope: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        scope: str | core.StringOut,
    ):
        super().__init__(
            args=LabelMatchStatement.Args(
                key=key,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        scope: str | core.StringOut = core.arg()


@core.schema
class Method(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class QueryString(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class SingleHeader(core.Schema):

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=SingleHeader.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class SingleQueryArgument(core.Schema):

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=SingleQueryArgument.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class UriPath(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class AllQueryArguments(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class Body(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class FieldToMatch(core.Schema):

    all_query_arguments: AllQueryArguments | None = core.attr(AllQueryArguments, default=None)

    body: Body | None = core.attr(Body, default=None)

    method: Method | None = core.attr(Method, default=None)

    query_string: QueryString | None = core.attr(QueryString, default=None)

    single_header: SingleHeader | None = core.attr(SingleHeader, default=None)

    single_query_argument: SingleQueryArgument | None = core.attr(SingleQueryArgument, default=None)

    uri_path: UriPath | None = core.attr(UriPath, default=None)

    def __init__(
        self,
        *,
        all_query_arguments: AllQueryArguments | None = None,
        body: Body | None = None,
        method: Method | None = None,
        query_string: QueryString | None = None,
        single_header: SingleHeader | None = None,
        single_query_argument: SingleQueryArgument | None = None,
        uri_path: UriPath | None = None,
    ):
        super().__init__(
            args=FieldToMatch.Args(
                all_query_arguments=all_query_arguments,
                body=body,
                method=method,
                query_string=query_string,
                single_header=single_header,
                single_query_argument=single_query_argument,
                uri_path=uri_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_query_arguments: AllQueryArguments | None = core.arg(default=None)

        body: Body | None = core.arg(default=None)

        method: Method | None = core.arg(default=None)

        query_string: QueryString | None = core.arg(default=None)

        single_header: SingleHeader | None = core.arg(default=None)

        single_query_argument: SingleQueryArgument | None = core.arg(default=None)

        uri_path: UriPath | None = core.arg(default=None)


@core.schema
class TextTransformation(core.Schema):

    priority: int | core.IntOut = core.attr(int)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        priority: int | core.IntOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=TextTransformation.Args(
                priority=priority,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class SizeConstraintStatement(core.Schema):

    comparison_operator: str | core.StringOut = core.attr(str)

    field_to_match: FieldToMatch | None = core.attr(FieldToMatch, default=None)

    size: int | core.IntOut = core.attr(int)

    text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation] = core.attr(
        TextTransformation, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        comparison_operator: str | core.StringOut,
        size: int | core.IntOut,
        text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation],
        field_to_match: FieldToMatch | None = None,
    ):
        super().__init__(
            args=SizeConstraintStatement.Args(
                comparison_operator=comparison_operator,
                size=size,
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison_operator: str | core.StringOut = core.arg()

        field_to_match: FieldToMatch | None = core.arg(default=None)

        size: int | core.IntOut = core.arg()

        text_transformation: list[TextTransformation] | core.ArrayOut[
            TextTransformation
        ] = core.arg()


@core.schema
class IpSetForwardedIpConfig(core.Schema):

    fallback_behavior: str | core.StringOut = core.attr(str)

    header_name: str | core.StringOut = core.attr(str)

    position: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        fallback_behavior: str | core.StringOut,
        header_name: str | core.StringOut,
        position: str | core.StringOut,
    ):
        super().__init__(
            args=IpSetForwardedIpConfig.Args(
                fallback_behavior=fallback_behavior,
                header_name=header_name,
                position=position,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        fallback_behavior: str | core.StringOut = core.arg()

        header_name: str | core.StringOut = core.arg()

        position: str | core.StringOut = core.arg()


@core.schema
class IpSetReferenceStatement(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    ip_set_forwarded_ip_config: IpSetForwardedIpConfig | None = core.attr(
        IpSetForwardedIpConfig, default=None
    )

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        ip_set_forwarded_ip_config: IpSetForwardedIpConfig | None = None,
    ):
        super().__init__(
            args=IpSetReferenceStatement.Args(
                arn=arn,
                ip_set_forwarded_ip_config=ip_set_forwarded_ip_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        ip_set_forwarded_ip_config: IpSetForwardedIpConfig | None = core.arg(default=None)


@core.schema
class XssMatchStatement(core.Schema):

    field_to_match: FieldToMatch | None = core.attr(FieldToMatch, default=None)

    text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation] = core.attr(
        TextTransformation, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation],
        field_to_match: FieldToMatch | None = None,
    ):
        super().__init__(
            args=XssMatchStatement.Args(
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch | None = core.arg(default=None)

        text_transformation: list[TextTransformation] | core.ArrayOut[
            TextTransformation
        ] = core.arg()


@core.schema
class RegexPatternSetReferenceStatement(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    field_to_match: FieldToMatch | None = core.attr(FieldToMatch, default=None)

    text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation] = core.attr(
        TextTransformation, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation],
        field_to_match: FieldToMatch | None = None,
    ):
        super().__init__(
            args=RegexPatternSetReferenceStatement.Args(
                arn=arn,
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        field_to_match: FieldToMatch | None = core.arg(default=None)

        text_transformation: list[TextTransformation] | core.ArrayOut[
            TextTransformation
        ] = core.arg()


@core.schema
class SqliMatchStatement(core.Schema):

    field_to_match: FieldToMatch | None = core.attr(FieldToMatch, default=None)

    text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation] = core.attr(
        TextTransformation, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation],
        field_to_match: FieldToMatch | None = None,
    ):
        super().__init__(
            args=SqliMatchStatement.Args(
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch | None = core.arg(default=None)

        text_transformation: list[TextTransformation] | core.ArrayOut[
            TextTransformation
        ] = core.arg()


@core.schema
class ByteMatchStatement(core.Schema):

    field_to_match: FieldToMatch | None = core.attr(FieldToMatch, default=None)

    positional_constraint: str | core.StringOut = core.attr(str)

    search_string: str | core.StringOut = core.attr(str)

    text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation] = core.attr(
        TextTransformation, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        positional_constraint: str | core.StringOut,
        search_string: str | core.StringOut,
        text_transformation: list[TextTransformation] | core.ArrayOut[TextTransformation],
        field_to_match: FieldToMatch | None = None,
    ):
        super().__init__(
            args=ByteMatchStatement.Args(
                positional_constraint=positional_constraint,
                search_string=search_string,
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch | None = core.arg(default=None)

        positional_constraint: str | core.StringOut = core.arg()

        search_string: str | core.StringOut = core.arg()

        text_transformation: list[TextTransformation] | core.ArrayOut[
            TextTransformation
        ] = core.arg()


@core.schema
class RuleStatementOrStatementStatementNotStatementStatement(core.Schema):

    byte_match_statement: ByteMatchStatement | None = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: GeoMatchStatement | None = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: IpSetReferenceStatement | None = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: LabelMatchStatement | None = core.attr(LabelMatchStatement, default=None)

    regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.attr(
        RegexPatternSetReferenceStatement, default=None
    )

    size_constraint_statement: SizeConstraintStatement | None = core.attr(
        SizeConstraintStatement, default=None
    )

    sqli_match_statement: SqliMatchStatement | None = core.attr(SqliMatchStatement, default=None)

    xss_match_statement: XssMatchStatement | None = core.attr(XssMatchStatement, default=None)

    def __init__(
        self,
        *,
        byte_match_statement: ByteMatchStatement | None = None,
        geo_match_statement: GeoMatchStatement | None = None,
        ip_set_reference_statement: IpSetReferenceStatement | None = None,
        label_match_statement: LabelMatchStatement | None = None,
        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = None,
        size_constraint_statement: SizeConstraintStatement | None = None,
        sqli_match_statement: SqliMatchStatement | None = None,
        xss_match_statement: XssMatchStatement | None = None,
    ):
        super().__init__(
            args=RuleStatementOrStatementStatementNotStatementStatement.Args(
                byte_match_statement=byte_match_statement,
                geo_match_statement=geo_match_statement,
                ip_set_reference_statement=ip_set_reference_statement,
                label_match_statement=label_match_statement,
                regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
                size_constraint_statement=size_constraint_statement,
                sqli_match_statement=sqli_match_statement,
                xss_match_statement=xss_match_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        byte_match_statement: ByteMatchStatement | None = core.arg(default=None)

        geo_match_statement: GeoMatchStatement | None = core.arg(default=None)

        ip_set_reference_statement: IpSetReferenceStatement | None = core.arg(default=None)

        label_match_statement: LabelMatchStatement | None = core.arg(default=None)

        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.arg(
            default=None
        )

        size_constraint_statement: SizeConstraintStatement | None = core.arg(default=None)

        sqli_match_statement: SqliMatchStatement | None = core.arg(default=None)

        xss_match_statement: XssMatchStatement | None = core.arg(default=None)


@core.schema
class RuleStatementOrStatementStatementNotStatement(core.Schema):

    statement: list[RuleStatementOrStatementStatementNotStatementStatement] | core.ArrayOut[
        RuleStatementOrStatementStatementNotStatementStatement
    ] = core.attr(RuleStatementOrStatementStatementNotStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[RuleStatementOrStatementStatementNotStatementStatement]
        | core.ArrayOut[RuleStatementOrStatementStatementNotStatementStatement],
    ):
        super().__init__(
            args=RuleStatementOrStatementStatementNotStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[RuleStatementOrStatementStatementNotStatementStatement] | core.ArrayOut[
            RuleStatementOrStatementStatementNotStatementStatement
        ] = core.arg()


@core.schema
class RuleStatementOrStatementStatementOrStatement(core.Schema):

    statement: list[RuleStatementOrStatementStatementNotStatementStatement] | core.ArrayOut[
        RuleStatementOrStatementStatementNotStatementStatement
    ] = core.attr(RuleStatementOrStatementStatementNotStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[RuleStatementOrStatementStatementNotStatementStatement]
        | core.ArrayOut[RuleStatementOrStatementStatementNotStatementStatement],
    ):
        super().__init__(
            args=RuleStatementOrStatementStatementOrStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[RuleStatementOrStatementStatementNotStatementStatement] | core.ArrayOut[
            RuleStatementOrStatementStatementNotStatementStatement
        ] = core.arg()


@core.schema
class RuleStatementOrStatementStatementAndStatement(core.Schema):

    statement: list[RuleStatementOrStatementStatementNotStatementStatement] | core.ArrayOut[
        RuleStatementOrStatementStatementNotStatementStatement
    ] = core.attr(RuleStatementOrStatementStatementNotStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[RuleStatementOrStatementStatementNotStatementStatement]
        | core.ArrayOut[RuleStatementOrStatementStatementNotStatementStatement],
    ):
        super().__init__(
            args=RuleStatementOrStatementStatementAndStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[RuleStatementOrStatementStatementNotStatementStatement] | core.ArrayOut[
            RuleStatementOrStatementStatementNotStatementStatement
        ] = core.arg()


@core.schema
class RuleStatementOrStatementStatement(core.Schema):

    and_statement: RuleStatementOrStatementStatementAndStatement | None = core.attr(
        RuleStatementOrStatementStatementAndStatement, default=None
    )

    byte_match_statement: ByteMatchStatement | None = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: GeoMatchStatement | None = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: IpSetReferenceStatement | None = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: LabelMatchStatement | None = core.attr(LabelMatchStatement, default=None)

    not_statement: RuleStatementOrStatementStatementNotStatement | None = core.attr(
        RuleStatementOrStatementStatementNotStatement, default=None
    )

    or_statement: RuleStatementOrStatementStatementOrStatement | None = core.attr(
        RuleStatementOrStatementStatementOrStatement, default=None
    )

    regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.attr(
        RegexPatternSetReferenceStatement, default=None
    )

    size_constraint_statement: SizeConstraintStatement | None = core.attr(
        SizeConstraintStatement, default=None
    )

    sqli_match_statement: SqliMatchStatement | None = core.attr(SqliMatchStatement, default=None)

    xss_match_statement: XssMatchStatement | None = core.attr(XssMatchStatement, default=None)

    def __init__(
        self,
        *,
        and_statement: RuleStatementOrStatementStatementAndStatement | None = None,
        byte_match_statement: ByteMatchStatement | None = None,
        geo_match_statement: GeoMatchStatement | None = None,
        ip_set_reference_statement: IpSetReferenceStatement | None = None,
        label_match_statement: LabelMatchStatement | None = None,
        not_statement: RuleStatementOrStatementStatementNotStatement | None = None,
        or_statement: RuleStatementOrStatementStatementOrStatement | None = None,
        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = None,
        size_constraint_statement: SizeConstraintStatement | None = None,
        sqli_match_statement: SqliMatchStatement | None = None,
        xss_match_statement: XssMatchStatement | None = None,
    ):
        super().__init__(
            args=RuleStatementOrStatementStatement.Args(
                and_statement=and_statement,
                byte_match_statement=byte_match_statement,
                geo_match_statement=geo_match_statement,
                ip_set_reference_statement=ip_set_reference_statement,
                label_match_statement=label_match_statement,
                not_statement=not_statement,
                or_statement=or_statement,
                regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
                size_constraint_statement=size_constraint_statement,
                sqli_match_statement=sqli_match_statement,
                xss_match_statement=xss_match_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_statement: RuleStatementOrStatementStatementAndStatement | None = core.arg(default=None)

        byte_match_statement: ByteMatchStatement | None = core.arg(default=None)

        geo_match_statement: GeoMatchStatement | None = core.arg(default=None)

        ip_set_reference_statement: IpSetReferenceStatement | None = core.arg(default=None)

        label_match_statement: LabelMatchStatement | None = core.arg(default=None)

        not_statement: RuleStatementOrStatementStatementNotStatement | None = core.arg(default=None)

        or_statement: RuleStatementOrStatementStatementOrStatement | None = core.arg(default=None)

        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.arg(
            default=None
        )

        size_constraint_statement: SizeConstraintStatement | None = core.arg(default=None)

        sqli_match_statement: SqliMatchStatement | None = core.arg(default=None)

        xss_match_statement: XssMatchStatement | None = core.arg(default=None)


@core.schema
class RuleStatementOrStatement(core.Schema):

    statement: list[RuleStatementOrStatementStatement] | core.ArrayOut[
        RuleStatementOrStatementStatement
    ] = core.attr(RuleStatementOrStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[RuleStatementOrStatementStatement]
        | core.ArrayOut[RuleStatementOrStatementStatement],
    ):
        super().__init__(
            args=RuleStatementOrStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[RuleStatementOrStatementStatement] | core.ArrayOut[
            RuleStatementOrStatementStatement
        ] = core.arg()


@core.schema
class RuleStatementAndStatement(core.Schema):

    statement: list[RuleStatementOrStatementStatement] | core.ArrayOut[
        RuleStatementOrStatementStatement
    ] = core.attr(RuleStatementOrStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[RuleStatementOrStatementStatement]
        | core.ArrayOut[RuleStatementOrStatementStatement],
    ):
        super().__init__(
            args=RuleStatementAndStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[RuleStatementOrStatementStatement] | core.ArrayOut[
            RuleStatementOrStatementStatement
        ] = core.arg()


@core.schema
class RuleStatementNotStatement(core.Schema):

    statement: list[RuleStatementOrStatementStatement] | core.ArrayOut[
        RuleStatementOrStatementStatement
    ] = core.attr(RuleStatementOrStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[RuleStatementOrStatementStatement]
        | core.ArrayOut[RuleStatementOrStatementStatement],
    ):
        super().__init__(
            args=RuleStatementNotStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[RuleStatementOrStatementStatement] | core.ArrayOut[
            RuleStatementOrStatementStatement
        ] = core.arg()


@core.schema
class RuleStatement(core.Schema):

    and_statement: RuleStatementAndStatement | None = core.attr(
        RuleStatementAndStatement, default=None
    )

    byte_match_statement: ByteMatchStatement | None = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: GeoMatchStatement | None = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: IpSetReferenceStatement | None = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: LabelMatchStatement | None = core.attr(LabelMatchStatement, default=None)

    not_statement: RuleStatementNotStatement | None = core.attr(
        RuleStatementNotStatement, default=None
    )

    or_statement: RuleStatementOrStatement | None = core.attr(
        RuleStatementOrStatement, default=None
    )

    regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.attr(
        RegexPatternSetReferenceStatement, default=None
    )

    size_constraint_statement: SizeConstraintStatement | None = core.attr(
        SizeConstraintStatement, default=None
    )

    sqli_match_statement: SqliMatchStatement | None = core.attr(SqliMatchStatement, default=None)

    xss_match_statement: XssMatchStatement | None = core.attr(XssMatchStatement, default=None)

    def __init__(
        self,
        *,
        and_statement: RuleStatementAndStatement | None = None,
        byte_match_statement: ByteMatchStatement | None = None,
        geo_match_statement: GeoMatchStatement | None = None,
        ip_set_reference_statement: IpSetReferenceStatement | None = None,
        label_match_statement: LabelMatchStatement | None = None,
        not_statement: RuleStatementNotStatement | None = None,
        or_statement: RuleStatementOrStatement | None = None,
        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = None,
        size_constraint_statement: SizeConstraintStatement | None = None,
        sqli_match_statement: SqliMatchStatement | None = None,
        xss_match_statement: XssMatchStatement | None = None,
    ):
        super().__init__(
            args=RuleStatement.Args(
                and_statement=and_statement,
                byte_match_statement=byte_match_statement,
                geo_match_statement=geo_match_statement,
                ip_set_reference_statement=ip_set_reference_statement,
                label_match_statement=label_match_statement,
                not_statement=not_statement,
                or_statement=or_statement,
                regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
                size_constraint_statement=size_constraint_statement,
                sqli_match_statement=sqli_match_statement,
                xss_match_statement=xss_match_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_statement: RuleStatementAndStatement | None = core.arg(default=None)

        byte_match_statement: ByteMatchStatement | None = core.arg(default=None)

        geo_match_statement: GeoMatchStatement | None = core.arg(default=None)

        ip_set_reference_statement: IpSetReferenceStatement | None = core.arg(default=None)

        label_match_statement: LabelMatchStatement | None = core.arg(default=None)

        not_statement: RuleStatementNotStatement | None = core.arg(default=None)

        or_statement: RuleStatementOrStatement | None = core.arg(default=None)

        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.arg(
            default=None
        )

        size_constraint_statement: SizeConstraintStatement | None = core.arg(default=None)

        sqli_match_statement: SqliMatchStatement | None = core.arg(default=None)

        xss_match_statement: XssMatchStatement | None = core.arg(default=None)


@core.schema
class InsertHeader(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=InsertHeader.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class CustomRequestHandling(core.Schema):

    insert_header: list[InsertHeader] | core.ArrayOut[InsertHeader] = core.attr(
        InsertHeader, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        insert_header: list[InsertHeader] | core.ArrayOut[InsertHeader],
    ):
        super().__init__(
            args=CustomRequestHandling.Args(
                insert_header=insert_header,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insert_header: list[InsertHeader] | core.ArrayOut[InsertHeader] = core.arg()


@core.schema
class Allow(core.Schema):

    custom_request_handling: CustomRequestHandling | None = core.attr(
        CustomRequestHandling, default=None
    )

    def __init__(
        self,
        *,
        custom_request_handling: CustomRequestHandling | None = None,
    ):
        super().__init__(
            args=Allow.Args(
                custom_request_handling=custom_request_handling,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_request_handling: CustomRequestHandling | None = core.arg(default=None)


@core.schema
class ResponseHeader(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResponseHeader.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class CustomResponse(core.Schema):

    custom_response_body_key: str | core.StringOut | None = core.attr(str, default=None)

    response_code: int | core.IntOut = core.attr(int)

    response_header: list[ResponseHeader] | core.ArrayOut[ResponseHeader] | None = core.attr(
        ResponseHeader, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        response_code: int | core.IntOut,
        custom_response_body_key: str | core.StringOut | None = None,
        response_header: list[ResponseHeader] | core.ArrayOut[ResponseHeader] | None = None,
    ):
        super().__init__(
            args=CustomResponse.Args(
                response_code=response_code,
                custom_response_body_key=custom_response_body_key,
                response_header=response_header,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_response_body_key: str | core.StringOut | None = core.arg(default=None)

        response_code: int | core.IntOut = core.arg()

        response_header: list[ResponseHeader] | core.ArrayOut[ResponseHeader] | None = core.arg(
            default=None
        )


@core.schema
class Block(core.Schema):

    custom_response: CustomResponse | None = core.attr(CustomResponse, default=None)

    def __init__(
        self,
        *,
        custom_response: CustomResponse | None = None,
    ):
        super().__init__(
            args=Block.Args(
                custom_response=custom_response,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_response: CustomResponse | None = core.arg(default=None)


@core.schema
class Count(core.Schema):

    custom_request_handling: CustomRequestHandling | None = core.attr(
        CustomRequestHandling, default=None
    )

    def __init__(
        self,
        *,
        custom_request_handling: CustomRequestHandling | None = None,
    ):
        super().__init__(
            args=Count.Args(
                custom_request_handling=custom_request_handling,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_request_handling: CustomRequestHandling | None = core.arg(default=None)


@core.schema
class Action(core.Schema):

    allow: Allow | None = core.attr(Allow, default=None)

    block: Block | None = core.attr(Block, default=None)

    count: Count | None = core.attr(Count, default=None)

    def __init__(
        self,
        *,
        allow: Allow | None = None,
        block: Block | None = None,
        count: Count | None = None,
    ):
        super().__init__(
            args=Action.Args(
                allow=allow,
                block=block,
                count=count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow: Allow | None = core.arg(default=None)

        block: Block | None = core.arg(default=None)

        count: Count | None = core.arg(default=None)


@core.schema
class RuleLabel(core.Schema):

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=RuleLabel.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class Rule(core.Schema):

    action: Action = core.attr(Action)

    name: str | core.StringOut = core.attr(str)

    priority: int | core.IntOut = core.attr(int)

    rule_label: list[RuleLabel] | core.ArrayOut[RuleLabel] | None = core.attr(
        RuleLabel, default=None, kind=core.Kind.array
    )

    statement: RuleStatement = core.attr(RuleStatement)

    visibility_config: VisibilityConfig = core.attr(VisibilityConfig)

    def __init__(
        self,
        *,
        action: Action,
        name: str | core.StringOut,
        priority: int | core.IntOut,
        statement: RuleStatement,
        visibility_config: VisibilityConfig,
        rule_label: list[RuleLabel] | core.ArrayOut[RuleLabel] | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                action=action,
                name=name,
                priority=priority,
                statement=statement,
                visibility_config=visibility_config,
                rule_label=rule_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        name: str | core.StringOut = core.arg()

        priority: int | core.IntOut = core.arg()

        rule_label: list[RuleLabel] | core.ArrayOut[RuleLabel] | None = core.arg(default=None)

        statement: RuleStatement = core.arg()

        visibility_config: VisibilityConfig = core.arg()


@core.schema
class CustomResponseBody(core.Schema):

    content: str | core.StringOut = core.attr(str)

    content_type: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        content: str | core.StringOut,
        content_type: str | core.StringOut,
        key: str | core.StringOut,
    ):
        super().__init__(
            args=CustomResponseBody.Args(
                content=content,
                content_type=content_type,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: str | core.StringOut = core.arg()

        content_type: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()


@core.resource(type="aws_wafv2_rule_group", namespace="waf")
class V2RuleGroup(core.Resource):
    """
    (Required) The Amazon Resource Name (ARN) of the IP Set that this statement references.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The web ACL capacity units (WCUs) required for this rule group. See
    [here](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateRuleGroup.html#API_CreateRuleGr
    oup_RequestSyntax) for general information and [here](https://docs.aws.amazon.com/waf/latest/develop
    erguide/waf-rule-statements-list.html) for capacity specific information.
    """
    capacity: int | core.IntOut = core.attr(int)

    """
    (Optional) Defines custom response bodies that can be referenced by `custom_response` actions. See [
    Custom Response Body](#custom-response-body) below for details.
    """
    custom_response_body: list[CustomResponseBody] | core.ArrayOut[
        CustomResponseBody
    ] | None = core.attr(CustomResponseBody, default=None, kind=core.Kind.array)

    """
    (Optional) A friendly description of the rule group.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the WAF rule group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    lock_token: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) A friendly name of the rule group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The rule blocks used to identify the web requests that you want to `allow`, `block`, or `
    count`. See [Rules](#rules) below for details.
    """
    rule: list[Rule] | core.ArrayOut[Rule] | None = core.attr(
        Rule, default=None, kind=core.Kind.array
    )

    """
    (Required, Forces new resource) Specifies whether this is for an AWS CloudFront distribution or for
    a regional application. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you mu
    st also specify the region `us-east-1` (N. Virginia) on the AWS provider.
    """
    scope: str | core.StringOut = core.attr(str)

    """
    (Optional) An array of key:value pairs to associate with the resource. If configured with a provider
    [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/d
    ocs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined
    at the provider-level.
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
    (Required) Defines and enables Amazon CloudWatch metrics and web request sample collection. See [Vis
    ibility Configuration](#visibility-configuration) below for details.
    """
    visibility_config: VisibilityConfig = core.attr(VisibilityConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        capacity: int | core.IntOut,
        name: str | core.StringOut,
        scope: str | core.StringOut,
        visibility_config: VisibilityConfig,
        custom_response_body: list[CustomResponseBody]
        | core.ArrayOut[CustomResponseBody]
        | None = None,
        description: str | core.StringOut | None = None,
        rule: list[Rule] | core.ArrayOut[Rule] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2RuleGroup.Args(
                capacity=capacity,
                name=name,
                scope=scope,
                visibility_config=visibility_config,
                custom_response_body=custom_response_body,
                description=description,
                rule=rule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity: int | core.IntOut = core.arg()

        custom_response_body: list[CustomResponseBody] | core.ArrayOut[
            CustomResponseBody
        ] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rule: list[Rule] | core.ArrayOut[Rule] | None = core.arg(default=None)

        scope: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        visibility_config: VisibilityConfig = core.arg()
