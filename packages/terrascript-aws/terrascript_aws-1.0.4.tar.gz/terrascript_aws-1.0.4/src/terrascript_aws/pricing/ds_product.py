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


@core.data(type="aws_pricing_product", namespace="pricing")
class DsProduct(core.Data):
    """
    (Required) A list of filters. Passed directly to the API (see GetProducts API reference). These filt
    ers must describe a single product, this resource will fail if more than one product is returned by
    the API.
    """

    filters: list[Filters] | core.ArrayOut[Filters] = core.attr(Filters, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the product returned from the API.
    """
    result: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The code of the service. Available service codes can be fetched using the DescribeService
    s pricing API call.
    """
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
