import terrascript.core as core


@core.resource(type="aws_ses_template", namespace="aws_ses")
class Template(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    html: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    subject: str | core.StringOut | None = core.attr(str, default=None)

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
