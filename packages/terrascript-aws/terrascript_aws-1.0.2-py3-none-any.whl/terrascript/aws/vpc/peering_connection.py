import terrascript.core as core


@core.schema
class Requester(core.Schema):

    allow_classic_link_to_remote_vpc: bool | core.BoolOut | None = core.attr(bool, default=None)

    allow_remote_vpc_dns_resolution: bool | core.BoolOut | None = core.attr(bool, default=None)

    allow_vpc_to_remote_classic_link: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        allow_classic_link_to_remote_vpc: bool | core.BoolOut | None = None,
        allow_remote_vpc_dns_resolution: bool | core.BoolOut | None = None,
        allow_vpc_to_remote_classic_link: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Requester.Args(
                allow_classic_link_to_remote_vpc=allow_classic_link_to_remote_vpc,
                allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution,
                allow_vpc_to_remote_classic_link=allow_vpc_to_remote_classic_link,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_classic_link_to_remote_vpc: bool | core.BoolOut | None = core.arg(default=None)

        allow_remote_vpc_dns_resolution: bool | core.BoolOut | None = core.arg(default=None)

        allow_vpc_to_remote_classic_link: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Accepter(core.Schema):

    allow_classic_link_to_remote_vpc: bool | core.BoolOut | None = core.attr(bool, default=None)

    allow_remote_vpc_dns_resolution: bool | core.BoolOut | None = core.attr(bool, default=None)

    allow_vpc_to_remote_classic_link: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        allow_classic_link_to_remote_vpc: bool | core.BoolOut | None = None,
        allow_remote_vpc_dns_resolution: bool | core.BoolOut | None = None,
        allow_vpc_to_remote_classic_link: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Accepter.Args(
                allow_classic_link_to_remote_vpc=allow_classic_link_to_remote_vpc,
                allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution,
                allow_vpc_to_remote_classic_link=allow_vpc_to_remote_classic_link,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_classic_link_to_remote_vpc: bool | core.BoolOut | None = core.arg(default=None)

        allow_remote_vpc_dns_resolution: bool | core.BoolOut | None = core.arg(default=None)

        allow_vpc_to_remote_classic_link: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_vpc_peering_connection", namespace="aws_vpc")
class PeeringConnection(core.Resource):

    accept_status: str | core.StringOut = core.attr(str, computed=True)

    accepter: Accepter | None = core.attr(Accepter, default=None, computed=True)

    auto_accept: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    peer_owner_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    peer_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    peer_vpc_id: str | core.StringOut = core.attr(str)

    requester: Requester | None = core.attr(Requester, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        peer_vpc_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
        accepter: Accepter | None = None,
        auto_accept: bool | core.BoolOut | None = None,
        peer_owner_id: str | core.StringOut | None = None,
        peer_region: str | core.StringOut | None = None,
        requester: Requester | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PeeringConnection.Args(
                peer_vpc_id=peer_vpc_id,
                vpc_id=vpc_id,
                accepter=accepter,
                auto_accept=auto_accept,
                peer_owner_id=peer_owner_id,
                peer_region=peer_region,
                requester=requester,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accepter: Accepter | None = core.arg(default=None)

        auto_accept: bool | core.BoolOut | None = core.arg(default=None)

        peer_owner_id: str | core.StringOut | None = core.arg(default=None)

        peer_region: str | core.StringOut | None = core.arg(default=None)

        peer_vpc_id: str | core.StringOut = core.arg()

        requester: Requester | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
