import terrascript.core as core


@core.schema
class ServiceAccountCredentials(core.Schema):

    account_name: str | core.StringOut = core.attr(str)

    account_password: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        account_name: str | core.StringOut,
        account_password: str | core.StringOut,
    ):
        super().__init__(
            args=ServiceAccountCredentials.Args(
                account_name=account_name,
                account_password=account_password,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_name: str | core.StringOut = core.arg()

        account_password: str | core.StringOut = core.arg()


@core.resource(type="aws_appstream_directory_config", namespace="appstream")
class DirectoryConfig(core.Resource):
    """
    Date and time, in UTC and extended RFC 3339 format, when the directory config was created.
    """

    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Fully qualified name of the directory.
    """
    directory_name: str | core.StringOut = core.attr(str)

    """
    Unique identifier (ID) of the appstream directory config.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Distinguished names of the organizational units for computer accounts.
    """
    organizational_unit_distinguished_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) Configuration block for the name of the directory and organizational unit (OU) to use to
    join the directory config to a Microsoft Active Directory domain. See [`service_account_credentials`
    ](#service_account_credentials) below.
    """
    service_account_credentials: ServiceAccountCredentials = core.attr(ServiceAccountCredentials)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_name: str | core.StringOut,
        organizational_unit_distinguished_names: list[str] | core.ArrayOut[core.StringOut],
        service_account_credentials: ServiceAccountCredentials,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryConfig.Args(
                directory_name=directory_name,
                organizational_unit_distinguished_names=organizational_unit_distinguished_names,
                service_account_credentials=service_account_credentials,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_name: str | core.StringOut = core.arg()

        organizational_unit_distinguished_names: list[str] | core.ArrayOut[
            core.StringOut
        ] = core.arg()

        service_account_credentials: ServiceAccountCredentials = core.arg()
