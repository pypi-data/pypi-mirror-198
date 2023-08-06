import terrascript.core as core


@core.resource(type="aws_backup_vault", namespace="backup")
class Vault(core.Resource):
    """
    The ARN of the vault.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Default: `false`) A boolean that indicates that all recovery points stored in the vault a
    re deleted so that the vault can be destroyed without error.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The name of the vault.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The server-side encryption key that is used to protect your backups.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Name of the backup vault to create.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The number of recovery points that are stored in a backup vault.
    """
    recovery_points: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Metadata that you can assign to help organize the resources that you create. If configure
    d with a provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashi
    corp/aws/latest/docs#default_tags-configuration-block) present, tags with matching keys will overwri
    te those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        force_destroy: bool | core.BoolOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Vault.Args(
                name=name,
                force_destroy=force_destroy,
                kms_key_arn=kms_key_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
