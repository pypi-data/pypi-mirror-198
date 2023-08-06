import terrascript.core as core


@core.schema
class DestinationOptions(core.Schema):

    file_format: str | core.StringOut | None = core.attr(str, default=None)

    hive_compatible_partitions: bool | core.BoolOut | None = core.attr(bool, default=None)

    per_hour_partition: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        file_format: str | core.StringOut | None = None,
        hive_compatible_partitions: bool | core.BoolOut | None = None,
        per_hour_partition: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=DestinationOptions.Args(
                file_format=file_format,
                hive_compatible_partitions=hive_compatible_partitions,
                per_hour_partition=per_hour_partition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file_format: str | core.StringOut | None = core.arg(default=None)

        hive_compatible_partitions: bool | core.BoolOut | None = core.arg(default=None)

        per_hour_partition: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_flow_log", namespace="aws_vpc")
class FlowLog(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    destination_options: DestinationOptions | None = core.attr(DestinationOptions, default=None)

    eni_id: str | core.StringOut | None = core.attr(str, default=None)

    iam_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    log_destination: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    log_destination_type: str | core.StringOut | None = core.attr(str, default=None)

    log_format: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    log_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    max_aggregation_interval: int | core.IntOut | None = core.attr(int, default=None)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    traffic_type: str | core.StringOut | None = core.attr(str, default=None)

    transit_gateway_attachment_id: str | core.StringOut | None = core.attr(str, default=None)

    transit_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    vpc_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_options: DestinationOptions | None = None,
        eni_id: str | core.StringOut | None = None,
        iam_role_arn: str | core.StringOut | None = None,
        log_destination: str | core.StringOut | None = None,
        log_destination_type: str | core.StringOut | None = None,
        log_format: str | core.StringOut | None = None,
        log_group_name: str | core.StringOut | None = None,
        max_aggregation_interval: int | core.IntOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        traffic_type: str | core.StringOut | None = None,
        transit_gateway_attachment_id: str | core.StringOut | None = None,
        transit_gateway_id: str | core.StringOut | None = None,
        vpc_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FlowLog.Args(
                destination_options=destination_options,
                eni_id=eni_id,
                iam_role_arn=iam_role_arn,
                log_destination=log_destination,
                log_destination_type=log_destination_type,
                log_format=log_format,
                log_group_name=log_group_name,
                max_aggregation_interval=max_aggregation_interval,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                traffic_type=traffic_type,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                transit_gateway_id=transit_gateway_id,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_options: DestinationOptions | None = core.arg(default=None)

        eni_id: str | core.StringOut | None = core.arg(default=None)

        iam_role_arn: str | core.StringOut | None = core.arg(default=None)

        log_destination: str | core.StringOut | None = core.arg(default=None)

        log_destination_type: str | core.StringOut | None = core.arg(default=None)

        log_format: str | core.StringOut | None = core.arg(default=None)

        log_group_name: str | core.StringOut | None = core.arg(default=None)

        max_aggregation_interval: int | core.IntOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        traffic_type: str | core.StringOut | None = core.arg(default=None)

        transit_gateway_attachment_id: str | core.StringOut | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
