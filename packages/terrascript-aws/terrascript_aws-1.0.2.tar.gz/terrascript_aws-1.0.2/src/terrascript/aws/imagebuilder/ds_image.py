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


@core.data(type="aws_imagebuilder_image", namespace="aws_imagebuilder")
class DsImage(core.Data):

    arn: str | core.StringOut = core.attr(str)

    build_version_arn: str | core.StringOut = core.attr(str, computed=True)

    container_recipe_arn: str | core.StringOut = core.attr(str, computed=True)

    date_created: str | core.StringOut = core.attr(str, computed=True)

    distribution_configuration_arn: str | core.StringOut = core.attr(str, computed=True)

    enhanced_image_metadata_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_recipe_arn: str | core.StringOut = core.attr(str, computed=True)

    image_tests_configuration: list[ImageTestsConfiguration] | core.ArrayOut[
        ImageTestsConfiguration
    ] = core.attr(ImageTestsConfiguration, computed=True, kind=core.Kind.array)

    infrastructure_configuration_arn: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    os_version: str | core.StringOut = core.attr(str, computed=True)

    output_resources: list[OutputResources] | core.ArrayOut[OutputResources] = core.attr(
        OutputResources, computed=True, kind=core.Kind.array
    )

    platform: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
