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


@core.data(type="aws_identitystore_user", namespace="identitystore")
class DsUser(core.Data):
    """
    (Required) Configuration block(s) for filtering. Currently, the AWS Identity Store API supports only
    1 filter. Detailed below.
    """

    filter: list[Filter] | core.ArrayOut[Filter] = core.attr(Filter, kind=core.Kind.array)

    """
    The identifier of the user in the Identity Store.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Identity Store ID associated with the Single Sign-On Instance.
    """
    identity_store_id: str | core.StringOut = core.attr(str)

    """
    (Optional)  The identifier for a user in the Identity Store.
    """
    user_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The user's user name value.
    """
    user_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter],
        identity_store_id: str | core.StringOut,
        user_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUser.Args(
                filter=filter,
                identity_store_id=identity_store_id,
                user_id=user_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] = core.arg()

        identity_store_id: str | core.StringOut = core.arg()

        user_id: str | core.StringOut | None = core.arg(default=None)
