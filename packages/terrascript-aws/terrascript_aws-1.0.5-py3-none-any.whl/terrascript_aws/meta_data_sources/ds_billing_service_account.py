import terrascript.core as core


@core.data(type="aws_billing_service_account", namespace="meta_data_sources")
class DsBillingServiceAccount(core.Data):
    """
    The ARN of the AWS billing service account.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS billing service account.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsBillingServiceAccount.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
