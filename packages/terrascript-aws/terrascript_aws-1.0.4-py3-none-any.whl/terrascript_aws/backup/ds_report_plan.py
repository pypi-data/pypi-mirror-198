import terrascript.core as core


@core.schema
class ReportDeliveryChannel(core.Schema):

    formats: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    s3_bucket_name: str | core.StringOut = core.attr(str, computed=True)

    s3_key_prefix: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        formats: list[str] | core.ArrayOut[core.StringOut],
        s3_bucket_name: str | core.StringOut,
        s3_key_prefix: str | core.StringOut,
    ):
        super().__init__(
            args=ReportDeliveryChannel.Args(
                formats=formats,
                s3_bucket_name=s3_bucket_name,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        formats: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        s3_bucket_name: str | core.StringOut = core.arg()

        s3_key_prefix: str | core.StringOut = core.arg()


@core.schema
class ReportSetting(core.Schema):

    framework_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    number_of_frameworks: int | core.IntOut = core.attr(int, computed=True)

    report_template: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        framework_arns: list[str] | core.ArrayOut[core.StringOut],
        number_of_frameworks: int | core.IntOut,
        report_template: str | core.StringOut,
    ):
        super().__init__(
            args=ReportSetting.Args(
                framework_arns=framework_arns,
                number_of_frameworks=number_of_frameworks,
                report_template=report_template,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        framework_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        number_of_frameworks: int | core.IntOut = core.arg()

        report_template: str | core.StringOut = core.arg()


@core.data(type="aws_backup_report_plan", namespace="backup")
class DsReportPlan(core.Data):
    """
    The ARN of the backup report plan.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time that a report plan is created, in Unix format and Coordinated Universal Time (UTC)
    .
    """
    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The deployment status of a report plan. The statuses are: `CREATE_IN_PROGRESS` | `UPDATE_IN_PROGRESS
    | `DELETE_IN_PROGRESS` | `COMPLETED`.
    """
    deployment_status: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the report plan.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The id of the report plan.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The backup report plan name.
    """
    name: str | core.StringOut = core.attr(str)

    """
    An object that contains information about where and how to deliver your reports, specifically your A
    mazon S3 bucket name, S3 key prefix, and the formats of your reports. Detailed below.
    """
    report_delivery_channel: list[ReportDeliveryChannel] | core.ArrayOut[
        ReportDeliveryChannel
    ] = core.attr(ReportDeliveryChannel, computed=True, kind=core.Kind.array)

    """
    An object that identifies the report template for the report. Reports are built using a report templ
    ate. Detailed below.
    """
    report_setting: list[ReportSetting] | core.ArrayOut[ReportSetting] = core.attr(
        ReportSetting, computed=True, kind=core.Kind.array
    )

    """
    Metadata that you can assign to help organize the report plans you create.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsReportPlan.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
