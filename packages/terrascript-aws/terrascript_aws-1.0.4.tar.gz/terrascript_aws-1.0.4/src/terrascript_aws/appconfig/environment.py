import terrascript.core as core


@core.schema
class Monitor(core.Schema):

    alarm_arn: str | core.StringOut = core.attr(str)

    alarm_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        alarm_arn: str | core.StringOut,
        alarm_role_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Monitor.Args(
                alarm_arn=alarm_arn,
                alarm_role_arn=alarm_role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarm_arn: str | core.StringOut = core.arg()

        alarm_role_arn: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_appconfig_environment", namespace="appconfig")
class Environment(core.Resource):
    """
    (Required, Forces new resource) The AppConfig application ID. Must be between 4 and 7 characters in
    length.
    """

    application_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the AppConfig Environment.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the environment. Can be at most 1024 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The AppConfig environment ID.
    """
    environment_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The AppConfig environment ID and application ID separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set of Amazon CloudWatch alarms to monitor during the deployment process. Maximum of 5. S
    ee [Monitor](#monitor) below for more details.
    """
    monitor: list[Monitor] | core.ArrayOut[Monitor] | None = core.attr(
        Monitor, default=None, kind=core.Kind.array
    )

    """
    (Required) The name for the environment. Must be between 1 and 64 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
        application_id: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        monitor: list[Monitor] | core.ArrayOut[Monitor] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Environment.Args(
                application_id=application_id,
                name=name,
                description=description,
                monitor=monitor,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        monitor: list[Monitor] | core.ArrayOut[Monitor] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
