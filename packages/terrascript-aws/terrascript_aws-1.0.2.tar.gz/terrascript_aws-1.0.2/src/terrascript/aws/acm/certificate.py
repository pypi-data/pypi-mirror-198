import terrascript.core as core


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


@core.resource(type="aws_acm_certificate", namespace="aws_acm")
class Certificate(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_authority_arn: str | core.StringOut | None = core.attr(str, default=None)

    certificate_body: str | core.StringOut | None = core.attr(str, default=None)

    certificate_chain: str | core.StringOut | None = core.attr(str, default=None)

    domain_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    domain_validation_options: list[DomainValidationOptions] | core.ArrayOut[
        DomainValidationOptions
    ] = core.attr(DomainValidationOptions, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    not_after: str | core.StringOut = core.attr(str, computed=True)

    not_before: str | core.StringOut = core.attr(str, computed=True)

    options: Options | None = core.attr(Options, default=None)

    private_key: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    subject_alternative_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    validation_emails: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    validation_method: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
