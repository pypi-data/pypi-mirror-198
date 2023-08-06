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


@core.data(type="aws_backup_report_plan", namespace="aws_backup")
class DsReportPlan(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    creation_time: str | core.StringOut = core.attr(str, computed=True)

    deployment_status: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    report_delivery_channel: list[ReportDeliveryChannel] | core.ArrayOut[
        ReportDeliveryChannel
    ] = core.attr(ReportDeliveryChannel, computed=True, kind=core.Kind.array)

    report_setting: list[ReportSetting] | core.ArrayOut[ReportSetting] = core.attr(
        ReportSetting, computed=True, kind=core.Kind.array
    )

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
