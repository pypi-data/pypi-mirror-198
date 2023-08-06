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


@core.resource(type="aws_appconfig_environment", namespace="aws_appconfig")
class Environment(core.Resource):

    application_id: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    environment_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    monitor: list[Monitor] | core.ArrayOut[Monitor] | None = core.attr(
        Monitor, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    state: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
