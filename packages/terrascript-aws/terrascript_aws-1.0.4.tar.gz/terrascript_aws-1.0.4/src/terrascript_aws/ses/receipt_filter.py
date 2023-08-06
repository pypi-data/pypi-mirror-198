import terrascript.core as core


@core.resource(type="aws_ses_receipt_filter", namespace="ses")
class ReceiptFilter(core.Resource):
    """
    The SES receipt filter ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The IP address or address range to filter, in CIDR notation
    """
    cidr: str | core.StringOut = core.attr(str)

    """
    The SES receipt filter name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the filter
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Block or Allow
    """
    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cidr: str | core.StringOut,
        name: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReceiptFilter.Args(
                cidr=cidr,
                name=name,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
