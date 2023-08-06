import terrascript.core as core


@core.resource(type="aws_lambda_permission", namespace="aws_lambda_")
class Permission(core.Resource):

    action: str | core.StringOut = core.attr(str)

    event_source_token: str | core.StringOut | None = core.attr(str, default=None)

    function_name: str | core.StringOut = core.attr(str)

    function_url_auth_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    principal: str | core.StringOut = core.attr(str)

    principal_org_id: str | core.StringOut | None = core.attr(str, default=None)

    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    source_account: str | core.StringOut | None = core.attr(str, default=None)

    source_arn: str | core.StringOut | None = core.attr(str, default=None)

    statement_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    statement_id_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        action: str | core.StringOut,
        function_name: str | core.StringOut,
        principal: str | core.StringOut,
        event_source_token: str | core.StringOut | None = None,
        function_url_auth_type: str | core.StringOut | None = None,
        principal_org_id: str | core.StringOut | None = None,
        qualifier: str | core.StringOut | None = None,
        source_account: str | core.StringOut | None = None,
        source_arn: str | core.StringOut | None = None,
        statement_id: str | core.StringOut | None = None,
        statement_id_prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permission.Args(
                action=action,
                function_name=function_name,
                principal=principal,
                event_source_token=event_source_token,
                function_url_auth_type=function_url_auth_type,
                principal_org_id=principal_org_id,
                qualifier=qualifier,
                source_account=source_account,
                source_arn=source_arn,
                statement_id=statement_id,
                statement_id_prefix=statement_id_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: str | core.StringOut = core.arg()

        event_source_token: str | core.StringOut | None = core.arg(default=None)

        function_name: str | core.StringOut = core.arg()

        function_url_auth_type: str | core.StringOut | None = core.arg(default=None)

        principal: str | core.StringOut = core.arg()

        principal_org_id: str | core.StringOut | None = core.arg(default=None)

        qualifier: str | core.StringOut | None = core.arg(default=None)

        source_account: str | core.StringOut | None = core.arg(default=None)

        source_arn: str | core.StringOut | None = core.arg(default=None)

        statement_id: str | core.StringOut | None = core.arg(default=None)

        statement_id_prefix: str | core.StringOut | None = core.arg(default=None)
