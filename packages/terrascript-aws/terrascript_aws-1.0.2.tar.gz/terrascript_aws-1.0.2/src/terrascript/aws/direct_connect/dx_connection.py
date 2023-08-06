import terrascript.core as core


@core.resource(type="aws_dx_connection", namespace="aws_direct_connect")
class DxConnection(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    aws_device: str | core.StringOut = core.attr(str, computed=True)

    bandwidth: str | core.StringOut = core.attr(str)

    has_logical_redundancy: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    jumbo_frame_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    location: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    provider_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        bandwidth: str | core.StringOut,
        location: str | core.StringOut,
        name: str | core.StringOut,
        provider_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxConnection.Args(
                bandwidth=bandwidth,
                location=location,
                name=name,
                provider_name=provider_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bandwidth: str | core.StringOut = core.arg()

        location: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        provider_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
