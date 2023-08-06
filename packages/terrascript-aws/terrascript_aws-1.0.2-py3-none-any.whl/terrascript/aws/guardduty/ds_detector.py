import terrascript.core as core


@core.data(type="aws_guardduty_detector", namespace="aws_guardduty")
class DsDetector(core.Data):

    finding_publishing_frequency: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    service_role_arn: str | core.StringOut = core.attr(str, computed=True)

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
