import terrascript.core as core


@core.resource(type="aws_storagegateway_tape_pool", namespace="storagegateway")
class TapePool(core.Resource):
    """
    Volume Amazon Resource Name (ARN), e.g., `aws_storagegateway_tape_pool.example arn:aws:storagegatewa
    y:us-east-1:123456789012:tapepool/pool-12345678`.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the new custom tape pool.
    """
    pool_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100
    years (36,500 days). Default value is 0.
    """
    retention_lock_time_in_days: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) Tape retention lock can be configured in two modes. When configured in governance mode, A
    WS accounts with specific IAM permissions are authorized to remove the tape retention lock from arch
    ived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by
    any user, including the root AWS account. Possible values are `COMPLIANCE`, `GOVERNANCE`, and `NONE
    . Default value is `NONE`.
    """
    retention_lock_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The storage class that is associated with the new custom pool. When you use your backup a
    pplication to eject the tape, the tape is archived directly into the storage class that corresponds
    to the pool. Possible values are `DEEP_ARCHIVE` or `GLACIER`.
    """
    storage_class: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        pool_name: str | core.StringOut,
        storage_class: str | core.StringOut,
        retention_lock_time_in_days: int | core.IntOut | None = None,
        retention_lock_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TapePool.Args(
                pool_name=pool_name,
                storage_class=storage_class,
                retention_lock_time_in_days=retention_lock_time_in_days,
                retention_lock_type=retention_lock_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        pool_name: str | core.StringOut = core.arg()

        retention_lock_time_in_days: int | core.IntOut | None = core.arg(default=None)

        retention_lock_type: str | core.StringOut | None = core.arg(default=None)

        storage_class: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
