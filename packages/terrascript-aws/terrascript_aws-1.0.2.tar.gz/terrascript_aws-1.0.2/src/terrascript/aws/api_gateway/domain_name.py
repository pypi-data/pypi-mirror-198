import terrascript.core as core


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


@core.resource(type="aws_api_gateway_domain_name", namespace="aws_api_gateway")
class DomainName(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    certificate_body: str | core.StringOut | None = core.attr(str, default=None)

    certificate_chain: str | core.StringOut | None = core.attr(str, default=None)

    certificate_name: str | core.StringOut | None = core.attr(str, default=None)

    certificate_private_key: str | core.StringOut | None = core.attr(str, default=None)

    certificate_upload_date: str | core.StringOut = core.attr(str, computed=True)

    cloudfront_domain_name: str | core.StringOut = core.attr(str, computed=True)

    cloudfront_zone_id: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut = core.attr(str)

    endpoint_configuration: EndpointConfiguration | None = core.attr(
        EndpointConfiguration, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    mutual_tls_authentication: MutualTlsAuthentication | None = core.attr(
        MutualTlsAuthentication, default=None
    )

    ownership_verification_certificate_arn: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    regional_certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    regional_certificate_name: str | core.StringOut | None = core.attr(str, default=None)

    regional_domain_name: str | core.StringOut = core.attr(str, computed=True)

    regional_zone_id: str | core.StringOut = core.attr(str, computed=True)

    security_policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
