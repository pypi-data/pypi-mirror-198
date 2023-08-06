import terrascript.core as core


@core.data(type="aws_outposts_site", namespace="outposts")
class DsSite(core.Data):
    """
    AWS Account identifier.
    """

    account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Description.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Identifier of the Site.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the Site.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSite.Args(
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)
