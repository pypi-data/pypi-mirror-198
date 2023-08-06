import terrascript.core as core


@core.resource(type="aws_codecommit_approval_rule_template_association", namespace="aws_codecommit")
class ApprovalRuleTemplateAssociation(core.Resource):

    approval_rule_template_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    repository_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        approval_rule_template_name: str | core.StringOut,
        repository_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApprovalRuleTemplateAssociation.Args(
                approval_rule_template_name=approval_rule_template_name,
                repository_name=repository_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        approval_rule_template_name: str | core.StringOut = core.arg()

        repository_name: str | core.StringOut = core.arg()
