import terrascript.core as core


@core.resource(type="aws_transfer_ssh_key", namespace="aws_transfer")
class SshKey(core.Resource):

    body: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    server_id: str | core.StringOut = core.attr(str)

    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        body: str | core.StringOut,
        server_id: str | core.StringOut,
        user_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SshKey.Args(
                body=body,
                server_id=server_id,
                user_name=user_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        body: str | core.StringOut = core.arg()

        server_id: str | core.StringOut = core.arg()

        user_name: str | core.StringOut = core.arg()
