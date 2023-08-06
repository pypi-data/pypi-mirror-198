import terrascript.core as core


@core.schema
class Filter(core.Schema):

    attribute_path: str | core.StringOut = core.attr(str)

    attribute_value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        attribute_path: str | core.StringOut,
        attribute_value: str | core.StringOut,
    ):
        super().__init__(
            args=Filter.Args(
                attribute_path=attribute_path,
                attribute_value=attribute_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute_path: str | core.StringOut = core.arg()

        attribute_value: str | core.StringOut = core.arg()


@core.data(type="aws_identitystore_group", namespace="identitystore")
class DsGroup(core.Data):
    """
    The group's display name value.
    """

    display_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block(s) for filtering. Currently, the AWS Identity Store API supports only
    1 filter. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] = core.attr(Filter, kind=core.Kind.array)

    """
    (Optional)  The identifier for a group in the Identity Store.
    """
    group_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The identifier of the group in the Identity Store.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Identity Store ID associated with the Single Sign-On Instance.
    """
    identity_store_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter],
        identity_store_id: str | core.StringOut,
        group_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsGroup.Args(
                filter=filter,
                identity_store_id=identity_store_id,
                group_id=group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] = core.arg()

        group_id: str | core.StringOut | None = core.arg(default=None)

        identity_store_id: str | core.StringOut = core.arg()
