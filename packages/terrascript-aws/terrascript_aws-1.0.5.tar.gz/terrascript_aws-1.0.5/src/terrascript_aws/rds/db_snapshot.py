import terrascript.core as core


@core.resource(type="aws_db_snapshot", namespace="rds")
class DbSnapshot(core.Resource):
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
    (Required) The DB Instance Identifier from which to take the snapshot.
    """
    db_instance_identifier: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) for the DB snapshot.
    """
    db_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Identifier for the snapshot.
    """
    db_snapshot_identifier: str | core.StringOut = core.attr(str)

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

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of t
    he snapshot.
    """
    iops: int | core.IntOut = core.attr(int, computed=True)

    """
    The ARN for the KMS encryption key.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    License model information for the restored DB instance.
    """
    license_model: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides the option group name for the DB snapshot.
    """
    option_group_name: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    snapshot_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross custome
    r or cross region copy.
    """
    source_db_snapshot_identifier: str | core.StringOut = core.attr(str, computed=True)

    """
    The region that the DB snapshot was created in or copied from.
    """
    source_region: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the status of this DB snapshot.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

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
    Provides the VPC ID associated with the DB snapshot.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_instance_identifier: str | core.StringOut,
        db_snapshot_identifier: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbSnapshot.Args(
                db_instance_identifier=db_instance_identifier,
                db_snapshot_identifier=db_snapshot_identifier,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_instance_identifier: str | core.StringOut = core.arg()

        db_snapshot_identifier: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
