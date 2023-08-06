import terrascript.core as core


@core.resource(type="aws_spot_datafeed_subscription", namespace="ec2")
class SpotDatafeedSubscription(core.Resource):
    """
    (Required) The Amazon S3 bucket in which to store the Spot instance data feed.
    """

    bucket: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Path of folder inside bucket to place spot pricing data.
    """
    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SpotDatafeedSubscription.Args(
                bucket=bucket,
                prefix=prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        prefix: str | core.StringOut | None = core.arg(default=None)
