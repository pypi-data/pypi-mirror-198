import terrascript.core as core


@core.resource(type="aws_appstream_user_stack_association", namespace="appstream")
class UserStackAssociation(core.Resource):
    """
    (Required) Authentication type for the user.
    """

    authentication_type: str | core.StringOut = core.attr(str)

    """
    Unique ID of the appstream User Stack association.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether a welcome email is sent to a user after the user is created in the user
    pool.
    """
    send_email_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    stack_name: str | core.StringOut = core.attr(str)

    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_type: str | core.StringOut,
        stack_name: str | core.StringOut,
        user_name: str | core.StringOut,
        send_email_notification: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserStackAssociation.Args(
                authentication_type=authentication_type,
                stack_name=stack_name,
                user_name=user_name,
                send_email_notification=send_email_notification,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_type: str | core.StringOut = core.arg()

        send_email_notification: bool | core.BoolOut | None = core.arg(default=None)

        stack_name: str | core.StringOut = core.arg()

        user_name: str | core.StringOut = core.arg()
