import terrascript.core as core


@core.data(type="aws_cur_report_definition", namespace="cost_and_usage_report")
class DsCurReportDefinition(core.Data):
    """
    A list of additional artifacts.
    """

    additional_artifacts: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    A list of schema elements.
    """
    additional_schema_elements: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Preferred format for report.
    """
    compression: str | core.StringOut = core.attr(str, computed=True)

    """
    Preferred compression format for report.
    """
    format: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    If true reports are updated after they have been finalized.
    """
    refresh_closed_reports: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) The name of the report definition to match.
    """
    report_name: str | core.StringOut = core.attr(str)

    """
    Overwrite the previous version of each report or to deliver the report in addition to the previous v
    ersions.
    """
    report_versioning: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of customer S3 bucket.
    """
    s3_bucket: str | core.StringOut = core.attr(str, computed=True)

    """
    Preferred report path prefix.
    """
    s3_prefix: str | core.StringOut = core.attr(str, computed=True)

    """
    Region of customer S3 bucket.
    """
    s3_region: str | core.StringOut = core.attr(str, computed=True)

    """
    The frequency on which report data are measured and displayed.
    """
    time_unit: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        report_name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsCurReportDefinition.Args(
                report_name=report_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        report_name: str | core.StringOut = core.arg()
