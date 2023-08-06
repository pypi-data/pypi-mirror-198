import terrascript.core as core


@core.schema
class Definition(core.Schema):

    assume_role: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    parameters: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        version: str | core.StringOut,
        assume_role: str | core.StringOut | None = None,
        parameters: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Definition.Args(
                name=name,
                version=version,
                assume_role=assume_role,
                parameters=parameters,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        assume_role: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parameters: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut = core.arg()


@core.resource(type="aws_servicecatalog_service_action", namespace="servicecatalog")
class ServiceAction(core.Resource):
    """
    (Optional) Language code. Valid values are `en` (English), `jp` (Japanese), and `zh` (Chinese). Defa
    ult is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Self-service action definition configuration block. Detailed below.
    """
    definition: Definition = core.attr(Definition)

    """
    (Optional) Self-service action description.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Identifier of the service action.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Self-service action name.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        definition: Definition,
        name: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceAction.Args(
                definition=definition,
                name=name,
                accept_language=accept_language,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        definition: Definition = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
