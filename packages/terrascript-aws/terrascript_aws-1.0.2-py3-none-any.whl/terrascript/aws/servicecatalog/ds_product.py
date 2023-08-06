import terrascript.core as core


@core.data(type="aws_servicecatalog_product", namespace="aws_servicecatalog")
class DsProduct(core.Data):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    created_time: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    distributor: str | core.StringOut = core.attr(str, computed=True)

    has_default_path: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str, computed=True)

    owner: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    support_description: str | core.StringOut = core.attr(str, computed=True)

    support_email: str | core.StringOut = core.attr(str, computed=True)

    support_url: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsProduct.Args(
                id=id,
                accept_language=accept_language,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
