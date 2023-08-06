import terrascript.core as core


@core.schema
class DomainValidationOptions(core.Schema):

    domain_name: str | core.StringOut = core.attr(str, computed=True)

    resource_record_name: str | core.StringOut = core.attr(str, computed=True)

    resource_record_type: str | core.StringOut = core.attr(str, computed=True)

    resource_record_value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        domain_name: str | core.StringOut,
        resource_record_name: str | core.StringOut,
        resource_record_type: str | core.StringOut,
        resource_record_value: str | core.StringOut,
    ):
        super().__init__(
            args=DomainValidationOptions.Args(
                domain_name=domain_name,
                resource_record_name=resource_record_name,
                resource_record_type=resource_record_type,
                resource_record_value=resource_record_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut = core.arg()

        resource_record_name: str | core.StringOut = core.arg()

        resource_record_type: str | core.StringOut = core.arg()

        resource_record_value: str | core.StringOut = core.arg()


@core.schema
class ValidationOption(core.Schema):

    domain_name: str | core.StringOut = core.attr(str)

    validation_domain: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        domain_name: str | core.StringOut,
        validation_domain: str | core.StringOut,
    ):
        super().__init__(
            args=ValidationOption.Args(
                domain_name=domain_name,
                validation_domain=validation_domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut = core.arg()

        validation_domain: str | core.StringOut = core.arg()


@core.schema
class Options(core.Schema):

    certificate_transparency_logging_preference: str | core.StringOut | None = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        certificate_transparency_logging_preference: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Options.Args(
                certificate_transparency_logging_preference=certificate_transparency_logging_preference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_transparency_logging_preference: str | core.StringOut | None = core.arg(
            default=None
        )


@core.resource(type="aws_acm_certificate", namespace="acm")
class Certificate(core.Resource):
    """
    The ARN of the certificate
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ARN of an ACM PCA
    """
    certificate_authority_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The certificate's PEM-formatted public key
    """
    certificate_body: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The certificate's PEM-formatted chain
    """
    certificate_chain: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A domain name for which the certificate should be issued
    """
    domain_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Set of domain validation objects which can be used to complete certificate validation. Can have more
    than one element, e.g., if SANs are defined. Only set if `DNS`-validation was used.
    """
    domain_validation_options: list[DomainValidationOptions] | core.ArrayOut[
        DomainValidationOptions
    ] = core.attr(DomainValidationOptions, computed=True, kind=core.Kind.array)

    """
    The ARN of the certificate
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The expiration date and time of the certificate.
    """
    not_after: str | core.StringOut = core.attr(str, computed=True)

    """
    The start of the validity period of the certificate.
    """
    not_before: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block used to set certificate options. Detailed below.
    """
    options: Options | None = core.attr(Options, default=None)

    """
    (Required) The certificate's PEM-formatted private key
    """
    private_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    Status of the certificate.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set of domains that should be SANs in the issued certificate. To remove all elements
    of a previously configured list, set this value equal to an empty list (`[]`) or use the [`terraform
    taint` command](https://www.terraform.io/docs/commands/taint.html) to trigger recreation.
    """
    subject_alternative_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
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

    """
    A list of addresses that received a validation E-Mail. Only set if `EMAIL`-validation was used.
    """
    validation_emails: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used fo
    r certificates that were imported into ACM and then into Terraform.
    """
    validation_method: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block used to specify information about the initial validation of each
    domain name. Detailed below.
    """
    validation_option: list[ValidationOption] | core.ArrayOut[ValidationOption] | None = core.attr(
        ValidationOption, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_authority_arn: str | core.StringOut | None = None,
        certificate_body: str | core.StringOut | None = None,
        certificate_chain: str | core.StringOut | None = None,
        domain_name: str | core.StringOut | None = None,
        options: Options | None = None,
        private_key: str | core.StringOut | None = None,
        subject_alternative_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        validation_method: str | core.StringOut | None = None,
        validation_option: list[ValidationOption] | core.ArrayOut[ValidationOption] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                certificate_authority_arn=certificate_authority_arn,
                certificate_body=certificate_body,
                certificate_chain=certificate_chain,
                domain_name=domain_name,
                options=options,
                private_key=private_key,
                subject_alternative_names=subject_alternative_names,
                tags=tags,
                tags_all=tags_all,
                validation_method=validation_method,
                validation_option=validation_option,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_authority_arn: str | core.StringOut | None = core.arg(default=None)

        certificate_body: str | core.StringOut | None = core.arg(default=None)

        certificate_chain: str | core.StringOut | None = core.arg(default=None)

        domain_name: str | core.StringOut | None = core.arg(default=None)

        options: Options | None = core.arg(default=None)

        private_key: str | core.StringOut | None = core.arg(default=None)

        subject_alternative_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        validation_method: str | core.StringOut | None = core.arg(default=None)

        validation_option: list[ValidationOption] | core.ArrayOut[
            ValidationOption
        ] | None = core.arg(default=None)
