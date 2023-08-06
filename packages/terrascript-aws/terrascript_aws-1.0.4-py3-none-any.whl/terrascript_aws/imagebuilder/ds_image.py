import terrascript.core as core


@core.schema
class ImageTestsConfiguration(core.Schema):

    image_tests_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    timeout_minutes: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        image_tests_enabled: bool | core.BoolOut,
        timeout_minutes: int | core.IntOut,
    ):
        super().__init__(
            args=ImageTestsConfiguration.Args(
                image_tests_enabled=image_tests_enabled,
                timeout_minutes=timeout_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_tests_enabled: bool | core.BoolOut = core.arg()

        timeout_minutes: int | core.IntOut = core.arg()


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


@core.data(type="aws_imagebuilder_image", namespace="imagebuilder")
class DsImage(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the image. The suffix can either be specified with wildcard
    s (`x.x.x`) to fetch the latest build version or a full build version (e.g., `2020.11.26/1`) to fetc
    h an exact version.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    Build version Amazon Resource Name (ARN) of the image. This will always have the `#.#.#/#` suffix.
    """
    build_version_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the container recipe.
    """
    container_recipe_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the image was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the Image Builder Distribution Configuration.
    """
    distribution_configuration_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether additional information about the image being created is collected.
    """
    enhanced_image_metadata_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the image recipe.
    """
    image_recipe_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    List of an object with image tests configuration.
    """
    image_tests_configuration: list[ImageTestsConfiguration] | core.ArrayOut[
        ImageTestsConfiguration
    ] = core.attr(ImageTestsConfiguration, computed=True, kind=core.Kind.array)

    """
    Amazon Resource Name (ARN) of the Image Builder Infrastructure Configuration.
    """
    infrastructure_configuration_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the image.
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
    Key-value map of resource tags for the image.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Version of the image.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsImage.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
