import terrascript.core as core


@core.schema
class CertificateValidationRecords(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        status: str | core.StringOut,
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=CertificateValidationRecords.Args(
                name=name,
                status=status,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_apprunner_custom_domain_association", namespace="aws_apprunner")
class CustomDomainAssociation(core.Resource):

    certificate_validation_records: list[CertificateValidationRecords] | core.ArrayOut[
        CertificateValidationRecords
    ] = core.attr(CertificateValidationRecords, computed=True, kind=core.Kind.array)

    dns_target: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut = core.attr(str)

    enable_www_subdomain: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    service_arn: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: str | core.StringOut,
        service_arn: str | core.StringOut,
        enable_www_subdomain: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CustomDomainAssociation.Args(
                domain_name=domain_name,
                service_arn=service_arn,
                enable_www_subdomain=enable_www_subdomain,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: str | core.StringOut = core.arg()

        enable_www_subdomain: bool | core.BoolOut | None = core.arg(default=None)

        service_arn: str | core.StringOut = core.arg()
