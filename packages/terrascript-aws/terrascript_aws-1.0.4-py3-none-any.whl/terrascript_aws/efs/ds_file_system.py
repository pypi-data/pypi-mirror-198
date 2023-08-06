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


@core.data(type="aws_efs_file_system", namespace="efs")
class DsFileSystem(core.Data):
    """
    Amazon Resource Name of the file system.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the Availability Zone in which the file system's One Zone storage classes exist.
    """
    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Availability Zone name in which the file system's One Zone storage classes exist.
    """
    availability_zone_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Restricts the list to the file system with this creation token.
    """
    creation_token: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug
    /mounting-fs-mount-cmd-dns-name.html).
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether EFS is encrypted.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) The ID that identifies the file system (e.g., fs-ccfc0d65).
    """
    file_system_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN for the KMS encryption key.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html)
    object.
    """
    lifecycle_policy: list[LifecyclePolicy] | core.ArrayOut[LifecyclePolicy] = core.attr(
        LifecyclePolicy, computed=True, kind=core.Kind.array
    )

    """
    The file system performance mode.
    """
    performance_mode: str | core.StringOut = core.attr(str, computed=True)

    """
    The throughput, measured in MiB/s, that you want to provision for the file system.
    """
    provisioned_throughput_in_mibps: float | core.FloatOut = core.attr(float, computed=True)

    """
    The current byte count used by the file system.
    """
    size_in_bytes: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Restricts the list to the file system with these tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Throughput mode for the file system.
    """
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
