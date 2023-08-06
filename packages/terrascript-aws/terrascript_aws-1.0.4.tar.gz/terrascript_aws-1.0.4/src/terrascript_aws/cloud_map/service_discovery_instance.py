import terrascript.core as core


@core.resource(type="aws_service_discovery_instance", namespace="cloud_map")
class ServiceDiscoveryInstance(core.Resource):
    """
    (Required) A map contains the attributes of the instance. Check the [doc](https://docs.aws.amazon.co
    m/cloud-map/latest/api/API_RegisterInstance.html#API_RegisterInstance_RequestSyntax) for the support
    ed attributes and syntax.
    """

    attributes: dict[str, str] | core.MapOut[core.StringOut] = core.attr(str, kind=core.Kind.map)

    """
    The ID of the instance.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, ForceNew) The ID of the service instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required, ForceNew) The ID of the service that you want to use to create the instance.
    """
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
