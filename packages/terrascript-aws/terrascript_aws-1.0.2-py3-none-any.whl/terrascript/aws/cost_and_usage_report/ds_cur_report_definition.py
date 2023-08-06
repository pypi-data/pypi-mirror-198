import terrascript.core as core


@core.data(type="aws_cur_report_definition", namespace="aws_cost_and_usage_report")
class DsCurReportDefinition(core.Data):

    additional_artifacts: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    additional_schema_elements: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    compression: str | core.StringOut = core.attr(str, computed=True)

    format: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    refresh_closed_reports: bool | core.BoolOut = core.attr(bool, computed=True)

    report_name: str | core.StringOut = core.attr(str)

    report_versioning: str | core.StringOut = core.attr(str, computed=True)

    s3_bucket: str | core.StringOut = core.attr(str, computed=True)

    s3_prefix: str | core.StringOut = core.attr(str, computed=True)

    s3_region: str | core.StringOut = core.attr(str, computed=True)

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
