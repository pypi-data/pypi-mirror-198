import terrascript.core as core


@core.resource(type="aws_lightsail_static_ip_attachment", namespace="lightsail")
class StaticIpAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Lightsail instance to attach the IP to
    """
    instance_name: str | core.StringOut = core.attr(str)

    """
    The allocated static IP address
    """
    ip_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the allocated static IP
    """
    static_ip_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_name: str | core.StringOut,
        static_ip_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StaticIpAttachment.Args(
                instance_name=instance_name,
                static_ip_name=static_ip_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_name: str | core.StringOut = core.arg()

        static_ip_name: str | core.StringOut = core.arg()
