import terrascript.core as core


@core.schema
class Entries(core.Schema):

    cidr: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
        description: str | core.StringOut,
    ):
        super().__init__(
            args=Entries.Args(
                cidr=cidr,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()

        description: str | core.StringOut = core.arg()


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


@core.data(type="aws_ec2_managed_prefix_list", namespace="vpc")
class DsEc2ManagedPrefixList(core.Data):
    """
    The address family of the prefix list. Valid values are `IPv4` and `IPv6`.
    """

    address_family: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the selected prefix list.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The set of entries in this prefix list. Each entry is an object with `cidr` and `description`.
    """
    entries: list[Entries] | core.ArrayOut[Entries] = core.attr(
        Entries, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) The ID of the prefix list to select.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    When then prefix list is managed, the maximum number of entries it supports, or null otherwise.
    """
    max_entries: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) The name of the prefix list to select.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The Account ID of the owner of a customer-managed prefix list, or `AWS` otherwise.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2ManagedPrefixList.Args(
                filter=filter,
                id=id,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
