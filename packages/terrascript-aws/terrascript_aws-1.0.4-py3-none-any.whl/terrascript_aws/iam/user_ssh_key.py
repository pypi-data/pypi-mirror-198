import terrascript.core as core


@core.resource(type="aws_iam_user_ssh_key", namespace="iam")
class UserSshKey(core.Resource):
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
    (Required) The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
    """
    public_key: str | core.StringOut = core.attr(str)

    """
    The unique identifier for the SSH public key.
    """
    ssh_public_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The status to assign to the SSH public key. Active means the key can be used for authenti
    cation with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`
    .
    """
    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name of the IAM user to associate the SSH public key with.
    """
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
