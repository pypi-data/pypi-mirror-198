import terrascript.core as core


@core.resource(type="aws_cur_report_definition", namespace="aws_cost_and_usage_report")
class CurReportDefinition(core.Resource):

    additional_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    additional_schema_elements: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    compression: str | core.StringOut = core.attr(str)

    format: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    refresh_closed_reports: bool | core.BoolOut | None = core.attr(bool, default=None)

    report_name: str | core.StringOut = core.attr(str)

    report_versioning: str | core.StringOut | None = core.attr(str, default=None)

    s3_bucket: str | core.StringOut = core.attr(str)

    s3_prefix: str | core.StringOut | None = core.attr(str, default=None)

    s3_region: str | core.StringOut = core.attr(str)

    time_unit: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        additional_schema_elements: list[str] | core.ArrayOut[core.StringOut],
        compression: str | core.StringOut,
        format: str | core.StringOut,
        report_name: str | core.StringOut,
        s3_bucket: str | core.StringOut,
        s3_region: str | core.StringOut,
        time_unit: str | core.StringOut,
        additional_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = None,
        refresh_closed_reports: bool | core.BoolOut | None = None,
        report_versioning: str | core.StringOut | None = None,
        s3_prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CurReportDefinition.Args(
                additional_schema_elements=additional_schema_elements,
                compression=compression,
                format=format,
                report_name=report_name,
                s3_bucket=s3_bucket,
                s3_region=s3_region,
                time_unit=time_unit,
                additional_artifacts=additional_artifacts,
                refresh_closed_reports=refresh_closed_reports,
                report_versioning=report_versioning,
                s3_prefix=s3_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        additional_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        additional_schema_elements: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        compression: str | core.StringOut = core.arg()

        format: str | core.StringOut = core.arg()

        refresh_closed_reports: bool | core.BoolOut | None = core.arg(default=None)

        report_name: str | core.StringOut = core.arg()

        report_versioning: str | core.StringOut | None = core.arg(default=None)

        s3_bucket: str | core.StringOut = core.arg()

        s3_prefix: str | core.StringOut | None = core.arg(default=None)

        s3_region: str | core.StringOut = core.arg()

        time_unit: str | core.StringOut = core.arg()
