import terrascript.core as core


@core.schema
class CreateDatabaseDefaultPermissions(core.Schema):

    permissions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    principal: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        permissions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        principal: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CreateDatabaseDefaultPermissions.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        principal: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CreateTableDefaultPermissions(core.Schema):

    permissions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    principal: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        permissions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        principal: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CreateTableDefaultPermissions.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        principal: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_lakeformation_data_lake_settings", namespace="lakeformation")
class DataLakeSettings(core.Resource):

    admins: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    catalog_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Up to three configuration blocks of principal permissions for default create database per
    missions. Detailed below.
    """
    create_database_default_permissions: list[CreateDatabaseDefaultPermissions] | core.ArrayOut[
        CreateDatabaseDefaultPermissions
    ] | None = core.attr(
        CreateDatabaseDefaultPermissions, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Up to three configuration blocks of principal permissions for default create table permis
    sions. Detailed below.
    """
    create_table_default_permissions: list[CreateTableDefaultPermissions] | core.ArrayOut[
        CreateTableDefaultPermissions
    ] | None = core.attr(
        CreateTableDefaultPermissions, default=None, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    trusted_resource_owners: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        admins: list[str] | core.ArrayOut[core.StringOut] | None = None,
        catalog_id: str | core.StringOut | None = None,
        create_database_default_permissions: list[CreateDatabaseDefaultPermissions]
        | core.ArrayOut[CreateDatabaseDefaultPermissions]
        | None = None,
        create_table_default_permissions: list[CreateTableDefaultPermissions]
        | core.ArrayOut[CreateTableDefaultPermissions]
        | None = None,
        trusted_resource_owners: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataLakeSettings.Args(
                admins=admins,
                catalog_id=catalog_id,
                create_database_default_permissions=create_database_default_permissions,
                create_table_default_permissions=create_table_default_permissions,
                trusted_resource_owners=trusted_resource_owners,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admins: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        catalog_id: str | core.StringOut | None = core.arg(default=None)

        create_database_default_permissions: list[CreateDatabaseDefaultPermissions] | core.ArrayOut[
            CreateDatabaseDefaultPermissions
        ] | None = core.arg(default=None)

        create_table_default_permissions: list[CreateTableDefaultPermissions] | core.ArrayOut[
            CreateTableDefaultPermissions
        ] | None = core.arg(default=None)

        trusted_resource_owners: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
