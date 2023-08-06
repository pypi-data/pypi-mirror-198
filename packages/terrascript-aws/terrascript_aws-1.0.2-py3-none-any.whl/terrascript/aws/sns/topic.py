import terrascript.core as core


@core.resource(type="aws_sns_topic", namespace="aws_sns")
class Topic(core.Resource):

    application_failure_feedback_role_arn: str | core.StringOut | None = core.attr(
        str, default=None
    )

    application_success_feedback_role_arn: str | core.StringOut | None = core.attr(
        str, default=None
    )

    application_success_feedback_sample_rate: int | core.IntOut | None = core.attr(
        int, default=None
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    content_based_deduplication: bool | core.BoolOut | None = core.attr(bool, default=None)

    delivery_policy: str | core.StringOut | None = core.attr(str, default=None)

    display_name: str | core.StringOut | None = core.attr(str, default=None)

    fifo_topic: bool | core.BoolOut | None = core.attr(bool, default=None)

    firehose_failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    firehose_success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    firehose_success_feedback_sample_rate: int | core.IntOut | None = core.attr(int, default=None)

    http_failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    http_success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    http_success_feedback_sample_rate: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_master_key_id: str | core.StringOut | None = core.attr(str, default=None)

    lambda_failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    lambda_success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    lambda_success_feedback_sample_rate: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    owner: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    sqs_failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    sqs_success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    sqs_success_feedback_sample_rate: int | core.IntOut | None = core.attr(int, default=None)

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
        application_failure_feedback_role_arn: str | core.StringOut | None = None,
        application_success_feedback_role_arn: str | core.StringOut | None = None,
        application_success_feedback_sample_rate: int | core.IntOut | None = None,
        content_based_deduplication: bool | core.BoolOut | None = None,
        delivery_policy: str | core.StringOut | None = None,
        display_name: str | core.StringOut | None = None,
        fifo_topic: bool | core.BoolOut | None = None,
        firehose_failure_feedback_role_arn: str | core.StringOut | None = None,
        firehose_success_feedback_role_arn: str | core.StringOut | None = None,
        firehose_success_feedback_sample_rate: int | core.IntOut | None = None,
        http_failure_feedback_role_arn: str | core.StringOut | None = None,
        http_success_feedback_role_arn: str | core.StringOut | None = None,
        http_success_feedback_sample_rate: int | core.IntOut | None = None,
        kms_master_key_id: str | core.StringOut | None = None,
        lambda_failure_feedback_role_arn: str | core.StringOut | None = None,
        lambda_success_feedback_role_arn: str | core.StringOut | None = None,
        lambda_success_feedback_sample_rate: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        sqs_failure_feedback_role_arn: str | core.StringOut | None = None,
        sqs_success_feedback_role_arn: str | core.StringOut | None = None,
        sqs_success_feedback_sample_rate: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Topic.Args(
                application_failure_feedback_role_arn=application_failure_feedback_role_arn,
                application_success_feedback_role_arn=application_success_feedback_role_arn,
                application_success_feedback_sample_rate=application_success_feedback_sample_rate,
                content_based_deduplication=content_based_deduplication,
                delivery_policy=delivery_policy,
                display_name=display_name,
                fifo_topic=fifo_topic,
                firehose_failure_feedback_role_arn=firehose_failure_feedback_role_arn,
                firehose_success_feedback_role_arn=firehose_success_feedback_role_arn,
                firehose_success_feedback_sample_rate=firehose_success_feedback_sample_rate,
                http_failure_feedback_role_arn=http_failure_feedback_role_arn,
                http_success_feedback_role_arn=http_success_feedback_role_arn,
                http_success_feedback_sample_rate=http_success_feedback_sample_rate,
                kms_master_key_id=kms_master_key_id,
                lambda_failure_feedback_role_arn=lambda_failure_feedback_role_arn,
                lambda_success_feedback_role_arn=lambda_success_feedback_role_arn,
                lambda_success_feedback_sample_rate=lambda_success_feedback_sample_rate,
                name=name,
                name_prefix=name_prefix,
                policy=policy,
                sqs_failure_feedback_role_arn=sqs_failure_feedback_role_arn,
                sqs_success_feedback_role_arn=sqs_success_feedback_role_arn,
                sqs_success_feedback_sample_rate=sqs_success_feedback_sample_rate,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_failure_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        application_success_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        application_success_feedback_sample_rate: int | core.IntOut | None = core.arg(default=None)

        content_based_deduplication: bool | core.BoolOut | None = core.arg(default=None)

        delivery_policy: str | core.StringOut | None = core.arg(default=None)

        display_name: str | core.StringOut | None = core.arg(default=None)

        fifo_topic: bool | core.BoolOut | None = core.arg(default=None)

        firehose_failure_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        firehose_success_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        firehose_success_feedback_sample_rate: int | core.IntOut | None = core.arg(default=None)

        http_failure_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        http_success_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        http_success_feedback_sample_rate: int | core.IntOut | None = core.arg(default=None)

        kms_master_key_id: str | core.StringOut | None = core.arg(default=None)

        lambda_failure_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        lambda_success_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        lambda_success_feedback_sample_rate: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        sqs_failure_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        sqs_success_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        sqs_success_feedback_sample_rate: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
