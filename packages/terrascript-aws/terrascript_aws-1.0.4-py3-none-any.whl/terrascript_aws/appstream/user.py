import terrascript.core as core


@core.resource(type="aws_appstream_user", namespace="appstream")
class User(core.Resource):
    """
    ARN of the appstream user.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Authentication type for the user. You must specify USERPOOL. Valid values: `API`, `SAML`,
    USERPOOL`
    """
    authentication_type: str | core.StringOut = core.attr(str)

    """
    Date and time, in UTC and extended RFC 3339 format, when the user was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether the user in the user pool is enabled.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) First name, or given name, of the user.
    """
    first_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    Unique ID of the appstream user.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Last name, or surname, of the user.
    """
    last_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Send an email notification.
    """
    send_email_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Email address of the user.
    """
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
