import terrascript.core as core


@core.schema
class SizeInBytes(core.Schema):

    value: int | core.IntOut = core.attr(int, computed=True)

    value_in_ia: int | core.IntOut = core.attr(int, computed=True)

    value_in_standard: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        value: int | core.IntOut,
        value_in_ia: int | core.IntOut,
        value_in_standard: int | core.IntOut,
    ):
        super().__init__(
            args=SizeInBytes.Args(
                value=value,
                value_in_ia=value_in_ia,
                value_in_standard=value_in_standard,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        value: int | core.IntOut = core.arg()

        value_in_ia: int | core.IntOut = core.arg()

        value_in_standard: int | core.IntOut = core.arg()


@core.schema
class LifecyclePolicy(core.Schema):

    transition_to_ia: str | core.StringOut | None = core.attr(str, default=None)

    transition_to_primary_storage_class: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        transition_to_ia: str | core.StringOut | None = None,
        transition_to_primary_storage_class: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LifecyclePolicy.Args(
                transition_to_ia=transition_to_ia,
                transition_to_primary_storage_class=transition_to_primary_storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        transition_to_ia: str | core.StringOut | None = core.arg(default=None)

        transition_to_primary_storage_class: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_efs_file_system", namespace="aws_efs")
class FileSystem(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    availability_zone_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    creation_token: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    lifecycle_policy: list[LifecyclePolicy] | core.ArrayOut[LifecyclePolicy] | None = core.attr(
        LifecyclePolicy, default=None, kind=core.Kind.array
    )

    number_of_mount_targets: int | core.IntOut = core.attr(int, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    performance_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    provisioned_throughput_in_mibps: float | core.FloatOut | None = core.attr(float, default=None)

    size_in_bytes: list[SizeInBytes] | core.ArrayOut[SizeInBytes] = core.attr(
        SizeInBytes, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput_mode: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone_name: str | core.StringOut | None = None,
        creation_token: str | core.StringOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        lifecycle_policy: list[LifecyclePolicy] | core.ArrayOut[LifecyclePolicy] | None = None,
        performance_mode: str | core.StringOut | None = None,
        provisioned_throughput_in_mibps: float | core.FloatOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        throughput_mode: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FileSystem.Args(
                availability_zone_name=availability_zone_name,
                creation_token=creation_token,
                encrypted=encrypted,
                kms_key_id=kms_key_id,
                lifecycle_policy=lifecycle_policy,
                performance_mode=performance_mode,
                provisioned_throughput_in_mibps=provisioned_throughput_in_mibps,
                tags=tags,
                tags_all=tags_all,
                throughput_mode=throughput_mode,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone_name: str | core.StringOut | None = core.arg(default=None)

        creation_token: str | core.StringOut | None = core.arg(default=None)

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        lifecycle_policy: list[LifecyclePolicy] | core.ArrayOut[LifecyclePolicy] | None = core.arg(
            default=None
        )

        performance_mode: str | core.StringOut | None = core.arg(default=None)

        provisioned_throughput_in_mibps: float | core.FloatOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput_mode: str | core.StringOut | None = core.arg(default=None)
