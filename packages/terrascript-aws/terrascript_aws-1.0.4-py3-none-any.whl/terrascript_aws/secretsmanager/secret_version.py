import terrascript.core as core


@core.resource(type="aws_secretsmanager_secret_version", namespace="secretsmanager")
class SecretVersion(core.Resource):
    """
    The ARN of the secret.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A pipe delimited combination of secret ID and version ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies binary data that you want to encrypt and store in this version of the secret. T
    his is required if secret_string is not set. Needs to be encoded to base64.
    """
    secret_binary: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Specifies the secret to which you want to add a new version. You can specify either the A
    mazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
    """
    secret_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies text data that you want to encrypt and store in this version of the secret. Thi
    s is required if secret_binary is not set.
    """
    secret_string: str | core.StringOut | None = core.attr(str, default=None)

    """
    The unique identifier of the version of the secret.
    """
    version_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies a list of staging labels that are attached to this version of the secret. A sta
    ging label must be unique to a single version of the secret. If you specify a staging label that's a
    lready associated with a different version of the same secret then that staging label is automatical
    ly removed from the other version and attached to this version. If you do not specify a value, then
    AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creati
    on.
    """
    version_stages: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        secret_id: str | core.StringOut,
        secret_binary: str | core.StringOut | None = None,
        secret_string: str | core.StringOut | None = None,
        version_stages: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecretVersion.Args(
                secret_id=secret_id,
                secret_binary=secret_binary,
                secret_string=secret_string,
                version_stages=version_stages,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        secret_binary: str | core.StringOut | None = core.arg(default=None)

        secret_id: str | core.StringOut = core.arg()

        secret_string: str | core.StringOut | None = core.arg(default=None)

        version_stages: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
