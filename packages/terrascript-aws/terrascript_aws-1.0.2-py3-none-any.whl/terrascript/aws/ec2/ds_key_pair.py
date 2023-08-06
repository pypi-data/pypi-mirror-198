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


@core.data(type="aws_key_pair", namespace="aws_ec2")
class DsKeyPair(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    create_time: str | core.StringOut = core.attr(str, computed=True)

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    fingerprint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    include_public_key: bool | core.BoolOut | None = core.attr(bool, default=None)

    key_name: str | core.StringOut | None = core.attr(str, default=None)

    key_pair_id: str | core.StringOut | None = core.attr(str, default=None)

    key_type: str | core.StringOut = core.attr(str, computed=True)

    public_key: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        include_public_key: bool | core.BoolOut | None = None,
        key_name: str | core.StringOut | None = None,
        key_pair_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsKeyPair.Args(
                filter=filter,
                include_public_key=include_public_key,
                key_name=key_name,
                key_pair_id=key_pair_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        include_public_key: bool | core.BoolOut | None = core.arg(default=None)

        key_name: str | core.StringOut | None = core.arg(default=None)

        key_pair_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
