import terrascript.core as core


@core.schema
class Container(core.Schema):

    command: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    container_name: str | core.StringOut = core.attr(str)

    environment: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    image: str | core.StringOut = core.attr(str)

    ports: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        container_name: str | core.StringOut,
        image: str | core.StringOut,
        command: list[str] | core.ArrayOut[core.StringOut] | None = None,
        environment: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        ports: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Container.Args(
                container_name=container_name,
                image=image,
                command=command,
                environment=environment,
                ports=ports,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        command: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        container_name: str | core.StringOut = core.arg()

        environment: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        image: str | core.StringOut = core.arg()

        ports: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class HealthCheck(core.Schema):

    healthy_threshold: int | core.IntOut | None = core.attr(int, default=None)

    interval_seconds: int | core.IntOut | None = core.attr(int, default=None)

    path: str | core.StringOut | None = core.attr(str, default=None)

    success_codes: str | core.StringOut | None = core.attr(str, default=None)

    timeout_seconds: int | core.IntOut | None = core.attr(int, default=None)

    unhealthy_threshold: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        healthy_threshold: int | core.IntOut | None = None,
        interval_seconds: int | core.IntOut | None = None,
        path: str | core.StringOut | None = None,
        success_codes: str | core.StringOut | None = None,
        timeout_seconds: int | core.IntOut | None = None,
        unhealthy_threshold: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=HealthCheck.Args(
                healthy_threshold=healthy_threshold,
                interval_seconds=interval_seconds,
                path=path,
                success_codes=success_codes,
                timeout_seconds=timeout_seconds,
                unhealthy_threshold=unhealthy_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        healthy_threshold: int | core.IntOut | None = core.arg(default=None)

        interval_seconds: int | core.IntOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        success_codes: str | core.StringOut | None = core.arg(default=None)

        timeout_seconds: int | core.IntOut | None = core.arg(default=None)

        unhealthy_threshold: int | core.IntOut | None = core.arg(default=None)


@core.schema
class PublicEndpoint(core.Schema):

    container_name: str | core.StringOut = core.attr(str)

    container_port: int | core.IntOut = core.attr(int)

    health_check: HealthCheck = core.attr(HealthCheck)

    def __init__(
        self,
        *,
        container_name: str | core.StringOut,
        container_port: int | core.IntOut,
        health_check: HealthCheck,
    ):
        super().__init__(
            args=PublicEndpoint.Args(
                container_name=container_name,
                container_port=container_port,
                health_check=health_check,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: str | core.StringOut = core.arg()

        container_port: int | core.IntOut = core.arg()

        health_check: HealthCheck = core.arg()


@core.resource(type="aws_lightsail_container_service_deployment_version", namespace="aws_lightsail")
class ContainerServiceDeploymentVersion(core.Resource):

    container: list[Container] | core.ArrayOut[Container] = core.attr(
        Container, kind=core.Kind.array
    )

    created_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    public_endpoint: PublicEndpoint | None = core.attr(PublicEndpoint, default=None)

    service_name: str | core.StringOut = core.attr(str)

    state: str | core.StringOut = core.attr(str, computed=True)

    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        container: list[Container] | core.ArrayOut[Container],
        service_name: str | core.StringOut,
        public_endpoint: PublicEndpoint | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContainerServiceDeploymentVersion.Args(
                container=container,
                service_name=service_name,
                public_endpoint=public_endpoint,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container: list[Container] | core.ArrayOut[Container] = core.arg()

        public_endpoint: PublicEndpoint | None = core.arg(default=None)

        service_name: str | core.StringOut = core.arg()
