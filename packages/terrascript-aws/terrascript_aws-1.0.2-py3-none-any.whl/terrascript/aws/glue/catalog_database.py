import terrascript.core as core


@core.schema
class TargetDatabase(core.Schema):

    catalog_id: str | core.StringOut = core.attr(str)

    database_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        catalog_id: str | core.StringOut,
        database_name: str | core.StringOut,
    ):
        super().__init__(
            args=TargetDatabase.Args(
                catalog_id=catalog_id,
                database_name=database_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut = core.arg()

        database_name: str | core.StringOut = core.arg()


@core.schema
class Principal(core.Schema):

    data_lake_principal_identifier: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        data_lake_principal_identifier: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Principal.Args(
                data_lake_principal_identifier=data_lake_principal_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_lake_principal_identifier: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CreateTableDefaultPermission(core.Schema):

    permissions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    principal: Principal | None = core.attr(Principal, default=None)

    def __init__(
        self,
        *,
        permissions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        principal: Principal | None = None,
    ):
        super().__init__(
            args=CreateTableDefaultPermission.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        principal: Principal | None = core.arg(default=None)


@core.resource(type="aws_glue_catalog_database", namespace="aws_glue")
class CatalogDatabase(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    create_table_default_permission: list[CreateTableDefaultPermission] | core.ArrayOut[
        CreateTableDefaultPermission
    ] | None = core.attr(
        CreateTableDefaultPermission, default=None, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    location_uri: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    target_database: TargetDatabase | None = core.attr(TargetDatabase, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        create_table_default_permission: list[CreateTableDefaultPermission]
        | core.ArrayOut[CreateTableDefaultPermission]
        | None = None,
        description: str | core.StringOut | None = None,
        location_uri: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_database: TargetDatabase | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CatalogDatabase.Args(
                name=name,
                catalog_id=catalog_id,
                create_table_default_permission=create_table_default_permission,
                description=description,
                location_uri=location_uri,
                parameters=parameters,
                target_database=target_database,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        create_table_default_permission: list[CreateTableDefaultPermission] | core.ArrayOut[
            CreateTableDefaultPermission
        ] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        location_uri: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_database: TargetDatabase | None = core.arg(default=None)
