import terrascript.core as core


@core.data(type="aws_api_gateway_api_key", namespace="api_gateway")
class DsApiKey(core.Data):
    """
    The date and time when the API Key was created.
    """

    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the API Key.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies whether the API Key is enabled.
    """
    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) The ID of the API Key to look up.
    """
    id: str | core.StringOut = core.attr(str)

    """
    The date and time when the API Key was last updated.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the name of the API Key.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Set to the value of the API Key.
    """
    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsApiKey.Args(
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
