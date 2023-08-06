import terrascript.core as core


@core.data(type="aws_iam_user_ssh_key", namespace="aws_iam")
class DsUserSshKey(core.Data):

    encoding: str | core.StringOut = core.attr(str)

    fingerprint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    public_key: str | core.StringOut = core.attr(str, computed=True)

    ssh_public_key_id: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        encoding: str | core.StringOut,
        ssh_public_key_id: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsUserSshKey.Args(
                encoding=encoding,
                ssh_public_key_id=ssh_public_key_id,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encoding: str | core.StringOut = core.arg()

        ssh_public_key_id: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()
