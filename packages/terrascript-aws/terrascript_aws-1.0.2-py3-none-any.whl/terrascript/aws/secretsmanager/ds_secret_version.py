import terrascript.core as core


@core.data(type="aws_secretsmanager_secret_version", namespace="aws_secretsmanager")
class DsSecretVersion(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    secret_binary: str | core.StringOut = core.attr(str, computed=True)

    secret_id: str | core.StringOut = core.attr(str)

    secret_string: str | core.StringOut = core.attr(str, computed=True)

    version_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
