import terrascript.core as core


@core.resource(type="aws_dynamodb_table_item", namespace="dynamodb")
class TableItem(core.Resource):
    """
    (Required) Hash key to use for lookups and identification of the item
    """

    hash_key: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) JSON representation of a map of attribute name/value pairs, one for each attribute. Only
    the primary key attributes are required; you can optionally provide other attribute name-value pairs
    for the item.
    """
    item: str | core.StringOut = core.attr(str)

    """
    (Optional) Range key to use for lookups and identification of the item. Required if there is range k
    ey defined in the table.
    """
    range_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name of the table to contain the item.
    """
    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        hash_key: str | core.StringOut,
        item: str | core.StringOut,
        table_name: str | core.StringOut,
        range_key: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TableItem.Args(
                hash_key=hash_key,
                item=item,
                table_name=table_name,
                range_key=range_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hash_key: str | core.StringOut = core.arg()

        item: str | core.StringOut = core.arg()

        range_key: str | core.StringOut | None = core.arg(default=None)

        table_name: str | core.StringOut = core.arg()
