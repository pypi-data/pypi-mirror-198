import terrascript.core as core


@core.schema
class SnapshotDeliveryProperties(core.Schema):

    delivery_frequency: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        delivery_frequency: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SnapshotDeliveryProperties.Args(
                delivery_frequency=delivery_frequency,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delivery_frequency: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_config_delivery_channel", namespace="config")
class DeliveryChannel(core.Resource):
    """
    The name of the delivery channel.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the delivery channel. Defaults to `default`. Changing it recreates the resour
    ce.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the S3 bucket used to store the configuration history.
    """
    s3_bucket_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The prefix for the specified S3 bucket.
    """
    s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN of the AWS KMS key used to encrypt objects delivered by AWS Config. Must belong t
    o the same Region as the destination S3 bucket.
    """
    s3_kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Options for how AWS Config delivers configuration snapshots. See below
    """
    snapshot_delivery_properties: SnapshotDeliveryProperties | None = core.attr(
        SnapshotDeliveryProperties, default=None
    )

    """
    (Optional) The ARN of the SNS topic that AWS Config delivers notifications to.
    """
    sns_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        s3_bucket_name: str | core.StringOut,
        name: str | core.StringOut | None = None,
        s3_key_prefix: str | core.StringOut | None = None,
        s3_kms_key_arn: str | core.StringOut | None = None,
        snapshot_delivery_properties: SnapshotDeliveryProperties | None = None,
        sns_topic_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeliveryChannel.Args(
                s3_bucket_name=s3_bucket_name,
                name=name,
                s3_key_prefix=s3_key_prefix,
                s3_kms_key_arn=s3_kms_key_arn,
                snapshot_delivery_properties=snapshot_delivery_properties,
                sns_topic_arn=sns_topic_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        s3_bucket_name: str | core.StringOut = core.arg()

        s3_key_prefix: str | core.StringOut | None = core.arg(default=None)

        s3_kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        snapshot_delivery_properties: SnapshotDeliveryProperties | None = core.arg(default=None)

        sns_topic_arn: str | core.StringOut | None = core.arg(default=None)
