import terrascript.core as core


@core.resource(type="aws_sns_topic", namespace="sns")
class Topic(core.Resource):
    """
    (Optional) IAM role for failure feedback
    """

    application_failure_feedback_role_arn: str | core.StringOut | None = core.attr(
        str, default=None
    )

    """
    (Optional) The IAM role permitted to receive success feedback for this topic
    """
    application_success_feedback_role_arn: str | core.StringOut | None = core.attr(
        str, default=None
    )

    """
    (Optional) Percentage of success to sample
    """
    application_success_feedback_sample_rate: int | core.IntOut | None = core.attr(
        int, default=None
    )

    """
    The ARN of the SNS topic, as a more obvious property (clone of id)
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Enables content-based deduplication for FIFO topics. For more information, see the [relat
    ed documentation](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-dedup.html)
    """
    content_based_deduplication: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/late
    st/dg/DeliveryPolicies.html)
    """
    delivery_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The display name for the topic
    """
    display_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Boolean indicating whether or not to create a FIFO (first-in-first-out) topic (default is
    false`).
    """
    fifo_topic: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) IAM role for failure feedback
    """
    firehose_failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IAM role permitted to receive success feedback for this topic
    """
    firehose_success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Percentage of success to sample
    """
    firehose_success_feedback_sample_rate: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) IAM role for failure feedback
    """
    http_failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IAM role permitted to receive success feedback for this topic
    """
    http_success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Percentage of success to sample
    """
    http_success_feedback_sample_rate: int | core.IntOut | None = core.attr(int, default=None)

    """
    The ARN of the SNS topic
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For mo
    re information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption
    .html#sse-key-terms)
    """
    kms_master_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) IAM role for failure feedback
    """
    lambda_failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IAM role permitted to receive success feedback for this topic
    """
    lambda_success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Percentage of success to sample
    """
    lambda_success_feedback_sample_rate: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The name of the topic. Topic names must be made up of only uppercase and lowercase ASCII
    letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long. For a FIF
    O (first-in-first-out) topic, the name must end with the `.fifo` suffix. If omitted, Terraform will
    assign a random, unique name. Conflicts with `name_prefix`
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The AWS Account ID of the SNS topic owner
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The fully-formed AWS policy as JSON. For more information about building AWS IAM policy d
    ocuments with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terrafo
    rm/aws/iam-policy).
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) IAM role for failure feedback
    """
    sqs_failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IAM role permitted to receive success feedback for this topic
    """
    sqs_success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Percentage of success to sample
    """
    sqs_success_feedback_sample_rate: int | core.IntOut | None = core.attr(int, default=None)

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
