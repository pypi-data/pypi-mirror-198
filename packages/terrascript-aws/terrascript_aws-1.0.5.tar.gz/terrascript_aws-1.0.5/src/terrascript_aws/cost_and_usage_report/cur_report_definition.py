import terrascript.core as core


@core.resource(type="aws_cur_report_definition", namespace="cost_and_usage_report")
class CurReportDefinition(core.Resource):
    """
    (Required) A list of additional artifacts. Valid values are: `REDSHIFT`, `QUICKSIGHT`, `ATHENA`. Whe
    n ATHENA exists within additional_artifacts, no other artifact type can be declared and report_versi
    oning must be `OVERWRITE_REPORT`.
    """

    additional_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) A list of schema elements. Valid values are: `RESOURCES`.
    """
    additional_schema_elements: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    The Amazon Resource Name (ARN) specifying the cur report.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Compression format for report. Valid values are: `GZIP`, `ZIP`, `Parquet`. If `Parquet` i
    s used, then format must also be `Parquet`.
    """
    compression: str | core.StringOut = core.attr(str)

    """
    (Required) Format for report. Valid values are: `textORcsv`, `Parquet`. If `Parquet` is used, then C
    ompression must also be `Parquet`.
    """
    format: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set to true to update your reports after they have been finalized if AWS detects charges
    related to previous months.
    """
    refresh_closed_reports: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Unique name for the report. Must start with a number/letter and is case sensitive. Limite
    d to 256 characters.
    """
    report_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Overwrite the previous version of each report or to deliver the report in addition to the
    previous versions. Valid values are: `CREATE_NEW_REPORT` and `OVERWRITE_REPORT`.
    """
    report_versioning: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name of the existing S3 bucket to hold generated reports.
    """
    s3_bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) Report path prefix. Limited to 256 characters.
    """
    s3_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Region of the existing S3 bucket to hold generated reports.
    """
    s3_region: str | core.StringOut = core.attr(str)

    """
    (Required) The frequency on which report data are measured and displayed.  Valid values are: `HOURLY
    , `DAILY`.
    """
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
