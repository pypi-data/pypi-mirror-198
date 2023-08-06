import terrascript.core as core


@core.resource(type="aws_storagegateway_tape_pool", namespace="aws_storagegateway")
class TapePool(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    pool_name: str | core.StringOut = core.attr(str)

    retention_lock_time_in_days: int | core.IntOut | None = core.attr(int, default=None)

    retention_lock_type: str | core.StringOut | None = core.attr(str, default=None)

    storage_class: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
