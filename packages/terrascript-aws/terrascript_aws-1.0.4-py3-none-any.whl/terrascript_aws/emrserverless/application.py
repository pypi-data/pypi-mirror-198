import terrascript.core as core


@core.schema
class NetworkConfiguration(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AutoStartConfiguration(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=AutoStartConfiguration.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class MaximumCapacity(core.Schema):

    cpu: str | core.StringOut = core.attr(str)

    disk: str | core.StringOut | None = core.attr(str, default=None)

    memory: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cpu: str | core.StringOut,
        memory: str | core.StringOut,
        disk: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MaximumCapacity.Args(
                cpu=cpu,
                memory=memory,
                disk=disk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu: str | core.StringOut = core.arg()

        disk: str | core.StringOut | None = core.arg(default=None)

        memory: str | core.StringOut = core.arg()


@core.schema
class AutoStopConfiguration(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    idle_timeout_minutes: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        idle_timeout_minutes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AutoStopConfiguration.Args(
                enabled=enabled,
                idle_timeout_minutes=idle_timeout_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        idle_timeout_minutes: int | core.IntOut | None = core.arg(default=None)


@core.schema
class WorkerConfiguration(core.Schema):

    cpu: str | core.StringOut = core.attr(str)

    disk: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    memory: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cpu: str | core.StringOut,
        memory: str | core.StringOut,
        disk: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=WorkerConfiguration.Args(
                cpu=cpu,
                memory=memory,
                disk=disk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu: str | core.StringOut = core.arg()

        disk: str | core.StringOut | None = core.arg(default=None)

        memory: str | core.StringOut = core.arg()


@core.schema
class InitialCapacityConfig(core.Schema):

    worker_configuration: WorkerConfiguration | None = core.attr(WorkerConfiguration, default=None)

    worker_count: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        worker_count: int | core.IntOut,
        worker_configuration: WorkerConfiguration | None = None,
    ):
        super().__init__(
            args=InitialCapacityConfig.Args(
                worker_count=worker_count,
                worker_configuration=worker_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        worker_configuration: WorkerConfiguration | None = core.arg(default=None)

        worker_count: int | core.IntOut = core.arg()


@core.schema
class InitialCapacity(core.Schema):

    initial_capacity_config: InitialCapacityConfig | None = core.attr(
        InitialCapacityConfig, default=None
    )

    initial_capacity_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        initial_capacity_type: str | core.StringOut,
        initial_capacity_config: InitialCapacityConfig | None = None,
    ):
        super().__init__(
            args=InitialCapacity.Args(
                initial_capacity_type=initial_capacity_type,
                initial_capacity_config=initial_capacity_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        initial_capacity_config: InitialCapacityConfig | None = core.arg(default=None)

        initial_capacity_type: str | core.StringOut = core.arg()


@core.resource(type="aws_emrserverless_application", namespace="emrserverless")
class Application(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_start_configuration: AutoStartConfiguration | None = core.attr(
        AutoStartConfiguration, default=None, computed=True
    )

    auto_stop_configuration: AutoStopConfiguration | None = core.attr(
        AutoStopConfiguration, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    initial_capacity: list[InitialCapacity] | core.ArrayOut[InitialCapacity] | None = core.attr(
        InitialCapacity, default=None, kind=core.Kind.array
    )

    maximum_capacity: MaximumCapacity | None = core.attr(MaximumCapacity, default=None)

    name: str | core.StringOut = core.attr(str)

    network_configuration: NetworkConfiguration | None = core.attr(
        NetworkConfiguration, default=None
    )

    release_label: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        release_label: str | core.StringOut,
        type: str | core.StringOut,
        auto_start_configuration: AutoStartConfiguration | None = None,
        auto_stop_configuration: AutoStopConfiguration | None = None,
        initial_capacity: list[InitialCapacity] | core.ArrayOut[InitialCapacity] | None = None,
        maximum_capacity: MaximumCapacity | None = None,
        network_configuration: NetworkConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                name=name,
                release_label=release_label,
                type=type,
                auto_start_configuration=auto_start_configuration,
                auto_stop_configuration=auto_stop_configuration,
                initial_capacity=initial_capacity,
                maximum_capacity=maximum_capacity,
                network_configuration=network_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_start_configuration: AutoStartConfiguration | None = core.arg(default=None)

        auto_stop_configuration: AutoStopConfiguration | None = core.arg(default=None)

        initial_capacity: list[InitialCapacity] | core.ArrayOut[InitialCapacity] | None = core.arg(
            default=None
        )

        maximum_capacity: MaximumCapacity | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        network_configuration: NetworkConfiguration | None = core.arg(default=None)

        release_label: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
