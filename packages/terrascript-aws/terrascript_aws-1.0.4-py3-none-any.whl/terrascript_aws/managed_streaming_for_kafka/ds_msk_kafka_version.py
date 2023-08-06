import terrascript.core as core


@core.data(type="aws_msk_kafka_version", namespace="managed_streaming_for_kafka")
class DsMskKafkaVersion(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Ordered list of preferred Kafka versions. The first match in this list will be returned.
    Either `preferred_versions` or `version` must be set.
    """
    preferred_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Status of the MSK Kafka version eg. `ACTIVE` or `DEPRECATED`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Version of MSK Kafka. For example 2.4.1.1 or "2.2.1" etc. Either `preferred_versions` or
    version` must be set.
    """
    version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        preferred_versions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMskKafkaVersion.Args(
                preferred_versions=preferred_versions,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        preferred_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        version: str | core.StringOut | None = core.arg(default=None)
