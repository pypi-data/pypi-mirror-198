import terrascript.core as core


@core.data(type="aws_servicecatalog_product", namespace="servicecatalog")
class DsProduct(core.Data):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default val
    ue is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    ARN of the product.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Time when the product was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the product.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Distributor (i.e., vendor) of the product.
    """
    distributor: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the product has a default path.
    """
    has_default_path: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) Product ID.
    """
    id: str | core.StringOut = core.attr(str)

    """
    Name of the product.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Owner of the product.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    Status of the product.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Support information about the product.
    """
    support_description: str | core.StringOut = core.attr(str, computed=True)

    """
    Contact email for product support.
    """
    support_email: str | core.StringOut = core.attr(str, computed=True)

    """
    Contact URL for product support.
    """
    support_url: str | core.StringOut = core.attr(str, computed=True)

    """
    Tags to apply to the product.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Type of product.
    """
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
