import terrascript.core as core


@core.resource(type="aws_securityhub_invite_accepter", namespace="securityhub")
class InviteAccepter(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    invitation_id: str | core.StringOut = core.attr(str, computed=True)

    master_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        master_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InviteAccepter.Args(
                master_id=master_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        master_id: str | core.StringOut = core.arg()
