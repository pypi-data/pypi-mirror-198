import terrascript.core as core


@core.schema
class Amis(core.Schema):

    account_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    image: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        account_id: str | core.StringOut,
        description: str | core.StringOut,
        image: str | core.StringOut,
        name: str | core.StringOut,
        region: str | core.StringOut,
    ):
        super().__init__(
            args=Amis.Args(
                account_id=account_id,
                description=description,
                image=image,
                name=name,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut = core.arg()

        description: str | core.StringOut = core.arg()

        image: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        region: str | core.StringOut = core.arg()


@core.schema
class OutputResources(core.Schema):

    amis: list[Amis] | core.ArrayOut[Amis] = core.attr(Amis, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        amis: list[Amis] | core.ArrayOut[Amis],
    ):
        super().__init__(
            args=OutputResources.Args(
                amis=amis,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amis: list[Amis] | core.ArrayOut[Amis] = core.arg()


@core.schema
class ImageTestsConfiguration(core.Schema):

    image_tests_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    timeout_minutes: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        image_tests_enabled: bool | core.BoolOut | None = None,
        timeout_minutes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ImageTestsConfiguration.Args(
                image_tests_enabled=image_tests_enabled,
                timeout_minutes=timeout_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_tests_enabled: bool | core.BoolOut | None = core.arg(default=None)

        timeout_minutes: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_imagebuilder_image", namespace="imagebuilder")
class Image(core.Resource):
    """
    Amazon Resource Name (ARN) of the image.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) - Amazon Resource Name (ARN) of the container recipe.
    """
    container_recipe_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    Date the image was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of the Image Builder Distribution Configuration.
    """
    distribution_configuration_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether additional information about the image being created is collected. Defaults to `t
    rue`.
    """
    enhanced_image_metadata_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of the image recipe.
    """
    image_recipe_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block with image tests configuration. Detailed below.
    """
    image_tests_configuration: ImageTestsConfiguration | None = core.attr(
        ImageTestsConfiguration, default=None, computed=True
    )

    """
    (Required) Amazon Resource Name (ARN) of the Image Builder Infrastructure Configuration.
    """
    infrastructure_configuration_arn: str | core.StringOut = core.attr(str)

    """
    name` - Name of the AMI.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Operating System version of the image.
    """
    os_version: str | core.StringOut = core.attr(str, computed=True)

    """
    List of objects with resources created by the image.
    """
    output_resources: list[OutputResources] | core.ArrayOut[OutputResources] = core.attr(
        OutputResources, computed=True, kind=core.Kind.array
    )

    """
    Platform of the image.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags for the Image Builder Image. If configured with a provider
    [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/d
    ocs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined
    at the provider-level.
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

    """
    Version of the image.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        infrastructure_configuration_arn: str | core.StringOut,
        container_recipe_arn: str | core.StringOut | None = None,
        distribution_configuration_arn: str | core.StringOut | None = None,
        enhanced_image_metadata_enabled: bool | core.BoolOut | None = None,
        image_recipe_arn: str | core.StringOut | None = None,
        image_tests_configuration: ImageTestsConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Image.Args(
                infrastructure_configuration_arn=infrastructure_configuration_arn,
                container_recipe_arn=container_recipe_arn,
                distribution_configuration_arn=distribution_configuration_arn,
                enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
                image_recipe_arn=image_recipe_arn,
                image_tests_configuration=image_tests_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_recipe_arn: str | core.StringOut | None = core.arg(default=None)

        distribution_configuration_arn: str | core.StringOut | None = core.arg(default=None)

        enhanced_image_metadata_enabled: bool | core.BoolOut | None = core.arg(default=None)

        image_recipe_arn: str | core.StringOut | None = core.arg(default=None)

        image_tests_configuration: ImageTestsConfiguration | None = core.arg(default=None)

        infrastructure_configuration_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
