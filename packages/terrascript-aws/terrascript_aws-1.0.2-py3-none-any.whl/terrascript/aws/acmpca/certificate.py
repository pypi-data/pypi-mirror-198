import terrascript.core as core


@core.schema
class Validity(core.Schema):

    type: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Validity.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_acmpca_certificate", namespace="aws_acmpca")
class Certificate(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate: str | core.StringOut = core.attr(str, computed=True)

    certificate_authority_arn: str | core.StringOut = core.attr(str)

    certificate_chain: str | core.StringOut = core.attr(str, computed=True)

    certificate_signing_request: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    signing_algorithm: str | core.StringOut = core.attr(str)

    template_arn: str | core.StringOut | None = core.attr(str, default=None)

    validity: Validity = core.attr(Validity)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_authority_arn: str | core.StringOut,
        certificate_signing_request: str | core.StringOut,
        signing_algorithm: str | core.StringOut,
        validity: Validity,
        template_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                certificate_authority_arn=certificate_authority_arn,
                certificate_signing_request=certificate_signing_request,
                signing_algorithm=signing_algorithm,
                validity=validity,
                template_arn=template_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_authority_arn: str | core.StringOut = core.arg()

        certificate_signing_request: str | core.StringOut = core.arg()

        signing_algorithm: str | core.StringOut = core.arg()

        template_arn: str | core.StringOut | None = core.arg(default=None)

        validity: Validity = core.arg()
