import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

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


@core.schema
class MutualTlsAuthentication(core.Schema):

    truststore_uri: str | core.StringOut = core.attr(str)

    truststore_version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        truststore_uri: str | core.StringOut,
        truststore_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MutualTlsAuthentication.Args(
                truststore_uri=truststore_uri,
                truststore_version=truststore_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        truststore_uri: str | core.StringOut = core.arg()

        truststore_version: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_api_gateway_domain_name", namespace="api_gateway")
class DomainName(core.Resource):
    """
    ARN of domain name.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source.
    Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate
    _body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_ce
    rtificate_name`.
    """
    certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Certificate issued for the domain name being registered, in PEM format. Only valid for `E
    DGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
    regional_certificate_name`.
    """
    certificate_body: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Certificate for the CA that issued the certificate, along with any intermediate CA certif
    icates required to create an unbroken chain to a certificate trusted by the intended API clients. On
    ly valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certifi
    cate_arn`, and `regional_certificate_name`.
    """
    certificate_chain: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Unique name to use when registering this certificate as an IAM server certificate. Confli
    cts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`. Required if
    certificate_arn` is not set.
    """
    certificate_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Private key associated with the domain certificate given in `certificate_body`. Only vali
    d for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_ar
    n`, and `regional_certificate_name`.
    """
    certificate_private_key: str | core.StringOut | None = core.attr(str, default=None)

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
    (Required) Fully-qualified domain name to register.
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block defining API endpoint information including type. See below.
    """
    endpoint_configuration: EndpointConfiguration | None = core.attr(
        EndpointConfiguration, default=None, computed=True
    )

    """
    Internal identifier assigned to this domain name by API Gateway.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Mutual TLS authentication configuration for the domain name. See below.
    """
    mutual_tls_authentication: MutualTlsAuthentication | None = core.attr(
        MutualTlsAuthentication, default=None
    )

    """
    (Optional) ARN of the AWS-issued certificate used to validate custom domain ownership (when `certifi
    cate_arn` is issued via an ACM Private CA or `mutual_tls_authentication` is configured with an ACM-i
    mported certificate.)
    """
    ownership_verification_certificate_arn: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source.
    Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`,
    certificate_body`, `certificate_chain`, and `certificate_private_key`.
    """
    regional_certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) User-friendly name of the certificate that will be used by regional endpoint for this dom
    ain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_cha
    in`, and `certificate_private_key`.
    """
    regional_certificate_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    Hostname for the custom domain's regional endpoint.
    """
    regional_domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
    """
    regional_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Transport Layer Security (TLS) version + cipher suite for this DomainName. Valid values a
    re `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
    """
    security_policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: str | core.StringOut,
        certificate_arn: str | core.StringOut | None = None,
        certificate_body: str | core.StringOut | None = None,
        certificate_chain: str | core.StringOut | None = None,
        certificate_name: str | core.StringOut | None = None,
        certificate_private_key: str | core.StringOut | None = None,
        endpoint_configuration: EndpointConfiguration | None = None,
        mutual_tls_authentication: MutualTlsAuthentication | None = None,
        ownership_verification_certificate_arn: str | core.StringOut | None = None,
        regional_certificate_arn: str | core.StringOut | None = None,
        regional_certificate_name: str | core.StringOut | None = None,
        security_policy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainName.Args(
                domain_name=domain_name,
                certificate_arn=certificate_arn,
                certificate_body=certificate_body,
                certificate_chain=certificate_chain,
                certificate_name=certificate_name,
                certificate_private_key=certificate_private_key,
                endpoint_configuration=endpoint_configuration,
                mutual_tls_authentication=mutual_tls_authentication,
                ownership_verification_certificate_arn=ownership_verification_certificate_arn,
                regional_certificate_arn=regional_certificate_arn,
                regional_certificate_name=regional_certificate_name,
                security_policy=security_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: str | core.StringOut | None = core.arg(default=None)

        certificate_body: str | core.StringOut | None = core.arg(default=None)

        certificate_chain: str | core.StringOut | None = core.arg(default=None)

        certificate_name: str | core.StringOut | None = core.arg(default=None)

        certificate_private_key: str | core.StringOut | None = core.arg(default=None)

        domain_name: str | core.StringOut = core.arg()

        endpoint_configuration: EndpointConfiguration | None = core.arg(default=None)

        mutual_tls_authentication: MutualTlsAuthentication | None = core.arg(default=None)

        ownership_verification_certificate_arn: str | core.StringOut | None = core.arg(default=None)

        regional_certificate_arn: str | core.StringOut | None = core.arg(default=None)

        regional_certificate_name: str | core.StringOut | None = core.arg(default=None)

        security_policy: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
