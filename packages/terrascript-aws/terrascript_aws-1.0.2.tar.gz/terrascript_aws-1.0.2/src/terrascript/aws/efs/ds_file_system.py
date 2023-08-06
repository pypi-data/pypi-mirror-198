import terrascript.core as core


@core.schema
class LifecyclePolicy(core.Schema):

    transition_to_ia: str | core.StringOut = core.attr(str, computed=True)

    transition_to_primary_storage_class: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        transition_to_ia: str | core.StringOut,
        transition_to_primary_storage_class: str | core.StringOut,
    ):
        super().__init__(
            args=LifecyclePolicy.Args(
                transition_to_ia=transition_to_ia,
                transition_to_primary_storage_class=transition_to_primary_storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        transition_to_ia: str | core.StringOut = core.arg()

        transition_to_primary_storage_class: str | core.StringOut = core.arg()


@core.data(type="aws_efs_file_system", namespace="aws_efs")
class DsFileSystem(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    availability_zone_name: str | core.StringOut = core.attr(str, computed=True)

    creation_token: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    file_system_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    lifecycle_policy: list[LifecyclePolicy] | core.ArrayOut[LifecyclePolicy] = core.attr(
        LifecyclePolicy, computed=True, kind=core.Kind.array
    )

    performance_mode: str | core.StringOut = core.attr(str, computed=True)

    provisioned_throughput_in_mibps: float | core.FloatOut = core.attr(float, computed=True)

    size_in_bytes: int | core.IntOut = core.attr(int, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput_mode: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        creation_token: str | core.StringOut | None = None,
        file_system_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFileSystem.Args(
                creation_token=creation_token,
                file_system_id=file_system_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        creation_token: str | core.StringOut | None = core.arg(default=None)

        file_system_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
