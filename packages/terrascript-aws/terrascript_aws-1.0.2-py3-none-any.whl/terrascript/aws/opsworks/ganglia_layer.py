import terrascript.core as core


@core.schema
class LogStreams(core.Schema):

    batch_count: int | core.IntOut | None = core.attr(int, default=None)

    batch_size: int | core.IntOut | None = core.attr(int, default=None)

    buffer_duration: int | core.IntOut | None = core.attr(int, default=None)

    datetime_format: str | core.StringOut | None = core.attr(str, default=None)

    encoding: str | core.StringOut | None = core.attr(str, default=None)

    file: str | core.StringOut = core.attr(str)

    file_fingerprint_lines: str | core.StringOut | None = core.attr(str, default=None)

    initial_position: str | core.StringOut | None = core.attr(str, default=None)

    log_group_name: str | core.StringOut = core.attr(str)

    multiline_start_pattern: str | core.StringOut | None = core.attr(str, default=None)

    time_zone: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        file: str | core.StringOut,
        log_group_name: str | core.StringOut,
        batch_count: int | core.IntOut | None = None,
        batch_size: int | core.IntOut | None = None,
        buffer_duration: int | core.IntOut | None = None,
        datetime_format: str | core.StringOut | None = None,
        encoding: str | core.StringOut | None = None,
        file_fingerprint_lines: str | core.StringOut | None = None,
        initial_position: str | core.StringOut | None = None,
        multiline_start_pattern: str | core.StringOut | None = None,
        time_zone: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LogStreams.Args(
                file=file,
                log_group_name=log_group_name,
                batch_count=batch_count,
                batch_size=batch_size,
                buffer_duration=buffer_duration,
                datetime_format=datetime_format,
                encoding=encoding,
                file_fingerprint_lines=file_fingerprint_lines,
                initial_position=initial_position,
                multiline_start_pattern=multiline_start_pattern,
                time_zone=time_zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        batch_count: int | core.IntOut | None = core.arg(default=None)

        batch_size: int | core.IntOut | None = core.arg(default=None)

        buffer_duration: int | core.IntOut | None = core.arg(default=None)

        datetime_format: str | core.StringOut | None = core.arg(default=None)

        encoding: str | core.StringOut | None = core.arg(default=None)

        file: str | core.StringOut = core.arg()

        file_fingerprint_lines: str | core.StringOut | None = core.arg(default=None)

        initial_position: str | core.StringOut | None = core.arg(default=None)

        log_group_name: str | core.StringOut = core.arg()

        multiline_start_pattern: str | core.StringOut | None = core.arg(default=None)

        time_zone: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CloudwatchConfiguration(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    log_streams: list[LogStreams] | core.ArrayOut[LogStreams] | None = core.attr(
        LogStreams, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        log_streams: list[LogStreams] | core.ArrayOut[LogStreams] | None = None,
    ):
        super().__init__(
            args=CloudwatchConfiguration.Args(
                enabled=enabled,
                log_streams=log_streams,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        log_streams: list[LogStreams] | core.ArrayOut[LogStreams] | None = core.arg(default=None)


@core.schema
class EbsVolume(core.Schema):

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    iops: int | core.IntOut | None = core.attr(int, default=None)

    mount_point: str | core.StringOut = core.attr(str)

    number_of_disks: int | core.IntOut = core.attr(int)

    raid_level: str | core.StringOut | None = core.attr(str, default=None)

    size: int | core.IntOut = core.attr(int)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        mount_point: str | core.StringOut,
        number_of_disks: int | core.IntOut,
        size: int | core.IntOut,
        encrypted: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        raid_level: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EbsVolume.Args(
                mount_point=mount_point,
                number_of_disks=number_of_disks,
                size=size,
                encrypted=encrypted,
                iops=iops,
                raid_level=raid_level,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        mount_point: str | core.StringOut = core.arg()

        number_of_disks: int | core.IntOut = core.arg()

        raid_level: str | core.StringOut | None = core.arg(default=None)

        size: int | core.IntOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_opsworks_ganglia_layer", namespace="aws_opsworks")
class GangliaLayer(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_assign_elastic_ips: bool | core.BoolOut | None = core.attr(bool, default=None)

    auto_assign_public_ips: bool | core.BoolOut | None = core.attr(bool, default=None)

    auto_healing: bool | core.BoolOut | None = core.attr(bool, default=None)

    cloudwatch_configuration: CloudwatchConfiguration | None = core.attr(
        CloudwatchConfiguration, default=None
    )

    custom_configure_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_deploy_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_instance_profile_arn: str | core.StringOut | None = core.attr(str, default=None)

    custom_json: str | core.StringOut | None = core.attr(str, default=None)

    custom_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_setup_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_shutdown_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_undeploy_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    drain_elb_on_shutdown: bool | core.BoolOut | None = core.attr(bool, default=None)

    ebs_volume: list[EbsVolume] | core.ArrayOut[EbsVolume] | None = core.attr(
        EbsVolume, default=None, computed=True, kind=core.Kind.array
    )

    elastic_load_balancer: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    install_updates_on_boot: bool | core.BoolOut | None = core.attr(bool, default=None)

    instance_shutdown_timeout: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    password: str | core.StringOut = core.attr(str)

    stack_id: str | core.StringOut = core.attr(str)

    system_packages: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: str | core.StringOut | None = core.attr(str, default=None)

    use_ebs_optimized_instances: bool | core.BoolOut | None = core.attr(bool, default=None)

    username: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        password: str | core.StringOut,
        stack_id: str | core.StringOut,
        auto_assign_elastic_ips: bool | core.BoolOut | None = None,
        auto_assign_public_ips: bool | core.BoolOut | None = None,
        auto_healing: bool | core.BoolOut | None = None,
        cloudwatch_configuration: CloudwatchConfiguration | None = None,
        custom_configure_recipes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        custom_deploy_recipes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        custom_instance_profile_arn: str | core.StringOut | None = None,
        custom_json: str | core.StringOut | None = None,
        custom_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        custom_setup_recipes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        custom_shutdown_recipes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        custom_undeploy_recipes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        drain_elb_on_shutdown: bool | core.BoolOut | None = None,
        ebs_volume: list[EbsVolume] | core.ArrayOut[EbsVolume] | None = None,
        elastic_load_balancer: str | core.StringOut | None = None,
        install_updates_on_boot: bool | core.BoolOut | None = None,
        instance_shutdown_timeout: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
        system_packages: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        url: str | core.StringOut | None = None,
        use_ebs_optimized_instances: bool | core.BoolOut | None = None,
        username: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GangliaLayer.Args(
                password=password,
                stack_id=stack_id,
                auto_assign_elastic_ips=auto_assign_elastic_ips,
                auto_assign_public_ips=auto_assign_public_ips,
                auto_healing=auto_healing,
                cloudwatch_configuration=cloudwatch_configuration,
                custom_configure_recipes=custom_configure_recipes,
                custom_deploy_recipes=custom_deploy_recipes,
                custom_instance_profile_arn=custom_instance_profile_arn,
                custom_json=custom_json,
                custom_security_group_ids=custom_security_group_ids,
                custom_setup_recipes=custom_setup_recipes,
                custom_shutdown_recipes=custom_shutdown_recipes,
                custom_undeploy_recipes=custom_undeploy_recipes,
                drain_elb_on_shutdown=drain_elb_on_shutdown,
                ebs_volume=ebs_volume,
                elastic_load_balancer=elastic_load_balancer,
                install_updates_on_boot=install_updates_on_boot,
                instance_shutdown_timeout=instance_shutdown_timeout,
                name=name,
                system_packages=system_packages,
                tags=tags,
                tags_all=tags_all,
                url=url,
                use_ebs_optimized_instances=use_ebs_optimized_instances,
                username=username,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_assign_elastic_ips: bool | core.BoolOut | None = core.arg(default=None)

        auto_assign_public_ips: bool | core.BoolOut | None = core.arg(default=None)

        auto_healing: bool | core.BoolOut | None = core.arg(default=None)

        cloudwatch_configuration: CloudwatchConfiguration | None = core.arg(default=None)

        custom_configure_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        custom_deploy_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        custom_instance_profile_arn: str | core.StringOut | None = core.arg(default=None)

        custom_json: str | core.StringOut | None = core.arg(default=None)

        custom_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        custom_setup_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        custom_shutdown_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        custom_undeploy_recipes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        drain_elb_on_shutdown: bool | core.BoolOut | None = core.arg(default=None)

        ebs_volume: list[EbsVolume] | core.ArrayOut[EbsVolume] | None = core.arg(default=None)

        elastic_load_balancer: str | core.StringOut | None = core.arg(default=None)

        install_updates_on_boot: bool | core.BoolOut | None = core.arg(default=None)

        instance_shutdown_timeout: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        password: str | core.StringOut = core.arg()

        stack_id: str | core.StringOut = core.arg()

        system_packages: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        url: str | core.StringOut | None = core.arg(default=None)

        use_ebs_optimized_instances: bool | core.BoolOut | None = core.arg(default=None)

        username: str | core.StringOut | None = core.arg(default=None)
