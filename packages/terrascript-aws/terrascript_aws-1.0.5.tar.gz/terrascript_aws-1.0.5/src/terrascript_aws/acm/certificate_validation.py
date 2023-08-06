import terrascript.core as core


@core.resource(type="aws_acm_certificate_validation", namespace="acm")
class CertificateValidation(core.Resource):
    """
    (Required) The ARN of the certificate that is being validated.
    """

    certificate_arn: str | core.StringOut = core.attr(str)

    """
    The time at which the certificate was issued
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of FQDNs that implement the validation. Only valid for DNS validation method ACM cer
    tificates. If this is set, the resource can implement additional sanity checks and has an explicit d
    ependency on the resource that is implementing the validation
    """
    validation_record_fqdns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_arn: str | core.StringOut,
        validation_record_fqdns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CertificateValidation.Args(
                certificate_arn=certificate_arn,
                validation_record_fqdns=validation_record_fqdns,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: str | core.StringOut = core.arg()

        validation_record_fqdns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
