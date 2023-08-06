import terrascript.core as core


@core.schema
class VpcSettings(core.Schema):

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcSettings.Args(
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.resource(type="aws_directory_service_region", namespace="ds")
class DirectoryServiceRegion(core.Resource):
    """
    (Optional) The number of domain controllers desired in the replicated directory. Minimum value of `2
    .
    """

    desired_number_of_domain_controllers: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    (Required) The identifier of the directory to which you want to add Region replication.
    """
    directory_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Region where you want to add domain controllers for replication.
    """
    region_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Map of tags to assign to this resource. If configured with a provider [`default_tags` con
    figuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-
    block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configurati
    on-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) VPC information in the replicated Region. Detailed below.
    """
    vpc_settings: VpcSettings = core.attr(VpcSettings)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: str | core.StringOut,
        region_name: str | core.StringOut,
        vpc_settings: VpcSettings,
        desired_number_of_domain_controllers: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceRegion.Args(
                directory_id=directory_id,
                region_name=region_name,
                vpc_settings=vpc_settings,
                desired_number_of_domain_controllers=desired_number_of_domain_controllers,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        desired_number_of_domain_controllers: int | core.IntOut | None = core.arg(default=None)

        directory_id: str | core.StringOut = core.arg()

        region_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_settings: VpcSettings = core.arg()
