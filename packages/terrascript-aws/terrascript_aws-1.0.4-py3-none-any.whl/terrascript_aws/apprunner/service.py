import terrascript.core as core


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


@core.resource(type="aws_apprunner_service", namespace="apprunner")
class Service(core.Resource):
    """
    ARN of the App Runner service.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of an App Runner automatic scaling configuration resource that you want to associate with your s
    ervice. If not provided, App Runner associates the latest revision of a default auto scaling configu
    ration.
    """
    auto_scaling_configuration_arn: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Forces new resource) An optional custom encryption key that App Runner uses to encrypt the copy of
    your source repository that it maintains and your service logs. By default, App Runner uses an AWS m
    anaged CMK. See [Encryption Configuration](#encryption-configuration) below for more details.
    """
    encryption_configuration: EncryptionConfiguration | None = core.attr(
        EncryptionConfiguration, default=None
    )

    """
    (Forces new resource) Settings of the health check that AWS App Runner performs to monitor the healt
    h of your service. See [Health Check Configuration](#health-check-configuration) below for more deta
    ils.
    """
    health_check_configuration: HealthCheckConfiguration | None = core.attr(
        HealthCheckConfiguration, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The runtime configuration of instances (scaling units) of the App Runner service. See [Instance Conf
    iguration](#instance-configuration) below for more details.
    """
    instance_configuration: InstanceConfiguration | None = core.attr(
        InstanceConfiguration, default=None, computed=True
    )

    """
    Configuration settings related to network traffic of the web application that the App Runner service
    runs. See [Network Configuration](#network-configuration) below for more details.
    """
    network_configuration: NetworkConfiguration | None = core.attr(
        NetworkConfiguration, default=None, computed=True
    )

    """
    The observability configuration of your service. See [Observability Configuration](#observability-co
    nfiguration) below for more details.
    """
    observability_configuration: ObservabilityConfiguration | None = core.attr(
        ObservabilityConfiguration, default=None
    )

    """
    An alphanumeric ID that App Runner generated for this service. Unique within the AWS Region.
    """
    service_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Forces new resource) Name of the service.
    """
    service_name: str | core.StringOut = core.attr(str)

    """
    A subdomain URL that App Runner generated for this service. You can use this URL to access your serv
    ice web application.
    """
    service_url: str | core.StringOut = core.attr(str, computed=True)

    """
    The source to deploy to the App Runner service. Can be a code or an image repository. See [Source Co
    nfiguration](#source-configuration) below for more details.
    """
    source_configuration: SourceConfiguration = core.attr(SourceConfiguration)

    """
    The current state of the App Runner service.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](h
    ttps://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-block) p
    resent, tags with matching keys will overwrite those defined at the provider-level.
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
