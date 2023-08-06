import terrascript.core as core


@core.schema
class ProxyConfiguration(core.Schema):

    container_name: str | core.StringOut = core.attr(str)

    properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        container_name: str | core.StringOut,
        properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProxyConfiguration.Args(
                container_name=container_name,
                properties=properties,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: str | core.StringOut = core.arg()

        properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EphemeralStorage(core.Schema):

    size_in_gib: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        size_in_gib: int | core.IntOut,
    ):
        super().__init__(
            args=EphemeralStorage.Args(
                size_in_gib=size_in_gib,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        size_in_gib: int | core.IntOut = core.arg()


@core.schema
class RuntimePlatform(core.Schema):

    cpu_architecture: str | core.StringOut | None = core.attr(str, default=None)

    operating_system_family: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cpu_architecture: str | core.StringOut | None = None,
        operating_system_family: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RuntimePlatform.Args(
                cpu_architecture=cpu_architecture,
                operating_system_family=operating_system_family,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_architecture: str | core.StringOut | None = core.arg(default=None)

        operating_system_family: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InferenceAccelerator(core.Schema):

    device_name: str | core.StringOut = core.attr(str)

    device_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        device_type: str | core.StringOut,
    ):
        super().__init__(
            args=InferenceAccelerator.Args(
                device_name=device_name,
                device_type=device_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        device_type: str | core.StringOut = core.arg()


@core.schema
class DockerVolumeConfiguration(core.Schema):

    autoprovision: bool | core.BoolOut | None = core.attr(bool, default=None)

    driver: str | core.StringOut | None = core.attr(str, default=None)

    driver_opts: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    labels: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    scope: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        autoprovision: bool | core.BoolOut | None = None,
        driver: str | core.StringOut | None = None,
        driver_opts: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        labels: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        scope: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DockerVolumeConfiguration.Args(
                autoprovision=autoprovision,
                driver=driver,
                driver_opts=driver_opts,
                labels=labels,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        autoprovision: bool | core.BoolOut | None = core.arg(default=None)

        driver: str | core.StringOut | None = core.arg(default=None)

        driver_opts: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        labels: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        scope: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EfsVolumeConfigurationAuthorizationConfig(core.Schema):

    access_point_id: str | core.StringOut | None = core.attr(str, default=None)

    iam: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_point_id: str | core.StringOut | None = None,
        iam: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EfsVolumeConfigurationAuthorizationConfig.Args(
                access_point_id=access_point_id,
                iam=iam,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_point_id: str | core.StringOut | None = core.arg(default=None)

        iam: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EfsVolumeConfiguration(core.Schema):

    authorization_config: EfsVolumeConfigurationAuthorizationConfig | None = core.attr(
        EfsVolumeConfigurationAuthorizationConfig, default=None
    )

    file_system_id: str | core.StringOut = core.attr(str)

    root_directory: str | core.StringOut | None = core.attr(str, default=None)

    transit_encryption: str | core.StringOut | None = core.attr(str, default=None)

    transit_encryption_port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        file_system_id: str | core.StringOut,
        authorization_config: EfsVolumeConfigurationAuthorizationConfig | None = None,
        root_directory: str | core.StringOut | None = None,
        transit_encryption: str | core.StringOut | None = None,
        transit_encryption_port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=EfsVolumeConfiguration.Args(
                file_system_id=file_system_id,
                authorization_config=authorization_config,
                root_directory=root_directory,
                transit_encryption=transit_encryption,
                transit_encryption_port=transit_encryption_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_config: EfsVolumeConfigurationAuthorizationConfig | None = core.arg(
            default=None
        )

        file_system_id: str | core.StringOut = core.arg()

        root_directory: str | core.StringOut | None = core.arg(default=None)

        transit_encryption: str | core.StringOut | None = core.arg(default=None)

        transit_encryption_port: int | core.IntOut | None = core.arg(default=None)


@core.schema
class FsxWindowsFileServerVolumeConfigurationAuthorizationConfig(core.Schema):

    credentials_parameter: str | core.StringOut = core.attr(str)

    domain: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        credentials_parameter: str | core.StringOut,
        domain: str | core.StringOut,
    ):
        super().__init__(
            args=FsxWindowsFileServerVolumeConfigurationAuthorizationConfig.Args(
                credentials_parameter=credentials_parameter,
                domain=domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credentials_parameter: str | core.StringOut = core.arg()

        domain: str | core.StringOut = core.arg()


@core.schema
class FsxWindowsFileServerVolumeConfiguration(core.Schema):

    authorization_config: FsxWindowsFileServerVolumeConfigurationAuthorizationConfig = core.attr(
        FsxWindowsFileServerVolumeConfigurationAuthorizationConfig
    )

    file_system_id: str | core.StringOut = core.attr(str)

    root_directory: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        authorization_config: FsxWindowsFileServerVolumeConfigurationAuthorizationConfig,
        file_system_id: str | core.StringOut,
        root_directory: str | core.StringOut,
    ):
        super().__init__(
            args=FsxWindowsFileServerVolumeConfiguration.Args(
                authorization_config=authorization_config,
                file_system_id=file_system_id,
                root_directory=root_directory,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_config: FsxWindowsFileServerVolumeConfigurationAuthorizationConfig = (
            core.arg()
        )

        file_system_id: str | core.StringOut = core.arg()

        root_directory: str | core.StringOut = core.arg()


@core.schema
class Volume(core.Schema):

    docker_volume_configuration: DockerVolumeConfiguration | None = core.attr(
        DockerVolumeConfiguration, default=None
    )

    efs_volume_configuration: EfsVolumeConfiguration | None = core.attr(
        EfsVolumeConfiguration, default=None
    )

    fsx_windows_file_server_volume_configuration: FsxWindowsFileServerVolumeConfiguration | None = (
        core.attr(FsxWindowsFileServerVolumeConfiguration, default=None)
    )

    host_path: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        docker_volume_configuration: DockerVolumeConfiguration | None = None,
        efs_volume_configuration: EfsVolumeConfiguration | None = None,
        fsx_windows_file_server_volume_configuration: FsxWindowsFileServerVolumeConfiguration
        | None = None,
        host_path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Volume.Args(
                name=name,
                docker_volume_configuration=docker_volume_configuration,
                efs_volume_configuration=efs_volume_configuration,
                fsx_windows_file_server_volume_configuration=fsx_windows_file_server_volume_configuration,
                host_path=host_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        docker_volume_configuration: DockerVolumeConfiguration | None = core.arg(default=None)

        efs_volume_configuration: EfsVolumeConfiguration | None = core.arg(default=None)

        fsx_windows_file_server_volume_configuration: FsxWindowsFileServerVolumeConfiguration | None = core.arg(
            default=None
        )

        host_path: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()


@core.schema
class PlacementConstraints(core.Schema):

    expression: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        expression: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PlacementConstraints.Args(
                type=type,
                expression=expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        expression: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_ecs_task_definition", namespace="ecs")
class TaskDefinition(core.Resource):
    """
    Full ARN of the Task Definition (including both `family` and `revision`).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A list of valid [container definitions](http://docs.aws.amazon.com/AmazonECS/latest/APIRe
    ference/API_ContainerDefinition.html) provided as a single valid JSON document. Please note that you
    should only provide values that are part of the container definition document. For a detailed descr
    iption of what parameters are available, see the [Task Definition Parameters](https://docs.aws.amazo
    n.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the official [De
    veloper Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
    """
    container_definitions: str | core.StringOut = core.attr(str)

    """
    (Optional) Number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this
    field is required.
    """
    cpu: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional)  The amount of ephemeral storage to allocate for the task. This parameter is used to expa
    nd the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on A
    WS Fargate. See [Ephemeral Storage](#ephemeral_storage).
    """
    ephemeral_storage: EphemeralStorage | None = core.attr(EphemeralStorage, default=None)

    """
    (Optional) ARN of the task execution role that the Amazon ECS container agent and the Docker daemon
    can assume.
    """
    execution_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A unique name for your task definition.
    """
    family: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block(s) with Inference Accelerators settings. [Detailed below.](#inference
    _accelerator)
    """
    inference_accelerator: list[InferenceAccelerator] | core.ArrayOut[
        InferenceAccelerator
    ] | None = core.attr(InferenceAccelerator, default=None, kind=core.Kind.array)

    """
    (Optional) IPC resource namespace to be used for the containers in the task The valid values are `ho
    st`, `task`, and `none`.
    """
    ipc_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE
    this field is required.
    """
    memory: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Docker networking mode to use for the containers in the task. Valid values are `none`, `b
    ridge`, `awsvpc`, and `host`.
    """
    network_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Process namespace to use for the containers in the task. The valid values are `host` and
    task`.
    """
    pid_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block for rules that are taken into consideration during task placement. Ma
    ximum number of `placement_constraints` is `10`. [Detailed below](#placement_constraints).
    """
    placement_constraints: list[PlacementConstraints] | core.ArrayOut[
        PlacementConstraints
    ] | None = core.attr(PlacementConstraints, default=None, kind=core.Kind.array)

    """
    (Optional) Configuration block for the App Mesh proxy. [Detailed below.](#proxy_configuration)
    """
    proxy_configuration: ProxyConfiguration | None = core.attr(ProxyConfiguration, default=None)

    """
    (Optional) Set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
    """
    requires_compatibilities: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Revision of the task in a particular family.
    """
    revision: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Configuration block for [runtime_platform](#runtime_platform) that containers in your tas
    k may use.
    """
    runtime_platform: RuntimePlatform | None = core.attr(RuntimePlatform, default=None)

    skip_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Optional) ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS ser
    vices.
    """
    task_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block for [volumes](#volume) that containers in your task may use. Detailed
    below.
    """
    volume: list[Volume] | core.ArrayOut[Volume] | None = core.attr(
        Volume, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        container_definitions: str | core.StringOut,
        family: str | core.StringOut,
        cpu: str | core.StringOut | None = None,
        ephemeral_storage: EphemeralStorage | None = None,
        execution_role_arn: str | core.StringOut | None = None,
        inference_accelerator: list[InferenceAccelerator]
        | core.ArrayOut[InferenceAccelerator]
        | None = None,
        ipc_mode: str | core.StringOut | None = None,
        memory: str | core.StringOut | None = None,
        network_mode: str | core.StringOut | None = None,
        pid_mode: str | core.StringOut | None = None,
        placement_constraints: list[PlacementConstraints]
        | core.ArrayOut[PlacementConstraints]
        | None = None,
        proxy_configuration: ProxyConfiguration | None = None,
        requires_compatibilities: list[str] | core.ArrayOut[core.StringOut] | None = None,
        runtime_platform: RuntimePlatform | None = None,
        skip_destroy: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        task_role_arn: str | core.StringOut | None = None,
        volume: list[Volume] | core.ArrayOut[Volume] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TaskDefinition.Args(
                container_definitions=container_definitions,
                family=family,
                cpu=cpu,
                ephemeral_storage=ephemeral_storage,
                execution_role_arn=execution_role_arn,
                inference_accelerator=inference_accelerator,
                ipc_mode=ipc_mode,
                memory=memory,
                network_mode=network_mode,
                pid_mode=pid_mode,
                placement_constraints=placement_constraints,
                proxy_configuration=proxy_configuration,
                requires_compatibilities=requires_compatibilities,
                runtime_platform=runtime_platform,
                skip_destroy=skip_destroy,
                tags=tags,
                tags_all=tags_all,
                task_role_arn=task_role_arn,
                volume=volume,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_definitions: str | core.StringOut = core.arg()

        cpu: str | core.StringOut | None = core.arg(default=None)

        ephemeral_storage: EphemeralStorage | None = core.arg(default=None)

        execution_role_arn: str | core.StringOut | None = core.arg(default=None)

        family: str | core.StringOut = core.arg()

        inference_accelerator: list[InferenceAccelerator] | core.ArrayOut[
            InferenceAccelerator
        ] | None = core.arg(default=None)

        ipc_mode: str | core.StringOut | None = core.arg(default=None)

        memory: str | core.StringOut | None = core.arg(default=None)

        network_mode: str | core.StringOut | None = core.arg(default=None)

        pid_mode: str | core.StringOut | None = core.arg(default=None)

        placement_constraints: list[PlacementConstraints] | core.ArrayOut[
            PlacementConstraints
        ] | None = core.arg(default=None)

        proxy_configuration: ProxyConfiguration | None = core.arg(default=None)

        requires_compatibilities: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        runtime_platform: RuntimePlatform | None = core.arg(default=None)

        skip_destroy: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        task_role_arn: str | core.StringOut | None = core.arg(default=None)

        volume: list[Volume] | core.ArrayOut[Volume] | None = core.arg(default=None)
