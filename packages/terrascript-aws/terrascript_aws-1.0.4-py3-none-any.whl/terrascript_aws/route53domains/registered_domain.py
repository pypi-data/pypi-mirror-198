import terrascript.core as core


@core.schema
class AdminContact(core.Schema):

    address_line_1: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    address_line_2: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    city: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    contact_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    country_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    email: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    fax: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    first_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    last_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    organization_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    phone_number: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    zip_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        address_line_1: str | core.StringOut | None = None,
        address_line_2: str | core.StringOut | None = None,
        city: str | core.StringOut | None = None,
        contact_type: str | core.StringOut | None = None,
        country_code: str | core.StringOut | None = None,
        email: str | core.StringOut | None = None,
        extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        fax: str | core.StringOut | None = None,
        first_name: str | core.StringOut | None = None,
        last_name: str | core.StringOut | None = None,
        organization_name: str | core.StringOut | None = None,
        phone_number: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        zip_code: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AdminContact.Args(
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                contact_type=contact_type,
                country_code=country_code,
                email=email,
                extra_params=extra_params,
                fax=fax,
                first_name=first_name,
                last_name=last_name,
                organization_name=organization_name,
                phone_number=phone_number,
                state=state,
                zip_code=zip_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_line_1: str | core.StringOut | None = core.arg(default=None)

        address_line_2: str | core.StringOut | None = core.arg(default=None)

        city: str | core.StringOut | None = core.arg(default=None)

        contact_type: str | core.StringOut | None = core.arg(default=None)

        country_code: str | core.StringOut | None = core.arg(default=None)

        email: str | core.StringOut | None = core.arg(default=None)

        extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        fax: str | core.StringOut | None = core.arg(default=None)

        first_name: str | core.StringOut | None = core.arg(default=None)

        last_name: str | core.StringOut | None = core.arg(default=None)

        organization_name: str | core.StringOut | None = core.arg(default=None)

        phone_number: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        zip_code: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TechContact(core.Schema):

    address_line_1: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    address_line_2: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    city: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    contact_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    country_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    email: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    fax: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    first_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    last_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    organization_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    phone_number: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    zip_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        address_line_1: str | core.StringOut | None = None,
        address_line_2: str | core.StringOut | None = None,
        city: str | core.StringOut | None = None,
        contact_type: str | core.StringOut | None = None,
        country_code: str | core.StringOut | None = None,
        email: str | core.StringOut | None = None,
        extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        fax: str | core.StringOut | None = None,
        first_name: str | core.StringOut | None = None,
        last_name: str | core.StringOut | None = None,
        organization_name: str | core.StringOut | None = None,
        phone_number: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        zip_code: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TechContact.Args(
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                contact_type=contact_type,
                country_code=country_code,
                email=email,
                extra_params=extra_params,
                fax=fax,
                first_name=first_name,
                last_name=last_name,
                organization_name=organization_name,
                phone_number=phone_number,
                state=state,
                zip_code=zip_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_line_1: str | core.StringOut | None = core.arg(default=None)

        address_line_2: str | core.StringOut | None = core.arg(default=None)

        city: str | core.StringOut | None = core.arg(default=None)

        contact_type: str | core.StringOut | None = core.arg(default=None)

        country_code: str | core.StringOut | None = core.arg(default=None)

        email: str | core.StringOut | None = core.arg(default=None)

        extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        fax: str | core.StringOut | None = core.arg(default=None)

        first_name: str | core.StringOut | None = core.arg(default=None)

        last_name: str | core.StringOut | None = core.arg(default=None)

        organization_name: str | core.StringOut | None = core.arg(default=None)

        phone_number: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        zip_code: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NameServer(core.Schema):

    glue_ips: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        glue_ips: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=NameServer.Args(
                name=name,
                glue_ips=glue_ips,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        glue_ips: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()


@core.schema
class RegistrantContact(core.Schema):

    address_line_1: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    address_line_2: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    city: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    contact_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    country_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    email: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    fax: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    first_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    last_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    organization_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    phone_number: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    zip_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        address_line_1: str | core.StringOut | None = None,
        address_line_2: str | core.StringOut | None = None,
        city: str | core.StringOut | None = None,
        contact_type: str | core.StringOut | None = None,
        country_code: str | core.StringOut | None = None,
        email: str | core.StringOut | None = None,
        extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        fax: str | core.StringOut | None = None,
        first_name: str | core.StringOut | None = None,
        last_name: str | core.StringOut | None = None,
        organization_name: str | core.StringOut | None = None,
        phone_number: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        zip_code: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RegistrantContact.Args(
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                contact_type=contact_type,
                country_code=country_code,
                email=email,
                extra_params=extra_params,
                fax=fax,
                first_name=first_name,
                last_name=last_name,
                organization_name=organization_name,
                phone_number=phone_number,
                state=state,
                zip_code=zip_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_line_1: str | core.StringOut | None = core.arg(default=None)

        address_line_2: str | core.StringOut | None = core.arg(default=None)

        city: str | core.StringOut | None = core.arg(default=None)

        contact_type: str | core.StringOut | None = core.arg(default=None)

        country_code: str | core.StringOut | None = core.arg(default=None)

        email: str | core.StringOut | None = core.arg(default=None)

        extra_params: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        fax: str | core.StringOut | None = core.arg(default=None)

        first_name: str | core.StringOut | None = core.arg(default=None)

        last_name: str | core.StringOut | None = core.arg(default=None)

        organization_name: str | core.StringOut | None = core.arg(default=None)

        phone_number: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        zip_code: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_route53domains_registered_domain", namespace="route53domains")
class RegisteredDomain(core.Resource):
    """
    Email address to contact to report incorrect contact information for a domain, to report that the do
    main is being used to send spam, to report that someone is cybersquatting on a domain name, or repor
    t some other type of abuse.
    """

    abuse_contact_email: str | core.StringOut = core.attr(str, computed=True)

    """
    Phone number for reporting abuse.
    """
    abuse_contact_phone: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Details about the domain administrative contact.
    """
    admin_contact: AdminContact | None = core.attr(AdminContact, default=None, computed=True)

    """
    (Optional) Whether domain administrative contact information is concealed from WHOIS queries. Defaul
    t: `true`.
    """
    admin_privacy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether the domain registration is set to renew automatically. Default: `true`.
    """
    auto_renew: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The date when the domain was created as found in the response to a WHOIS query.
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the registered domain.
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    The date when the registration for the domain is set to expire.
    """
    expiration_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The domain name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The list of nameservers for the domain.
    """
    name_server: list[NameServer] | core.ArrayOut[NameServer] | None = core.attr(
        NameServer, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Details about the domain registrant.
    """
    registrant_contact: RegistrantContact | None = core.attr(
        RegistrantContact, default=None, computed=True
    )

    """
    (Optional) Whether domain registrant contact information is concealed from WHOIS queries. Default: `
    true`.
    """
    registrant_privacy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Name of the registrar of the domain as identified in the registry.
    """
    registrar_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Web address of the registrar.
    """
    registrar_url: str | core.StringOut = core.attr(str, computed=True)

    """
    Reseller of the domain.
    """
    reseller: str | core.StringOut = core.attr(str, computed=True)

    """
    List of [domain name status codes](https://www.icann.org/resources/pages/epp-status-codes-2014-06-16
    en).
    """
    status_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
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
    (Optional) Details about the domain technical contact.
    """
    tech_contact: TechContact | None = core.attr(TechContact, default=None, computed=True)

    """
    (Optional) Whether domain technical contact information is concealed from WHOIS queries. Default: `t
    rue`.
    """
    tech_privacy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether the domain is locked for transfer. Default: `true`.
    """
    transfer_lock: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The last updated date of the domain as found in the response to a WHOIS query.
    """
    updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.
    """
    whois_server: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: str | core.StringOut,
        admin_contact: AdminContact | None = None,
        admin_privacy: bool | core.BoolOut | None = None,
        auto_renew: bool | core.BoolOut | None = None,
        name_server: list[NameServer] | core.ArrayOut[NameServer] | None = None,
        registrant_contact: RegistrantContact | None = None,
        registrant_privacy: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tech_contact: TechContact | None = None,
        tech_privacy: bool | core.BoolOut | None = None,
        transfer_lock: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegisteredDomain.Args(
                domain_name=domain_name,
                admin_contact=admin_contact,
                admin_privacy=admin_privacy,
                auto_renew=auto_renew,
                name_server=name_server,
                registrant_contact=registrant_contact,
                registrant_privacy=registrant_privacy,
                tags=tags,
                tags_all=tags_all,
                tech_contact=tech_contact,
                tech_privacy=tech_privacy,
                transfer_lock=transfer_lock,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admin_contact: AdminContact | None = core.arg(default=None)

        admin_privacy: bool | core.BoolOut | None = core.arg(default=None)

        auto_renew: bool | core.BoolOut | None = core.arg(default=None)

        domain_name: str | core.StringOut = core.arg()

        name_server: list[NameServer] | core.ArrayOut[NameServer] | None = core.arg(default=None)

        registrant_contact: RegistrantContact | None = core.arg(default=None)

        registrant_privacy: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tech_contact: TechContact | None = core.arg(default=None)

        tech_privacy: bool | core.BoolOut | None = core.arg(default=None)

        transfer_lock: bool | core.BoolOut | None = core.arg(default=None)
