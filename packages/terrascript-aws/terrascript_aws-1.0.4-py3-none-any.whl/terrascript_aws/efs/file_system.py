import terrascript.core as core


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


@core.resource(type="aws_efs_file_system", namespace="efs")
class FileSystem(core.Resource):
    """
    Amazon Resource Name of the file system.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the Availability Zone in which the file system's One Zone storage classes exist.
    """
    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) the AWS Availability Zone in which to create the file system. Used to create a file syste
    m that uses One Zone storage classes. See [user guide](https://docs.aws.amazon.com/efs/latest/ug/sto
    rage-classes.html) for more information.
    """
    availability_zone_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) A unique name (a maximum of 64 characters are allowed)
    """
    creation_token: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug
    /mounting-fs-mount-cmd-dns-name.html).
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If true, the disk will be encrypted.
    """
    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The ID that identifies the file system (e.g., fs-ccfc0d65).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set
    to true.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecycleP
    olicy.html) object (documented below).
    """
    lifecycle_policy: list[LifecyclePolicy] | core.ArrayOut[LifecyclePolicy] | None = core.attr(
        LifecyclePolicy, default=None, kind=core.Kind.array
    )

    """
    The current number of mount targets that the file system has.
    """
    number_of_mount_targets: int | core.IntOut = core.attr(int, computed=True)

    """
    The AWS account that created the file system. If the file system was createdby an IAM user, the pare
    nt account to which the user belongs is the owner.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The file system performance mode. Can be either `"generalPurpose"` or `"maxIO"` (Default:
    "generalPurpose"`).
    """
    performance_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The throughput, measured in MiB/s, that you want to provision for the file system. Only a
    pplicable with `throughput_mode` set to `provisioned`.
    """
    provisioned_throughput_in_mibps: float | core.FloatOut | None = core.attr(float, default=None)

    """
    The latest known metered size (in bytes) of data stored in the file system, the value is not the exa
    ct size that the file system was at any point in time. See [Size In Bytes](#size-in-bytes).
    """
    size_in_bytes: list[SizeInBytes] | core.ArrayOut[SizeInBytes] = core.attr(
        SizeInBytes, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the file system. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `p
    rovisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
    """
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
