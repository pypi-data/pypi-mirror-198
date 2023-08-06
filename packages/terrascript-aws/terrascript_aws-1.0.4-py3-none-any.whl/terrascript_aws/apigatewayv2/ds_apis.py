import terrascript.core as core


@core.data(type="aws_apigatewayv2_apis", namespace="apigatewayv2")
class DsApis(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of API identifiers.
    """
    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The API name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The API protocol.
    """
    protocol_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags, each pair of which must exactly match
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut | None = None,
        protocol_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsApis.Args(
                name=name,
                protocol_type=protocol_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        protocol_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
