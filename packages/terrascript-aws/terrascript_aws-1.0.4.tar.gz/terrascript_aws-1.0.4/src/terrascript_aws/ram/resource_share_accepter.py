import terrascript.core as core


@core.resource(type="aws_ram_resource_share_accepter", namespace="ram")
class ResourceShareAccepter(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    invitation_arn: str | core.StringOut = core.attr(str, computed=True)

    receiver_account_id: str | core.StringOut = core.attr(str, computed=True)

    resources: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    sender_account_id: str | core.StringOut = core.attr(str, computed=True)

    share_arn: str | core.StringOut = core.attr(str)

    share_id: str | core.StringOut = core.attr(str, computed=True)

    share_name: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        share_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceShareAccepter.Args(
                share_arn=share_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        share_arn: str | core.StringOut = core.arg()
