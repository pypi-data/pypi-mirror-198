import terrascript.core as core


@core.schema
class InputParameter(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=InputParameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Scope(core.Schema):

    compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut],
        compliance_resource_types: list[str] | core.ArrayOut[core.StringOut],
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
        compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Control(core.Schema):

    input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] = core.attr(
        InputParameter, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    scope: list[Scope] | core.ArrayOut[Scope] = core.attr(
        Scope, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter],
        name: str | core.StringOut,
        scope: list[Scope] | core.ArrayOut[Scope],
    ):
        super().__init__(
            args=Control.Args(
                input_parameter=input_parameter,
                name=name,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] = core.arg()

        name: str | core.StringOut = core.arg()

        scope: list[Scope] | core.ArrayOut[Scope] = core.arg()


@core.data(type="aws_backup_framework", namespace="aws_backup")
class DsFramework(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    control: list[Control] | core.ArrayOut[Control] = core.attr(
        Control, computed=True, kind=core.Kind.array
    )

    creation_time: str | core.StringOut = core.attr(str, computed=True)

    deployment_status: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFramework.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
