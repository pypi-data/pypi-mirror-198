import terrascript.core as core


@core.schema
class Logging(core.Schema):

    bucket_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    enable: bool | core.BoolOut = core.attr(bool)

    log_destination_type: str | core.StringOut | None = core.attr(str, default=None)

    log_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        enable: bool | core.BoolOut,
        bucket_name: str | core.StringOut | None = None,
        log_destination_type: str | core.StringOut | None = None,
        log_exports: list[str] | core.ArrayOut[core.StringOut] | None = None,
        s3_key_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Logging.Args(
                enable=enable,
                bucket_name=bucket_name,
                log_destination_type=log_destination_type,
                log_exports=log_exports,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut | None = core.arg(default=None)

        enable: bool | core.BoolOut = core.arg()

        log_destination_type: str | core.StringOut | None = core.arg(default=None)

        log_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        s3_key_prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ClusterNodes(core.Schema):

    node_role: str | core.StringOut = core.attr(str, computed=True)

    private_ip_address: str | core.StringOut = core.attr(str, computed=True)

    public_ip_address: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        node_role: str | core.StringOut,
        private_ip_address: str | core.StringOut,
        public_ip_address: str | core.StringOut,
    ):
        super().__init__(
            args=ClusterNodes.Args(
                node_role=node_role,
                private_ip_address=private_ip_address,
                public_ip_address=public_ip_address,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        node_role: str | core.StringOut = core.arg()

        private_ip_address: str | core.StringOut = core.arg()

        public_ip_address: str | core.StringOut = core.arg()


@core.schema
class SnapshotCopy(core.Schema):

    destination_region: str | core.StringOut = core.attr(str)

    grant_name: str | core.StringOut | None = core.attr(str, default=None)

    retention_period: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        destination_region: str | core.StringOut,
        grant_name: str | core.StringOut | None = None,
        retention_period: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=SnapshotCopy.Args(
                destination_region=destination_region,
                grant_name=grant_name,
                retention_period=retention_period,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_region: str | core.StringOut = core.arg()

        grant_name: str | core.StringOut | None = core.arg(default=None)

        retention_period: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_redshift_cluster", namespace="redshift")
class Cluster(core.Resource):
    """
    (Optional) If true , major version upgrades can be applied during the maintenance window to the Amaz
    on Redshift engine that is running on the cluster. Default is `true`.
    """

    allow_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether any cluster modifications are applied immediately, or during the next m
    aintenance window. Default is `false`.
    """
    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The value represents how the cluster is configured to use AQUA (Advanced Query Accelerato
    r) after the cluster is restored. Possible values are `enabled`, `disabled`, and `auto`. Requires Cl
    uster reboot.
    """
    aqua_configuration_status: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    Amazon Resource Name (ARN) of cluster
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The number of days that automated snapshots are retained. If the value is 0, automated sn
    apshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshot
    s when you want with create-cluster-snapshot. Default is 1.
    """
    automated_snapshot_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster
    . For example, if you have several EC2 instances running in a specific Availability Zone, then you m
    ight want the cluster to be provisioned in the same zone in order to decrease network latency. Can o
    nly be changed if `availability_zone_relocation_enabled` is `true`.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) If true, the cluster can be relocated to another availabity zone, either automatically by
    AWS or when requested. Default is `false`. Available for use on clusters from the RA3 instance fami
    ly.
    """
    availability_zone_relocation_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The Cluster Identifier. Must be a lower case string.
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    The nodes in the cluster. Cluster node blocks are documented below
    """
    cluster_nodes: list[ClusterNodes] | core.ArrayOut[ClusterNodes] = core.attr(
        ClusterNodes, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The name of the parameter group to be associated with this cluster.
    """
    cluster_parameter_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The public key for the cluster
    """
    cluster_public_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The specific revision number of the database in the cluster
    """
    cluster_revision_number: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) A list of security groups to be associated with this cluster.
    """
    cluster_security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The name of a cluster subnet group to be associated with this cluster. If this parameter
    is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
    """
    cluster_subnet_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The cluster type to use. Either `single-node` or `multi-node`.
    """
    cluster_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The version of the Amazon Redshift engine software that you want to deploy on the cluster
    .
    """
    cluster_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the first database to be created when the cluster is created.
    """
    database_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster w
    hen the cluster was created.
    """
    default_iam_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The DNS name of the cluster
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Elastic IP (EIP) address for the cluster.
    """
    elastic_ip: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) If true , the data in the cluster is encrypted at rest.
    """
    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The connection endpoint
    """
    endpoint: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) If true , enhanced VPC routing is enabled.
    """
    enhanced_vpc_routing: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) The identifier of the final snapshot that is to be created immediately before deleting th
    e cluster. If this parameter is provided, `skip_final_snapshot` must be false.
    """
    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated
    to the cluster at any time.
    """
    iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The Redshift Cluster ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN for the KMS encryption key. When specifying `kms_key_id`, `encrypted` needs to be
    set to true.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Logging, documented below.
    """
    logging: Logging | None = core.attr(Logging, default=None)

    """
    (Optional) The name of the maintenance track for the restored cluster. When you take a snapshot, the
    snapshot inherits the MaintenanceTrack value from the cluster. The snapshot might be on a different
    track than the cluster that was the source for the snapshot. For example, suppose that you take a s
    napshot of  a cluster that is on the current track and then change the cluster to be on the trailing
    track. In this case, the snapshot and the source cluster are on different tracks. Default value is
    current`.
    """
    maintenance_track_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional)  The default number of days to retain a manual snapshot. If the value is -1, the snapshot
    is retained indefinitely. This setting doesn't change the retention period of existing snapshots. V
    alid values are between `-1` and `3653`. Default value is `-1`.
    """
    manual_snapshot_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required unless a `snapshot_identifier` is provided) Password for the master DB user.
    """
    master_password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required unless a `snapshot_identifier` is provided) Username for the master DB user.
    """
    master_username: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The node type to be provisioned for the cluster.
    """
    node_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The number of compute nodes in the cluster. This parameter is required when the ClusterTy
    pe parameter is specified as multi-node. Default is 1.
    """
    number_of_nodes: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The AWS customer account used to create or copy the snapshot. Required if you are restori
    ng a snapshot you do not own, optional if you own the snapshot.
    """
    owner_account: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The port number on which the cluster accepts incoming connections. Valid values are betwe
    en `1115` and `65535`.
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The weekly time range (in UTC) during which automated cluster maintenance can occur.
    """
    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) If true, the cluster can be accessed from a public network. Default is `true`.
    """
    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Determines whether a final snapshot of the cluster is created before Amazon Redshift dele
    tes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snaps
    hot is created before the cluster is deleted. Default is false.
    """
    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The name of the cluster the source snapshot was created from.
    """
    snapshot_cluster_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration of automatic copy of snapshots from one region to another. Documented below
    .
    """
    snapshot_copy: SnapshotCopy | None = core.attr(SnapshotCopy, default=None)

    """
    (Optional) The name of the snapshot from which to create the new cluster.
    """
    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

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
    (Optional) A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        node_type: str | core.StringOut,
        allow_version_upgrade: bool | core.BoolOut | None = None,
        apply_immediately: bool | core.BoolOut | None = None,
        aqua_configuration_status: str | core.StringOut | None = None,
        automated_snapshot_retention_period: int | core.IntOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        availability_zone_relocation_enabled: bool | core.BoolOut | None = None,
        cluster_parameter_group_name: str | core.StringOut | None = None,
        cluster_public_key: str | core.StringOut | None = None,
        cluster_revision_number: str | core.StringOut | None = None,
        cluster_security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        cluster_subnet_group_name: str | core.StringOut | None = None,
        cluster_type: str | core.StringOut | None = None,
        cluster_version: str | core.StringOut | None = None,
        database_name: str | core.StringOut | None = None,
        default_iam_role_arn: str | core.StringOut | None = None,
        elastic_ip: str | core.StringOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        endpoint: str | core.StringOut | None = None,
        enhanced_vpc_routing: bool | core.BoolOut | None = None,
        final_snapshot_identifier: str | core.StringOut | None = None,
        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = None,
        kms_key_id: str | core.StringOut | None = None,
        logging: Logging | None = None,
        maintenance_track_name: str | core.StringOut | None = None,
        manual_snapshot_retention_period: int | core.IntOut | None = None,
        master_password: str | core.StringOut | None = None,
        master_username: str | core.StringOut | None = None,
        number_of_nodes: int | core.IntOut | None = None,
        owner_account: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        skip_final_snapshot: bool | core.BoolOut | None = None,
        snapshot_cluster_identifier: str | core.StringOut | None = None,
        snapshot_copy: SnapshotCopy | None = None,
        snapshot_identifier: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                cluster_identifier=cluster_identifier,
                node_type=node_type,
                allow_version_upgrade=allow_version_upgrade,
                apply_immediately=apply_immediately,
                aqua_configuration_status=aqua_configuration_status,
                automated_snapshot_retention_period=automated_snapshot_retention_period,
                availability_zone=availability_zone,
                availability_zone_relocation_enabled=availability_zone_relocation_enabled,
                cluster_parameter_group_name=cluster_parameter_group_name,
                cluster_public_key=cluster_public_key,
                cluster_revision_number=cluster_revision_number,
                cluster_security_groups=cluster_security_groups,
                cluster_subnet_group_name=cluster_subnet_group_name,
                cluster_type=cluster_type,
                cluster_version=cluster_version,
                database_name=database_name,
                default_iam_role_arn=default_iam_role_arn,
                elastic_ip=elastic_ip,
                encrypted=encrypted,
                endpoint=endpoint,
                enhanced_vpc_routing=enhanced_vpc_routing,
                final_snapshot_identifier=final_snapshot_identifier,
                iam_roles=iam_roles,
                kms_key_id=kms_key_id,
                logging=logging,
                maintenance_track_name=maintenance_track_name,
                manual_snapshot_retention_period=manual_snapshot_retention_period,
                master_password=master_password,
                master_username=master_username,
                number_of_nodes=number_of_nodes,
                owner_account=owner_account,
                port=port,
                preferred_maintenance_window=preferred_maintenance_window,
                publicly_accessible=publicly_accessible,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_cluster_identifier=snapshot_cluster_identifier,
                snapshot_copy=snapshot_copy,
                snapshot_identifier=snapshot_identifier,
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
        allow_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        aqua_configuration_status: str | core.StringOut | None = core.arg(default=None)

        automated_snapshot_retention_period: int | core.IntOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        availability_zone_relocation_enabled: bool | core.BoolOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut = core.arg()

        cluster_parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        cluster_public_key: str | core.StringOut | None = core.arg(default=None)

        cluster_revision_number: str | core.StringOut | None = core.arg(default=None)

        cluster_security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        cluster_subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        cluster_type: str | core.StringOut | None = core.arg(default=None)

        cluster_version: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut | None = core.arg(default=None)

        default_iam_role_arn: str | core.StringOut | None = core.arg(default=None)

        elastic_ip: str | core.StringOut | None = core.arg(default=None)

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        endpoint: str | core.StringOut | None = core.arg(default=None)

        enhanced_vpc_routing: bool | core.BoolOut | None = core.arg(default=None)

        final_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        logging: Logging | None = core.arg(default=None)

        maintenance_track_name: str | core.StringOut | None = core.arg(default=None)

        manual_snapshot_retention_period: int | core.IntOut | None = core.arg(default=None)

        master_password: str | core.StringOut | None = core.arg(default=None)

        master_username: str | core.StringOut | None = core.arg(default=None)

        node_type: str | core.StringOut = core.arg()

        number_of_nodes: int | core.IntOut | None = core.arg(default=None)

        owner_account: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        skip_final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        snapshot_copy: SnapshotCopy | None = core.arg(default=None)

        snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
