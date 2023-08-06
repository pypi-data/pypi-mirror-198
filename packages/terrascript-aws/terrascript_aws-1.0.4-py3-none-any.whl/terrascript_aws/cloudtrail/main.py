import terrascript.core as core


@core.schema
class FieldSelector(core.Schema):

    ends_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    equals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    field: str | core.StringOut = core.attr(str)

    not_ends_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    not_equals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    not_starts_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    starts_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        field: str | core.StringOut,
        ends_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
        equals: list[str] | core.ArrayOut[core.StringOut] | None = None,
        not_ends_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
        not_equals: list[str] | core.ArrayOut[core.StringOut] | None = None,
        not_starts_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
        starts_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=FieldSelector.Args(
                field=field,
                ends_with=ends_with,
                equals=equals,
                not_ends_with=not_ends_with,
                not_equals=not_equals,
                not_starts_with=not_starts_with,
                starts_with=starts_with,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ends_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        equals: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        field: str | core.StringOut = core.arg()

        not_ends_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        not_equals: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        not_starts_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        starts_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AdvancedEventSelector(core.Schema):

    field_selector: list[FieldSelector] | core.ArrayOut[FieldSelector] = core.attr(
        FieldSelector, kind=core.Kind.array
    )

    name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        field_selector: list[FieldSelector] | core.ArrayOut[FieldSelector],
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AdvancedEventSelector.Args(
                field_selector=field_selector,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_selector: list[FieldSelector] | core.ArrayOut[FieldSelector] = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InsightSelector(core.Schema):

    insight_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        insight_type: str | core.StringOut,
    ):
        super().__init__(
            args=InsightSelector.Args(
                insight_type=insight_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insight_type: str | core.StringOut = core.arg()


@core.schema
class DataResource(core.Schema):

    type: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=DataResource.Args(
                type=type,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class EventSelector(core.Schema):

    data_resource: list[DataResource] | core.ArrayOut[DataResource] | None = core.attr(
        DataResource, default=None, kind=core.Kind.array
    )

    exclude_management_event_sources: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    include_management_events: bool | core.BoolOut | None = core.attr(bool, default=None)

    read_write_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        data_resource: list[DataResource] | core.ArrayOut[DataResource] | None = None,
        exclude_management_event_sources: list[str] | core.ArrayOut[core.StringOut] | None = None,
        include_management_events: bool | core.BoolOut | None = None,
        read_write_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EventSelector.Args(
                data_resource=data_resource,
                exclude_management_event_sources=exclude_management_event_sources,
                include_management_events=include_management_events,
                read_write_type=read_write_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_resource: list[DataResource] | core.ArrayOut[DataResource] | None = core.arg(
            default=None
        )

        exclude_management_event_sources: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        include_management_events: bool | core.BoolOut | None = core.arg(default=None)

        read_write_type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_cloudtrail", namespace="cloudtrail")
class Main(core.Resource):
    """
    (Optional) Specifies an advanced event selector for enabling data event logging. Fields documented b
    elow. Conflicts with `event_selector`.
    """

    advanced_event_selector: list[AdvancedEventSelector] | core.ArrayOut[
        AdvancedEventSelector
    ] | None = core.attr(AdvancedEventSelector, default=None, kind=core.Kind.array)

    """
    ARN of the trail.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Log group name using an ARN that represents the log group to which CloudTrail logs will b
    e delivered. Note that CloudTrail requires the Log Stream wildcard.
    """
    cloud_watch_logs_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Role for the CloudWatch Logs endpoint to assume to write to a user’s log group.
    """
    cloud_watch_logs_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether log file integrity validation is enabled. Defaults to `false`.
    """
    enable_log_file_validation: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enables logging for the trail. Defaults to `true`. Setting this to `false` will pause log
    ging.
    """
    enable_logging: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies an event selector for enabling data event logging. Fields documented below. Ple
    ase note the [CloudTrail limits](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCl
    oudTrail-Limits.html) when configuring these. Conflicts with `advanced_event_selector`.
    """
    event_selector: list[EventSelector] | core.ArrayOut[EventSelector] | None = core.attr(
        EventSelector, default=None, kind=core.Kind.array
    )

    """
    Region in which the trail was created.
    """
    home_region: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the trail.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether the trail is publishing events from global services such as IAM to the log files.
    Defaults to `true`.
    """
    include_global_service_events: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Configuration block for identifying unusual operational activity. See details below.
    """
    insight_selector: list[InsightSelector] | core.ArrayOut[InsightSelector] | None = core.attr(
        InsightSelector, default=None, kind=core.Kind.array
    )

    """
    (Optional) Whether the trail is created in the current region or in all regions. Defaults to `false`
    .
    """
    is_multi_region_trail: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether the trail is an AWS Organizations trail. Organization trails log events for the m
    aster account and all member accounts. Can only be created in the organization master account. Defau
    lts to `false`.
    """
    is_organization_trail: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) KMS key ARN to use to encrypt the logs delivered by CloudTrail.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name of the trail.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Name of the S3 bucket designated for publishing log files.
    """
    s3_bucket_name: str | core.StringOut = core.attr(str)

    """
    (Optional) S3 key prefix that follows the name of the bucket you have designated for log file delive
    ry.
    """
    s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the Amazon SNS topic defined for notification of log file delivery.
    """
    sns_topic_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Map of tags to assign to the trail. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        s3_bucket_name: str | core.StringOut,
        advanced_event_selector: list[AdvancedEventSelector]
        | core.ArrayOut[AdvancedEventSelector]
        | None = None,
        cloud_watch_logs_group_arn: str | core.StringOut | None = None,
        cloud_watch_logs_role_arn: str | core.StringOut | None = None,
        enable_log_file_validation: bool | core.BoolOut | None = None,
        enable_logging: bool | core.BoolOut | None = None,
        event_selector: list[EventSelector] | core.ArrayOut[EventSelector] | None = None,
        include_global_service_events: bool | core.BoolOut | None = None,
        insight_selector: list[InsightSelector] | core.ArrayOut[InsightSelector] | None = None,
        is_multi_region_trail: bool | core.BoolOut | None = None,
        is_organization_trail: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        s3_key_prefix: str | core.StringOut | None = None,
        sns_topic_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                name=name,
                s3_bucket_name=s3_bucket_name,
                advanced_event_selector=advanced_event_selector,
                cloud_watch_logs_group_arn=cloud_watch_logs_group_arn,
                cloud_watch_logs_role_arn=cloud_watch_logs_role_arn,
                enable_log_file_validation=enable_log_file_validation,
                enable_logging=enable_logging,
                event_selector=event_selector,
                include_global_service_events=include_global_service_events,
                insight_selector=insight_selector,
                is_multi_region_trail=is_multi_region_trail,
                is_organization_trail=is_organization_trail,
                kms_key_id=kms_key_id,
                s3_key_prefix=s3_key_prefix,
                sns_topic_name=sns_topic_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        advanced_event_selector: list[AdvancedEventSelector] | core.ArrayOut[
            AdvancedEventSelector
        ] | None = core.arg(default=None)

        cloud_watch_logs_group_arn: str | core.StringOut | None = core.arg(default=None)

        cloud_watch_logs_role_arn: str | core.StringOut | None = core.arg(default=None)

        enable_log_file_validation: bool | core.BoolOut | None = core.arg(default=None)

        enable_logging: bool | core.BoolOut | None = core.arg(default=None)

        event_selector: list[EventSelector] | core.ArrayOut[EventSelector] | None = core.arg(
            default=None
        )

        include_global_service_events: bool | core.BoolOut | None = core.arg(default=None)

        insight_selector: list[InsightSelector] | core.ArrayOut[InsightSelector] | None = core.arg(
            default=None
        )

        is_multi_region_trail: bool | core.BoolOut | None = core.arg(default=None)

        is_organization_trail: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        s3_bucket_name: str | core.StringOut = core.arg()

        s3_key_prefix: str | core.StringOut | None = core.arg(default=None)

        sns_topic_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
