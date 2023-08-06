import terrascript.core as core


@core.schema
class PhysicalConnectionRequirements(core.Schema):

    availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    security_group_id_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        availability_zone: str | core.StringOut | None = None,
        security_group_id_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PhysicalConnectionRequirements.Args(
                availability_zone=availability_zone,
                security_group_id_list=security_group_id_list,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        security_group_id_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_glue_connection", namespace="glue")
class Connection(core.Resource):
    """
    The ARN of the Glue Connection.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    connection_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    connection_type: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Catalog ID and name of the connection
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    match_criteria: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
    """
    physical_connection_requirements: PhysicalConnectionRequirements | None = core.attr(
        PhysicalConnectionRequirements, default=None
    )

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        connection_properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        connection_type: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        match_criteria: list[str] | core.ArrayOut[core.StringOut] | None = None,
        physical_connection_requirements: PhysicalConnectionRequirements | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Connection.Args(
                name=name,
                catalog_id=catalog_id,
                connection_properties=connection_properties,
                connection_type=connection_type,
                description=description,
                match_criteria=match_criteria,
                physical_connection_requirements=physical_connection_requirements,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        connection_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        connection_type: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        match_criteria: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        physical_connection_requirements: PhysicalConnectionRequirements | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
