import terrascript.core as core


@core.resource(type="aws_securityhub_product_subscription", namespace="aws_securityhub")
class ProductSubscription(core.Resource):
    """
    The ARN of a resource that represents your subscription to the product that generates the findings t
    hat you want to import into Security Hub.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN of the product that generates findings that you want to import into Security Hub
    see below.
    """
    product_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        product_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProductSubscription.Args(
                product_arn=product_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        product_arn: str | core.StringOut = core.arg()
