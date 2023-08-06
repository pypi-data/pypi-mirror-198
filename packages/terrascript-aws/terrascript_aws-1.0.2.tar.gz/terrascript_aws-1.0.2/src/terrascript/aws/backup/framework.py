import terrascript.core as core


@core.schema
class Scope(core.Schema):

    compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Scope.Args(
                compliance_resource_ids=compliance_resource_ids,
                compliance_resource_types=compliance_resource_types,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class InputParameter(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InputParameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Control(core.Schema):

    input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = core.attr(
        InputParameter, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    scope: Scope | None = core.attr(Scope, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = None,
        scope: Scope | None = None,
    ):
        super().__init__(
            args=Control.Args(
                name=name,
                input_parameter=input_parameter,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        scope: Scope | None = core.arg(default=None)


@core.resource(type="aws_backup_framework", namespace="aws_backup")
class Framework(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    control: list[Control] | core.ArrayOut[Control] = core.attr(Control, kind=core.Kind.array)

    creation_time: str | core.StringOut = core.attr(str, computed=True)

    deployment_status: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

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
        control: list[Control] | core.ArrayOut[Control],
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Framework.Args(
                control=control,
                name=name,
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
        control: list[Control] | core.ArrayOut[Control] = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
