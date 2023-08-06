import terrascript.core as core


@core.schema
class AppversionLifecycle(core.Schema):

    delete_source_from_s3: bool | core.BoolOut | None = core.attr(bool, default=None)

    max_age_in_days: int | core.IntOut | None = core.attr(int, default=None)

    max_count: int | core.IntOut | None = core.attr(int, default=None)

    service_role: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        service_role: str | core.StringOut,
        delete_source_from_s3: bool | core.BoolOut | None = None,
        max_age_in_days: int | core.IntOut | None = None,
        max_count: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AppversionLifecycle.Args(
                service_role=service_role,
                delete_source_from_s3=delete_source_from_s3,
                max_age_in_days=max_age_in_days,
                max_count=max_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_source_from_s3: bool | core.BoolOut | None = core.arg(default=None)

        max_age_in_days: int | core.IntOut | None = core.arg(default=None)

        max_count: int | core.IntOut | None = core.arg(default=None)

        service_role: str | core.StringOut = core.arg()


@core.resource(type="aws_elastic_beanstalk_application", namespace="elastic_beanstalk")
class Application(core.Resource):

    appversion_lifecycle: AppversionLifecycle | None = core.attr(AppversionLifecycle, default=None)

    """
    The ARN assigned by AWS for this Elastic Beanstalk Application.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Short description of the application
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the application, must be unique within your account
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of tags for the Elastic Beanstalk Application. If configured with a provide
    r [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/
    docs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined
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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        appversion_lifecycle: AppversionLifecycle | None = None,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                name=name,
                appversion_lifecycle=appversion_lifecycle,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        appversion_lifecycle: AppversionLifecycle | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
