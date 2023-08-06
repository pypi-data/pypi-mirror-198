import terrascript.core as core


@core.schema
class Parameters(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Parameters.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_dax_parameter_group", namespace="dynamodb_accelerator")
class DaxParameterGroup(core.Resource):
    """
    (Optional, ForceNew) A description of the parameter group.
    """

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name of the parameter group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the parameter.
    """
    name: str | core.StringOut = core.attr(str)

    parameters: list[Parameters] | core.ArrayOut[Parameters] | None = core.attr(
        Parameters, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        parameters: list[Parameters] | core.ArrayOut[Parameters] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DaxParameterGroup.Args(
                name=name,
                description=description,
                parameters=parameters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parameters: list[Parameters] | core.ArrayOut[Parameters] | None = core.arg(default=None)
