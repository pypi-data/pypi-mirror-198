import terrascript.core as core


@core.schema
class AllSettings(core.Schema):

    name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut = core.attr(str)

    resource: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        namespace: str | core.StringOut,
        value: str | core.StringOut,
        resource: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AllSettings.Args(
                name=name,
                namespace=namespace,
                value=value,
                resource=resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()

        resource: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut = core.arg()


@core.schema
class Setting(core.Schema):

    name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut = core.attr(str)

    resource: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        namespace: str | core.StringOut,
        value: str | core.StringOut,
        resource: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Setting.Args(
                name=name,
                namespace=namespace,
                value=value,
                resource=resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()

        resource: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_elastic_beanstalk_environment", namespace="aws_elastic_beanstalk")
class Environment(core.Resource):

    all_settings: list[AllSettings] | core.ArrayOut[AllSettings] = core.attr(
        AllSettings, computed=True, kind=core.Kind.array
    )

    application: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    autoscaling_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cname: str | core.StringOut = core.attr(str, computed=True)

    cname_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    endpoint_url: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instances: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    launch_configurations: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    load_balancers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    platform_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    poll_interval: str | core.StringOut | None = core.attr(str, default=None)

    queues: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    setting: list[Setting] | core.ArrayOut[Setting] | None = core.attr(
        Setting, default=None, kind=core.Kind.array
    )

    solution_stack_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    template_name: str | core.StringOut | None = core.attr(str, default=None)

    tier: str | core.StringOut | None = core.attr(str, default=None)

    triggers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    version_label: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    wait_for_ready_timeout: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        application: str | core.StringOut,
        name: str | core.StringOut,
        cname_prefix: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        platform_arn: str | core.StringOut | None = None,
        poll_interval: str | core.StringOut | None = None,
        setting: list[Setting] | core.ArrayOut[Setting] | None = None,
        solution_stack_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        template_name: str | core.StringOut | None = None,
        tier: str | core.StringOut | None = None,
        version_label: str | core.StringOut | None = None,
        wait_for_ready_timeout: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Environment.Args(
                application=application,
                name=name,
                cname_prefix=cname_prefix,
                description=description,
                platform_arn=platform_arn,
                poll_interval=poll_interval,
                setting=setting,
                solution_stack_name=solution_stack_name,
                tags=tags,
                tags_all=tags_all,
                template_name=template_name,
                tier=tier,
                version_label=version_label,
                wait_for_ready_timeout=wait_for_ready_timeout,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application: str | core.StringOut = core.arg()

        cname_prefix: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        platform_arn: str | core.StringOut | None = core.arg(default=None)

        poll_interval: str | core.StringOut | None = core.arg(default=None)

        setting: list[Setting] | core.ArrayOut[Setting] | None = core.arg(default=None)

        solution_stack_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        template_name: str | core.StringOut | None = core.arg(default=None)

        tier: str | core.StringOut | None = core.arg(default=None)

        version_label: str | core.StringOut | None = core.arg(default=None)

        wait_for_ready_timeout: str | core.StringOut | None = core.arg(default=None)
