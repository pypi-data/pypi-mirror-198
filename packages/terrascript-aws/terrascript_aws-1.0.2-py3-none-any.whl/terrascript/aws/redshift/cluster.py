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


@core.resource(type="aws_redshift_cluster", namespace="aws_redshift")
class Cluster(core.Resource):

    allow_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None)

    aqua_configuration_status: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    automated_snapshot_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    availability_zone_relocation_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    cluster_identifier: str | core.StringOut = core.attr(str)

    cluster_nodes: list[ClusterNodes] | core.ArrayOut[ClusterNodes] = core.attr(
        ClusterNodes, computed=True, kind=core.Kind.array
    )

    cluster_parameter_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    cluster_public_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cluster_revision_number: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    cluster_security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    cluster_subnet_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    cluster_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cluster_version: str | core.StringOut | None = core.attr(str, default=None)

    database_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    default_iam_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    elastic_ip: str | core.StringOut | None = core.attr(str, default=None)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    endpoint: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    enhanced_vpc_routing: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    logging: Logging | None = core.attr(Logging, default=None)

    maintenance_track_name: str | core.StringOut | None = core.attr(str, default=None)

    manual_snapshot_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    master_password: str | core.StringOut | None = core.attr(str, default=None)

    master_username: str | core.StringOut | None = core.attr(str, default=None)

    node_type: str | core.StringOut = core.attr(str)

    number_of_nodes: int | core.IntOut | None = core.attr(int, default=None)

    owner_account: str | core.StringOut | None = core.attr(str, default=None)

    port: int | core.IntOut | None = core.attr(int, default=None)

    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    snapshot_cluster_identifier: str | core.StringOut | None = core.attr(str, default=None)

    snapshot_copy: SnapshotCopy | None = core.attr(SnapshotCopy, default=None)

    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
