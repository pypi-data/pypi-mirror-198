import terrascript.core as core


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


@core.resource(type="aws_elastic_beanstalk_configuration_template", namespace="elastic_beanstalk")
class ConfigurationTemplate(core.Resource):

    application: str | core.StringOut = core.attr(str)

    """
    (Optional) Short description of the Template
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    environment_id: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A unique name for this Template.
    """
    name: str | core.StringOut = core.attr(str)

    setting: list[Setting] | core.ArrayOut[Setting] | None = core.attr(
        Setting, default=None, computed=True, kind=core.Kind.array
    )

    solution_stack_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        application: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        environment_id: str | core.StringOut | None = None,
        setting: list[Setting] | core.ArrayOut[Setting] | None = None,
        solution_stack_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationTemplate.Args(
                application=application,
                name=name,
                description=description,
                environment_id=environment_id,
                setting=setting,
                solution_stack_name=solution_stack_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        environment_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        setting: list[Setting] | core.ArrayOut[Setting] | None = core.arg(default=None)

        solution_stack_name: str | core.StringOut | None = core.arg(default=None)
