import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_ami_ids", namespace="ec2")
class DsAmiIds(core.Data):
    """
    (Optional) Limit search to users with *explicit* launch
    """

    executable_users: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) One or more name/value pairs to filter off of. There
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A regex string to apply to the AMI list returned
    """
    name_regex: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) List of AMI owners to limit search. At least 1 value must be specified. Valid values: an
    AWS account ID, `self` (the current account), or an AWS owner alias (e.g., `amazon`, `aws-marketplac
    e`, `microsoft`).
    """
    owners: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    sort_ascending: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        owners: list[str] | core.ArrayOut[core.StringOut],
        executable_users: list[str] | core.ArrayOut[core.StringOut] | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        name_regex: str | core.StringOut | None = None,
        sort_ascending: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAmiIds.Args(
                owners=owners,
                executable_users=executable_users,
                filter=filter,
                name_regex=name_regex,
                sort_ascending=sort_ascending,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        executable_users: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        name_regex: str | core.StringOut | None = core.arg(default=None)

        owners: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        sort_ascending: bool | core.BoolOut | None = core.arg(default=None)
