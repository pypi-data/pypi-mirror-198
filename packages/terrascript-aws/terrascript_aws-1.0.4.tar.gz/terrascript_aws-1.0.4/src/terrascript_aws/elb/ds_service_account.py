import terrascript.core as core


@core.data(type="aws_elb_service_account", namespace="elb")
class DsServiceAccount(core.Data):
    """
    The ARN of the AWS ELB service account in the selected region.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS ELB service account in the selected region.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Name of the region whose AWS ELB account ID is desired.
    """
    region: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServiceAccount.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: str | core.StringOut | None = core.arg(default=None)
