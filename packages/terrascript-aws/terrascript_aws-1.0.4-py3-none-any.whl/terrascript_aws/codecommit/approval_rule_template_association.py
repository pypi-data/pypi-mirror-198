import terrascript.core as core


@core.resource(type="aws_codecommit_approval_rule_template_association", namespace="codecommit")
class ApprovalRuleTemplateAssociation(core.Resource):
    """
    (Required) The name for the approval rule template.
    """

    approval_rule_template_name: str | core.StringOut = core.attr(str)

    """
    The name of the approval rule template and name of the repository, separated by a comma (`,`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the repository that you want to associate with the template.
    """
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
