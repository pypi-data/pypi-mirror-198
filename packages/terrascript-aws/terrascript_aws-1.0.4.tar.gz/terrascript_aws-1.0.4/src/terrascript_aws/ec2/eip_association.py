import terrascript.core as core


@core.resource(type="aws_eip_association", namespace="ec2")
class EipAssociation(core.Resource):
    """
    (Optional) The allocation ID. This is required for EC2-VPC.
    """

    allocation_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Boolean) Whether to allow an Elastic IP to
    """
    allow_reassociation: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the instance. This is required for
    """
    instance_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The ID of the network interface. If the
    """
    network_interface_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The primary or secondary private IP address
    """
    private_ip_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The Elastic IP address. This is required for EC2-Classic.
    """
    public_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        allocation_id: str | core.StringOut | None = None,
        allow_reassociation: bool | core.BoolOut | None = None,
        instance_id: str | core.StringOut | None = None,
        network_interface_id: str | core.StringOut | None = None,
        private_ip_address: str | core.StringOut | None = None,
        public_ip: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EipAssociation.Args(
                allocation_id=allocation_id,
                allow_reassociation=allow_reassociation,
                instance_id=instance_id,
                network_interface_id=network_interface_id,
                private_ip_address=private_ip_address,
                public_ip=public_ip,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocation_id: str | core.StringOut | None = core.arg(default=None)

        allow_reassociation: bool | core.BoolOut | None = core.arg(default=None)

        instance_id: str | core.StringOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut | None = core.arg(default=None)

        private_ip_address: str | core.StringOut | None = core.arg(default=None)

        public_ip: str | core.StringOut | None = core.arg(default=None)
