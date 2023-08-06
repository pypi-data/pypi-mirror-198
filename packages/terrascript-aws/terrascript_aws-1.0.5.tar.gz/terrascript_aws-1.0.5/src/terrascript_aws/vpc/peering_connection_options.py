import terrascript.core as core


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


@core.resource(type="aws_vpc_peering_connection_options", namespace="vpc")
class PeeringConnectionOptions(core.Resource):

    accepter: Accepter | None = core.attr(Accepter, default=None, computed=True)

    """
    The ID of the VPC Peering Connection Options.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    requester: Requester | None = core.attr(Requester, default=None, computed=True)

    """
    (Required) The ID of the requester VPC peering connection.
    """
    vpc_peering_connection_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_peering_connection_id: str | core.StringOut,
        accepter: Accepter | None = None,
        requester: Requester | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PeeringConnectionOptions.Args(
                vpc_peering_connection_id=vpc_peering_connection_id,
                accepter=accepter,
                requester=requester,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accepter: Accepter | None = core.arg(default=None)

        requester: Requester | None = core.arg(default=None)

        vpc_peering_connection_id: str | core.StringOut = core.arg()
