import terrascript.core as core


@core.resource(type="aws_codecommit_approval_rule_template", namespace="codecommit")
class ApprovalRuleTemplate(core.Resource):
    """
    The ID of the approval rule template
    """

    approval_rule_template_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The content of the approval rule template. Maximum of 3000 characters.
    """
    content: str | core.StringOut = core.attr(str)

    """
    The date the approval rule template was created, in [RFC3339 format](https://tools.ietf.org/html/rfc
    3339#section-5.8).
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the approval rule template. Maximum of 1000 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

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
    (Required) The name for the approval rule template. Maximum of 100 characters.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The SHA-256 hash signature for the content of the approval rule template.
    """
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
