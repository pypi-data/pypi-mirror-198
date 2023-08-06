import terrascript.core as core


@core.resource(type="aws_db_snapshot_copy", namespace="rds")
class DbSnapshotCopy(core.Resource):
    """
    Specifies the allocated storage size in gigabytes (GB).
    """

    allocated_storage: int | core.IntOut = core.attr(int, computed=True)

    """
    Specifies the name of the Availability Zone the DB instance was located in at the time of the DB sna
    pshot.
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to copy existing tags. Defaults to `false`.
    """
    copy_tags: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Amazon Resource Name (ARN) for the DB snapshot.
    """
    db_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Destination region to place snapshot copy.
    """
    destination_region: str | core.StringOut | None = core.attr(str, default=None)

    """
    Specifies whether the DB snapshot is encrypted.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies the name of the database engine.
    """
    engine: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the version of the database engine.
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Snapshot Identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of t
    he snapshot.
    """
    iops: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) KMS key ID.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    License model information for the restored DB instance.
    """
    license_model: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides the option group name for the DB snapshot.
    """
    option_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) he URL that contains a Signature Version 4 signed request.
    """
    presigned_url: str | core.StringOut | None = core.attr(str, default=None)

    snapshot_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Snapshot identifier of the source snapshot.
    """
    source_db_snapshot_identifier: str | core.StringOut = core.attr(str)

    """
    The region that the DB snapshot was created in or copied from.
    """
    source_region: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the storage type associated with DB snapshot.
    """
    storage_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) The external custom Availability Zone.
    """
    target_custom_availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The Identifier for the snapshot.
    """
    target_db_snapshot_identifier: str | core.StringOut = core.attr(str)

    """
    Provides the VPC ID associated with the DB snapshot.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        source_db_snapshot_identifier: str | core.StringOut,
        target_db_snapshot_identifier: str | core.StringOut,
        copy_tags: bool | core.BoolOut | None = None,
        destination_region: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        option_group_name: str | core.StringOut | None = None,
        presigned_url: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_custom_availability_zone: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbSnapshotCopy.Args(
                source_db_snapshot_identifier=source_db_snapshot_identifier,
                target_db_snapshot_identifier=target_db_snapshot_identifier,
                copy_tags=copy_tags,
                destination_region=destination_region,
                kms_key_id=kms_key_id,
                option_group_name=option_group_name,
                presigned_url=presigned_url,
                tags=tags,
                tags_all=tags_all,
                target_custom_availability_zone=target_custom_availability_zone,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        copy_tags: bool | core.BoolOut | None = core.arg(default=None)

        destination_region: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        option_group_name: str | core.StringOut | None = core.arg(default=None)

        presigned_url: str | core.StringOut | None = core.arg(default=None)

        source_db_snapshot_identifier: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_custom_availability_zone: str | core.StringOut | None = core.arg(default=None)

        target_db_snapshot_identifier: str | core.StringOut = core.arg()
