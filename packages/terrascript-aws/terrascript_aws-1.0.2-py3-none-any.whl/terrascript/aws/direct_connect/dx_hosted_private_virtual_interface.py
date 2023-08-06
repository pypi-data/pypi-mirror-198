import terrascript.core as core


@core.resource(type="aws_dx_hosted_private_virtual_interface", namespace="aws_direct_connect")
class DxHostedPrivateVirtualInterface(core.Resource):

    address_family: str | core.StringOut = core.attr(str)

    amazon_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    amazon_side_asn: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    aws_device: str | core.StringOut = core.attr(str, computed=True)

    bgp_asn: int | core.IntOut = core.attr(int)

    bgp_auth_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    connection_id: str | core.StringOut = core.attr(str)

    customer_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    jumbo_frame_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    mtu: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut = core.attr(str)

    owner_account_id: str | core.StringOut = core.attr(str)

    vlan: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        address_family: str | core.StringOut,
        bgp_asn: int | core.IntOut,
        connection_id: str | core.StringOut,
        name: str | core.StringOut,
        owner_account_id: str | core.StringOut,
        vlan: int | core.IntOut,
        amazon_address: str | core.StringOut | None = None,
        bgp_auth_key: str | core.StringOut | None = None,
        customer_address: str | core.StringOut | None = None,
        mtu: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxHostedPrivateVirtualInterface.Args(
                address_family=address_family,
                bgp_asn=bgp_asn,
                connection_id=connection_id,
                name=name,
                owner_account_id=owner_account_id,
                vlan=vlan,
                amazon_address=amazon_address,
                bgp_auth_key=bgp_auth_key,
                customer_address=customer_address,
                mtu=mtu,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address_family: str | core.StringOut = core.arg()

        amazon_address: str | core.StringOut | None = core.arg(default=None)

        bgp_asn: int | core.IntOut = core.arg()

        bgp_auth_key: str | core.StringOut | None = core.arg(default=None)

        connection_id: str | core.StringOut = core.arg()

        customer_address: str | core.StringOut | None = core.arg(default=None)

        mtu: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        owner_account_id: str | core.StringOut = core.arg()

        vlan: int | core.IntOut = core.arg()
