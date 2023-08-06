import terrascript.core as core


@core.resource(type="aws_detective_member", namespace="aws_detective")
class Member(core.Resource):

    account_id: str | core.StringOut = core.attr(str)

    administrator_id: str | core.StringOut = core.attr(str, computed=True)

    disable_email_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    disabled_reason: str | core.StringOut = core.attr(str, computed=True)

    email_address: str | core.StringOut = core.attr(str)

    graph_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    invited_time: str | core.StringOut = core.attr(str, computed=True)

    message: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    updated_time: str | core.StringOut = core.attr(str, computed=True)

    volume_usage_in_bytes: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut,
        email_address: str | core.StringOut,
        graph_arn: str | core.StringOut,
        disable_email_notification: bool | core.BoolOut | None = None,
        message: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                email_address=email_address,
                graph_arn=graph_arn,
                disable_email_notification=disable_email_notification,
                message=message,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut = core.arg()

        disable_email_notification: bool | core.BoolOut | None = core.arg(default=None)

        email_address: str | core.StringOut = core.arg()

        graph_arn: str | core.StringOut = core.arg()

        message: str | core.StringOut | None = core.arg(default=None)
