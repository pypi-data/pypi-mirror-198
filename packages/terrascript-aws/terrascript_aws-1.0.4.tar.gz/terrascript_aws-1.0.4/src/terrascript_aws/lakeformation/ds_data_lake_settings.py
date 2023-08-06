import terrascript.core as core


@core.schema
class CreateTableDefaultPermissions(core.Schema):

    permissions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    principal: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        permissions: list[str] | core.ArrayOut[core.StringOut],
        principal: str | core.StringOut,
    ):
        super().__init__(
            args=CreateTableDefaultPermissions.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        principal: str | core.StringOut = core.arg()


@core.schema
class CreateDatabaseDefaultPermissions(core.Schema):

    permissions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    principal: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        permissions: list[str] | core.ArrayOut[core.StringOut],
        principal: str | core.StringOut,
    ):
        super().__init__(
            args=CreateDatabaseDefaultPermissions.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        principal: str | core.StringOut = core.arg()


@core.data(type="aws_lakeformation_data_lake_settings", namespace="lakeformation")
class DsDataLakeSettings(core.Data):

    admins: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    catalog_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    Up to three configuration blocks of principal permissions for default create database permissions. D
    etailed below.
    """
    create_database_default_permissions: list[CreateDatabaseDefaultPermissions] | core.ArrayOut[
        CreateDatabaseDefaultPermissions
    ] = core.attr(CreateDatabaseDefaultPermissions, computed=True, kind=core.Kind.array)

    """
    Up to three configuration blocks of principal permissions for default create table permissions. Deta
    iled below.
    """
    create_table_default_permissions: list[CreateTableDefaultPermissions] | core.ArrayOut[
        CreateTableDefaultPermissions
    ] = core.attr(CreateTableDefaultPermissions, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    trusted_resource_owners: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        catalog_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDataLakeSettings.Args(
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)
