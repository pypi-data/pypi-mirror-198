import terrascript.core as core


@core.resource(type="aws_customer_gateway", namespace="vpn")
class CustomerGateway(core.Resource):
    """
    The ARN of the customer gateway.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
    """
    bgp_asn: str | core.StringOut = core.attr(str)

    """
    (Optional) The Amazon Resource Name (ARN) for the customer gateway certificate.
    """
    certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A name for the customer gateway device.
    """
    device_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The amazon-assigned ID of the gateway.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The IPv4 address for the customer gateway device's outside interface.
    """
    ip_address: str | core.StringOut = core.attr(str)

    """
    (Optional) Tags to apply to the gateway. If configured with a provider [`default_tags` configuration
    block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration
    block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Required) The type of customer gateway. The only type AWS
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bgp_asn: str | core.StringOut,
        ip_address: str | core.StringOut,
        type: str | core.StringOut,
        certificate_arn: str | core.StringOut | None = None,
        device_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CustomerGateway.Args(
                bgp_asn=bgp_asn,
                ip_address=ip_address,
                type=type,
                certificate_arn=certificate_arn,
                device_name=device_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bgp_asn: str | core.StringOut = core.arg()

        certificate_arn: str | core.StringOut | None = core.arg(default=None)

        device_name: str | core.StringOut | None = core.arg(default=None)

        ip_address: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
