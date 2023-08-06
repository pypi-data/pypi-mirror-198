import terrascript.core as core


@core.schema
class StopCondition(core.Schema):

    source: str | core.StringOut = core.attr(str)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        source: str | core.StringOut,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StopCondition.Args(
                source=source,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source: str | core.StringOut = core.arg()

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ResourceTag(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceTag.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Filter(core.Schema):

    path: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        path: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                path=path,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Target(core.Schema):

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    resource_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    resource_tag: list[ResourceTag] | core.ArrayOut[ResourceTag] | None = core.attr(
        ResourceTag, default=None, kind=core.Kind.array
    )

    resource_type: str | core.StringOut = core.attr(str)

    selection_mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        resource_type: str | core.StringOut,
        selection_mode: str | core.StringOut,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        resource_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        resource_tag: list[ResourceTag] | core.ArrayOut[ResourceTag] | None = None,
    ):
        super().__init__(
            args=Target.Args(
                name=name,
                resource_type=resource_type,
                selection_mode=selection_mode,
                filter=filter,
                resource_arns=resource_arns,
                resource_tag=resource_tag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        resource_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        resource_tag: list[ResourceTag] | core.ArrayOut[ResourceTag] | None = core.arg(default=None)

        resource_type: str | core.StringOut = core.arg()

        selection_mode: str | core.StringOut = core.arg()


@core.schema
class Parameter(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Parameter.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ActionTarget(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ActionTarget.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Action(core.Schema):

    action_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    start_after: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    target: ActionTarget | None = core.attr(ActionTarget, default=None)

    def __init__(
        self,
        *,
        action_id: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = None,
        start_after: list[str] | core.ArrayOut[core.StringOut] | None = None,
        target: ActionTarget | None = None,
    ):
        super().__init__(
            args=Action.Args(
                action_id=action_id,
                name=name,
                description=description,
                parameter=parameter,
                start_after=start_after,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.arg(default=None)

        start_after: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        target: ActionTarget | None = core.arg(default=None)


@core.resource(type="aws_fis_experiment_template", namespace="fis")
class ExperimentTemplate(core.Resource):
    """
    (Required) Action to be performed during an experiment. See below.
    """

    action: list[Action] | core.ArrayOut[Action] = core.attr(Action, kind=core.Kind.array)

    """
    (Required) Description for the experiment template.
    """
    description: str | core.StringOut = core.attr(str)

    """
    Experiment Template ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ARN of an IAM role that grants the AWS FIS service permission to perform service actions
    on your behalf.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Required) When an ongoing experiment should be stopped. See below.
    """
    stop_condition: list[StopCondition] | core.ArrayOut[StopCondition] = core.attr(
        StopCondition, kind=core.Kind.array
    )

    """
    (Optional) Key-value mapping of tags. If configured with a provider [`default_tags` configuration bl
    ock](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-bl
    ock) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Target of an action. See below.
    """
    target: list[Target] | core.ArrayOut[Target] | None = core.attr(
        Target, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        action: list[Action] | core.ArrayOut[Action],
        description: str | core.StringOut,
        role_arn: str | core.StringOut,
        stop_condition: list[StopCondition] | core.ArrayOut[StopCondition],
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target: list[Target] | core.ArrayOut[Target] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ExperimentTemplate.Args(
                action=action,
                description=description,
                role_arn=role_arn,
                stop_condition=stop_condition,
                tags=tags,
                tags_all=tags_all,
                target=target,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: list[Action] | core.ArrayOut[Action] = core.arg()

        description: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        stop_condition: list[StopCondition] | core.ArrayOut[StopCondition] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target: list[Target] | core.ArrayOut[Target] | None = core.arg(default=None)
