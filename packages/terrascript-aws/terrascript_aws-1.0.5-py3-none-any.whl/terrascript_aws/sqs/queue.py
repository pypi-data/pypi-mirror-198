import terrascript.core as core


@core.resource(type="aws_sqs_queue", namespace="sqs")
class Queue(core.Resource):
    """
    The ARN of the SQS queue
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Enables content-based deduplication for FIFO queues. For more information, see the [relat
    ed documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-que
    ues.html#FIFO-queues-exactly-once-processing)
    """
    content_based_deduplication: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether message deduplication occurs at the message group or queue level. Valid
    values are `messageGroup` and `queue` (default).
    """
    deduplication_scope: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The time in seconds that the delivery of all messages in the queue will be delayed. An in
    teger from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.
    """
    delay_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.
    """
    fifo_queue: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether the FIFO queue throughput quota applies to the entire queue or per mess
    age group. Valid values are `perQueue` (default) and `perMessageGroupId`.
    """
    fifo_throughput_limit: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The URL for the created Amazon SQS queue.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or d
    ecrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1
    minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).
    """
    kms_data_key_reuse_period_seconds: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For mo
    re information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloper
    Guide/sqs-server-side-encryption.html#sqs-sse-key-terms).
    """
    kms_master_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The limit of how many bytes a message can contain before Amazon SQS rejects it. An intege
    r from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (25
    6 KiB).
    """
    max_message_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60
    (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
    """
    message_retention_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The name of the queue. Queue names must be made up of only uppercase and lowercase ASCII
    letters, numbers, underscores, and hyphens, and must be between 1 and 80 characters long. For a FIFO
    (first-in-first-out) queue, the name must end with the `.fifo` suffix. If omitted, Terraform will a
    ssign a random, unique name. Conflicts with `name_prefix`
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The JSON policy for the SQS queue. For more information about building AWS IAM policy doc
    uments with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform
    /aws/iam-policy).
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The time for which a ReceiveMessage call will wait for a message to arrive (long polling)
    before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning t
    hat the call will return immediately.
    """
    receive_wait_time_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The JSON policy to set up the Dead Letter Queue redrive permission, see [AWS docs](https:
    //docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html).
    """
    redrive_allow_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.c
    om/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifyin
    g `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).
    """
    redrive_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Boolean to enable server-side encryption (SSE) of message content with SQS-owned encrypti
    on keys. Defaults to `false`. See [Encryption at rest](https://docs.aws.amazon.com/AWSSimpleQueueSer
    vice/latest/SQSDeveloperGuide/sqs-server-side-encryption.html).
    """
    sqs_managed_sse_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A map of tags to assign to the queue. If configured with a provider [`default_tags` confi
    guration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-confi
    guration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    Same as `id`: The URL for the created Amazon SQS queue.
    """
    url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default
    for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs
    .aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).
    """
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
