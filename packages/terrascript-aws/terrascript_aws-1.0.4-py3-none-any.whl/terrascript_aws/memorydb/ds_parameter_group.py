import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.data(type="aws_memorydb_parameter_group", namespace="memorydb")
class DsParameterGroup(core.Data):
    """
    ARN of the parameter group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the parameter group.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The engine version that the parameter group can be used with.
    """
    family: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the parameter group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the parameter group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Set of user-defined MemoryDB parameters applied by the parameter group.
    """
    parameter: list[Parameter] | core.ArrayOut[Parameter] = core.attr(
        Parameter, computed=True, kind=core.Kind.array
    )

    """
    A map of tags assigned to the parameter group.
    """
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
            args=DsParameterGroup.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
