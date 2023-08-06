import terrascript.core as core


@core.data(type="aws_secretsmanager_secret_version", namespace="secretsmanager")
class DsSecretVersion(core.Data):
    """
    The ARN of the secret.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifier of this version of the secret.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The decrypted part of the protected secret information that was originally provided as a binary.
    """
    secret_binary: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the secret containing the version that you want to retrieve. You can specify ei
    ther the Amazon Resource Name (ARN) or the friendly name of the secret.
    """
    secret_id: str | core.StringOut = core.attr(str)

    """
    The decrypted part of the protected secret information that was originally provided as a string.
    """
    secret_string: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the unique identifier of the version of the secret that you want to retrieve. O
    verrides `version_stage`.
    """
    version_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies the secret version that you want to retrieve by the staging label attached to t
    he version. Defaults to `AWSCURRENT`.
    """
    version_stage: str | core.StringOut | None = core.attr(str, default=None)

    version_stages: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        secret_id: str | core.StringOut,
        version_id: str | core.StringOut | None = None,
        version_stage: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSecretVersion.Args(
                secret_id=secret_id,
                version_id=version_id,
                version_stage=version_stage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        secret_id: str | core.StringOut = core.arg()

        version_id: str | core.StringOut | None = core.arg(default=None)

        version_stage: str | core.StringOut | None = core.arg(default=None)
