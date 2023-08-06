import terrascript.core as core


@core.schema
class ResourceUris(core.Schema):

    resource_type: str | core.StringOut = core.attr(str)

    uri: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_type: str | core.StringOut,
        uri: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceUris.Args(
                resource_type=resource_type,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_type: str | core.StringOut = core.arg()

        uri: str | core.StringOut = core.arg()


@core.resource(type="aws_glue_user_defined_function", namespace="glue")
class UserDefinedFunction(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ID of the Glue Catalog to create the function in. If omitted, this defaults to the AWS Ac
    count ID.
    """
    catalog_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The Java class that contains the function code.
    """
    class_name: str | core.StringOut = core.attr(str)

    create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Database to create the Function.
    """
    database_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the function.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The owner of the function.
    """
    owner_name: str | core.StringOut = core.attr(str)

    """
    (Required) The owner type. can be one of `USER`, `ROLE`, and `GROUP`.
    """
    owner_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The configuration block for Resource URIs. See [resource uris](#resource-uris) below for
    more details.
    """
    resource_uris: list[ResourceUris] | core.ArrayOut[ResourceUris] | None = core.attr(
        ResourceUris, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        class_name: str | core.StringOut,
        database_name: str | core.StringOut,
        name: str | core.StringOut,
        owner_name: str | core.StringOut,
        owner_type: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        resource_uris: list[ResourceUris] | core.ArrayOut[ResourceUris] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserDefinedFunction.Args(
                class_name=class_name,
                database_name=database_name,
                name=name,
                owner_name=owner_name,
                owner_type=owner_type,
                catalog_id=catalog_id,
                resource_uris=resource_uris,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        class_name: str | core.StringOut = core.arg()

        database_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        owner_name: str | core.StringOut = core.arg()

        owner_type: str | core.StringOut = core.arg()

        resource_uris: list[ResourceUris] | core.ArrayOut[ResourceUris] | None = core.arg(
            default=None
        )
