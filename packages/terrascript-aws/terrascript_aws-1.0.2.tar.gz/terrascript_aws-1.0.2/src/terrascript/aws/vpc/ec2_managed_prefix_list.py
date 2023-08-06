import terrascript.core as core


@core.schema
class Entry(core.Schema):

    cidr: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
        description: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Entry.Args(
                cidr=cidr,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ec2_managed_prefix_list", namespace="aws_vpc")
class Ec2ManagedPrefixList(core.Resource):

    address_family: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    entry: list[Entry] | core.ArrayOut[Entry] | None = core.attr(
        Entry, default=None, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    max_entries: int | core.IntOut = core.attr(int)

    name: str | core.StringOut = core.attr(str)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        address_family: str | core.StringOut,
        max_entries: int | core.IntOut,
        name: str | core.StringOut,
        entry: list[Entry] | core.ArrayOut[Entry] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ManagedPrefixList.Args(
                address_family=address_family,
                max_entries=max_entries,
                name=name,
                entry=entry,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address_family: str | core.StringOut = core.arg()

        entry: list[Entry] | core.ArrayOut[Entry] | None = core.arg(default=None)

        max_entries: int | core.IntOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
