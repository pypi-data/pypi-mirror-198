import terrascript.core as core


@core.resource(type="aws_lightsail_static_ip", namespace="lightsail")
class StaticIp(core.Resource):
    """
    The ARN of the Lightsail static IP
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The allocated static IP address
    """
    ip_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for the allocated static IP
    """
    name: str | core.StringOut = core.attr(str)

    """
    The support code.
    """
    support_code: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StaticIp.Args(
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()
