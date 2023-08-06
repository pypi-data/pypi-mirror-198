import terrascript.core as core


@core.schema
class DomainNameConfiguration(core.Schema):

    certificate_arn: str | core.StringOut = core.attr(str)

    endpoint_type: str | core.StringOut = core.attr(str)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    ownership_verification_certificate_arn: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    security_policy: str | core.StringOut = core.attr(str)

    target_domain_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        certificate_arn: str | core.StringOut,
        endpoint_type: str | core.StringOut,
        hosted_zone_id: str | core.StringOut,
        security_policy: str | core.StringOut,
        target_domain_name: str | core.StringOut,
        ownership_verification_certificate_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DomainNameConfiguration.Args(
                certificate_arn=certificate_arn,
                endpoint_type=endpoint_type,
                hosted_zone_id=hosted_zone_id,
                security_policy=security_policy,
                target_domain_name=target_domain_name,
                ownership_verification_certificate_arn=ownership_verification_certificate_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_arn: str | core.StringOut = core.arg()

        endpoint_type: str | core.StringOut = core.arg()

        hosted_zone_id: str | core.StringOut = core.arg()

        ownership_verification_certificate_arn: str | core.StringOut | None = core.arg(default=None)

        security_policy: str | core.StringOut = core.arg()

        target_domain_name: str | core.StringOut = core.arg()


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


@core.resource(type="aws_apigatewayv2_domain_name", namespace="apigatewayv2")
class DomainName(core.Resource):
    """
    [API mapping selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apig
    ateway-websocket-api-selection-expressions.html#apigateway-websocket-api-mapping-selection-expressio
    ns) for the domain name.
    """

    api_mapping_selection_expression: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the domain name.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Domain name. Must be between 1 and 512 characters in length.
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    (Required) Domain name configuration. See below.
    """
    domain_name_configuration: DomainNameConfiguration = core.attr(DomainNameConfiguration)

    """
    Domain name identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Mutual TLS authentication configuration for the domain name.
    """
    mutual_tls_authentication: MutualTlsAuthentication | None = core.attr(
        MutualTlsAuthentication, default=None
    )

    """
    (Optional) Map of tags to assign to the domain name. If configured with a provider [`default_tags` c
    onfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-c
    onfiguration-block) present, tags with matching keys will overwrite those defined at the provider-le
    vel.
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
        domain_name_configuration: DomainNameConfiguration,
        mutual_tls_authentication: MutualTlsAuthentication | None = None,
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
                domain_name_configuration=domain_name_configuration,
                mutual_tls_authentication=mutual_tls_authentication,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: str | core.StringOut = core.arg()

        domain_name_configuration: DomainNameConfiguration = core.arg()

        mutual_tls_authentication: MutualTlsAuthentication | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
