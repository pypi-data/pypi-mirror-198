import terrascript.core as core


@core.schema
class SelfManagedActiveDirectoryConfiguration(core.Schema):

    dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    domain_name: str | core.StringOut = core.attr(str)

    file_system_administrators_group: str | core.StringOut | None = core.attr(str, default=None)

    organizational_unit_distinguished_name: str | core.StringOut | None = core.attr(
        str, default=None
    )

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        dns_ips: list[str] | core.ArrayOut[core.StringOut],
        domain_name: str | core.StringOut,
        password: str | core.StringOut,
        username: str | core.StringOut,
        file_system_administrators_group: str | core.StringOut | None = None,
        organizational_unit_distinguished_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SelfManagedActiveDirectoryConfiguration.Args(
                dns_ips=dns_ips,
                domain_name=domain_name,
                password=password,
                username=username,
                file_system_administrators_group=file_system_administrators_group,
                organizational_unit_distinguished_name=organizational_unit_distinguished_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        domain_name: str | core.StringOut = core.arg()

        file_system_administrators_group: str | core.StringOut | None = core.arg(default=None)

        organizational_unit_distinguished_name: str | core.StringOut | None = core.arg(default=None)

        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class ActiveDirectoryConfiguration(core.Schema):

    netbios_name: str | core.StringOut | None = core.attr(str, default=None)

    self_managed_active_directory_configuration: SelfManagedActiveDirectoryConfiguration | None = (
        core.attr(SelfManagedActiveDirectoryConfiguration, default=None)
    )

    def __init__(
        self,
        *,
        netbios_name: str | core.StringOut | None = None,
        self_managed_active_directory_configuration: SelfManagedActiveDirectoryConfiguration
        | None = None,
    ):
        super().__init__(
            args=ActiveDirectoryConfiguration.Args(
                netbios_name=netbios_name,
                self_managed_active_directory_configuration=self_managed_active_directory_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        netbios_name: str | core.StringOut | None = core.arg(default=None)

        self_managed_active_directory_configuration: SelfManagedActiveDirectoryConfiguration | None = core.arg(
            default=None
        )


@core.schema
class Management(core.Schema):

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: str | core.StringOut,
        ip_addresses: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Management.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut = core.arg()

        ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Nfs(core.Schema):

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: str | core.StringOut,
        ip_addresses: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Nfs.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut = core.arg()

        ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Smb(core.Schema):

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: str | core.StringOut,
        ip_addresses: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Smb.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut = core.arg()

        ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Iscsi(core.Schema):

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: str | core.StringOut,
        ip_addresses: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Iscsi.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut = core.arg()

        ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Endpoints(core.Schema):

    iscsi: list[Iscsi] | core.ArrayOut[Iscsi] = core.attr(
        Iscsi, computed=True, kind=core.Kind.array
    )

    management: list[Management] | core.ArrayOut[Management] = core.attr(
        Management, computed=True, kind=core.Kind.array
    )

    nfs: list[Nfs] | core.ArrayOut[Nfs] = core.attr(Nfs, computed=True, kind=core.Kind.array)

    smb: list[Smb] | core.ArrayOut[Smb] = core.attr(Smb, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        iscsi: list[Iscsi] | core.ArrayOut[Iscsi],
        management: list[Management] | core.ArrayOut[Management],
        nfs: list[Nfs] | core.ArrayOut[Nfs],
        smb: list[Smb] | core.ArrayOut[Smb],
    ):
        super().__init__(
            args=Endpoints.Args(
                iscsi=iscsi,
                management=management,
                nfs=nfs,
                smb=smb,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iscsi: list[Iscsi] | core.ArrayOut[Iscsi] = core.arg()

        management: list[Management] | core.ArrayOut[Management] = core.arg()

        nfs: list[Nfs] | core.ArrayOut[Nfs] = core.arg()

        smb: list[Smb] | core.ArrayOut[Smb] = core.arg()


@core.resource(type="aws_fsx_ontap_storage_virtual_machine", namespace="aws_fsx")
class OntapStorageVirtualMachine(core.Resource):

    active_directory_configuration: ActiveDirectoryConfiguration | None = core.attr(
        ActiveDirectoryConfiguration, default=None
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    endpoints: list[Endpoints] | core.ArrayOut[Endpoints] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    file_system_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    root_volume_security_style: str | core.StringOut | None = core.attr(str, default=None)

    subtype: str | core.StringOut = core.attr(str, computed=True)

    svm_admin_password: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    uuid: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        file_system_id: str | core.StringOut,
        name: str | core.StringOut,
        active_directory_configuration: ActiveDirectoryConfiguration | None = None,
        root_volume_security_style: str | core.StringOut | None = None,
        svm_admin_password: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OntapStorageVirtualMachine.Args(
                file_system_id=file_system_id,
                name=name,
                active_directory_configuration=active_directory_configuration,
                root_volume_security_style=root_volume_security_style,
                svm_admin_password=svm_admin_password,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        active_directory_configuration: ActiveDirectoryConfiguration | None = core.arg(default=None)

        file_system_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        root_volume_security_style: str | core.StringOut | None = core.arg(default=None)

        svm_admin_password: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
