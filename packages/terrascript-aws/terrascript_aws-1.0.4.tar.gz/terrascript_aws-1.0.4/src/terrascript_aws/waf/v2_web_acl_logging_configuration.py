import terrascript.core as core


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
class RedactedFields(core.Schema):

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
            args=RedactedFields.Args(
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
class ActionCondition(core.Schema):

    action: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        action: str | core.StringOut,
    ):
        super().__init__(
            args=ActionCondition.Args(
                action=action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut = core.arg()


@core.schema
class LabelNameCondition(core.Schema):

    label_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        label_name: str | core.StringOut,
    ):
        super().__init__(
            args=LabelNameCondition.Args(
                label_name=label_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        label_name: str | core.StringOut = core.arg()


@core.schema
class Condition(core.Schema):

    action_condition: ActionCondition | None = core.attr(ActionCondition, default=None)

    label_name_condition: LabelNameCondition | None = core.attr(LabelNameCondition, default=None)

    def __init__(
        self,
        *,
        action_condition: ActionCondition | None = None,
        label_name_condition: LabelNameCondition | None = None,
    ):
        super().__init__(
            args=Condition.Args(
                action_condition=action_condition,
                label_name_condition=label_name_condition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_condition: ActionCondition | None = core.arg(default=None)

        label_name_condition: LabelNameCondition | None = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    behavior: str | core.StringOut = core.attr(str)

    condition: list[Condition] | core.ArrayOut[Condition] = core.attr(
        Condition, kind=core.Kind.array
    )

    requirement: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        behavior: str | core.StringOut,
        condition: list[Condition] | core.ArrayOut[Condition],
        requirement: str | core.StringOut,
    ):
        super().__init__(
            args=Filter.Args(
                behavior=behavior,
                condition=condition,
                requirement=requirement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        behavior: str | core.StringOut = core.arg()

        condition: list[Condition] | core.ArrayOut[Condition] = core.arg()

        requirement: str | core.StringOut = core.arg()


@core.schema
class LoggingFilter(core.Schema):

    default_behavior: str | core.StringOut = core.attr(str)

    filter: list[Filter] | core.ArrayOut[Filter] = core.attr(Filter, kind=core.Kind.array)

    def __init__(
        self,
        *,
        default_behavior: str | core.StringOut,
        filter: list[Filter] | core.ArrayOut[Filter],
    ):
        super().__init__(
            args=LoggingFilter.Args(
                default_behavior=default_behavior,
                filter=filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_behavior: str | core.StringOut = core.arg()

        filter: list[Filter] | core.ArrayOut[Filter] = core.arg()


@core.resource(type="aws_wafv2_web_acl_logging_configuration", namespace="waf")
class V2WebAclLoggingConfiguration(core.Resource):
    """
    The Amazon Resource Name (ARN) of the WAFv2 Web ACL.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Kinesis Data Firehose, Cloudwatch Log log group, or S3 bucket Amazon Resource
    Names (ARNs) that you want to associate with the web ACL.
    """
    log_destination_configs: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) A configuration block that specifies which web requests are kept in the logs and which ar
    e dropped. You can filter on the rule action and on the web request labels that were applied by matc
    hing rules during web ACL evaluation. See [Logging Filter](#logging-filter) below for more details.
    """
    logging_filter: LoggingFilter | None = core.attr(LoggingFilter, default=None)

    """
    (Optional) The parts of the request that you want to keep out of the logs. Up to 100 `redacted_field
    s` blocks are supported. See [Redacted Fields](#redacted-fields) below for more details.
    """
    redacted_fields: list[RedactedFields] | core.ArrayOut[RedactedFields] | None = core.attr(
        RedactedFields, default=None, kind=core.Kind.array
    )

    """
    (Required) The Amazon Resource Name (ARN) of the web ACL that you want to associate with `log_destin
    ation_configs`.
    """
    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        log_destination_configs: list[str] | core.ArrayOut[core.StringOut],
        resource_arn: str | core.StringOut,
        logging_filter: LoggingFilter | None = None,
        redacted_fields: list[RedactedFields] | core.ArrayOut[RedactedFields] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2WebAclLoggingConfiguration.Args(
                log_destination_configs=log_destination_configs,
                resource_arn=resource_arn,
                logging_filter=logging_filter,
                redacted_fields=redacted_fields,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        log_destination_configs: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        logging_filter: LoggingFilter | None = core.arg(default=None)

        redacted_fields: list[RedactedFields] | core.ArrayOut[RedactedFields] | None = core.arg(
            default=None
        )

        resource_arn: str | core.StringOut = core.arg()
