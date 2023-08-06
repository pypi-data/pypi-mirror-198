import terrascript.core as core


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


@core.resource(type="aws_s3_bucket_website_configuration", namespace="aws_s3")
class BucketWebsiteConfiguration(core.Resource):

    bucket: str | core.StringOut = core.attr(str)

    error_document: ErrorDocument | None = core.attr(ErrorDocument, default=None)

    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    index_document: IndexDocument | None = core.attr(IndexDocument, default=None)

    redirect_all_requests_to: RedirectAllRequestsTo | None = core.attr(
        RedirectAllRequestsTo, default=None
    )

    routing_rule: list[RoutingRule] | core.ArrayOut[RoutingRule] | None = core.attr(
        RoutingRule, default=None, computed=True, kind=core.Kind.array
    )

    routing_rules: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    website_domain: str | core.StringOut = core.attr(str, computed=True)

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
