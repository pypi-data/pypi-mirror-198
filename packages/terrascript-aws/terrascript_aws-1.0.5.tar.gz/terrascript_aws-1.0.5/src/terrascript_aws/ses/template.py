import terrascript.core as core


@core.resource(type="aws_ses_template", namespace="ses")
class Template(core.Resource):
    """
    The ARN of the SES template
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The HTML body of the email. Must be less than 500KB in size, including both the text and
    HTML parts.
    """
    html: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name of the SES template
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the template. Cannot exceed 64 characters. You will refer to this name when y
    ou send email.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The subject line of the email.
    """
    subject: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The email body that will be visible to recipients whose email clients do not display HTML
    . Must be less than 500KB in size, including both the text and HTML parts.
    """
    text: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        html: str | core.StringOut | None = None,
        subject: str | core.StringOut | None = None,
        text: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Template.Args(
                name=name,
                html=html,
                subject=subject,
                text=text,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        html: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        subject: str | core.StringOut | None = core.arg(default=None)

        text: str | core.StringOut | None = core.arg(default=None)
