import terrascript.core as core


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


@core.data(type="aws_imagebuilder_image_pipeline", namespace="aws_imagebuilder")
class DsImagePipeline(core.Data):

    arn: str | core.StringOut = core.attr(str)

    container_recipe_arn: str | core.StringOut = core.attr(str, computed=True)

    date_created: str | core.StringOut = core.attr(str, computed=True)

    date_last_run: str | core.StringOut = core.attr(str, computed=True)

    date_next_run: str | core.StringOut = core.attr(str, computed=True)

    date_updated: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    distribution_configuration_arn: str | core.StringOut = core.attr(str, computed=True)

    enhanced_image_metadata_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_recipe_arn: str | core.StringOut = core.attr(str, computed=True)

    image_tests_configuration: list[ImageTestsConfiguration] | core.ArrayOut[
        ImageTestsConfiguration
    ] = core.attr(ImageTestsConfiguration, computed=True, kind=core.Kind.array)

    infrastructure_configuration_arn: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    platform: str | core.StringOut = core.attr(str, computed=True)

    schedule: list[Schedule] | core.ArrayOut[Schedule] = core.attr(
        Schedule, computed=True, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

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
