import terrascript.core as core


@core.resource(type="aws_service_discovery_instance", namespace="aws_cloud_map")
class ServiceDiscoveryInstance(core.Resource):

    attributes: dict[str, str] | core.MapOut[core.StringOut] = core.attr(str, kind=core.Kind.map)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    service_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        attributes: dict[str, str] | core.MapOut[core.StringOut],
        instance_id: str | core.StringOut,
        service_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceDiscoveryInstance.Args(
                attributes=attributes,
                instance_id=instance_id,
                service_id=service_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        instance_id: str | core.StringOut = core.arg()

        service_id: str | core.StringOut = core.arg()
