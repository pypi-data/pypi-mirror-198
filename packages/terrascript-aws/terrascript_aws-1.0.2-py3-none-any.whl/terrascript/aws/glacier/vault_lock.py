import terrascript.core as core


@core.resource(type="aws_glacier_vault_lock", namespace="aws_glacier")
class VaultLock(core.Resource):

    complete_lock: bool | core.BoolOut = core.attr(bool)

    id: str | core.StringOut = core.attr(str, computed=True)

    ignore_deletion_error: bool | core.BoolOut | None = core.attr(bool, default=None)

    policy: str | core.StringOut = core.attr(str)

    vault_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        complete_lock: bool | core.BoolOut,
        policy: str | core.StringOut,
        vault_name: str | core.StringOut,
        ignore_deletion_error: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VaultLock.Args(
                complete_lock=complete_lock,
                policy=policy,
                vault_name=vault_name,
                ignore_deletion_error=ignore_deletion_error,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        complete_lock: bool | core.BoolOut = core.arg()

        ignore_deletion_error: bool | core.BoolOut | None = core.arg(default=None)

        policy: str | core.StringOut = core.arg()

        vault_name: str | core.StringOut = core.arg()
