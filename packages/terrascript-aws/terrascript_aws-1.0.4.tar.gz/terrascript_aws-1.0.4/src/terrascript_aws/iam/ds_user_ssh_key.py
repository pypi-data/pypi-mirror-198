import terrascript.core as core


@core.data(type="aws_iam_user_ssh_key", namespace="iam")
class DsUserSshKey(core.Data):
    """
    (Required) Specifies the public key encoding format to use in the response. To retrieve the public k
    ey in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
    """

    encoding: str | core.StringOut = core.attr(str)

    """
    The MD5 message digest of the SSH public key.
    """
    fingerprint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The SSH public key.
    """
    public_key: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The unique identifier for the SSH public key.
    """
    ssh_public_key_id: str | core.StringOut = core.attr(str)

    """
    The status of the SSH public key. Active means that the key can be used for authentication with an C
    odeCommit repository. Inactive means that the key cannot be used.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the IAM user associated with the SSH public key.
    """
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
