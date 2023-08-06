import terrascript.core as core


@core.resource(type="aws_dms_replication_instance", namespace="dms")
class ReplicationInstance(core.Resource):
    """
    (Optional, Default: 50, Min: 5, Max: 6144) The amount of storage (in gigabytes) to be initially allo
    cated for the replication instance.
    """

    allocated_storage: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional, Default: false) Indicates that major version upgrades are allowed.
    """
    allow_major_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, Default: false) Indicates whether the changes should be applied immediately or during the
    next maintenance window. Only used when updating an existing resource.
    """
    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, Default: false) Indicates that minor engine upgrades will be applied automatically to the
    replication instance during the maintenance window.
    """
    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) The EC2 Availability Zone that the replication instance will be created in.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The engine version number of the replication instance.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connectio
    n parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default en
    cryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has
    a different default encryption key for each AWS region.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies if the replication instance is a multi-az deployment. You cannot set the `avail
    ability_zone` parameter if the `multi_az` parameter is set to `true`.
    """
    multi_az: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) The weekly time range during which system maintenance can occur, in Universal Coordinated
    Time (UTC).
    """
    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, Default: false) Specifies the accessibility options for the replication instance. A value
    of true represents an instance with a public IP address. A value of false represents an instance wi
    th a private IP address.
    """
    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The Amazon Resource Name (ARN) of the replication instance.
    """
    replication_instance_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The compute and memory capacity of the replication instance as specified by the replicati
    on instance class. See [AWS DMS User Guide](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Re
    plicationInstance.Types.html) for available instance sizes and advice on which one to choose.
    """
    replication_instance_class: str | core.StringOut = core.attr(str)

    """
    (Required) The replication instance identifier. This parameter is stored as a lowercase string.
    """
    replication_instance_id: str | core.StringOut = core.attr(str)

    """
    A list of the private IP addresses of the replication instance.
    """
    replication_instance_private_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    A list of the public IP addresses of the replication instance.
    """
    replication_instance_public_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A subnet group to associate with the replication instance.
    """
    replication_subnet_group_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
    (Optional) A list of VPC security group IDs to be used with the replication instance. The VPC securi
    ty groups must work with the VPC containing the replication instance.
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        replication_instance_class: str | core.StringOut,
        replication_instance_id: str | core.StringOut,
        allocated_storage: int | core.IntOut | None = None,
        allow_major_version_upgrade: bool | core.BoolOut | None = None,
        apply_immediately: bool | core.BoolOut | None = None,
        auto_minor_version_upgrade: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        multi_az: bool | core.BoolOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        replication_subnet_group_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationInstance.Args(
                replication_instance_class=replication_instance_class,
                replication_instance_id=replication_instance_id,
                allocated_storage=allocated_storage,
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                engine_version=engine_version,
                kms_key_arn=kms_key_arn,
                multi_az=multi_az,
                preferred_maintenance_window=preferred_maintenance_window,
                publicly_accessible=publicly_accessible,
                replication_subnet_group_id=replication_subnet_group_id,
                tags=tags,
                tags_all=tags_all,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocated_storage: int | core.IntOut | None = core.arg(default=None)

        allow_major_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        auto_minor_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        multi_az: bool | core.BoolOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        replication_instance_class: str | core.StringOut = core.arg()

        replication_instance_id: str | core.StringOut = core.arg()

        replication_subnet_group_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
