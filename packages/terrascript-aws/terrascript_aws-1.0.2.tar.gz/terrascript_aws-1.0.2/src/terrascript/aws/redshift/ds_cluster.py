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


@core.data(type="aws_redshift_cluster", namespace="aws_redshift")
class DsCluster(core.Data):

    allow_version_upgrade: bool | core.BoolOut = core.attr(bool, computed=True)

    aqua_configuration_status: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    automated_snapshot_retention_period: int | core.IntOut = core.attr(int, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    availability_zone_relocation_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    bucket_name: str | core.StringOut = core.attr(str, computed=True)

    cluster_identifier: str | core.StringOut = core.attr(str)

    cluster_nodes: list[ClusterNodes] | core.ArrayOut[ClusterNodes] = core.attr(
        ClusterNodes, computed=True, kind=core.Kind.array
    )

    cluster_parameter_group_name: str | core.StringOut = core.attr(str, computed=True)

    cluster_public_key: str | core.StringOut = core.attr(str, computed=True)

    cluster_revision_number: str | core.StringOut = core.attr(str, computed=True)

    cluster_security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cluster_subnet_group_name: str | core.StringOut = core.attr(str, computed=True)

    cluster_type: str | core.StringOut = core.attr(str, computed=True)

    cluster_version: str | core.StringOut = core.attr(str, computed=True)

    database_name: str | core.StringOut = core.attr(str, computed=True)

    default_iam_role_arn: str | core.StringOut = core.attr(str, computed=True)

    elastic_ip: str | core.StringOut = core.attr(str, computed=True)

    enable_logging: bool | core.BoolOut = core.attr(bool, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    enhanced_vpc_routing: bool | core.BoolOut = core.attr(bool, computed=True)

    iam_roles: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    log_destination_type: str | core.StringOut = core.attr(str, computed=True)

    log_exports: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    maintenance_track_name: str | core.StringOut = core.attr(str, computed=True)

    manual_snapshot_retention_period: int | core.IntOut = core.attr(int, computed=True)

    master_username: str | core.StringOut = core.attr(str, computed=True)

    node_type: str | core.StringOut = core.attr(str, computed=True)

    number_of_nodes: int | core.IntOut = core.attr(int, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    preferred_maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    publicly_accessible: bool | core.BoolOut = core.attr(bool, computed=True)

    s3_key_prefix: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

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
