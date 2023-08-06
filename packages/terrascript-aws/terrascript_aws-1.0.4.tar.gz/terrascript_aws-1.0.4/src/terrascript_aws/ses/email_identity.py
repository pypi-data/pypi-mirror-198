import terrascript.core as core


@core.resource(type="aws_ses_email_identity", namespace="ses")
class EmailIdentity(core.Resource):
    """
    The ARN of the email identity.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The email address to assign to SES
    """
    email: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        email: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EmailIdentity.Args(
                email=email,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        email: str | core.StringOut = core.arg()
