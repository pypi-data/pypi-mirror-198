import terrascript.core as core


@core.schema
class MasterUserOptions(core.Schema):

    master_user_arn: str | core.StringOut | None = core.attr(str, default=None)

    master_user_name: str | core.StringOut | None = core.attr(str, default=None)

    master_user_password: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        master_user_arn: str | core.StringOut | None = None,
        master_user_name: str | core.StringOut | None = None,
        master_user_password: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MasterUserOptions.Args(
                master_user_arn=master_user_arn,
                master_user_name=master_user_name,
                master_user_password=master_user_password,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        master_user_arn: str | core.StringOut | None = core.arg(default=None)

        master_user_name: str | core.StringOut | None = core.arg(default=None)

        master_user_password: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AdvancedSecurityOptions(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    internal_user_database_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    master_user_options: MasterUserOptions | None = core.attr(MasterUserOptions, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        internal_user_database_enabled: bool | core.BoolOut | None = None,
        master_user_options: MasterUserOptions | None = None,
    ):
        super().__init__(
            args=AdvancedSecurityOptions.Args(
                enabled=enabled,
                internal_user_database_enabled=internal_user_database_enabled,
                master_user_options=master_user_options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        internal_user_database_enabled: bool | core.BoolOut | None = core.arg(default=None)

        master_user_options: MasterUserOptions | None = core.arg(default=None)


@core.schema
class SnapshotOptions(core.Schema):

    automated_snapshot_start_hour: int | core.IntOut = core.attr(int)

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
class NodeToNodeEncryption(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

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
class ZoneAwarenessConfig(core.Schema):

    availability_zone_count: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        availability_zone_count: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ZoneAwarenessConfig.Args(
                availability_zone_count=availability_zone_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone_count: int | core.IntOut | None = core.arg(default=None)


@core.schema
class ColdStorageOptions(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ColdStorageOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class ClusterConfig(core.Schema):

    cold_storage_options: ColdStorageOptions | None = core.attr(
        ColdStorageOptions, default=None, computed=True
    )

    dedicated_master_count: int | core.IntOut | None = core.attr(int, default=None)

    dedicated_master_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    dedicated_master_type: str | core.StringOut | None = core.attr(str, default=None)

    instance_count: int | core.IntOut | None = core.attr(int, default=None)

    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    warm_count: int | core.IntOut | None = core.attr(int, default=None)

    warm_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    warm_type: str | core.StringOut | None = core.attr(str, default=None)

    zone_awareness_config: ZoneAwarenessConfig | None = core.attr(ZoneAwarenessConfig, default=None)

    zone_awareness_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        cold_storage_options: ColdStorageOptions | None = None,
        dedicated_master_count: int | core.IntOut | None = None,
        dedicated_master_enabled: bool | core.BoolOut | None = None,
        dedicated_master_type: str | core.StringOut | None = None,
        instance_count: int | core.IntOut | None = None,
        instance_type: str | core.StringOut | None = None,
        warm_count: int | core.IntOut | None = None,
        warm_enabled: bool | core.BoolOut | None = None,
        warm_type: str | core.StringOut | None = None,
        zone_awareness_config: ZoneAwarenessConfig | None = None,
        zone_awareness_enabled: bool | core.BoolOut | None = None,
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
        cold_storage_options: ColdStorageOptions | None = core.arg(default=None)

        dedicated_master_count: int | core.IntOut | None = core.arg(default=None)

        dedicated_master_enabled: bool | core.BoolOut | None = core.arg(default=None)

        dedicated_master_type: str | core.StringOut | None = core.arg(default=None)

        instance_count: int | core.IntOut | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        warm_count: int | core.IntOut | None = core.arg(default=None)

        warm_enabled: bool | core.BoolOut | None = core.arg(default=None)

        warm_type: str | core.StringOut | None = core.arg(default=None)

        zone_awareness_config: ZoneAwarenessConfig | None = core.arg(default=None)

        zone_awareness_enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class VpcOptions(core.Schema):

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zones: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=VpcOptions.Args(
                availability_zones=availability_zones,
                vpc_id=vpc_id,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class CognitoOptions(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    identity_pool_id: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        identity_pool_id: str | core.StringOut,
        role_arn: str | core.StringOut,
        user_pool_id: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=CognitoOptions.Args(
                identity_pool_id=identity_pool_id,
                role_arn=role_arn,
                user_pool_id=user_pool_id,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        identity_pool_id: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        user_pool_id: str | core.StringOut = core.arg()


@core.schema
class EncryptAtRest(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EncryptAtRest.Args(
                enabled=enabled,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        kms_key_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DomainEndpointOptions(core.Schema):

    custom_endpoint: str | core.StringOut | None = core.attr(str, default=None)

    custom_endpoint_certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    custom_endpoint_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    enforce_https: bool | core.BoolOut | None = core.attr(bool, default=None)

    tls_security_policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        custom_endpoint: str | core.StringOut | None = None,
        custom_endpoint_certificate_arn: str | core.StringOut | None = None,
        custom_endpoint_enabled: bool | core.BoolOut | None = None,
        enforce_https: bool | core.BoolOut | None = None,
        tls_security_policy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DomainEndpointOptions.Args(
                custom_endpoint=custom_endpoint,
                custom_endpoint_certificate_arn=custom_endpoint_certificate_arn,
                custom_endpoint_enabled=custom_endpoint_enabled,
                enforce_https=enforce_https,
                tls_security_policy=tls_security_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_endpoint: str | core.StringOut | None = core.arg(default=None)

        custom_endpoint_certificate_arn: str | core.StringOut | None = core.arg(default=None)

        custom_endpoint_enabled: bool | core.BoolOut | None = core.arg(default=None)

        enforce_https: bool | core.BoolOut | None = core.arg(default=None)

        tls_security_policy: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EbsOptions(core.Schema):

    ebs_enabled: bool | core.BoolOut = core.attr(bool)

    iops: int | core.IntOut | None = core.attr(int, default=None)

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        ebs_enabled: bool | core.BoolOut,
        iops: int | core.IntOut | None = None,
        throughput: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
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

        iops: int | core.IntOut | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LogPublishingOptions(core.Schema):

    cloudwatch_log_group_arn: str | core.StringOut = core.attr(str)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    log_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cloudwatch_log_group_arn: str | core.StringOut,
        log_type: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=LogPublishingOptions.Args(
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                log_type=log_type,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group_arn: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        log_type: str | core.StringOut = core.arg()


@core.schema
class Duration(core.Schema):

    unit: str | core.StringOut = core.attr(str)

    value: int | core.IntOut = core.attr(int)

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

    cron_expression_for_recurrence: str | core.StringOut = core.attr(str)

    duration: Duration = core.attr(Duration)

    start_at: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cron_expression_for_recurrence: str | core.StringOut,
        duration: Duration,
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

        duration: Duration = core.arg()

        start_at: str | core.StringOut = core.arg()


@core.schema
class AutoTuneOptions(core.Schema):

    desired_state: str | core.StringOut = core.attr(str)

    maintenance_schedule: list[MaintenanceSchedule] | core.ArrayOut[
        MaintenanceSchedule
    ] | None = core.attr(MaintenanceSchedule, default=None, computed=True, kind=core.Kind.array)

    rollback_on_disable: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        desired_state: str | core.StringOut,
        maintenance_schedule: list[MaintenanceSchedule]
        | core.ArrayOut[MaintenanceSchedule]
        | None = None,
        rollback_on_disable: str | core.StringOut | None = None,
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
        ] | None = core.arg(default=None)

        rollback_on_disable: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_elasticsearch_domain", namespace="aws_elasticsearch")
class Domain(core.Resource):

    access_policies: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    advanced_options: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    advanced_security_options: AdvancedSecurityOptions | None = core.attr(
        AdvancedSecurityOptions, default=None, computed=True
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_tune_options: AutoTuneOptions | None = core.attr(
        AutoTuneOptions, default=None, computed=True
    )

    cluster_config: ClusterConfig | None = core.attr(ClusterConfig, default=None, computed=True)

    cognito_options: CognitoOptions | None = core.attr(CognitoOptions, default=None)

    domain_endpoint_options: DomainEndpointOptions | None = core.attr(
        DomainEndpointOptions, default=None, computed=True
    )

    domain_id: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut = core.attr(str)

    ebs_options: EbsOptions | None = core.attr(EbsOptions, default=None, computed=True)

    elasticsearch_version: str | core.StringOut | None = core.attr(str, default=None)

    encrypt_at_rest: EncryptAtRest | None = core.attr(EncryptAtRest, default=None, computed=True)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kibana_endpoint: str | core.StringOut = core.attr(str, computed=True)

    log_publishing_options: list[LogPublishingOptions] | core.ArrayOut[
        LogPublishingOptions
    ] | None = core.attr(LogPublishingOptions, default=None, kind=core.Kind.array)

    node_to_node_encryption: NodeToNodeEncryption | None = core.attr(
        NodeToNodeEncryption, default=None, computed=True
    )

    snapshot_options: SnapshotOptions | None = core.attr(SnapshotOptions, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_options: VpcOptions | None = core.attr(VpcOptions, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: str | core.StringOut,
        access_policies: str | core.StringOut | None = None,
        advanced_options: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        advanced_security_options: AdvancedSecurityOptions | None = None,
        auto_tune_options: AutoTuneOptions | None = None,
        cluster_config: ClusterConfig | None = None,
        cognito_options: CognitoOptions | None = None,
        domain_endpoint_options: DomainEndpointOptions | None = None,
        ebs_options: EbsOptions | None = None,
        elasticsearch_version: str | core.StringOut | None = None,
        encrypt_at_rest: EncryptAtRest | None = None,
        log_publishing_options: list[LogPublishingOptions]
        | core.ArrayOut[LogPublishingOptions]
        | None = None,
        node_to_node_encryption: NodeToNodeEncryption | None = None,
        snapshot_options: SnapshotOptions | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_options: VpcOptions | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Domain.Args(
                domain_name=domain_name,
                access_policies=access_policies,
                advanced_options=advanced_options,
                advanced_security_options=advanced_security_options,
                auto_tune_options=auto_tune_options,
                cluster_config=cluster_config,
                cognito_options=cognito_options,
                domain_endpoint_options=domain_endpoint_options,
                ebs_options=ebs_options,
                elasticsearch_version=elasticsearch_version,
                encrypt_at_rest=encrypt_at_rest,
                log_publishing_options=log_publishing_options,
                node_to_node_encryption=node_to_node_encryption,
                snapshot_options=snapshot_options,
                tags=tags,
                tags_all=tags_all,
                vpc_options=vpc_options,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policies: str | core.StringOut | None = core.arg(default=None)

        advanced_options: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        advanced_security_options: AdvancedSecurityOptions | None = core.arg(default=None)

        auto_tune_options: AutoTuneOptions | None = core.arg(default=None)

        cluster_config: ClusterConfig | None = core.arg(default=None)

        cognito_options: CognitoOptions | None = core.arg(default=None)

        domain_endpoint_options: DomainEndpointOptions | None = core.arg(default=None)

        domain_name: str | core.StringOut = core.arg()

        ebs_options: EbsOptions | None = core.arg(default=None)

        elasticsearch_version: str | core.StringOut | None = core.arg(default=None)

        encrypt_at_rest: EncryptAtRest | None = core.arg(default=None)

        log_publishing_options: list[LogPublishingOptions] | core.ArrayOut[
            LogPublishingOptions
        ] | None = core.arg(default=None)

        node_to_node_encryption: NodeToNodeEncryption | None = core.arg(default=None)

        snapshot_options: SnapshotOptions | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_options: VpcOptions | None = core.arg(default=None)
