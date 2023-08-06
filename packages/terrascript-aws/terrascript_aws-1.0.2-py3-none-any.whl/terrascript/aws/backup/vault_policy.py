import terrascript.core as core


@core.resource(type="aws_backup_vault_policy", namespace="aws_backup")
class VaultPolicy(core.Resource):

    backup_vault_arn: str | core.StringOut = core.attr(str, computed=True)

    backup_vault_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        backup_vault_name: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VaultPolicy.Args(
                backup_vault_name=backup_vault_name,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        backup_vault_name: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
