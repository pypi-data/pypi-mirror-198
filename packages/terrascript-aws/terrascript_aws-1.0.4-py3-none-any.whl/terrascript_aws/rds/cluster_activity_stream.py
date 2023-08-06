import terrascript.core as core


@core.resource(type="aws_rds_cluster_activity_stream", namespace="rds")
class ClusterActivityStream(core.Resource):
    """
    (Optional, Forces new resources) Specifies whether the database activity stream includes engine-nati
    ve audit fields. This option only applies to an Oracle DB instance. By default, no engine-native aud
    it fields are included. Defaults `false`.
    """

    engine_native_audit_fields_included: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Amazon Resource Name (ARN) of the DB cluster.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the Amazon Kinesis data stream to be used for the database activity stream.
    """
    kinesis_stream_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resources) The AWS KMS key identifier for encrypting messages in the database
    activity stream. The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the
    KMS key.
    """
    kms_key_id: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resources) Specifies the mode of the database activity stream. Database events
    such as a change or access generate an activity stream event. The database session can handle these
    events either synchronously or asynchronously. One of: `sync`, `async`.
    """
    mode: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resources) The Amazon Resource Name (ARN) of the DB cluster.
    """
    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        kms_key_id: str | core.StringOut,
        mode: str | core.StringOut,
        resource_arn: str | core.StringOut,
        engine_native_audit_fields_included: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterActivityStream.Args(
                kms_key_id=kms_key_id,
                mode=mode,
                resource_arn=resource_arn,
                engine_native_audit_fields_included=engine_native_audit_fields_included,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        engine_native_audit_fields_included: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut = core.arg()

        mode: str | core.StringOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()
