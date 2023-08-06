import terrascript.core as core


@core.schema
class IpSetDescriptor(core.Schema):

    type: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=IpSetDescriptor.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_wafregional_ipset", namespace="wafregional")
class Ipset(core.Resource):
    """
    The ARN of the WAF IPSet.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the WAF IPSet.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range
    (in CIDR notation) from which web requests originate.
    """
    ip_set_descriptor: list[IpSetDescriptor] | core.ArrayOut[IpSetDescriptor] | None = core.attr(
        IpSetDescriptor, default=None, kind=core.Kind.array
    )

    """
    (Required) The name or description of the IPSet.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        ip_set_descriptor: list[IpSetDescriptor] | core.ArrayOut[IpSetDescriptor] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ipset.Args(
                name=name,
                ip_set_descriptor=ip_set_descriptor,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ip_set_descriptor: list[IpSetDescriptor] | core.ArrayOut[IpSetDescriptor] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()
