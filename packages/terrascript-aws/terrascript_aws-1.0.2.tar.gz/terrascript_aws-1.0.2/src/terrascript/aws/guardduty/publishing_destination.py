import terrascript.core as core


@core.resource(type="aws_guardduty_publishing_destination", namespace="aws_guardduty")
class PublishingDestination(core.Resource):

    destination_arn: str | core.StringOut = core.attr(str)

    destination_type: str | core.StringOut | None = core.attr(str, default=None)

    detector_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
