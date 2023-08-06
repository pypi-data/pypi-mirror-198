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
class Schedule(core.Schema):

    pipeline_execution_start_condition: str | core.StringOut = core.attr(str, computed=True)

    schedule_expression: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        pipeline_execution_start_condition: str | core.StringOut,
        schedule_expression: str | core.StringOut,
    ):
        super().__init__(
            args=Schedule.Args(
                pipeline_execution_start_condition=pipeline_execution_start_condition,
                schedule_expression=schedule_expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pipeline_execution_start_condition: str | core.StringOut = core.arg()

        schedule_expression: str | core.StringOut = core.arg()


@core.data(type="aws_imagebuilder_image_pipeline", namespace="imagebuilder")
class DsImagePipeline(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the image pipeline.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    Amazon Resource Name (ARN) of the container recipe.
    """
    container_recipe_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the image pipeline was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the image pipeline was last run.
    """
    date_last_run: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the image pipeline will run next.
    """
    date_next_run: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the image pipeline was updated.
    """
    date_updated: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the image pipeline.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

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
    Name of the image pipeline.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Platform of the image pipeline.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    List of an object with schedule settings.
    """
    schedule: list[Schedule] | core.ArrayOut[Schedule] = core.attr(
        Schedule, computed=True, kind=core.Kind.array
    )

    """
    Status of the image pipeline.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags for the image pipeline.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsImagePipeline.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
