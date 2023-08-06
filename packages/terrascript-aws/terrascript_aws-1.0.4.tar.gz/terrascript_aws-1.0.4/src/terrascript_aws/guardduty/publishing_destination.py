import terrascript.core as core


@core.resource(type="aws_guardduty_publishing_destination", namespace="guardduty")
class PublishingDestination(core.Resource):
    """
    (Required) The bucket arn and prefix under which the findings get exported. Bucket-ARN is required,
    the prefix is optional and will be `AWSLogs/[Account-ID]/GuardDuty/[Region]/` if not provided
    """

    destination_arn: str | core.StringOut = core.attr(str)

    destination_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The detector ID of the GuardDuty.
    """
    detector_id: str | core.StringOut = core.attr(str)

    """
    The ID of the GuardDuty PublishingDestination and the detector ID. Format: `<DetectorID>:<Publishing
    DestinationID>`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN of the KMS key used to encrypt GuardDuty findings. GuardDuty enforces this to be
    encrypted.
    """
    kms_key_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_arn: str | core.StringOut,
        detector_id: str | core.StringOut,
        kms_key_arn: str | core.StringOut,
        destination_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PublishingDestination.Args(
                destination_arn=destination_arn,
                detector_id=detector_id,
                kms_key_arn=kms_key_arn,
                destination_type=destination_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_arn: str | core.StringOut = core.arg()

        destination_type: str | core.StringOut | None = core.arg(default=None)

        detector_id: str | core.StringOut = core.arg()

        kms_key_arn: str | core.StringOut = core.arg()
