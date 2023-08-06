import terrascript.core as core


@core.data(type="aws_cloudfront_log_delivery_canonical_user_id", namespace="cloudfront")
class DsLogDeliveryCanonicalUserId(core.Data):
    """
    The canonical user ID for the AWS `awslogsdelivery` account in the region.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The region you'd like the zone for. By default, fetches the current region.
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
            args=DsLogDeliveryCanonicalUserId.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: str | core.StringOut | None = core.arg(default=None)
