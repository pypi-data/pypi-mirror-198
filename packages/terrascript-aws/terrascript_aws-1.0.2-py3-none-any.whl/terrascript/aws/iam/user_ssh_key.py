import terrascript.core as core


@core.resource(type="aws_iam_user_ssh_key", namespace="aws_iam")
class UserSshKey(core.Resource):

    encoding: str | core.StringOut = core.attr(str)

    fingerprint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    public_key: str | core.StringOut = core.attr(str)

    ssh_public_key_id: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        encoding: str | core.StringOut,
        public_key: str | core.StringOut,
        username: str | core.StringOut,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserSshKey.Args(
                encoding=encoding,
                public_key=public_key,
                username=username,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        encoding: str | core.StringOut = core.arg()

        public_key: str | core.StringOut = core.arg()

        status: str | core.StringOut | None = core.arg(default=None)

        username: str | core.StringOut = core.arg()
