import terrascript.core as core


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


@core.schema
class Body(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


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
class ExcludedRule(core.Schema):

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=ExcludedRule.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class RuleGroupReferenceStatement(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    excluded_rule: list[ExcludedRule] | core.ArrayOut[ExcludedRule] | None = core.attr(
        ExcludedRule, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        excluded_rule: list[ExcludedRule] | core.ArrayOut[ExcludedRule] | None = None,
    ):
        super().__init__(
            args=RuleGroupReferenceStatement.Args(
                arn=arn,
                excluded_rule=excluded_rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        excluded_rule: list[ExcludedRule] | core.ArrayOut[ExcludedRule] | None = core.arg(
            default=None
        )


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
class ScopeDownStatementAndStatementStatementNotStatementStatement(core.Schema):

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
            args=ScopeDownStatementAndStatementStatementNotStatementStatement.Args(
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
class ScopeDownStatementAndStatementStatementNotStatement(core.Schema):

    statement: list[ScopeDownStatementAndStatementStatementNotStatementStatement] | core.ArrayOut[
        ScopeDownStatementAndStatementStatementNotStatementStatement
    ] = core.attr(
        ScopeDownStatementAndStatementStatementNotStatementStatement, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        statement: list[ScopeDownStatementAndStatementStatementNotStatementStatement]
        | core.ArrayOut[ScopeDownStatementAndStatementStatementNotStatementStatement],
    ):
        super().__init__(
            args=ScopeDownStatementAndStatementStatementNotStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[
            ScopeDownStatementAndStatementStatementNotStatementStatement
        ] | core.ArrayOut[ScopeDownStatementAndStatementStatementNotStatementStatement] = core.arg()


@core.schema
class ScopeDownStatementAndStatementStatementAndStatement(core.Schema):

    statement: list[ScopeDownStatementAndStatementStatementNotStatementStatement] | core.ArrayOut[
        ScopeDownStatementAndStatementStatementNotStatementStatement
    ] = core.attr(
        ScopeDownStatementAndStatementStatementNotStatementStatement, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        statement: list[ScopeDownStatementAndStatementStatementNotStatementStatement]
        | core.ArrayOut[ScopeDownStatementAndStatementStatementNotStatementStatement],
    ):
        super().__init__(
            args=ScopeDownStatementAndStatementStatementAndStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[
            ScopeDownStatementAndStatementStatementNotStatementStatement
        ] | core.ArrayOut[ScopeDownStatementAndStatementStatementNotStatementStatement] = core.arg()


@core.schema
class ScopeDownStatementAndStatementStatementOrStatement(core.Schema):

    statement: list[ScopeDownStatementAndStatementStatementNotStatementStatement] | core.ArrayOut[
        ScopeDownStatementAndStatementStatementNotStatementStatement
    ] = core.attr(
        ScopeDownStatementAndStatementStatementNotStatementStatement, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        statement: list[ScopeDownStatementAndStatementStatementNotStatementStatement]
        | core.ArrayOut[ScopeDownStatementAndStatementStatementNotStatementStatement],
    ):
        super().__init__(
            args=ScopeDownStatementAndStatementStatementOrStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[
            ScopeDownStatementAndStatementStatementNotStatementStatement
        ] | core.ArrayOut[ScopeDownStatementAndStatementStatementNotStatementStatement] = core.arg()


@core.schema
class ScopeDownStatementAndStatementStatement(core.Schema):

    and_statement: ScopeDownStatementAndStatementStatementAndStatement | None = core.attr(
        ScopeDownStatementAndStatementStatementAndStatement, default=None
    )

    byte_match_statement: ByteMatchStatement | None = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: GeoMatchStatement | None = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: IpSetReferenceStatement | None = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: LabelMatchStatement | None = core.attr(LabelMatchStatement, default=None)

    not_statement: ScopeDownStatementAndStatementStatementNotStatement | None = core.attr(
        ScopeDownStatementAndStatementStatementNotStatement, default=None
    )

    or_statement: ScopeDownStatementAndStatementStatementOrStatement | None = core.attr(
        ScopeDownStatementAndStatementStatementOrStatement, default=None
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
        and_statement: ScopeDownStatementAndStatementStatementAndStatement | None = None,
        byte_match_statement: ByteMatchStatement | None = None,
        geo_match_statement: GeoMatchStatement | None = None,
        ip_set_reference_statement: IpSetReferenceStatement | None = None,
        label_match_statement: LabelMatchStatement | None = None,
        not_statement: ScopeDownStatementAndStatementStatementNotStatement | None = None,
        or_statement: ScopeDownStatementAndStatementStatementOrStatement | None = None,
        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = None,
        size_constraint_statement: SizeConstraintStatement | None = None,
        sqli_match_statement: SqliMatchStatement | None = None,
        xss_match_statement: XssMatchStatement | None = None,
    ):
        super().__init__(
            args=ScopeDownStatementAndStatementStatement.Args(
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
        and_statement: ScopeDownStatementAndStatementStatementAndStatement | None = core.arg(
            default=None
        )

        byte_match_statement: ByteMatchStatement | None = core.arg(default=None)

        geo_match_statement: GeoMatchStatement | None = core.arg(default=None)

        ip_set_reference_statement: IpSetReferenceStatement | None = core.arg(default=None)

        label_match_statement: LabelMatchStatement | None = core.arg(default=None)

        not_statement: ScopeDownStatementAndStatementStatementNotStatement | None = core.arg(
            default=None
        )

        or_statement: ScopeDownStatementAndStatementStatementOrStatement | None = core.arg(
            default=None
        )

        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.arg(
            default=None
        )

        size_constraint_statement: SizeConstraintStatement | None = core.arg(default=None)

        sqli_match_statement: SqliMatchStatement | None = core.arg(default=None)

        xss_match_statement: XssMatchStatement | None = core.arg(default=None)


@core.schema
class ScopeDownStatementAndStatement(core.Schema):

    statement: list[ScopeDownStatementAndStatementStatement] | core.ArrayOut[
        ScopeDownStatementAndStatementStatement
    ] = core.attr(ScopeDownStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[ScopeDownStatementAndStatementStatement]
        | core.ArrayOut[ScopeDownStatementAndStatementStatement],
    ):
        super().__init__(
            args=ScopeDownStatementAndStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[ScopeDownStatementAndStatementStatement] | core.ArrayOut[
            ScopeDownStatementAndStatementStatement
        ] = core.arg()


@core.schema
class ScopeDownStatementNotStatement(core.Schema):

    statement: list[ScopeDownStatementAndStatementStatement] | core.ArrayOut[
        ScopeDownStatementAndStatementStatement
    ] = core.attr(ScopeDownStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[ScopeDownStatementAndStatementStatement]
        | core.ArrayOut[ScopeDownStatementAndStatementStatement],
    ):
        super().__init__(
            args=ScopeDownStatementNotStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[ScopeDownStatementAndStatementStatement] | core.ArrayOut[
            ScopeDownStatementAndStatementStatement
        ] = core.arg()


@core.schema
class ScopeDownStatementOrStatement(core.Schema):

    statement: list[ScopeDownStatementAndStatementStatement] | core.ArrayOut[
        ScopeDownStatementAndStatementStatement
    ] = core.attr(ScopeDownStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: list[ScopeDownStatementAndStatementStatement]
        | core.ArrayOut[ScopeDownStatementAndStatementStatement],
    ):
        super().__init__(
            args=ScopeDownStatementOrStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: list[ScopeDownStatementAndStatementStatement] | core.ArrayOut[
            ScopeDownStatementAndStatementStatement
        ] = core.arg()


@core.schema
class ScopeDownStatement(core.Schema):

    and_statement: ScopeDownStatementAndStatement | None = core.attr(
        ScopeDownStatementAndStatement, default=None
    )

    byte_match_statement: ByteMatchStatement | None = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: GeoMatchStatement | None = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: IpSetReferenceStatement | None = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: LabelMatchStatement | None = core.attr(LabelMatchStatement, default=None)

    not_statement: ScopeDownStatementNotStatement | None = core.attr(
        ScopeDownStatementNotStatement, default=None
    )

    or_statement: ScopeDownStatementOrStatement | None = core.attr(
        ScopeDownStatementOrStatement, default=None
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
        and_statement: ScopeDownStatementAndStatement | None = None,
        byte_match_statement: ByteMatchStatement | None = None,
        geo_match_statement: GeoMatchStatement | None = None,
        ip_set_reference_statement: IpSetReferenceStatement | None = None,
        label_match_statement: LabelMatchStatement | None = None,
        not_statement: ScopeDownStatementNotStatement | None = None,
        or_statement: ScopeDownStatementOrStatement | None = None,
        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = None,
        size_constraint_statement: SizeConstraintStatement | None = None,
        sqli_match_statement: SqliMatchStatement | None = None,
        xss_match_statement: XssMatchStatement | None = None,
    ):
        super().__init__(
            args=ScopeDownStatement.Args(
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
        and_statement: ScopeDownStatementAndStatement | None = core.arg(default=None)

        byte_match_statement: ByteMatchStatement | None = core.arg(default=None)

        geo_match_statement: GeoMatchStatement | None = core.arg(default=None)

        ip_set_reference_statement: IpSetReferenceStatement | None = core.arg(default=None)

        label_match_statement: LabelMatchStatement | None = core.arg(default=None)

        not_statement: ScopeDownStatementNotStatement | None = core.arg(default=None)

        or_statement: ScopeDownStatementOrStatement | None = core.arg(default=None)

        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.arg(
            default=None
        )

        size_constraint_statement: SizeConstraintStatement | None = core.arg(default=None)

        sqli_match_statement: SqliMatchStatement | None = core.arg(default=None)

        xss_match_statement: XssMatchStatement | None = core.arg(default=None)


@core.schema
class RateBasedStatement(core.Schema):

    aggregate_key_type: str | core.StringOut | None = core.attr(str, default=None)

    forwarded_ip_config: ForwardedIpConfig | None = core.attr(ForwardedIpConfig, default=None)

    limit: int | core.IntOut = core.attr(int)

    scope_down_statement: ScopeDownStatement | None = core.attr(ScopeDownStatement, default=None)

    def __init__(
        self,
        *,
        limit: int | core.IntOut,
        aggregate_key_type: str | core.StringOut | None = None,
        forwarded_ip_config: ForwardedIpConfig | None = None,
        scope_down_statement: ScopeDownStatement | None = None,
    ):
        super().__init__(
            args=RateBasedStatement.Args(
                limit=limit,
                aggregate_key_type=aggregate_key_type,
                forwarded_ip_config=forwarded_ip_config,
                scope_down_statement=scope_down_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregate_key_type: str | core.StringOut | None = core.arg(default=None)

        forwarded_ip_config: ForwardedIpConfig | None = core.arg(default=None)

        limit: int | core.IntOut = core.arg()

        scope_down_statement: ScopeDownStatement | None = core.arg(default=None)


@core.schema
class RuleStatementOrStatementStatement(core.Schema):

    and_statement: ScopeDownStatementAndStatement | None = core.attr(
        ScopeDownStatementAndStatement, default=None
    )

    byte_match_statement: ByteMatchStatement | None = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: GeoMatchStatement | None = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: IpSetReferenceStatement | None = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: LabelMatchStatement | None = core.attr(LabelMatchStatement, default=None)

    not_statement: ScopeDownStatementNotStatement | None = core.attr(
        ScopeDownStatementNotStatement, default=None
    )

    or_statement: ScopeDownStatementOrStatement | None = core.attr(
        ScopeDownStatementOrStatement, default=None
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
        and_statement: ScopeDownStatementAndStatement | None = None,
        byte_match_statement: ByteMatchStatement | None = None,
        geo_match_statement: GeoMatchStatement | None = None,
        ip_set_reference_statement: IpSetReferenceStatement | None = None,
        label_match_statement: LabelMatchStatement | None = None,
        not_statement: ScopeDownStatementNotStatement | None = None,
        or_statement: ScopeDownStatementOrStatement | None = None,
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
        and_statement: ScopeDownStatementAndStatement | None = core.arg(default=None)

        byte_match_statement: ByteMatchStatement | None = core.arg(default=None)

        geo_match_statement: GeoMatchStatement | None = core.arg(default=None)

        ip_set_reference_statement: IpSetReferenceStatement | None = core.arg(default=None)

        label_match_statement: LabelMatchStatement | None = core.arg(default=None)

        not_statement: ScopeDownStatementNotStatement | None = core.arg(default=None)

        or_statement: ScopeDownStatementOrStatement | None = core.arg(default=None)

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
class ManagedRuleGroupStatement(core.Schema):

    excluded_rule: list[ExcludedRule] | core.ArrayOut[ExcludedRule] | None = core.attr(
        ExcludedRule, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    scope_down_statement: ScopeDownStatement | None = core.attr(ScopeDownStatement, default=None)

    vendor_name: str | core.StringOut = core.attr(str)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        vendor_name: str | core.StringOut,
        excluded_rule: list[ExcludedRule] | core.ArrayOut[ExcludedRule] | None = None,
        scope_down_statement: ScopeDownStatement | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ManagedRuleGroupStatement.Args(
                name=name,
                vendor_name=vendor_name,
                excluded_rule=excluded_rule,
                scope_down_statement=scope_down_statement,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        excluded_rule: list[ExcludedRule] | core.ArrayOut[ExcludedRule] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        scope_down_statement: ScopeDownStatement | None = core.arg(default=None)

        vendor_name: str | core.StringOut = core.arg()

        version: str | core.StringOut | None = core.arg(default=None)


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

    managed_rule_group_statement: ManagedRuleGroupStatement | None = core.attr(
        ManagedRuleGroupStatement, default=None
    )

    not_statement: RuleStatementNotStatement | None = core.attr(
        RuleStatementNotStatement, default=None
    )

    or_statement: RuleStatementOrStatement | None = core.attr(
        RuleStatementOrStatement, default=None
    )

    rate_based_statement: RateBasedStatement | None = core.attr(RateBasedStatement, default=None)

    regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.attr(
        RegexPatternSetReferenceStatement, default=None
    )

    rule_group_reference_statement: RuleGroupReferenceStatement | None = core.attr(
        RuleGroupReferenceStatement, default=None
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
        managed_rule_group_statement: ManagedRuleGroupStatement | None = None,
        not_statement: RuleStatementNotStatement | None = None,
        or_statement: RuleStatementOrStatement | None = None,
        rate_based_statement: RateBasedStatement | None = None,
        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = None,
        rule_group_reference_statement: RuleGroupReferenceStatement | None = None,
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
                managed_rule_group_statement=managed_rule_group_statement,
                not_statement=not_statement,
                or_statement=or_statement,
                rate_based_statement=rate_based_statement,
                regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
                rule_group_reference_statement=rule_group_reference_statement,
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

        managed_rule_group_statement: ManagedRuleGroupStatement | None = core.arg(default=None)

        not_statement: RuleStatementNotStatement | None = core.arg(default=None)

        or_statement: RuleStatementOrStatement | None = core.arg(default=None)

        rate_based_statement: RateBasedStatement | None = core.arg(default=None)

        regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = core.arg(
            default=None
        )

        rule_group_reference_statement: RuleGroupReferenceStatement | None = core.arg(default=None)

        size_constraint_statement: SizeConstraintStatement | None = core.arg(default=None)

        sqli_match_statement: SqliMatchStatement | None = core.arg(default=None)

        xss_match_statement: XssMatchStatement | None = core.arg(default=None)


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
class Captcha(core.Schema):

    custom_request_handling: CustomRequestHandling | None = core.attr(
        CustomRequestHandling, default=None
    )

    def __init__(
        self,
        *,
        custom_request_handling: CustomRequestHandling | None = None,
    ):
        super().__init__(
            args=Captcha.Args(
                custom_request_handling=custom_request_handling,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_request_handling: CustomRequestHandling | None = core.arg(default=None)


@core.schema
class ActionCount(core.Schema):

    custom_request_handling: CustomRequestHandling | None = core.attr(
        CustomRequestHandling, default=None
    )

    def __init__(
        self,
        *,
        custom_request_handling: CustomRequestHandling | None = None,
    ):
        super().__init__(
            args=ActionCount.Args(
                custom_request_handling=custom_request_handling,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_request_handling: CustomRequestHandling | None = core.arg(default=None)


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
class Action(core.Schema):

    allow: Allow | None = core.attr(Allow, default=None)

    block: Block | None = core.attr(Block, default=None)

    captcha: Captcha | None = core.attr(Captcha, default=None)

    count: ActionCount | None = core.attr(ActionCount, default=None)

    def __init__(
        self,
        *,
        allow: Allow | None = None,
        block: Block | None = None,
        captcha: Captcha | None = None,
        count: ActionCount | None = None,
    ):
        super().__init__(
            args=Action.Args(
                allow=allow,
                block=block,
                captcha=captcha,
                count=count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow: Allow | None = core.arg(default=None)

        block: Block | None = core.arg(default=None)

        captcha: Captcha | None = core.arg(default=None)

        count: ActionCount | None = core.arg(default=None)


@core.schema
class OverrideActionCount(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class None_(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class OverrideAction(core.Schema):

    count: OverrideActionCount | None = core.attr(OverrideActionCount, default=None)

    none: None_ | None = core.attr(None_, default=None)

    def __init__(
        self,
        *,
        count: OverrideActionCount | None = None,
        none: None_ | None = None,
    ):
        super().__init__(
            args=OverrideAction.Args(
                count=count,
                none=none,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: OverrideActionCount | None = core.arg(default=None)

        none: None_ | None = core.arg(default=None)


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

    action: Action | None = core.attr(Action, default=None)

    name: str | core.StringOut = core.attr(str)

    override_action: OverrideAction | None = core.attr(OverrideAction, default=None)

    priority: int | core.IntOut = core.attr(int)

    rule_label: list[RuleLabel] | core.ArrayOut[RuleLabel] | None = core.attr(
        RuleLabel, default=None, kind=core.Kind.array
    )

    statement: RuleStatement = core.attr(RuleStatement)

    visibility_config: VisibilityConfig = core.attr(VisibilityConfig)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        priority: int | core.IntOut,
        statement: RuleStatement,
        visibility_config: VisibilityConfig,
        action: Action | None = None,
        override_action: OverrideAction | None = None,
        rule_label: list[RuleLabel] | core.ArrayOut[RuleLabel] | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                name=name,
                priority=priority,
                statement=statement,
                visibility_config=visibility_config,
                action=action,
                override_action=override_action,
                rule_label=rule_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        override_action: OverrideAction | None = core.arg(default=None)

        priority: int | core.IntOut = core.arg()

        rule_label: list[RuleLabel] | core.ArrayOut[RuleLabel] | None = core.arg(default=None)

        statement: RuleStatement = core.arg()

        visibility_config: VisibilityConfig = core.arg()


@core.schema
class DefaultAction(core.Schema):

    allow: Allow | None = core.attr(Allow, default=None)

    block: Block | None = core.attr(Block, default=None)

    def __init__(
        self,
        *,
        allow: Allow | None = None,
        block: Block | None = None,
    ):
        super().__init__(
            args=DefaultAction.Args(
                allow=allow,
                block=block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow: Allow | None = core.arg(default=None)

        block: Block | None = core.arg(default=None)


@core.resource(type="aws_wafv2_web_acl", namespace="waf")
class V2WebAcl(core.Resource):
    """
    (Required) The Amazon Resource Name (ARN) of the IP Set that this statement references.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Web ACL capacity units (WCUs) currently being used by this web ACL.
    """
    capacity: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Defines custom response bodies that can be referenced by `custom_response` actions. See [
    Custom Response Body](#custom-response-body) below for details.
    """
    custom_response_body: list[CustomResponseBody] | core.ArrayOut[
        CustomResponseBody
    ] | None = core.attr(CustomResponseBody, default=None, kind=core.Kind.array)

    """
    (Required) Action to perform if none of the `rules` contained in the WebACL match. See [Default Acti
    on](#default-action) below for details.
    """
    default_action: DefaultAction = core.attr(DefaultAction)

    """
    (Optional) Friendly description of the WebACL.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the WAF WebACL.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    lock_token: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Friendly name of the WebACL.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Rule blocks used to identify the web requests that you want to `allow`, `block`, or `coun
    t`. See [Rules](#rules) below for details.
    """
    rule: list[Rule] | core.ArrayOut[Rule] | None = core.attr(
        Rule, default=None, kind=core.Kind.array
    )

    """
    (Required) Specifies whether this is for an AWS CloudFront distribution or for a regional applicatio
    n. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the r
    egion `us-east-1` (N. Virginia) on the AWS provider.
    """
    scope: str | core.StringOut = core.attr(str)

    """
    (Optional) Map of key-value pairs to associate with the resource. If configured with a provider [`de
    fault_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#d
    efault_tags-configuration-block) present, tags with matching keys will overwrite those defined at th
    e provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
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
        default_action: DefaultAction,
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
            args=V2WebAcl.Args(
                default_action=default_action,
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
        custom_response_body: list[CustomResponseBody] | core.ArrayOut[
            CustomResponseBody
        ] | None = core.arg(default=None)

        default_action: DefaultAction = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rule: list[Rule] | core.ArrayOut[Rule] | None = core.arg(default=None)

        scope: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        visibility_config: VisibilityConfig = core.arg()
