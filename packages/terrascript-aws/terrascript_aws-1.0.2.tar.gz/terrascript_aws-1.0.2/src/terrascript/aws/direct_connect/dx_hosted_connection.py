import terrascript.core as core


@core.resource(type="aws_dx_hosted_connection", namespace="aws_direct_connect")
class DxHostedConnection(core.Resource):

    aws_device: str | core.StringOut = core.attr(str, computed=True)

    bandwidth: str | core.StringOut = core.attr(str)

    connection_id: str | core.StringOut = core.attr(str)

    has_logical_redundancy: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    jumbo_frame_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    lag_id: str | core.StringOut = core.attr(str, computed=True)

    loa_issue_time: str | core.StringOut = core.attr(str, computed=True)

    location: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    owner_account_id: str | core.StringOut = core.attr(str)

    partner_name: str | core.StringOut = core.attr(str, computed=True)

    provider_name: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    vlan: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        bandwidth: str | core.StringOut,
        connection_id: str | core.StringOut,
        name: str | core.StringOut,
        owner_account_id: str | core.StringOut,
        vlan: int | core.IntOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxHostedConnection.Args(
                bandwidth=bandwidth,
                connection_id=connection_id,
                name=name,
                owner_account_id=owner_account_id,
                vlan=vlan,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bandwidth: str | core.StringOut = core.arg()

        connection_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        owner_account_id: str | core.StringOut = core.arg()

        vlan: int | core.IntOut = core.arg()
