import terrascript.core as core


@core.data(type="aws_iam_openid_connect_provider", namespace="aws_iam")
class DsOpenidConnectProvider(core.Data):

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    client_id_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    thumbprint_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    url: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        url: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOpenidConnectProvider.Args(
                arn=arn,
                tags=tags,
                url=url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        url: str | core.StringOut | None = core.arg(default=None)
