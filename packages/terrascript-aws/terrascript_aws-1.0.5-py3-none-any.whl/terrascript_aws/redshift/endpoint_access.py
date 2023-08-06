import terrascript.core as core


@core.schema
class NetworkInterface(core.Schema):

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    private_ip_address: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zone: str | core.StringOut,
        network_interface_id: str | core.StringOut,
        private_ip_address: str | core.StringOut,
        subnet_id: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkInterface.Args(
                availability_zone=availability_zone,
                network_interface_id=network_interface_id,
                private_ip_address=private_ip_address,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut = core.arg()

        network_interface_id: str | core.StringOut = core.arg()

        private_ip_address: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()


@core.schema
class VpcEndpoint(core.Schema):

    network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface] = core.attr(
        NetworkInterface, computed=True, kind=core.Kind.array
    )

    vpc_endpoint_id: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface],
        vpc_endpoint_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcEndpoint.Args(
                network_interface=network_interface,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface] = core.arg()

        vpc_endpoint_id: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.resource(type="aws_redshift_endpoint_access", namespace="redshift")
class EndpointAccess(core.Resource):
    """
    The DNS address of the endpoint.
    """

    address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The cluster identifier of the cluster to access.
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    (Required) The Redshift-managed VPC endpoint name.
    """
    endpoint_name: str | core.StringOut = core.attr(str)

    """
    The Redshift-managed VPC endpoint name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The port number on which the cluster accepts incoming connections.
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) The Amazon Web Services account ID of the owner of the cluster. This is only required if
    the cluster is in another Amazon Web Services account.
    """
    resource_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The subnet group from which Amazon Redshift chooses the subnet to deploy the endpoint.
    """
    subnet_group_name: str | core.StringOut = core.attr(str)

    """
    The connection endpoint for connecting to an Amazon Redshift cluster through the proxy. See details
    below.
    """
    vpc_endpoint: list[VpcEndpoint] | core.ArrayOut[VpcEndpoint] = core.attr(
        VpcEndpoint, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The security group that defines the ports, protocols, and sources for inbound traffic tha
    t you are authorizing into your endpoint.
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        endpoint_name: str | core.StringOut,
        subnet_group_name: str | core.StringOut,
        resource_owner: str | core.StringOut | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointAccess.Args(
                cluster_identifier=cluster_identifier,
                endpoint_name=endpoint_name,
                subnet_group_name=subnet_group_name,
                resource_owner=resource_owner,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_identifier: str | core.StringOut = core.arg()

        endpoint_name: str | core.StringOut = core.arg()

        resource_owner: str | core.StringOut | None = core.arg(default=None)

        subnet_group_name: str | core.StringOut = core.arg()

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
