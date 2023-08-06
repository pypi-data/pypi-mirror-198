import terrascript.core as core


@core.resource(type="aws_glacier_vault_lock", namespace="glacier")
class VaultLock(core.Resource):
    """
    (Required) Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this canno
    t be undone. If set to `false`, the Glacier Lock Policy remains in a testing mode for 24 hours. Afte
    r that time, the Glacier Lock Policy is automatically removed by Glacier and the Terraform resource
    will show as needing recreation. Changing this from `false` to `true` will show as resource recreati
    on, which is expected. Changing this from `true` to `false` is not possible unless the Glacier Vault
    is recreated at the same time.
    """

    complete_lock: bool | core.BoolOut = core.attr(bool)

    """
    Glacier Vault name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Allow Terraform to ignore the error returned when attempting to delete the Glacier Lock P
    olicy. This can be used to delete or recreate the Glacier Vault via Terraform, for example, if the G
    lacier Vault Lock policy permits that action. This should only be used in conjunction with `complete
    _lock` being set to `true`.
    """
    ignore_deletion_error: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the Glacier Vault.
    """
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
