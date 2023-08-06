import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        types: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=EndpointConfiguration.Args(
                types=types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        types: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_api_gateway_domain_name", namespace="api_gateway")
class DsDomainName(core.Data):
    """
    ARN of the found custom domain name.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN for an AWS-managed certificate that is used by edge-optimized endpoint for this domain name.
    """
    certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the certificate that is used by edge-optimized endpoint for this domain name.
    """
    certificate_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Upload date associated with the domain certificate.
    """
    certificate_upload_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Hostname created by Cloudfront to represent the distribution that implements this domain name mappin
    g.
    """
    cloudfront_domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`) that can be used to create a Route53 alias re
    cord for the distribution.
    """
    cloudfront_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Fully-qualified domain name to look up. If no domain name is found, an error will be retu
    rned.
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    List of objects with the endpoint configuration of this domain name.
    """
    endpoint_configuration: list[EndpointConfiguration] | core.ArrayOut[
        EndpointConfiguration
    ] = core.attr(EndpointConfiguration, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN for an AWS-managed certificate that is used for validating the regional domain name.
    """
    regional_certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    User-friendly name of the certificate that is used by regional endpoint for this domain name.
    """
    regional_certificate_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Hostname for the custom domain's regional endpoint.
    """
    regional_domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
    """
    regional_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Security policy for the domain name.
    """
    security_policy: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDomainName.Args(
                domain_name=domain_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
