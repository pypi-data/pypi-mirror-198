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


@core.resource(type="aws_route53domains_registered_domain", namespace="aws_route53domains")
class RegisteredDomain(core.Resource):

    abuse_contact_email: str | core.StringOut = core.attr(str, computed=True)

    abuse_contact_phone: str | core.StringOut = core.attr(str, computed=True)

    admin_contact: AdminContact | None = core.attr(AdminContact, default=None, computed=True)

    admin_privacy: bool | core.BoolOut | None = core.attr(bool, default=None)

    auto_renew: bool | core.BoolOut | None = core.attr(bool, default=None)

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut = core.attr(str)

    expiration_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name_server: list[NameServer] | core.ArrayOut[NameServer] | None = core.attr(
        NameServer, default=None, computed=True, kind=core.Kind.array
    )

    registrant_contact: RegistrantContact | None = core.attr(
        RegistrantContact, default=None, computed=True
    )

    registrant_privacy: bool | core.BoolOut | None = core.attr(bool, default=None)

    registrar_name: str | core.StringOut = core.attr(str, computed=True)

    registrar_url: str | core.StringOut = core.attr(str, computed=True)

    reseller: str | core.StringOut = core.attr(str, computed=True)

    status_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tech_contact: TechContact | None = core.attr(TechContact, default=None, computed=True)

    tech_privacy: bool | core.BoolOut | None = core.attr(bool, default=None)

    transfer_lock: bool | core.BoolOut | None = core.attr(bool, default=None)

    updated_date: str | core.StringOut = core.attr(str, computed=True)

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
