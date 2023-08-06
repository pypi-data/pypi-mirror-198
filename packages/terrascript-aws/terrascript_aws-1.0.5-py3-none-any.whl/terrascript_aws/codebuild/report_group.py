import terrascript.core as core


@core.schema
class S3Destination(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    encryption_disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    encryption_key: str | core.StringOut = core.attr(str)

    packaging: str | core.StringOut | None = core.attr(str, default=None)

    path: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        encryption_key: str | core.StringOut,
        encryption_disabled: bool | core.BoolOut | None = None,
        packaging: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Destination.Args(
                bucket=bucket,
                encryption_key=encryption_key,
                encryption_disabled=encryption_disabled,
                packaging=packaging,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        encryption_disabled: bool | core.BoolOut | None = core.arg(default=None)

        encryption_key: str | core.StringOut = core.arg()

        packaging: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ExportConfig(core.Schema):

    s3_destination: S3Destination | None = core.attr(S3Destination, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        s3_destination: S3Destination | None = None,
    ):
        super().__init__(
            args=ExportConfig.Args(
                type=type,
                s3_destination=s3_destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_destination: S3Destination | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_codebuild_report_group", namespace="codebuild")
class ReportGroup(core.Resource):
    """
    The ARN of Report Group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time this Report Group was created.
    """
    created: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If `true`, deletes any reports that belong to a report group before deleting the report g
    roup. If `false`, you must delete any reports in the report group before deleting it. Default value
    is `false`.
    """
    delete_reports: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Information about the destination where the raw data of this Report Group is exported. se
    e [Export Config](#export-config) documented below.
    """
    export_config: ExportConfig = core.attr(ExportConfig)

    """
    The ARN of Report Group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of a Report Group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Required) The type of the Report Group. Valid value are `TEST` and `CODE_COVERAGE`.
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        export_config: ExportConfig,
        name: str | core.StringOut,
        type: str | core.StringOut,
        delete_reports: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReportGroup.Args(
                export_config=export_config,
                name=name,
                type=type,
                delete_reports=delete_reports,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delete_reports: bool | core.BoolOut | None = core.arg(default=None)

        export_config: ExportConfig = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
