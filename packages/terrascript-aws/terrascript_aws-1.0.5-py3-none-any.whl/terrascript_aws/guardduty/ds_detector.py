import terrascript.core as core


@core.data(type="aws_guardduty_detector", namespace="guardduty")
class DsDetector(core.Data):
    """
    The frequency of notifications sent about subsequent finding occurrences.
    """

    finding_publishing_frequency: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the detector.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The service-linked role that grants GuardDuty access to the resources in the AWS account.
    """
    service_role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The current status of the detector.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDetector.Args(
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)
