import terrascript.core as core


@core.resource(type="aws_wafv2_ip_set", namespace="waf")
class V2IpSet(core.Resource):
    """
    (Required) Contains an array of strings that specify one or more IP addresses or blocks of IP addres
    ses in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all address ranges for IP ve
    rsions IPv4 and IPv6.
    """

    addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The Amazon Resource Name (ARN) that identifies the cluster.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A friendly description of the IP set.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    A unique identifier for the set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specify IPV4 or IPV6. Valid values are `IPV4` or `IPV6`.
    """
    ip_address_version: str | core.StringOut = core.attr(str)

    lock_token: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A friendly name of the IP set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies whether this is for an AWS CloudFront distribution or for a regional applicatio
    n. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the R
    egion US East (N. Virginia).
    """
    scope: str | core.StringOut = core.attr(str)

    """
    (Optional) An array of key:value pairs to associate with the resource. If configured with a provider
    [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/d
    ocs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined
    at the provider-level.
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
        ip_address_version: str | core.StringOut,
        name: str | core.StringOut,
        scope: str | core.StringOut,
        addresses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2IpSet.Args(
                ip_address_version=ip_address_version,
                name=name,
                scope=scope,
                addresses=addresses,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        ip_address_version: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        scope: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
