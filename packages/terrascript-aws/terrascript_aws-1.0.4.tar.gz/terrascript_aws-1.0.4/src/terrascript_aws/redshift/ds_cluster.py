import terrascript.core as core


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


@core.data(type="aws_redshift_cluster", namespace="redshift")
class DsCluster(core.Data):
    """
    Whether major version upgrades can be applied during maintenance period
    """

    allow_version_upgrade: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The value represents how the cluster is configured to use AQUA.
    """
    aqua_configuration_status: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of cluster.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The backup retention period
    """
    automated_snapshot_retention_period: int | core.IntOut = core.attr(int, computed=True)

    """
    The availability zone of the cluster
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether the cluster is able to be relocated to another availability zone.
    """
    availability_zone_relocation_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The name of the S3 bucket where the log files are to be stored
    """
    bucket_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The cluster identifier
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    The nodes in the cluster. Cluster node blocks are documented below
    """
    cluster_nodes: list[ClusterNodes] | core.ArrayOut[ClusterNodes] = core.attr(
        ClusterNodes, computed=True, kind=core.Kind.array
    )

    """
    The name of the parameter group to be associated with this cluster
    """
    cluster_parameter_group_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The public key for the cluster
    """
    cluster_public_key: str | core.StringOut = core.attr(str, computed=True)

    """
    The cluster revision number
    """
    cluster_revision_number: str | core.StringOut = core.attr(str, computed=True)

    """
    The security groups associated with the cluster
    """
    cluster_security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The name of a cluster subnet group to be associated with this cluster
    """
    cluster_subnet_group_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The cluster type
    """
    cluster_type: str | core.StringOut = core.attr(str, computed=True)

    cluster_version: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the default database in the cluster
    """
    database_name: str | core.StringOut = core.attr(str, computed=True)

    """
    ∂The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cl
    uster was created.
    """
    default_iam_role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Elastic IP of the cluster
    """
    elastic_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether cluster logging is enabled
    """
    enable_logging: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether the cluster data is encrypted
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The cluster endpoint
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether enhanced VPC routing is enabled
    """
    enhanced_vpc_routing: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The IAM roles associated to the cluster
    """
    iam_roles: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The KMS encryption key associated to the cluster
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The log destination type.
    """
    log_destination_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The collection of exported log types. Log types include the connection log, user log and user activi
    ty log.
    """
    log_exports: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The name of the maintenance track for the restored cluster.
    """
    maintenance_track_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional)  The default number of days to retain a manual snapshot.
    """
    manual_snapshot_retention_period: int | core.IntOut = core.attr(int, computed=True)

    """
    Username for the master DB user
    """
    master_username: str | core.StringOut = core.attr(str, computed=True)

    """
    The cluster node type
    """
    node_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of nodes in the cluster
    """
    number_of_nodes: int | core.IntOut = core.attr(int, computed=True)

    """
    The port the cluster responds on
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    """
    The maintenance window
    """
    preferred_maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the cluster is publicly accessible
    """
    publicly_accessible: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The folder inside the S3 bucket where the log files are stored
    """
    s3_key_prefix: str | core.StringOut = core.attr(str, computed=True)

    """
    The tags associated to the cluster
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    The VPC Id associated with the cluster
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The VPC security group Ids associated with the cluster
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                cluster_identifier=cluster_identifier,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_identifier: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
