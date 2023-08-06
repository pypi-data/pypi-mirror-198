import terrascript.core as core


@core.resource(type="aws_sns_sms_preferences", namespace="sns")
class SmsPreferences(core.Resource):
    """
    (Optional) A string, such as your business brand, that is displayed as the sender on the receiving d
    evice.
    """

    default_sender_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The type of SMS message that you will send by default. Possible values are: Promotional,
    Transactional
    """
    default_sms_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in Clou
    dWatch Logs.
    """
    delivery_status_iam_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The percentage of successful SMS deliveries for which Amazon SNS will write logs in Cloud
    Watch Logs. The value must be between 0 and 100.
    """
    delivery_status_success_sampling_rate: str | core.StringOut | None = core.attr(
        str, default=None
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The maximum amount in USD that you are willing to spend each month to send SMS messages.
    """
    monthly_spend_limit: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
    """
    usage_report_s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        default_sender_id: str | core.StringOut | None = None,
        default_sms_type: str | core.StringOut | None = None,
        delivery_status_iam_role_arn: str | core.StringOut | None = None,
        delivery_status_success_sampling_rate: str | core.StringOut | None = None,
        monthly_spend_limit: int | core.IntOut | None = None,
        usage_report_s3_bucket: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SmsPreferences.Args(
                default_sender_id=default_sender_id,
                default_sms_type=default_sms_type,
                delivery_status_iam_role_arn=delivery_status_iam_role_arn,
                delivery_status_success_sampling_rate=delivery_status_success_sampling_rate,
                monthly_spend_limit=monthly_spend_limit,
                usage_report_s3_bucket=usage_report_s3_bucket,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_sender_id: str | core.StringOut | None = core.arg(default=None)

        default_sms_type: str | core.StringOut | None = core.arg(default=None)

        delivery_status_iam_role_arn: str | core.StringOut | None = core.arg(default=None)

        delivery_status_success_sampling_rate: str | core.StringOut | None = core.arg(default=None)

        monthly_spend_limit: int | core.IntOut | None = core.arg(default=None)

        usage_report_s3_bucket: str | core.StringOut | None = core.arg(default=None)
