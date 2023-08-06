import terrascript.core as core


@core.schema
class IpAddress(core.Schema):

    ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ip_id: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        ip_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
        ip: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=IpAddress.Args(
                ip_id=ip_id,
                subnet_id=subnet_id,
                ip=ip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip: str | core.StringOut | None = core.arg(default=None)

        ip_id: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()


@core.resource(type="aws_route53_resolver_endpoint", namespace="route53_resolver")
class Endpoint(core.Resource):
    """
    The ARN of the Route 53 Resolver endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The direction of DNS queries to or from the Route 53 Resolver endpoint.
    """
    direction: str | core.StringOut = core.attr(str)

    """
    The ID of the VPC that you want to create the resolver endpoint in.
    """
    host_vpc_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the Route 53 Resolver endpoint.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The subnets and IP addresses in your VPC that you want DNS queries to pass through on the
    way from your VPCs
    """
    ip_address: list[IpAddress] | core.ArrayOut[IpAddress] = core.attr(
        IpAddress, kind=core.Kind.array
    )

    """
    (Optional) The friendly name of the Route 53 Resolver endpoint.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of one or more security groups that you want to use to control access to this VPC.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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

    def __init__(
        self,
        resource_name: str,
        *,
        direction: str | core.StringOut,
        ip_address: list[IpAddress] | core.ArrayOut[IpAddress],
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                direction=direction,
                ip_address=ip_address,
                security_group_ids=security_group_ids,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        direction: str | core.StringOut = core.arg()

        ip_address: list[IpAddress] | core.ArrayOut[IpAddress] = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
