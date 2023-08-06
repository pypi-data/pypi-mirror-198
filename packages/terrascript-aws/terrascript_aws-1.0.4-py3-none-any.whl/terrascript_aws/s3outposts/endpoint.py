import terrascript.core as core


@core.schema
class NetworkInterfaces(core.Schema):

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        network_interface_id: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkInterfaces.Args(
                network_interface_id=network_interface_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        network_interface_id: str | core.StringOut = core.arg()


@core.resource(type="aws_s3outposts_endpoint", namespace="s3outposts")
class Endpoint(core.Resource):
    """
    Amazon Resource Name (ARN) of the endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    VPC CIDR block of the endpoint.
    """
    cidr_block: str | core.StringOut = core.attr(str, computed=True)

    """
    UTC creation time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).
    """
    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the endpoint.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of nested attributes for associated Elastic Network Interfaces (ENIs).
    """
    network_interfaces: list[NetworkInterfaces] | core.ArrayOut[NetworkInterfaces] = core.attr(
        NetworkInterfaces, computed=True, kind=core.Kind.array
    )

    """
    (Required) Identifier of the Outpost to contain this endpoint.
    """
    outpost_id: str | core.StringOut = core.attr(str)

    """
    (Required) Identifier of the EC2 Security Group.
    """
    security_group_id: str | core.StringOut = core.attr(str)

    """
    (Required) Identifier of the EC2 Subnet.
    """
    subnet_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        outpost_id: str | core.StringOut,
        security_group_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                outpost_id=outpost_id,
                security_group_id=security_group_id,
                subnet_id=subnet_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        outpost_id: str | core.StringOut = core.arg()

        security_group_id: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()
