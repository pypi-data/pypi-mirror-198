import terrascript.core as core


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


@core.resource(type="aws_opsworks_java_app_layer", namespace="opsworks")
class JavaAppLayer(core.Resource):
    """
    (Optional) Keyword for the application container to use. Defaults to "tomcat".
    """

    app_server: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Version of the selected application container to use. Defaults to "7".
    """
    app_server_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name(ARN) of the layer.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to automatically assign an elastic IP address to the layer's instances.
    """
    auto_assign_elastic_ips: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) For stacks belonging to a VPC, whether to automatically assign a public IP address to eac
    h of the layer's instances.
    """
    auto_assign_public_ips: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether to enable auto-healing for the layer.
    """
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

    """
    (Optional) The ARN of an IAM profile that will be used for the layer's instances.
    """
    custom_instance_profile_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Custom JSON attributes to apply to the layer.
    """
    custom_json: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Ids for a set of security groups to apply to the layer's instances.
    """
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

    """
    (Optional) Whether to enable Elastic Load Balancing connection draining.
    """
    drain_elb_on_shutdown: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) `ebs_volume` blocks, as described below, will each create an EBS volume and connect it to
    the layer's instances.
    """
    ebs_volume: list[EbsVolume] | core.ArrayOut[EbsVolume] | None = core.attr(
        EbsVolume, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Name of an Elastic Load Balancer to attach to this layer
    """
    elastic_load_balancer: str | core.StringOut | None = core.attr(str, default=None)

    """
    The id of the layer.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to install OS and package updates on each instance when it boots.
    """
    install_updates_on_boot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the S
    hutdown event.
    """
    instance_shutdown_timeout: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Options to set for the JVM.
    """
    jvm_options: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Keyword for the type of JVM to use. Defaults to `openjdk`.
    """
    jvm_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Version of JVM to use. Defaults to "7".
    """
    jvm_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A human-readable name for the layer.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The id of the stack the layer will belong to.
    """
    stack_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Names of a set of system packages to install on the layer's instances.
    """
    system_packages: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
    (Optional) Whether to use EBS-optimized instances.
    """
    use_ebs_optimized_instances: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        stack_id: str | core.StringOut,
        app_server: str | core.StringOut | None = None,
        app_server_version: str | core.StringOut | None = None,
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
        jvm_options: str | core.StringOut | None = None,
        jvm_type: str | core.StringOut | None = None,
        jvm_version: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        system_packages: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        use_ebs_optimized_instances: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=JavaAppLayer.Args(
                stack_id=stack_id,
                app_server=app_server,
                app_server_version=app_server_version,
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
                jvm_options=jvm_options,
                jvm_type=jvm_type,
                jvm_version=jvm_version,
                name=name,
                system_packages=system_packages,
                tags=tags,
                tags_all=tags_all,
                use_ebs_optimized_instances=use_ebs_optimized_instances,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_server: str | core.StringOut | None = core.arg(default=None)

        app_server_version: str | core.StringOut | None = core.arg(default=None)

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

        jvm_options: str | core.StringOut | None = core.arg(default=None)

        jvm_type: str | core.StringOut | None = core.arg(default=None)

        jvm_version: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        stack_id: str | core.StringOut = core.arg()

        system_packages: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        use_ebs_optimized_instances: bool | core.BoolOut | None = core.arg(default=None)
