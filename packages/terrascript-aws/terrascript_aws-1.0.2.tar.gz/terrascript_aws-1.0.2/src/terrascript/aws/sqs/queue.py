import terrascript.core as core


@core.resource(type="aws_sqs_queue", namespace="aws_sqs")
class Queue(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    content_based_deduplication: bool | core.BoolOut | None = core.attr(bool, default=None)

    deduplication_scope: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    delay_seconds: int | core.IntOut | None = core.attr(int, default=None)

    fifo_queue: bool | core.BoolOut | None = core.attr(bool, default=None)

    fifo_throughput_limit: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_data_key_reuse_period_seconds: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    kms_master_key_id: str | core.StringOut | None = core.attr(str, default=None)

    max_message_size: int | core.IntOut | None = core.attr(int, default=None)

    message_retention_seconds: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    receive_wait_time_seconds: int | core.IntOut | None = core.attr(int, default=None)

    redrive_allow_policy: str | core.StringOut | None = core.attr(str, default=None)

    redrive_policy: str | core.StringOut | None = core.attr(str, default=None)

    sqs_managed_sse_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: str | core.StringOut = core.attr(str, computed=True)

    visibility_timeout_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        content_based_deduplication: bool | core.BoolOut | None = None,
        deduplication_scope: str | core.StringOut | None = None,
        delay_seconds: int | core.IntOut | None = None,
        fifo_queue: bool | core.BoolOut | None = None,
        fifo_throughput_limit: str | core.StringOut | None = None,
        kms_data_key_reuse_period_seconds: int | core.IntOut | None = None,
        kms_master_key_id: str | core.StringOut | None = None,
        max_message_size: int | core.IntOut | None = None,
        message_retention_seconds: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        receive_wait_time_seconds: int | core.IntOut | None = None,
        redrive_allow_policy: str | core.StringOut | None = None,
        redrive_policy: str | core.StringOut | None = None,
        sqs_managed_sse_enabled: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        visibility_timeout_seconds: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Queue.Args(
                content_based_deduplication=content_based_deduplication,
                deduplication_scope=deduplication_scope,
                delay_seconds=delay_seconds,
                fifo_queue=fifo_queue,
                fifo_throughput_limit=fifo_throughput_limit,
                kms_data_key_reuse_period_seconds=kms_data_key_reuse_period_seconds,
                kms_master_key_id=kms_master_key_id,
                max_message_size=max_message_size,
                message_retention_seconds=message_retention_seconds,
                name=name,
                name_prefix=name_prefix,
                policy=policy,
                receive_wait_time_seconds=receive_wait_time_seconds,
                redrive_allow_policy=redrive_allow_policy,
                redrive_policy=redrive_policy,
                sqs_managed_sse_enabled=sqs_managed_sse_enabled,
                tags=tags,
                tags_all=tags_all,
                visibility_timeout_seconds=visibility_timeout_seconds,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_based_deduplication: bool | core.BoolOut | None = core.arg(default=None)

        deduplication_scope: str | core.StringOut | None = core.arg(default=None)

        delay_seconds: int | core.IntOut | None = core.arg(default=None)

        fifo_queue: bool | core.BoolOut | None = core.arg(default=None)

        fifo_throughput_limit: str | core.StringOut | None = core.arg(default=None)

        kms_data_key_reuse_period_seconds: int | core.IntOut | None = core.arg(default=None)

        kms_master_key_id: str | core.StringOut | None = core.arg(default=None)

        max_message_size: int | core.IntOut | None = core.arg(default=None)

        message_retention_seconds: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        receive_wait_time_seconds: int | core.IntOut | None = core.arg(default=None)

        redrive_allow_policy: str | core.StringOut | None = core.arg(default=None)

        redrive_policy: str | core.StringOut | None = core.arg(default=None)

        sqs_managed_sse_enabled: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        visibility_timeout_seconds: int | core.IntOut | None = core.arg(default=None)
