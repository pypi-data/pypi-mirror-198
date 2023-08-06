import terrascript.core as core


@core.resource(type="aws_appstream_user", namespace="aws_appstream")
class User(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_type: str | core.StringOut = core.attr(str)

    created_time: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    first_name: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_name: str | core.StringOut | None = core.attr(str, default=None)

    send_email_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_type: str | core.StringOut,
        user_name: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        first_name: str | core.StringOut | None = None,
        last_name: str | core.StringOut | None = None,
        send_email_notification: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                authentication_type=authentication_type,
                user_name=user_name,
                enabled=enabled,
                first_name=first_name,
                last_name=last_name,
                send_email_notification=send_email_notification,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_type: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        first_name: str | core.StringOut | None = core.arg(default=None)

        last_name: str | core.StringOut | None = core.arg(default=None)

        send_email_notification: bool | core.BoolOut | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()
