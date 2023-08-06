import terrascript.core as core


@core.resource(type="aws_detective_invitation_accepter", namespace="detective")
class InvitationAccepter(core.Resource):
    """
    (Required) ARN of the behavior graph that the member account is accepting the invitation for.
    """

    graph_arn: str | core.StringOut = core.attr(str)

    """
    Unique identifier (ID) of the Detective invitation accepter.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        graph_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InvitationAccepter.Args(
                graph_arn=graph_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        graph_arn: str | core.StringOut = core.arg()
