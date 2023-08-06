import terrascript.core as core


@core.resource(type="aws_networkmanager_attachment_accepter", namespace="networkmanager")
class AttachmentAccepter(core.Resource):
    """
    (Required) The ID of the attachment.
    """

    attachment_id: str | core.StringOut = core.attr(str)

    """
    The policy rule number associated with the attachment.
    """
    attachment_policy_rule_number: int | core.IntOut = core.attr(int, computed=True)

    """
    The type of attachment. Valid values can be found in the [AWS Documentation](https://docs.aws.amazon
    .com/networkmanager/latest/APIReference/API_ListAttachments.html#API_ListAttachments_RequestSyntax)
    """
    attachment_type: str | core.StringOut = core.attr(str)

    """
    The ARN of a core network.
    """
    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The id of a core network.
    """
    core_network_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Region where the edge is located.
    """
    edge_location: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the attachment account owner.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The attachment resource ARN.
    """
    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the segment attachment.
    """
    segment_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the attachment.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        attachment_id: str | core.StringOut,
        attachment_type: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AttachmentAccepter.Args(
                attachment_id=attachment_id,
                attachment_type=attachment_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attachment_id: str | core.StringOut = core.arg()

        attachment_type: str | core.StringOut = core.arg()
