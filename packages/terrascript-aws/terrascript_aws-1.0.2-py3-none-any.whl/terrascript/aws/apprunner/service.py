import terrascript.core as core


@core.schema
class EgressConfiguration(core.Schema):

    egress_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    vpc_connector_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        egress_type: str | core.StringOut | None = None,
        vpc_connector_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EgressConfiguration.Args(
                egress_type=egress_type,
                vpc_connector_arn=vpc_connector_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        egress_type: str | core.StringOut | None = core.arg(default=None)

        vpc_connector_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NetworkConfiguration(core.Schema):

    egress_configuration: EgressConfiguration | None = core.attr(EgressConfiguration, default=None)

    def __init__(
        self,
        *,
        egress_configuration: EgressConfiguration | None = None,
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                egress_configuration=egress_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        egress_configuration: EgressConfiguration | None = core.arg(default=None)


@core.schema
class HealthCheckConfiguration(core.Schema):

    healthy_threshold: int | core.IntOut | None = core.attr(int, default=None)

    interval: int | core.IntOut | None = core.attr(int, default=None)

    path: str | core.StringOut | None = core.attr(str, default=None)

    protocol: str | core.StringOut | None = core.attr(str, default=None)

    timeout: int | core.IntOut | None = core.attr(int, default=None)

    unhealthy_threshold: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        healthy_threshold: int | core.IntOut | None = None,
        interval: int | core.IntOut | None = None,
        path: str | core.StringOut | None = None,
        protocol: str | core.StringOut | None = None,
        timeout: int | core.IntOut | None = None,
        unhealthy_threshold: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=HealthCheckConfiguration.Args(
                healthy_threshold=healthy_threshold,
                interval=interval,
                path=path,
                protocol=protocol,
                timeout=timeout,
                unhealthy_threshold=unhealthy_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        healthy_threshold: int | core.IntOut | None = core.arg(default=None)

        interval: int | core.IntOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        protocol: str | core.StringOut | None = core.arg(default=None)

        timeout: int | core.IntOut | None = core.arg(default=None)

        unhealthy_threshold: int | core.IntOut | None = core.arg(default=None)


@core.schema
class EncryptionConfiguration(core.Schema):

    kms_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        kms_key: str | core.StringOut,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                kms_key=kms_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key: str | core.StringOut = core.arg()


@core.schema
class ObservabilityConfiguration(core.Schema):

    observability_configuration_arn: str | core.StringOut = core.attr(str)

    observability_enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        observability_configuration_arn: str | core.StringOut,
        observability_enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=ObservabilityConfiguration.Args(
                observability_configuration_arn=observability_configuration_arn,
                observability_enabled=observability_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        observability_configuration_arn: str | core.StringOut = core.arg()

        observability_enabled: bool | core.BoolOut = core.arg()


@core.schema
class InstanceConfiguration(core.Schema):

    cpu: str | core.StringOut | None = core.attr(str, default=None)

    instance_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    memory: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cpu: str | core.StringOut | None = None,
        instance_role_arn: str | core.StringOut | None = None,
        memory: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InstanceConfiguration.Args(
                cpu=cpu,
                instance_role_arn=instance_role_arn,
                memory=memory,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu: str | core.StringOut | None = core.arg(default=None)

        instance_role_arn: str | core.StringOut | None = core.arg(default=None)

        memory: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ImageConfiguration(core.Schema):

    port: str | core.StringOut | None = core.attr(str, default=None)

    runtime_environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    start_command: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        port: str | core.StringOut | None = None,
        runtime_environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        start_command: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ImageConfiguration.Args(
                port=port,
                runtime_environment_variables=runtime_environment_variables,
                start_command=start_command,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        port: str | core.StringOut | None = core.arg(default=None)

        runtime_environment_variables: dict[str, str] | core.MapOut[
            core.StringOut
        ] | None = core.arg(default=None)

        start_command: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ImageRepository(core.Schema):

    image_configuration: ImageConfiguration | None = core.attr(ImageConfiguration, default=None)

    image_identifier: str | core.StringOut = core.attr(str)

    image_repository_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        image_identifier: str | core.StringOut,
        image_repository_type: str | core.StringOut,
        image_configuration: ImageConfiguration | None = None,
    ):
        super().__init__(
            args=ImageRepository.Args(
                image_identifier=image_identifier,
                image_repository_type=image_repository_type,
                image_configuration=image_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_configuration: ImageConfiguration | None = core.arg(default=None)

        image_identifier: str | core.StringOut = core.arg()

        image_repository_type: str | core.StringOut = core.arg()


@core.schema
class AuthenticationConfiguration(core.Schema):

    access_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    connection_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_role_arn: str | core.StringOut | None = None,
        connection_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AuthenticationConfiguration.Args(
                access_role_arn=access_role_arn,
                connection_arn=connection_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_role_arn: str | core.StringOut | None = core.arg(default=None)

        connection_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CodeConfigurationValues(core.Schema):

    build_command: str | core.StringOut | None = core.attr(str, default=None)

    port: str | core.StringOut | None = core.attr(str, default=None)

    runtime: str | core.StringOut = core.attr(str)

    runtime_environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    start_command: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        runtime: str | core.StringOut,
        build_command: str | core.StringOut | None = None,
        port: str | core.StringOut | None = None,
        runtime_environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        start_command: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CodeConfigurationValues.Args(
                runtime=runtime,
                build_command=build_command,
                port=port,
                runtime_environment_variables=runtime_environment_variables,
                start_command=start_command,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        build_command: str | core.StringOut | None = core.arg(default=None)

        port: str | core.StringOut | None = core.arg(default=None)

        runtime: str | core.StringOut = core.arg()

        runtime_environment_variables: dict[str, str] | core.MapOut[
            core.StringOut
        ] | None = core.arg(default=None)

        start_command: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CodeConfiguration(core.Schema):

    code_configuration_values: CodeConfigurationValues | None = core.attr(
        CodeConfigurationValues, default=None
    )

    configuration_source: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        configuration_source: str | core.StringOut,
        code_configuration_values: CodeConfigurationValues | None = None,
    ):
        super().__init__(
            args=CodeConfiguration.Args(
                configuration_source=configuration_source,
                code_configuration_values=code_configuration_values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        code_configuration_values: CodeConfigurationValues | None = core.arg(default=None)

        configuration_source: str | core.StringOut = core.arg()


@core.schema
class SourceCodeVersion(core.Schema):

    type: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=SourceCodeVersion.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class CodeRepository(core.Schema):

    code_configuration: CodeConfiguration | None = core.attr(CodeConfiguration, default=None)

    repository_url: str | core.StringOut = core.attr(str)

    source_code_version: SourceCodeVersion = core.attr(SourceCodeVersion)

    def __init__(
        self,
        *,
        repository_url: str | core.StringOut,
        source_code_version: SourceCodeVersion,
        code_configuration: CodeConfiguration | None = None,
    ):
        super().__init__(
            args=CodeRepository.Args(
                repository_url=repository_url,
                source_code_version=source_code_version,
                code_configuration=code_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        code_configuration: CodeConfiguration | None = core.arg(default=None)

        repository_url: str | core.StringOut = core.arg()

        source_code_version: SourceCodeVersion = core.arg()


@core.schema
class SourceConfiguration(core.Schema):

    authentication_configuration: AuthenticationConfiguration | None = core.attr(
        AuthenticationConfiguration, default=None
    )

    auto_deployments_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    code_repository: CodeRepository | None = core.attr(CodeRepository, default=None)

    image_repository: ImageRepository | None = core.attr(ImageRepository, default=None)

    def __init__(
        self,
        *,
        authentication_configuration: AuthenticationConfiguration | None = None,
        auto_deployments_enabled: bool | core.BoolOut | None = None,
        code_repository: CodeRepository | None = None,
        image_repository: ImageRepository | None = None,
    ):
        super().__init__(
            args=SourceConfiguration.Args(
                authentication_configuration=authentication_configuration,
                auto_deployments_enabled=auto_deployments_enabled,
                code_repository=code_repository,
                image_repository=image_repository,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_configuration: AuthenticationConfiguration | None = core.arg(default=None)

        auto_deployments_enabled: bool | core.BoolOut | None = core.arg(default=None)

        code_repository: CodeRepository | None = core.arg(default=None)

        image_repository: ImageRepository | None = core.arg(default=None)


@core.resource(type="aws_apprunner_service", namespace="aws_apprunner")
class Service(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_scaling_configuration_arn: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    encryption_configuration: EncryptionConfiguration | None = core.attr(
        EncryptionConfiguration, default=None
    )

    health_check_configuration: HealthCheckConfiguration | None = core.attr(
        HealthCheckConfiguration, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_configuration: InstanceConfiguration | None = core.attr(
        InstanceConfiguration, default=None, computed=True
    )

    network_configuration: NetworkConfiguration | None = core.attr(
        NetworkConfiguration, default=None, computed=True
    )

    observability_configuration: ObservabilityConfiguration | None = core.attr(
        ObservabilityConfiguration, default=None
    )

    service_id: str | core.StringOut = core.attr(str, computed=True)

    service_name: str | core.StringOut = core.attr(str)

    service_url: str | core.StringOut = core.attr(str, computed=True)

    source_configuration: SourceConfiguration = core.attr(SourceConfiguration)

    status: str | core.StringOut = core.attr(str, computed=True)

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
        service_name: str | core.StringOut,
        source_configuration: SourceConfiguration,
        auto_scaling_configuration_arn: str | core.StringOut | None = None,
        encryption_configuration: EncryptionConfiguration | None = None,
        health_check_configuration: HealthCheckConfiguration | None = None,
        instance_configuration: InstanceConfiguration | None = None,
        network_configuration: NetworkConfiguration | None = None,
        observability_configuration: ObservabilityConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Service.Args(
                service_name=service_name,
                source_configuration=source_configuration,
                auto_scaling_configuration_arn=auto_scaling_configuration_arn,
                encryption_configuration=encryption_configuration,
                health_check_configuration=health_check_configuration,
                instance_configuration=instance_configuration,
                network_configuration=network_configuration,
                observability_configuration=observability_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_scaling_configuration_arn: str | core.StringOut | None = core.arg(default=None)

        encryption_configuration: EncryptionConfiguration | None = core.arg(default=None)

        health_check_configuration: HealthCheckConfiguration | None = core.arg(default=None)

        instance_configuration: InstanceConfiguration | None = core.arg(default=None)

        network_configuration: NetworkConfiguration | None = core.arg(default=None)

        observability_configuration: ObservabilityConfiguration | None = core.arg(default=None)

        service_name: str | core.StringOut = core.arg()

        source_configuration: SourceConfiguration = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
