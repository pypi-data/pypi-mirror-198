import terrascript.core as core


@core.resource(type="aws_codecommit_approval_rule_template", namespace="aws_codecommit")
class ApprovalRuleTemplate(core.Resource):

    approval_rule_template_id: str | core.StringOut = core.attr(str, computed=True)

    content: str | core.StringOut = core.attr(str)

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_modified_date: str | core.StringOut = core.attr(str, computed=True)

    last_modified_user: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    rule_content_sha256: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        content: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApprovalRuleTemplate.Args(
                content=content,
                name=name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
