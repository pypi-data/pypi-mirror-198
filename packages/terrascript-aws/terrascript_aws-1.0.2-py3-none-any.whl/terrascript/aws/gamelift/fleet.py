import terrascript.core as core


@core.schema
class Ec2InboundPermission(core.Schema):

    from_port: int | core.IntOut = core.attr(int)

    ip_range: str | core.StringOut = core.attr(str)

    protocol: str | core.StringOut = core.attr(str)

    to_port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut,
        ip_range: str | core.StringOut,
        protocol: str | core.StringOut,
        to_port: int | core.IntOut,
    ):
        super().__init__(
            args=Ec2InboundPermission.Args(
                from_port=from_port,
                ip_range=ip_range,
                protocol=protocol,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: int | core.IntOut = core.arg()

        ip_range: str | core.StringOut = core.arg()

        protocol: str | core.StringOut = core.arg()

        to_port: int | core.IntOut = core.arg()


@core.schema
class ResourceCreationLimitPolicy(core.Schema):

    new_game_sessions_per_creator: int | core.IntOut | None = core.attr(int, default=None)

    policy_period_in_minutes: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        new_game_sessions_per_creator: int | core.IntOut | None = None,
        policy_period_in_minutes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ResourceCreationLimitPolicy.Args(
                new_game_sessions_per_creator=new_game_sessions_per_creator,
                policy_period_in_minutes=policy_period_in_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        new_game_sessions_per_creator: int | core.IntOut | None = core.arg(default=None)

        policy_period_in_minutes: int | core.IntOut | None = core.arg(default=None)


@core.schema
class CertificateConfiguration(core.Schema):

    certificate_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        certificate_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CertificateConfiguration.Args(
                certificate_type=certificate_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ServerProcess(core.Schema):

    concurrent_executions: int | core.IntOut = core.attr(int)

    launch_path: str | core.StringOut = core.attr(str)

    parameters: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        concurrent_executions: int | core.IntOut,
        launch_path: str | core.StringOut,
        parameters: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ServerProcess.Args(
                concurrent_executions=concurrent_executions,
                launch_path=launch_path,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        concurrent_executions: int | core.IntOut = core.arg()

        launch_path: str | core.StringOut = core.arg()

        parameters: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RuntimeConfiguration(core.Schema):

    game_session_activation_timeout_seconds: int | core.IntOut | None = core.attr(int, default=None)

    max_concurrent_game_session_activations: int | core.IntOut | None = core.attr(int, default=None)

    server_process: list[ServerProcess] | core.ArrayOut[ServerProcess] | None = core.attr(
        ServerProcess, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        game_session_activation_timeout_seconds: int | core.IntOut | None = None,
        max_concurrent_game_session_activations: int | core.IntOut | None = None,
        server_process: list[ServerProcess] | core.ArrayOut[ServerProcess] | None = None,
    ):
        super().__init__(
            args=RuntimeConfiguration.Args(
                game_session_activation_timeout_seconds=game_session_activation_timeout_seconds,
                max_concurrent_game_session_activations=max_concurrent_game_session_activations,
                server_process=server_process,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        game_session_activation_timeout_seconds: int | core.IntOut | None = core.arg(default=None)

        max_concurrent_game_session_activations: int | core.IntOut | None = core.arg(default=None)

        server_process: list[ServerProcess] | core.ArrayOut[ServerProcess] | None = core.arg(
            default=None
        )


@core.resource(type="aws_gamelift_fleet", namespace="aws_gamelift")
class Fleet(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    build_arn: str | core.StringOut = core.attr(str, computed=True)

    build_id: str | core.StringOut | None = core.attr(str, default=None)

    certificate_configuration: CertificateConfiguration | None = core.attr(
        CertificateConfiguration, default=None, computed=True
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    ec2_inbound_permission: list[Ec2InboundPermission] | core.ArrayOut[
        Ec2InboundPermission
    ] | None = core.attr(Ec2InboundPermission, default=None, computed=True, kind=core.Kind.array)

    ec2_instance_type: str | core.StringOut = core.attr(str)

    fleet_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    log_paths: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    metric_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    new_game_session_protection_policy: str | core.StringOut | None = core.attr(str, default=None)

    operating_system: str | core.StringOut = core.attr(str, computed=True)

    resource_creation_limit_policy: ResourceCreationLimitPolicy | None = core.attr(
        ResourceCreationLimitPolicy, default=None
    )

    runtime_configuration: RuntimeConfiguration | None = core.attr(
        RuntimeConfiguration, default=None
    )

    script_arn: str | core.StringOut = core.attr(str, computed=True)

    script_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        ec2_instance_type: str | core.StringOut,
        name: str | core.StringOut,
        build_id: str | core.StringOut | None = None,
        certificate_configuration: CertificateConfiguration | None = None,
        description: str | core.StringOut | None = None,
        ec2_inbound_permission: list[Ec2InboundPermission]
        | core.ArrayOut[Ec2InboundPermission]
        | None = None,
        fleet_type: str | core.StringOut | None = None,
        instance_role_arn: str | core.StringOut | None = None,
        metric_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        new_game_session_protection_policy: str | core.StringOut | None = None,
        resource_creation_limit_policy: ResourceCreationLimitPolicy | None = None,
        runtime_configuration: RuntimeConfiguration | None = None,
        script_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Fleet.Args(
                ec2_instance_type=ec2_instance_type,
                name=name,
                build_id=build_id,
                certificate_configuration=certificate_configuration,
                description=description,
                ec2_inbound_permission=ec2_inbound_permission,
                fleet_type=fleet_type,
                instance_role_arn=instance_role_arn,
                metric_groups=metric_groups,
                new_game_session_protection_policy=new_game_session_protection_policy,
                resource_creation_limit_policy=resource_creation_limit_policy,
                runtime_configuration=runtime_configuration,
                script_id=script_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        build_id: str | core.StringOut | None = core.arg(default=None)

        certificate_configuration: CertificateConfiguration | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        ec2_inbound_permission: list[Ec2InboundPermission] | core.ArrayOut[
            Ec2InboundPermission
        ] | None = core.arg(default=None)

        ec2_instance_type: str | core.StringOut = core.arg()

        fleet_type: str | core.StringOut | None = core.arg(default=None)

        instance_role_arn: str | core.StringOut | None = core.arg(default=None)

        metric_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        new_game_session_protection_policy: str | core.StringOut | None = core.arg(default=None)

        resource_creation_limit_policy: ResourceCreationLimitPolicy | None = core.arg(default=None)

        runtime_configuration: RuntimeConfiguration | None = core.arg(default=None)

        script_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
