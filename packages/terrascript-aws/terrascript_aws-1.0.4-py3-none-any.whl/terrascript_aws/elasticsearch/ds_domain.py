import terrascript.core as core


@core.schema
class EncryptionAtRest(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        kms_key_id: str | core.StringOut,
    ):
        super().__init__(
            args=EncryptionAtRest.Args(
                enabled=enabled,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        kms_key_id: str | core.StringOut = core.arg()


@core.schema
class AdvancedSecurityOptions(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    internal_user_database_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        internal_user_database_enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=AdvancedSecurityOptions.Args(
                enabled=enabled,
                internal_user_database_enabled=internal_user_database_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        internal_user_database_enabled: bool | core.BoolOut = core.arg()


@core.schema
class CognitoOptions(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    identity_pool_id: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    user_pool_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        identity_pool_id: str | core.StringOut,
        role_arn: str | core.StringOut,
        user_pool_id: str | core.StringOut,
    ):
        super().__init__(
            args=CognitoOptions.Args(
                enabled=enabled,
                identity_pool_id=identity_pool_id,
                role_arn=role_arn,
                user_pool_id=user_pool_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        identity_pool_id: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        user_pool_id: str | core.StringOut = core.arg()


@core.schema
class NodeToNodeEncryption(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=NodeToNodeEncryption.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class SnapshotOptions(core.Schema):

    automated_snapshot_start_hour: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        automated_snapshot_start_hour: int | core.IntOut,
    ):
        super().__init__(
            args=SnapshotOptions.Args(
                automated_snapshot_start_hour=automated_snapshot_start_hour,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        automated_snapshot_start_hour: int | core.IntOut = core.arg()


@core.schema
class Duration(core.Schema):

    unit: str | core.StringOut = core.attr(str, computed=True)

    value: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        unit: str | core.StringOut,
        value: int | core.IntOut,
    ):
        super().__init__(
            args=Duration.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: str | core.StringOut = core.arg()

        value: int | core.IntOut = core.arg()


@core.schema
class MaintenanceSchedule(core.Schema):

    cron_expression_for_recurrence: str | core.StringOut = core.attr(str, computed=True)

    duration: list[Duration] | core.ArrayOut[Duration] = core.attr(
        Duration, computed=True, kind=core.Kind.array
    )

    start_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cron_expression_for_recurrence: str | core.StringOut,
        duration: list[Duration] | core.ArrayOut[Duration],
        start_at: str | core.StringOut,
    ):
        super().__init__(
            args=MaintenanceSchedule.Args(
                cron_expression_for_recurrence=cron_expression_for_recurrence,
                duration=duration,
                start_at=start_at,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cron_expression_for_recurrence: str | core.StringOut = core.arg()

        duration: list[Duration] | core.ArrayOut[Duration] = core.arg()

        start_at: str | core.StringOut = core.arg()


@core.schema
class AutoTuneOptions(core.Schema):

    desired_state: str | core.StringOut = core.attr(str, computed=True)

    maintenance_schedule: list[MaintenanceSchedule] | core.ArrayOut[
        MaintenanceSchedule
    ] = core.attr(MaintenanceSchedule, computed=True, kind=core.Kind.array)

    rollback_on_disable: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        desired_state: str | core.StringOut,
        maintenance_schedule: list[MaintenanceSchedule] | core.ArrayOut[MaintenanceSchedule],
        rollback_on_disable: str | core.StringOut,
    ):
        super().__init__(
            args=AutoTuneOptions.Args(
                desired_state=desired_state,
                maintenance_schedule=maintenance_schedule,
                rollback_on_disable=rollback_on_disable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        desired_state: str | core.StringOut = core.arg()

        maintenance_schedule: list[MaintenanceSchedule] | core.ArrayOut[
            MaintenanceSchedule
        ] = core.arg()

        rollback_on_disable: str | core.StringOut = core.arg()


@core.schema
class VpcOptions(core.Schema):

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zones: list[str] | core.ArrayOut[core.StringOut],
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcOptions.Args(
                availability_zones=availability_zones,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class ZoneAwarenessConfig(core.Schema):

    availability_zone_count: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        availability_zone_count: int | core.IntOut,
    ):
        super().__init__(
            args=ZoneAwarenessConfig.Args(
                availability_zone_count=availability_zone_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone_count: int | core.IntOut = core.arg()


@core.schema
class ColdStorageOptions(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=ColdStorageOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class ClusterConfig(core.Schema):

    cold_storage_options: list[ColdStorageOptions] | core.ArrayOut[ColdStorageOptions] = core.attr(
        ColdStorageOptions, computed=True, kind=core.Kind.array
    )

    dedicated_master_count: int | core.IntOut = core.attr(int, computed=True)

    dedicated_master_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    dedicated_master_type: str | core.StringOut = core.attr(str, computed=True)

    instance_count: int | core.IntOut = core.attr(int, computed=True)

    instance_type: str | core.StringOut = core.attr(str, computed=True)

    warm_count: int | core.IntOut = core.attr(int, computed=True)

    warm_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    warm_type: str | core.StringOut = core.attr(str, computed=True)

    zone_awareness_config: list[ZoneAwarenessConfig] | core.ArrayOut[
        ZoneAwarenessConfig
    ] = core.attr(ZoneAwarenessConfig, computed=True, kind=core.Kind.array)

    zone_awareness_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        cold_storage_options: list[ColdStorageOptions] | core.ArrayOut[ColdStorageOptions],
        dedicated_master_count: int | core.IntOut,
        dedicated_master_enabled: bool | core.BoolOut,
        dedicated_master_type: str | core.StringOut,
        instance_count: int | core.IntOut,
        instance_type: str | core.StringOut,
        warm_count: int | core.IntOut,
        warm_enabled: bool | core.BoolOut,
        warm_type: str | core.StringOut,
        zone_awareness_config: list[ZoneAwarenessConfig] | core.ArrayOut[ZoneAwarenessConfig],
        zone_awareness_enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=ClusterConfig.Args(
                cold_storage_options=cold_storage_options,
                dedicated_master_count=dedicated_master_count,
                dedicated_master_enabled=dedicated_master_enabled,
                dedicated_master_type=dedicated_master_type,
                instance_count=instance_count,
                instance_type=instance_type,
                warm_count=warm_count,
                warm_enabled=warm_enabled,
                warm_type=warm_type,
                zone_awareness_config=zone_awareness_config,
                zone_awareness_enabled=zone_awareness_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cold_storage_options: list[ColdStorageOptions] | core.ArrayOut[
            ColdStorageOptions
        ] = core.arg()

        dedicated_master_count: int | core.IntOut = core.arg()

        dedicated_master_enabled: bool | core.BoolOut = core.arg()

        dedicated_master_type: str | core.StringOut = core.arg()

        instance_count: int | core.IntOut = core.arg()

        instance_type: str | core.StringOut = core.arg()

        warm_count: int | core.IntOut = core.arg()

        warm_enabled: bool | core.BoolOut = core.arg()

        warm_type: str | core.StringOut = core.arg()

        zone_awareness_config: list[ZoneAwarenessConfig] | core.ArrayOut[
            ZoneAwarenessConfig
        ] = core.arg()

        zone_awareness_enabled: bool | core.BoolOut = core.arg()


@core.schema
class EbsOptions(core.Schema):

    ebs_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ebs_enabled: bool | core.BoolOut,
        iops: int | core.IntOut,
        throughput: int | core.IntOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
    ):
        super().__init__(
            args=EbsOptions.Args(
                ebs_enabled=ebs_enabled,
                iops=iops,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ebs_enabled: bool | core.BoolOut = core.arg()

        iops: int | core.IntOut = core.arg()

        throughput: int | core.IntOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.schema
class LogPublishingOptions(core.Schema):

    cloudwatch_log_group_arn: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    log_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cloudwatch_log_group_arn: str | core.StringOut,
        enabled: bool | core.BoolOut,
        log_type: str | core.StringOut,
    ):
        super().__init__(
            args=LogPublishingOptions.Args(
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                enabled=enabled,
                log_type=log_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group_arn: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut = core.arg()

        log_type: str | core.StringOut = core.arg()


@core.data(type="aws_elasticsearch_domain", namespace="elasticsearch")
class DsDomain(core.Data):

    access_policies: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value string pairs to specify advanced configuration options.
    """
    advanced_options: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    Status of the Elasticsearch domain's advanced security options. The block consists of the following
    attributes:
    """
    advanced_security_options: list[AdvancedSecurityOptions] | core.ArrayOut[
        AdvancedSecurityOptions
    ] = core.attr(AdvancedSecurityOptions, computed=True, kind=core.Kind.array)

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Configuration of the Auto-Tune options of the domain.
    """
    auto_tune_options: list[AutoTuneOptions] | core.ArrayOut[AutoTuneOptions] = core.attr(
        AutoTuneOptions, computed=True, kind=core.Kind.array
    )

    """
    Cluster configuration of the domain.
    """
    cluster_config: list[ClusterConfig] | core.ArrayOut[ClusterConfig] = core.attr(
        ClusterConfig, computed=True, kind=core.Kind.array
    )

    """
    Domain Amazon Cognito Authentication options for Kibana.
    """
    cognito_options: list[CognitoOptions] | core.ArrayOut[CognitoOptions] = core.attr(
        CognitoOptions, computed=True, kind=core.Kind.array
    )

    created: bool | core.BoolOut = core.attr(bool, computed=True)

    deleted: bool | core.BoolOut = core.attr(bool, computed=True)

    domain_id: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut = core.attr(str)

    """
    EBS Options for the instances in the domain.
    """
    ebs_options: list[EbsOptions] | core.ArrayOut[EbsOptions] = core.attr(
        EbsOptions, computed=True, kind=core.Kind.array
    )

    elasticsearch_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Domain encryption at rest related options.
    """
    encryption_at_rest: list[EncryptionAtRest] | core.ArrayOut[EncryptionAtRest] = core.attr(
        EncryptionAtRest, computed=True, kind=core.Kind.array
    )

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Domain-specific endpoint used to access the Kibana application.
    """
    kibana_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    Domain log publishing related options.
    """
    log_publishing_options: list[LogPublishingOptions] | core.ArrayOut[
        LogPublishingOptions
    ] = core.attr(LogPublishingOptions, computed=True, kind=core.Kind.array)

    """
    Domain in transit encryption related options.
    """
    node_to_node_encryption: list[NodeToNodeEncryption] | core.ArrayOut[
        NodeToNodeEncryption
    ] = core.attr(NodeToNodeEncryption, computed=True, kind=core.Kind.array)

    processing: bool | core.BoolOut = core.attr(bool, computed=True)

    snapshot_options: list[SnapshotOptions] | core.ArrayOut[SnapshotOptions] = core.attr(
        SnapshotOptions, computed=True, kind=core.Kind.array
    )

    """
    The tags assigned to the domain.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    VPC Options for private Elasticsearch domains.
    """
    vpc_options: list[VpcOptions] | core.ArrayOut[VpcOptions] = core.attr(
        VpcOptions, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDomain.Args(
                domain_name=domain_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
