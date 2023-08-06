import terrascript.core as core


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


@core.schema
class Schedule(core.Schema):

    pipeline_execution_start_condition: str | core.StringOut | None = core.attr(str, default=None)

    schedule_expression: str | core.StringOut = core.attr(str)

    timezone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        schedule_expression: str | core.StringOut,
        pipeline_execution_start_condition: str | core.StringOut | None = None,
        timezone: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Schedule.Args(
                schedule_expression=schedule_expression,
                pipeline_execution_start_condition=pipeline_execution_start_condition,
                timezone=timezone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pipeline_execution_start_condition: str | core.StringOut | None = core.arg(default=None)

        schedule_expression: str | core.StringOut = core.arg()

        timezone: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_imagebuilder_image_pipeline", namespace="imagebuilder")
class ImagePipeline(core.Resource):
    """
    Amazon Resource Name (ARN) of the image pipeline.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of the container recipe.
    """
    container_recipe_arn: str | core.StringOut | None = core.attr(str, default=None)

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
    (Optional) Description of the image pipeline.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

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
    (Required) Name of the image pipeline.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Platform of the image pipeline.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block with schedule settings. Detailed below.
    """
    schedule: Schedule | None = core.attr(Schedule, default=None)

    """
    (Optional) Status of the image pipeline. Valid values are `DISABLED` and `ENABLED`. Defaults to `ENA
    BLED`.
    """
    status: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags for the image pipeline. If configured with a provider [`de
    fault_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#d
    efault_tags-configuration-block) present, tags with matching keys will overwrite those defined at th
    e provider-level.
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
        infrastructure_configuration_arn: str | core.StringOut,
        name: str | core.StringOut,
        container_recipe_arn: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        distribution_configuration_arn: str | core.StringOut | None = None,
        enhanced_image_metadata_enabled: bool | core.BoolOut | None = None,
        image_recipe_arn: str | core.StringOut | None = None,
        image_tests_configuration: ImageTestsConfiguration | None = None,
        schedule: Schedule | None = None,
        status: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ImagePipeline.Args(
                infrastructure_configuration_arn=infrastructure_configuration_arn,
                name=name,
                container_recipe_arn=container_recipe_arn,
                description=description,
                distribution_configuration_arn=distribution_configuration_arn,
                enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
                image_recipe_arn=image_recipe_arn,
                image_tests_configuration=image_tests_configuration,
                schedule=schedule,
                status=status,
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

        description: str | core.StringOut | None = core.arg(default=None)

        distribution_configuration_arn: str | core.StringOut | None = core.arg(default=None)

        enhanced_image_metadata_enabled: bool | core.BoolOut | None = core.arg(default=None)

        image_recipe_arn: str | core.StringOut | None = core.arg(default=None)

        image_tests_configuration: ImageTestsConfiguration | None = core.arg(default=None)

        infrastructure_configuration_arn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        schedule: Schedule | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
