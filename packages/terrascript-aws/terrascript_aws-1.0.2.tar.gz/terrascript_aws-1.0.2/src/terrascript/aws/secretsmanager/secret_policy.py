import terrascript.core as core


@core.resource(type="aws_secretsmanager_secret_policy", namespace="aws_secretsmanager")
class SecretPolicy(core.Resource):

    block_public_policy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str)

    secret_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        secret_arn: str | core.StringOut,
        block_public_policy: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecretPolicy.Args(
                policy=policy,
                secret_arn=secret_arn,
                block_public_policy=block_public_policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_public_policy: bool | core.BoolOut | None = core.arg(default=None)

        policy: str | core.StringOut = core.arg()

        secret_arn: str | core.StringOut = core.arg()
