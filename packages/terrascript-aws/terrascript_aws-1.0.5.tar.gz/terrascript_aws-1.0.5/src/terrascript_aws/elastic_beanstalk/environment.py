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


@core.resource(type="aws_elastic_beanstalk_environment", namespace="elastic_beanstalk")
class Environment(core.Resource):

    all_settings: list[AllSettings] | core.ArrayOut[AllSettings] = core.attr(
        AllSettings, computed=True, kind=core.Kind.array
    )

    application: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The autoscaling groups used by this Environment.
    """
    autoscaling_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Fully qualified DNS name for this Environment.
    """
    cname: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Prefix to use for the fully qualified DNS name of
    """
    cname_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Short description of the Environment
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The URL to the Load Balancer for this Environment
    """
    endpoint_url: str | core.StringOut = core.attr(str, computed=True)

    """
    ID of the Elastic Beanstalk Environment.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Instances used by this Environment.
    """
    instances: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Launch configurations in use by this Environment.
    """
    launch_configurations: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Elastic load balancers in use by this Environment.
    """
    load_balancers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) A unique name for this Environment. This name is used
    """
    name: str | core.StringOut = core.attr(str)

    platform_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    poll_interval: str | core.StringOut | None = core.attr(str, default=None)

    """
    SQS queues in use by this Environment.
    """
    queues: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    setting: list[Setting] | core.ArrayOut[Setting] | None = core.attr(
        Setting, default=None, kind=core.Kind.array
    )

    solution_stack_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A set of tags to apply to the Environment. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-l
    evel.
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

    template_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Elastic Beanstalk Environment tier. Valid values are `Worker`
    """
    tier: str | core.StringOut | None = core.attr(str, default=None)

    """
    Autoscaling triggers in use by this Environment.
    """
    triggers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The name of the Elastic Beanstalk Application Version
    """
    version_label: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Default `20m`) The maximum
    """
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
