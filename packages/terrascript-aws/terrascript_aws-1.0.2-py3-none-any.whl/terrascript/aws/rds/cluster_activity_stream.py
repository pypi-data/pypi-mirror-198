import terrascript.core as core


@core.resource(type="aws_rds_cluster_activity_stream", namespace="aws_rds")
class ClusterActivityStream(core.Resource):

    engine_native_audit_fields_included: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kinesis_stream_name: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str)

    mode: str | core.StringOut = core.attr(str)

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
