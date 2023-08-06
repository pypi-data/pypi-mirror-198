import terrascript.core as core


@core.resource(type="aws_secretsmanager_secret_version", namespace="aws_secretsmanager")
class SecretVersion(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    secret_binary: str | core.StringOut | None = core.attr(str, default=None)

    secret_id: str | core.StringOut = core.attr(str)

    secret_string: str | core.StringOut | None = core.attr(str, default=None)

    version_id: str | core.StringOut = core.attr(str, computed=True)

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
