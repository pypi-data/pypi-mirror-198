import terrascript.core as core


@core.schema
class IndexDocument(core.Schema):

    suffix: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        suffix: str | core.StringOut,
    ):
        super().__init__(
            args=IndexDocument.Args(
                suffix=suffix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        suffix: str | core.StringOut = core.arg()


@core.schema
class ErrorDocument(core.Schema):

    key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
    ):
        super().__init__(
            args=ErrorDocument.Args(
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()


@core.schema
class Redirect(core.Schema):

    host_name: str | core.StringOut | None = core.attr(str, default=None)

    http_redirect_code: str | core.StringOut | None = core.attr(str, default=None)

    protocol: str | core.StringOut | None = core.attr(str, default=None)

    replace_key_prefix_with: str | core.StringOut | None = core.attr(str, default=None)

    replace_key_with: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        host_name: str | core.StringOut | None = None,
        http_redirect_code: str | core.StringOut | None = None,
        protocol: str | core.StringOut | None = None,
        replace_key_prefix_with: str | core.StringOut | None = None,
        replace_key_with: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Redirect.Args(
                host_name=host_name,
                http_redirect_code=http_redirect_code,
                protocol=protocol,
                replace_key_prefix_with=replace_key_prefix_with,
                replace_key_with=replace_key_with,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host_name: str | core.StringOut | None = core.arg(default=None)

        http_redirect_code: str | core.StringOut | None = core.arg(default=None)

        protocol: str | core.StringOut | None = core.arg(default=None)

        replace_key_prefix_with: str | core.StringOut | None = core.arg(default=None)

        replace_key_with: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Condition(core.Schema):

    http_error_code_returned_equals: str | core.StringOut | None = core.attr(str, default=None)

    key_prefix_equals: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_error_code_returned_equals: str | core.StringOut | None = None,
        key_prefix_equals: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Condition.Args(
                http_error_code_returned_equals=http_error_code_returned_equals,
                key_prefix_equals=key_prefix_equals,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_error_code_returned_equals: str | core.StringOut | None = core.arg(default=None)

        key_prefix_equals: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RoutingRule(core.Schema):

    condition: Condition | None = core.attr(Condition, default=None)

    redirect: Redirect = core.attr(Redirect)

    def __init__(
        self,
        *,
        redirect: Redirect,
        condition: Condition | None = None,
    ):
        super().__init__(
            args=RoutingRule.Args(
                redirect=redirect,
                condition=condition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition: Condition | None = core.arg(default=None)

        redirect: Redirect = core.arg()


@core.schema
class RedirectAllRequestsTo(core.Schema):

    host_name: str | core.StringOut = core.attr(str)

    protocol: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        host_name: str | core.StringOut,
        protocol: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RedirectAllRequestsTo.Args(
                host_name=host_name,
                protocol=protocol,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host_name: str | core.StringOut = core.arg()

        protocol: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_s3_bucket_website_configuration", namespace="s3")
class BucketWebsiteConfiguration(core.Resource):
    """
    (Required, Forces new resource) The name of the bucket.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional, Conflicts with `redirect_all_requests_to`) The name of the error document for the website
    [detailed below](#error_document).
    """
    error_document: ErrorDocument | None = core.attr(ErrorDocument, default=None)

    """
    (Optional, Forces new resource) The account ID of the expected bucket owner.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    The `bucket` or `bucket` and `expected_bucket_owner` separated by a comma (`,`) if the latter is pro
    vided.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Required if `redirect_all_requests_to` is not specified) The name of the index document f
    or the website [detailed below](#index_document).
    """
    index_document: IndexDocument | None = core.attr(IndexDocument, default=None)

    """
    (Optional, Required if `index_document` is not specified) The redirect behavior for every request to
    this bucket's website endpoint [detailed below](#redirect_all_requests_to). Conflicts with `error_d
    ocument`, `index_document`, and `routing_rule`.
    """
    redirect_all_requests_to: RedirectAllRequestsTo | None = core.attr(
        RedirectAllRequestsTo, default=None
    )

    """
    (Optional, Conflicts with `redirect_all_requests_to` and `routing_rules`) List of rules that define
    when a redirect is applied and the redirect behavior [detailed below](#routing_rule).
    """
    routing_rule: list[RoutingRule] | core.ArrayOut[RoutingRule] | None = core.attr(
        RoutingRule, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional, Conflicts with `routing_rule` and `redirect_all_requests_to`) A json array containing [ro
    uting rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websit
    econfiguration-routingrules.html)
    """
    routing_rules: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The domain of the website endpoint. This is used to create Route 53 alias records.
    """
    website_domain: str | core.StringOut = core.attr(str, computed=True)

    """
    The website endpoint.
    """
    website_endpoint: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        error_document: ErrorDocument | None = None,
        expected_bucket_owner: str | core.StringOut | None = None,
        index_document: IndexDocument | None = None,
        redirect_all_requests_to: RedirectAllRequestsTo | None = None,
        routing_rule: list[RoutingRule] | core.ArrayOut[RoutingRule] | None = None,
        routing_rules: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketWebsiteConfiguration.Args(
                bucket=bucket,
                error_document=error_document,
                expected_bucket_owner=expected_bucket_owner,
                index_document=index_document,
                redirect_all_requests_to=redirect_all_requests_to,
                routing_rule=routing_rule,
                routing_rules=routing_rules,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        error_document: ErrorDocument | None = core.arg(default=None)

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        index_document: IndexDocument | None = core.arg(default=None)

        redirect_all_requests_to: RedirectAllRequestsTo | None = core.arg(default=None)

        routing_rule: list[RoutingRule] | core.ArrayOut[RoutingRule] | None = core.arg(default=None)

        routing_rules: str | core.StringOut | None = core.arg(default=None)
