import terrascript.core as core


@core.data(type="aws_billing_service_account", namespace="aws_meta_data_sources")
class DsBillingServiceAccount(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

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
