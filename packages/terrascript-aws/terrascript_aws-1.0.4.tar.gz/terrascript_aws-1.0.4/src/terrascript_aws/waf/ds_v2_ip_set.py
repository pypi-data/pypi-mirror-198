import terrascript.core as core


@core.data(type="aws_wafv2_ip_set", namespace="waf")
class DsV2IpSet(core.Data):
    """
    An array of strings that specify one or more IP addresses or blocks of IP addresses in Classless Int
    er-Domain Routing (CIDR) notation.
    """

    addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The Amazon Resource Name (ARN) of the entity.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the set that helps with identification.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifier for the set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IP address version of the set.
    """
    ip_address_version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the WAFv2 IP Set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies whether this is for an AWS CloudFront distribution or for a regional applicatio
    n. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the r
    egion `us-east-1` (N. Virginia) on the AWS provider.
    """
    scope: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        scope: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsV2IpSet.Args(
                name=name,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        scope: str | core.StringOut = core.arg()
