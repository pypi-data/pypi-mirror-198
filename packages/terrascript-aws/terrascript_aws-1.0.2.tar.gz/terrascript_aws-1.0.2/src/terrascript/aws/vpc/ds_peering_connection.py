import terrascript.core as core


@core.schema
class PeerCidrBlockSet(core.Schema):

    cidr_block: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cidr_block: str | core.StringOut,
    ):
        super().__init__(
            args=PeerCidrBlockSet.Args(
                cidr_block=cidr_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: str | core.StringOut = core.arg()


@core.schema
class CidrBlockSet(core.Schema):

    cidr_block: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cidr_block: str | core.StringOut,
    ):
        super().__init__(
            args=CidrBlockSet.Args(
                cidr_block=cidr_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: str | core.StringOut = core.arg()


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


@core.data(type="aws_vpc_peering_connection", namespace="aws_vpc")
class DsPeeringConnection(core.Data):

    accepter: dict[str, bool] | core.MapOut[core.BoolOut] = core.attr(
        bool, computed=True, kind=core.Kind.map
    )

    cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cidr_block_set: list[CidrBlockSet] | core.ArrayOut[CidrBlockSet] = core.attr(
        CidrBlockSet, computed=True, kind=core.Kind.array
    )

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    owner_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    peer_cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    peer_cidr_block_set: list[PeerCidrBlockSet] | core.ArrayOut[PeerCidrBlockSet] = core.attr(
        PeerCidrBlockSet, computed=True, kind=core.Kind.array
    )

    peer_owner_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    peer_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    peer_vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    requester: dict[str, bool] | core.MapOut[core.BoolOut] = core.attr(
        bool, computed=True, kind=core.Kind.map
    )

    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cidr_block: str | core.StringOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        owner_id: str | core.StringOut | None = None,
        peer_cidr_block: str | core.StringOut | None = None,
        peer_owner_id: str | core.StringOut | None = None,
        peer_region: str | core.StringOut | None = None,
        peer_vpc_id: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPeeringConnection.Args(
                cidr_block=cidr_block,
                filter=filter,
                id=id,
                owner_id=owner_id,
                peer_cidr_block=peer_cidr_block,
                peer_owner_id=peer_owner_id,
                peer_region=peer_region,
                peer_vpc_id=peer_vpc_id,
                region=region,
                status=status,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: str | core.StringOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        owner_id: str | core.StringOut | None = core.arg(default=None)

        peer_cidr_block: str | core.StringOut | None = core.arg(default=None)

        peer_owner_id: str | core.StringOut | None = core.arg(default=None)

        peer_region: str | core.StringOut | None = core.arg(default=None)

        peer_vpc_id: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
