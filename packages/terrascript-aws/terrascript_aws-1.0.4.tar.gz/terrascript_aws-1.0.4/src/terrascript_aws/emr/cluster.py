import terrascript.core as core


@core.schema
class AutoTerminationPolicy(core.Schema):

    idle_timeout: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        idle_timeout: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AutoTerminationPolicy.Args(
                idle_timeout=idle_timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle_timeout: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Configurations(core.Schema):

    classification: str | core.StringOut | None = core.attr(str, default=None)

    properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        classification: str | core.StringOut | None = None,
        properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Configurations.Args(
                classification=classification,
                properties=properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classification: str | core.StringOut | None = core.arg(default=None)

        properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class InstanceTypeConfigsEbsConfig(core.Schema):

    iops: int | core.IntOut | None = core.attr(int, default=None)

    size: int | core.IntOut = core.attr(int)

    type: str | core.StringOut = core.attr(str)

    volumes_per_instance: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        size: int | core.IntOut,
        type: str | core.StringOut,
        iops: int | core.IntOut | None = None,
        volumes_per_instance: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=InstanceTypeConfigsEbsConfig.Args(
                size=size,
                type=type,
                iops=iops,
                volumes_per_instance=volumes_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: int | core.IntOut | None = core.arg(default=None)

        size: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()

        volumes_per_instance: int | core.IntOut | None = core.arg(default=None)


@core.schema
class InstanceTypeConfigs(core.Schema):

    bid_price: str | core.StringOut | None = core.attr(str, default=None)

    bid_price_as_percentage_of_on_demand_price: float | core.FloatOut | None = core.attr(
        float, default=None
    )

    configurations: list[Configurations] | core.ArrayOut[Configurations] | None = core.attr(
        Configurations, default=None, kind=core.Kind.array
    )

    ebs_config: list[InstanceTypeConfigsEbsConfig] | core.ArrayOut[
        InstanceTypeConfigsEbsConfig
    ] | None = core.attr(
        InstanceTypeConfigsEbsConfig, default=None, computed=True, kind=core.Kind.array
    )

    instance_type: str | core.StringOut = core.attr(str)

    weighted_capacity: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        instance_type: str | core.StringOut,
        bid_price: str | core.StringOut | None = None,
        bid_price_as_percentage_of_on_demand_price: float | core.FloatOut | None = None,
        configurations: list[Configurations] | core.ArrayOut[Configurations] | None = None,
        ebs_config: list[InstanceTypeConfigsEbsConfig]
        | core.ArrayOut[InstanceTypeConfigsEbsConfig]
        | None = None,
        weighted_capacity: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=InstanceTypeConfigs.Args(
                instance_type=instance_type,
                bid_price=bid_price,
                bid_price_as_percentage_of_on_demand_price=bid_price_as_percentage_of_on_demand_price,
                configurations=configurations,
                ebs_config=ebs_config,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bid_price: str | core.StringOut | None = core.arg(default=None)

        bid_price_as_percentage_of_on_demand_price: float | core.FloatOut | None = core.arg(
            default=None
        )

        configurations: list[Configurations] | core.ArrayOut[Configurations] | None = core.arg(
            default=None
        )

        ebs_config: list[InstanceTypeConfigsEbsConfig] | core.ArrayOut[
            InstanceTypeConfigsEbsConfig
        ] | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        weighted_capacity: int | core.IntOut | None = core.arg(default=None)


@core.schema
class OnDemandSpecification(core.Schema):

    allocation_strategy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        allocation_strategy: str | core.StringOut,
    ):
        super().__init__(
            args=OnDemandSpecification.Args(
                allocation_strategy=allocation_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: str | core.StringOut = core.arg()


@core.schema
class SpotSpecification(core.Schema):

    allocation_strategy: str | core.StringOut = core.attr(str)

    block_duration_minutes: int | core.IntOut | None = core.attr(int, default=None)

    timeout_action: str | core.StringOut = core.attr(str)

    timeout_duration_minutes: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        allocation_strategy: str | core.StringOut,
        timeout_action: str | core.StringOut,
        timeout_duration_minutes: int | core.IntOut,
        block_duration_minutes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=SpotSpecification.Args(
                allocation_strategy=allocation_strategy,
                timeout_action=timeout_action,
                timeout_duration_minutes=timeout_duration_minutes,
                block_duration_minutes=block_duration_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: str | core.StringOut = core.arg()

        block_duration_minutes: int | core.IntOut | None = core.arg(default=None)

        timeout_action: str | core.StringOut = core.arg()

        timeout_duration_minutes: int | core.IntOut = core.arg()


@core.schema
class LaunchSpecifications(core.Schema):

    on_demand_specification: list[OnDemandSpecification] | core.ArrayOut[
        OnDemandSpecification
    ] | None = core.attr(OnDemandSpecification, default=None, kind=core.Kind.array)

    spot_specification: list[SpotSpecification] | core.ArrayOut[
        SpotSpecification
    ] | None = core.attr(SpotSpecification, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        on_demand_specification: list[OnDemandSpecification]
        | core.ArrayOut[OnDemandSpecification]
        | None = None,
        spot_specification: list[SpotSpecification]
        | core.ArrayOut[SpotSpecification]
        | None = None,
    ):
        super().__init__(
            args=LaunchSpecifications.Args(
                on_demand_specification=on_demand_specification,
                spot_specification=spot_specification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_demand_specification: list[OnDemandSpecification] | core.ArrayOut[
            OnDemandSpecification
        ] | None = core.arg(default=None)

        spot_specification: list[SpotSpecification] | core.ArrayOut[
            SpotSpecification
        ] | None = core.arg(default=None)


@core.schema
class MasterInstanceFleet(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_type_configs: list[InstanceTypeConfigs] | core.ArrayOut[
        InstanceTypeConfigs
    ] | None = core.attr(InstanceTypeConfigs, default=None, kind=core.Kind.array)

    launch_specifications: LaunchSpecifications | None = core.attr(
        LaunchSpecifications, default=None
    )

    name: str | core.StringOut | None = core.attr(str, default=None)

    provisioned_on_demand_capacity: int | core.IntOut = core.attr(int, computed=True)

    provisioned_spot_capacity: int | core.IntOut = core.attr(int, computed=True)

    target_on_demand_capacity: int | core.IntOut | None = core.attr(int, default=None)

    target_spot_capacity: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        provisioned_on_demand_capacity: int | core.IntOut,
        provisioned_spot_capacity: int | core.IntOut,
        instance_type_configs: list[InstanceTypeConfigs]
        | core.ArrayOut[InstanceTypeConfigs]
        | None = None,
        launch_specifications: LaunchSpecifications | None = None,
        name: str | core.StringOut | None = None,
        target_on_demand_capacity: int | core.IntOut | None = None,
        target_spot_capacity: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=MasterInstanceFleet.Args(
                id=id,
                provisioned_on_demand_capacity=provisioned_on_demand_capacity,
                provisioned_spot_capacity=provisioned_spot_capacity,
                instance_type_configs=instance_type_configs,
                launch_specifications=launch_specifications,
                name=name,
                target_on_demand_capacity=target_on_demand_capacity,
                target_spot_capacity=target_spot_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        instance_type_configs: list[InstanceTypeConfigs] | core.ArrayOut[
            InstanceTypeConfigs
        ] | None = core.arg(default=None)

        launch_specifications: LaunchSpecifications | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        provisioned_on_demand_capacity: int | core.IntOut = core.arg()

        provisioned_spot_capacity: int | core.IntOut = core.arg()

        target_on_demand_capacity: int | core.IntOut | None = core.arg(default=None)

        target_spot_capacity: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Ec2Attributes(core.Schema):

    additional_master_security_groups: str | core.StringOut | None = core.attr(str, default=None)

    additional_slave_security_groups: str | core.StringOut | None = core.attr(str, default=None)

    emr_managed_master_security_group: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    emr_managed_slave_security_group: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    instance_profile: str | core.StringOut = core.attr(str)

    key_name: str | core.StringOut | None = core.attr(str, default=None)

    service_access_security_group: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        instance_profile: str | core.StringOut,
        additional_master_security_groups: str | core.StringOut | None = None,
        additional_slave_security_groups: str | core.StringOut | None = None,
        emr_managed_master_security_group: str | core.StringOut | None = None,
        emr_managed_slave_security_group: str | core.StringOut | None = None,
        key_name: str | core.StringOut | None = None,
        service_access_security_group: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Ec2Attributes.Args(
                instance_profile=instance_profile,
                additional_master_security_groups=additional_master_security_groups,
                additional_slave_security_groups=additional_slave_security_groups,
                emr_managed_master_security_group=emr_managed_master_security_group,
                emr_managed_slave_security_group=emr_managed_slave_security_group,
                key_name=key_name,
                service_access_security_group=service_access_security_group,
                subnet_id=subnet_id,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        additional_master_security_groups: str | core.StringOut | None = core.arg(default=None)

        additional_slave_security_groups: str | core.StringOut | None = core.arg(default=None)

        emr_managed_master_security_group: str | core.StringOut | None = core.arg(default=None)

        emr_managed_slave_security_group: str | core.StringOut | None = core.arg(default=None)

        instance_profile: str | core.StringOut = core.arg()

        key_name: str | core.StringOut | None = core.arg(default=None)

        service_access_security_group: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class HadoopJarStep(core.Schema):

    args: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    jar: str | core.StringOut = core.attr(str)

    main_class: str | core.StringOut | None = core.attr(str, default=None)

    properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        jar: str | core.StringOut,
        args: list[str] | core.ArrayOut[core.StringOut] | None = None,
        main_class: str | core.StringOut | None = None,
        properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=HadoopJarStep.Args(
                jar=jar,
                args=args,
                main_class=main_class,
                properties=properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        args: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        jar: str | core.StringOut = core.arg()

        main_class: str | core.StringOut | None = core.arg(default=None)

        properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Step(core.Schema):

    action_on_failure: str | core.StringOut = core.attr(str)

    hadoop_jar_step: HadoopJarStep = core.attr(HadoopJarStep)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        action_on_failure: str | core.StringOut,
        hadoop_jar_step: HadoopJarStep,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Step.Args(
                action_on_failure=action_on_failure,
                hadoop_jar_step=hadoop_jar_step,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_on_failure: str | core.StringOut = core.arg()

        hadoop_jar_step: HadoopJarStep = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class CoreInstanceGroupEbsConfig(core.Schema):

    iops: int | core.IntOut | None = core.attr(int, default=None)

    size: int | core.IntOut = core.attr(int)

    throughput: int | core.IntOut | None = core.attr(int, default=None)

    type: str | core.StringOut = core.attr(str)

    volumes_per_instance: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        size: int | core.IntOut,
        type: str | core.StringOut,
        iops: int | core.IntOut | None = None,
        throughput: int | core.IntOut | None = None,
        volumes_per_instance: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CoreInstanceGroupEbsConfig.Args(
                size=size,
                type=type,
                iops=iops,
                throughput=throughput,
                volumes_per_instance=volumes_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: int | core.IntOut | None = core.arg(default=None)

        size: int | core.IntOut = core.arg()

        throughput: int | core.IntOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        volumes_per_instance: int | core.IntOut | None = core.arg(default=None)


@core.schema
class CoreInstanceGroup(core.Schema):

    autoscaling_policy: str | core.StringOut | None = core.attr(str, default=None)

    bid_price: str | core.StringOut | None = core.attr(str, default=None)

    ebs_config: list[CoreInstanceGroupEbsConfig] | core.ArrayOut[
        CoreInstanceGroupEbsConfig
    ] | None = core.attr(
        CoreInstanceGroupEbsConfig, default=None, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_count: int | core.IntOut | None = core.attr(int, default=None)

    instance_type: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        instance_type: str | core.StringOut,
        autoscaling_policy: str | core.StringOut | None = None,
        bid_price: str | core.StringOut | None = None,
        ebs_config: list[CoreInstanceGroupEbsConfig]
        | core.ArrayOut[CoreInstanceGroupEbsConfig]
        | None = None,
        instance_count: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CoreInstanceGroup.Args(
                id=id,
                instance_type=instance_type,
                autoscaling_policy=autoscaling_policy,
                bid_price=bid_price,
                ebs_config=ebs_config,
                instance_count=instance_count,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        autoscaling_policy: str | core.StringOut | None = core.arg(default=None)

        bid_price: str | core.StringOut | None = core.arg(default=None)

        ebs_config: list[CoreInstanceGroupEbsConfig] | core.ArrayOut[
            CoreInstanceGroupEbsConfig
        ] | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        instance_count: int | core.IntOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class BootstrapAction(core.Schema):

    args: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        path: str | core.StringOut,
        args: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=BootstrapAction.Args(
                name=name,
                path=path,
                args=args,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        args: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        path: str | core.StringOut = core.arg()


@core.schema
class KerberosAttributes(core.Schema):

    ad_domain_join_password: str | core.StringOut | None = core.attr(str, default=None)

    ad_domain_join_user: str | core.StringOut | None = core.attr(str, default=None)

    cross_realm_trust_principal_password: str | core.StringOut | None = core.attr(str, default=None)

    kdc_admin_password: str | core.StringOut = core.attr(str)

    realm: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        kdc_admin_password: str | core.StringOut,
        realm: str | core.StringOut,
        ad_domain_join_password: str | core.StringOut | None = None,
        ad_domain_join_user: str | core.StringOut | None = None,
        cross_realm_trust_principal_password: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=KerberosAttributes.Args(
                kdc_admin_password=kdc_admin_password,
                realm=realm,
                ad_domain_join_password=ad_domain_join_password,
                ad_domain_join_user=ad_domain_join_user,
                cross_realm_trust_principal_password=cross_realm_trust_principal_password,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ad_domain_join_password: str | core.StringOut | None = core.arg(default=None)

        ad_domain_join_user: str | core.StringOut | None = core.arg(default=None)

        cross_realm_trust_principal_password: str | core.StringOut | None = core.arg(default=None)

        kdc_admin_password: str | core.StringOut = core.arg()

        realm: str | core.StringOut = core.arg()


@core.schema
class CoreInstanceFleet(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_type_configs: list[InstanceTypeConfigs] | core.ArrayOut[
        InstanceTypeConfigs
    ] | None = core.attr(InstanceTypeConfigs, default=None, kind=core.Kind.array)

    launch_specifications: LaunchSpecifications | None = core.attr(
        LaunchSpecifications, default=None
    )

    name: str | core.StringOut | None = core.attr(str, default=None)

    provisioned_on_demand_capacity: int | core.IntOut = core.attr(int, computed=True)

    provisioned_spot_capacity: int | core.IntOut = core.attr(int, computed=True)

    target_on_demand_capacity: int | core.IntOut | None = core.attr(int, default=None)

    target_spot_capacity: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        provisioned_on_demand_capacity: int | core.IntOut,
        provisioned_spot_capacity: int | core.IntOut,
        instance_type_configs: list[InstanceTypeConfigs]
        | core.ArrayOut[InstanceTypeConfigs]
        | None = None,
        launch_specifications: LaunchSpecifications | None = None,
        name: str | core.StringOut | None = None,
        target_on_demand_capacity: int | core.IntOut | None = None,
        target_spot_capacity: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CoreInstanceFleet.Args(
                id=id,
                provisioned_on_demand_capacity=provisioned_on_demand_capacity,
                provisioned_spot_capacity=provisioned_spot_capacity,
                instance_type_configs=instance_type_configs,
                launch_specifications=launch_specifications,
                name=name,
                target_on_demand_capacity=target_on_demand_capacity,
                target_spot_capacity=target_spot_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        instance_type_configs: list[InstanceTypeConfigs] | core.ArrayOut[
            InstanceTypeConfigs
        ] | None = core.arg(default=None)

        launch_specifications: LaunchSpecifications | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        provisioned_on_demand_capacity: int | core.IntOut = core.arg()

        provisioned_spot_capacity: int | core.IntOut = core.arg()

        target_on_demand_capacity: int | core.IntOut | None = core.arg(default=None)

        target_spot_capacity: int | core.IntOut | None = core.arg(default=None)


@core.schema
class MasterInstanceGroup(core.Schema):

    bid_price: str | core.StringOut | None = core.attr(str, default=None)

    ebs_config: list[CoreInstanceGroupEbsConfig] | core.ArrayOut[
        CoreInstanceGroupEbsConfig
    ] | None = core.attr(
        CoreInstanceGroupEbsConfig, default=None, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_count: int | core.IntOut | None = core.attr(int, default=None)

    instance_type: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        instance_type: str | core.StringOut,
        bid_price: str | core.StringOut | None = None,
        ebs_config: list[CoreInstanceGroupEbsConfig]
        | core.ArrayOut[CoreInstanceGroupEbsConfig]
        | None = None,
        instance_count: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MasterInstanceGroup.Args(
                id=id,
                instance_type=instance_type,
                bid_price=bid_price,
                ebs_config=ebs_config,
                instance_count=instance_count,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bid_price: str | core.StringOut | None = core.arg(default=None)

        ebs_config: list[CoreInstanceGroupEbsConfig] | core.ArrayOut[
            CoreInstanceGroupEbsConfig
        ] | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        instance_count: int | core.IntOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_emr_cluster", namespace="emr")
class Cluster(core.Resource):
    """
    (Optional) JSON string for selecting additional features such as adding proxy information. Note: Cur
    rently there is no API to retrieve the value of this argument after EMR cluster creation from provid
    er, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outs
    ide Terraform.
    """

    additional_info: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A case-insensitive list of applications for Amazon EMR to install and configure when laun
    ching the cluster. For a list of applications available for each Amazon EMR release version, see the
    [Amazon EMR Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-componen
    ts.html).
    """
    applications: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An auto-termination policy for an Amazon EMR cluster. An auto-termination policy defines
    the amount of idle time in seconds after which a cluster automatically terminates. See [Auto Termina
    tion Policy](#auto_termination_policy) Below.
    """
    auto_termination_policy: AutoTerminationPolicy | None = core.attr(
        AutoTerminationPolicy, default=None
    )

    """
    (Optional) IAM role for automatic scaling policies. The IAM role provides permissions that the autom
    atic scaling feature requires to launch and terminate EC2 instances in an instance group.
    """
    autoscaling_role: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Ordered list of bootstrap actions that will be run before Hadoop is started on the cluste
    r nodes. See below.
    """
    bootstrap_action: list[BootstrapAction] | core.ArrayOut[BootstrapAction] | None = core.attr(
        BootstrapAction, default=None, kind=core.Kind.array
    )

    cluster_state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of configurations supplied for the EMR cluster you are creating. Supply a configurat
    ion object for applications to override their default configuration. See [AWS Documentation](https:/
    /docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html) for more information.
    """
    configurations: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) JSON string for supplying list of configurations for the EMR cluster.
    """
    configurations_json: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block to use an [Instance Fleet](https://docs.aws.amazon.com/emr/latest/Man
    agementGuide/emr-instance-fleet.html) for the core node type. Cannot be specified if any `core_insta
    nce_group` configuration blocks are set. Detailed below.
    """
    core_instance_fleet: CoreInstanceFleet | None = core.attr(
        CoreInstanceFleet, default=None, computed=True
    )

    """
    (Optional) Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/Man
    agementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [core node type
    ](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-co
    re).
    """
    core_instance_group: CoreInstanceGroup | None = core.attr(
        CoreInstanceGroup, default=None, computed=True
    )

    """
    (Optional) Custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazo
    n EMR version 5.7.0 and later.
    """
    custom_ami_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 inst
    ance. Available in Amazon EMR version 4.x and later.
    """
    ebs_root_volume_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Attributes for the EC2 instances running the job flow. See below.
    """
    ec2_attributes: Ec2Attributes | None = core.attr(Ec2Attributes, default=None)

    """
    ID of the cluster.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Switch on/off run cluster with no steps or when all steps are complete (default is on)
    """
    keep_job_flow_alive_when_no_steps: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Kerberos configuration for the cluster. See below.
    """
    kerberos_attributes: KerberosAttributes | None = core.attr(KerberosAttributes, default=None)

    """
    (Optional) List of [step states](https://docs.aws.amazon.com/emr/latest/APIReference/API_StepStatus.
    html) used to filter returned steps
    """
    list_steps_states: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) AWS KMS customer master key (CMK) key ID or arn used for encrypting log files. This attri
    bute is only available with EMR version 5.30.0 and later, excluding EMR 6.0.0.
    """
    log_encryption_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) S3 bucket to write the log files of the job flow. If a value is not provided, logs are no
    t created.
    """
    log_uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block to use an [Instance Fleet](https://docs.aws.amazon.com/emr/latest/Man
    agementGuide/emr-instance-fleet.html) for the master node type. Cannot be specified if any `master_i
    nstance_group` configuration blocks are set. Detailed below.
    """
    master_instance_fleet: MasterInstanceFleet | None = core.attr(
        MasterInstanceFleet, default=None, computed=True
    )

    """
    (Optional) Configuration block to use an [Instance Group](https://docs.aws.amazon.com/emr/latest/Man
    agementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for the [master node ty
    pe](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-
    master).
    """
    master_instance_group: MasterInstanceGroup | None = core.attr(
        MasterInstanceGroup, default=None, computed=True
    )

    """
    The DNS name of the master node. If the cluster is on a private subnet, this is the private DNS name
    . On a public subnet, this is the public DNS name.
    """
    master_public_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the job flow.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Release label for the Amazon EMR release.
    """
    release_label: str | core.StringOut = core.attr(str)

    """
    (Optional) Way that individual Amazon EC2 instances terminate when an automatic scale-in activity oc
    curs or an `instance group` is resized.
    """
    scale_down_behavior: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Security configuration name to attach to the EMR cluster. Only valid for EMR clusters wit
    h `release_label` 4.8.0 or greater.
    """
    security_configuration: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) IAM role that will be assumed by the Amazon EMR service to access AWS resources.
    """
    service_role: str | core.StringOut = core.attr(str)

    """
    (Optional) List of steps to run when creating the cluster. See below. It is highly recommended to ut
    ilize the [lifecycle configuration block](https://www.terraform.io/docs/configuration/meta-arguments
    /lifecycle.html) with `ignore_changes` if other steps are being managed outside of Terraform. This a
    rgument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-
    as-blocks.html).
    """
    step: list[Step] | core.ArrayOut[Step] | None = core.attr(
        Step, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Number of steps that can be executed concurrently. You can specify a maximum of 256 steps
    . Only valid for EMR clusters with `release_label` 5.28.0 or greater (default is 1).
    """
    step_concurrency_level: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) list of tags to apply to the EMR Cluster. If configured with a provider [`default_tags` c
    onfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-c
    onfiguration-block) present, tags with matching keys will overwrite those defined at the provider-le
    vel.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Switch on/off termination protection (default is `false`, except when using multiple mast
    er nodes). Before attempting to destroy the resource when termination protection is enabled, this co
    nfiguration must be applied with its value set to `false`.
    """
    termination_protection: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Whether the job flow is visible to all IAM users of the AWS account associated with the j
    ob flow. Default value is `true`.
    """
    visible_to_all_users: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        release_label: str | core.StringOut,
        service_role: str | core.StringOut,
        additional_info: str | core.StringOut | None = None,
        applications: list[str] | core.ArrayOut[core.StringOut] | None = None,
        auto_termination_policy: AutoTerminationPolicy | None = None,
        autoscaling_role: str | core.StringOut | None = None,
        bootstrap_action: list[BootstrapAction] | core.ArrayOut[BootstrapAction] | None = None,
        configurations: str | core.StringOut | None = None,
        configurations_json: str | core.StringOut | None = None,
        core_instance_fleet: CoreInstanceFleet | None = None,
        core_instance_group: CoreInstanceGroup | None = None,
        custom_ami_id: str | core.StringOut | None = None,
        ebs_root_volume_size: int | core.IntOut | None = None,
        ec2_attributes: Ec2Attributes | None = None,
        keep_job_flow_alive_when_no_steps: bool | core.BoolOut | None = None,
        kerberos_attributes: KerberosAttributes | None = None,
        list_steps_states: list[str] | core.ArrayOut[core.StringOut] | None = None,
        log_encryption_kms_key_id: str | core.StringOut | None = None,
        log_uri: str | core.StringOut | None = None,
        master_instance_fleet: MasterInstanceFleet | None = None,
        master_instance_group: MasterInstanceGroup | None = None,
        scale_down_behavior: str | core.StringOut | None = None,
        security_configuration: str | core.StringOut | None = None,
        step: list[Step] | core.ArrayOut[Step] | None = None,
        step_concurrency_level: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        termination_protection: bool | core.BoolOut | None = None,
        visible_to_all_users: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                name=name,
                release_label=release_label,
                service_role=service_role,
                additional_info=additional_info,
                applications=applications,
                auto_termination_policy=auto_termination_policy,
                autoscaling_role=autoscaling_role,
                bootstrap_action=bootstrap_action,
                configurations=configurations,
                configurations_json=configurations_json,
                core_instance_fleet=core_instance_fleet,
                core_instance_group=core_instance_group,
                custom_ami_id=custom_ami_id,
                ebs_root_volume_size=ebs_root_volume_size,
                ec2_attributes=ec2_attributes,
                keep_job_flow_alive_when_no_steps=keep_job_flow_alive_when_no_steps,
                kerberos_attributes=kerberos_attributes,
                list_steps_states=list_steps_states,
                log_encryption_kms_key_id=log_encryption_kms_key_id,
                log_uri=log_uri,
                master_instance_fleet=master_instance_fleet,
                master_instance_group=master_instance_group,
                scale_down_behavior=scale_down_behavior,
                security_configuration=security_configuration,
                step=step,
                step_concurrency_level=step_concurrency_level,
                tags=tags,
                tags_all=tags_all,
                termination_protection=termination_protection,
                visible_to_all_users=visible_to_all_users,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        additional_info: str | core.StringOut | None = core.arg(default=None)

        applications: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        auto_termination_policy: AutoTerminationPolicy | None = core.arg(default=None)

        autoscaling_role: str | core.StringOut | None = core.arg(default=None)

        bootstrap_action: list[BootstrapAction] | core.ArrayOut[BootstrapAction] | None = core.arg(
            default=None
        )

        configurations: str | core.StringOut | None = core.arg(default=None)

        configurations_json: str | core.StringOut | None = core.arg(default=None)

        core_instance_fleet: CoreInstanceFleet | None = core.arg(default=None)

        core_instance_group: CoreInstanceGroup | None = core.arg(default=None)

        custom_ami_id: str | core.StringOut | None = core.arg(default=None)

        ebs_root_volume_size: int | core.IntOut | None = core.arg(default=None)

        ec2_attributes: Ec2Attributes | None = core.arg(default=None)

        keep_job_flow_alive_when_no_steps: bool | core.BoolOut | None = core.arg(default=None)

        kerberos_attributes: KerberosAttributes | None = core.arg(default=None)

        list_steps_states: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        log_encryption_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        log_uri: str | core.StringOut | None = core.arg(default=None)

        master_instance_fleet: MasterInstanceFleet | None = core.arg(default=None)

        master_instance_group: MasterInstanceGroup | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        release_label: str | core.StringOut = core.arg()

        scale_down_behavior: str | core.StringOut | None = core.arg(default=None)

        security_configuration: str | core.StringOut | None = core.arg(default=None)

        service_role: str | core.StringOut = core.arg()

        step: list[Step] | core.ArrayOut[Step] | None = core.arg(default=None)

        step_concurrency_level: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        termination_protection: bool | core.BoolOut | None = core.arg(default=None)

        visible_to_all_users: bool | core.BoolOut | None = core.arg(default=None)
