import terrascript.core as core


@core.schema
class ReportSetting(core.Schema):

    framework_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    number_of_frameworks: int | core.IntOut | None = core.attr(int, default=None)

    report_template: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        report_template: str | core.StringOut,
        framework_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        number_of_frameworks: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ReportSetting.Args(
                report_template=report_template,
                framework_arns=framework_arns,
                number_of_frameworks=number_of_frameworks,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        framework_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        number_of_frameworks: int | core.IntOut | None = core.arg(default=None)

        report_template: str | core.StringOut = core.arg()


@core.schema
class ReportDeliveryChannel(core.Schema):

    formats: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    s3_bucket_name: str | core.StringOut = core.attr(str)

    s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_bucket_name: str | core.StringOut,
        formats: list[str] | core.ArrayOut[core.StringOut] | None = None,
        s3_key_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ReportDeliveryChannel.Args(
                s3_bucket_name=s3_bucket_name,
                formats=formats,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        formats: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        s3_bucket_name: str | core.StringOut = core.arg()

        s3_key_prefix: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_backup_report_plan", namespace="backup")
class ReportPlan(core.Resource):
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
    (Optional) The description of the report plan with a maximum of 1,024 characters
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The id of the backup report plan.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The unique name of the report plan. The name must be between 1 and 256 characters, starti
    ng with a letter, and consisting of letters, numbers, and underscores.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) An object that contains information about where and how to deliver your reports, specific
    ally your Amazon S3 bucket name, S3 key prefix, and the formats of your reports. Detailed below.
    """
    report_delivery_channel: ReportDeliveryChannel = core.attr(ReportDeliveryChannel)

    """
    (Required) An object that identifies the report template for the report. Reports are built using a r
    eport template. Detailed below.
    """
    report_setting: ReportSetting = core.attr(ReportSetting)

    """
    (Optional) Metadata that you can assign to help organize the report plans you create. If configured
    with a provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashico
    rp/aws/latest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite
    those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        report_delivery_channel: ReportDeliveryChannel,
        report_setting: ReportSetting,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReportPlan.Args(
                name=name,
                report_delivery_channel=report_delivery_channel,
                report_setting=report_setting,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        report_delivery_channel: ReportDeliveryChannel = core.arg()

        report_setting: ReportSetting = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
