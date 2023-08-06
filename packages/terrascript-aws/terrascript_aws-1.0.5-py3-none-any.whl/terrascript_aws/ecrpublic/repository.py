import terrascript.core as core


@core.schema
class CatalogData(core.Schema):

    about_text: str | core.StringOut | None = core.attr(str, default=None)

    architectures: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    logo_image_blob: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    operating_systems: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    usage_text: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        about_text: str | core.StringOut | None = None,
        architectures: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        logo_image_blob: str | core.StringOut | None = None,
        operating_systems: list[str] | core.ArrayOut[core.StringOut] | None = None,
        usage_text: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CatalogData.Args(
                about_text=about_text,
                architectures=architectures,
                description=description,
                logo_image_blob=logo_image_blob,
                operating_systems=operating_systems,
                usage_text=usage_text,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        about_text: str | core.StringOut | None = core.arg(default=None)

        architectures: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        logo_image_blob: str | core.StringOut | None = core.arg(default=None)

        operating_systems: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        usage_text: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ecrpublic_repository", namespace="ecrpublic")
class Repository(core.Resource):
    """
    Full ARN of the repository.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Catalog data configuration for the repository. See [below for schema](#catalog_data).
    """
    catalog_data: CatalogData | None = core.attr(CatalogData, default=None)

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The repository name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The registry ID where the repository was created.
    """
    registry_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the repository.
    """
    repository_name: str | core.StringOut = core.attr(str)

    """
    The URI of the repository.
    """
    repository_uri: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        repository_name: str | core.StringOut,
        catalog_data: CatalogData | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Repository.Args(
                repository_name=repository_name,
                catalog_data=catalog_data,
                force_destroy=force_destroy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_data: CatalogData | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        repository_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
