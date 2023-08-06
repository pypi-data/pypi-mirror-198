import terrascript.core as core


@core.schema
class Filters(core.Schema):

    field: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        field: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Filters.Args(
                field=field,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.data(type="aws_pricing_product", namespace="aws_pricing")
class DsProduct(core.Data):

    filters: list[Filters] | core.ArrayOut[Filters] = core.attr(Filters, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    result: str | core.StringOut = core.attr(str, computed=True)

    service_code: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        filters: list[Filters] | core.ArrayOut[Filters],
        service_code: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsProduct.Args(
                filters=filters,
                service_code=service_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filters: list[Filters] | core.ArrayOut[Filters] = core.arg()

        service_code: str | core.StringOut = core.arg()
