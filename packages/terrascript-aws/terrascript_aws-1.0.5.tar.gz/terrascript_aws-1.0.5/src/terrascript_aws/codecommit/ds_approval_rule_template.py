import terrascript.core as core


@core.data(type="aws_codecommit_approval_rule_template", namespace="codecommit")
class DsApprovalRuleTemplate(core.Data):
    """
    The ID of the approval rule template.
    """

    approval_rule_template_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The content of the approval rule template.
    """
    content: str | core.StringOut = core.attr(str, computed=True)

    """
    The date the approval rule template was created, in [RFC3339 format](https://tools.ietf.org/html/rfc
    3339#section-5.8).
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the approval rule template.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The date the approval rule template was most recently changed, in [RFC3339 format](https://tools.iet
    f.org/html/rfc3339#section-5.8).
    """
    last_modified_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule tem
    plate.
    """
    last_modified_user: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for the approval rule template. This needs to be less than 100 characters.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The SHA-256 hash signature for the content of the approval rule template.
    """
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
