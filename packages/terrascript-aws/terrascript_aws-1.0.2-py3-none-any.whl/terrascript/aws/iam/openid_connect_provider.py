import terrascript.core as core


@core.resource(type="aws_iam_openid_connect_provider", namespace="aws_iam")
class OpenidConnectProvider(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    client_id_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    thumbprint_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        client_id_list: list[str] | core.ArrayOut[core.StringOut],
        thumbprint_list: list[str] | core.ArrayOut[core.StringOut],
        url: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OpenidConnectProvider.Args(
                client_id_list=client_id_list,
                thumbprint_list=thumbprint_list,
                url=url,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_id_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        thumbprint_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        url: str | core.StringOut = core.arg()
