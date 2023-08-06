import terrascript.core as core


@core.data(type="aws_msk_kafka_version", namespace="aws_managed_streaming_for_kafka")
class DsMskKafkaVersion(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    preferred_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

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
