import terrascript.core as core


@core.resource(type="aws_network_acl_association", namespace="vpc")
class NetworkAclAssociation(core.Resource):
    """
    The ID of the network ACL association
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the network ACL.
    """
    network_acl_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the associated Subnet.
    """
    subnet_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        network_acl_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkAclAssociation.Args(
                network_acl_id=network_acl_id,
                subnet_id=subnet_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        network_acl_id: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()
