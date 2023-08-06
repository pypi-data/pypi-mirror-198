import terrascript.core as core


@core.data(type="aws_codecommit_approval_rule_template", namespace="aws_codecommit")
class DsApprovalRuleTemplate(core.Data):

    approval_rule_template_id: str | core.StringOut = core.attr(str, computed=True)

    content: str | core.StringOut = core.attr(str, computed=True)

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_modified_date: str | core.StringOut = core.attr(str, computed=True)

    last_modified_user: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    rule_content_sha256: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsApprovalRuleTemplate.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
