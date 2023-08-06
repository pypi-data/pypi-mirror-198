import terrascript.core as core


@core.schema
class SubDomain(core.Schema):

    branch_name: str | core.StringOut = core.attr(str)

    dns_record: str | core.StringOut = core.attr(str, computed=True)

    prefix: str | core.StringOut = core.attr(str)

    verified: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        branch_name: str | core.StringOut,
        dns_record: str | core.StringOut,
        prefix: str | core.StringOut,
        verified: bool | core.BoolOut,
    ):
        super().__init__(
            args=SubDomain.Args(
                branch_name=branch_name,
                dns_record=dns_record,
                prefix=prefix,
                verified=verified,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        branch_name: str | core.StringOut = core.arg()

        dns_record: str | core.StringOut = core.arg()

        prefix: str | core.StringOut = core.arg()

        verified: bool | core.BoolOut = core.arg()


@core.resource(type="aws_amplify_domain_association", namespace="amplify")
class DomainAssociation(core.Resource):
    """
    (Required) The unique ID for an Amplify app.
    """

    app_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) for the domain association.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The DNS record for certificate verification.
    """
    certificate_verification_dns_record: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The domain name for the domain association.
    """
    domain_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The setting for the subdomain. Documented below.
    """
    sub_domain: list[SubDomain] | core.ArrayOut[SubDomain] = core.attr(
        SubDomain, kind=core.Kind.array
    )

    """
    (Optional) If enabled, the resource will wait for the domain association status to change to `PENDIN
    G_DEPLOYMENT` or `AVAILABLE`. Setting this to `false` will skip the process. Default: `true`.
    """
    wait_for_verification: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        app_id: str | core.StringOut,
        domain_name: str | core.StringOut,
        sub_domain: list[SubDomain] | core.ArrayOut[SubDomain],
        wait_for_verification: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainAssociation.Args(
                app_id=app_id,
                domain_name=domain_name,
                sub_domain=sub_domain,
                wait_for_verification=wait_for_verification,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_id: str | core.StringOut = core.arg()

        domain_name: str | core.StringOut = core.arg()

        sub_domain: list[SubDomain] | core.ArrayOut[SubDomain] = core.arg()

        wait_for_verification: bool | core.BoolOut | None = core.arg(default=None)
