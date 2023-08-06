import terrascript.core as core


@core.resource(type="aws_networkmanager_attachment_accepter", namespace="aws_networkmanager")
class AttachmentAccepter(core.Resource):

    attachment_id: str | core.StringOut = core.attr(str)

    attachment_policy_rule_number: int | core.IntOut = core.attr(int, computed=True)

    attachment_type: str | core.StringOut = core.attr(str)

    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    core_network_id: str | core.StringOut = core.attr(str, computed=True)

    edge_location: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    segment_name: str | core.StringOut = core.attr(str, computed=True)

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
