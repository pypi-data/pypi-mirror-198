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

    display_name: str | core.StringOut = core.attr(str, computed=True)

    filter: list[Filter] | core.ArrayOut[Filter] = core.attr(Filter, kind=core.Kind.array)

    group_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

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
