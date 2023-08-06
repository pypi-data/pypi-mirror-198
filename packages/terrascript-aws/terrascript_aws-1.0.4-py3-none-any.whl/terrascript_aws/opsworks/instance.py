import terrascript.core as core


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    device_name: str | core.StringOut = core.attr(str)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        delete_on_termination: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                device_name=device_name,
                delete_on_termination=delete_on_termination,
                iops=iops,
                snapshot_id=snapshot_id,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut | None = core.arg(default=None)

        device_name: str | core.StringOut = core.arg()

        iops: int | core.IntOut | None = core.arg(default=None)

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: str | core.StringOut = core.attr(str)

    virtual_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        virtual_name: str | core.StringOut,
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        virtual_name: str | core.StringOut = core.arg()


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                iops=iops,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_opsworks_instance", namespace="opsworks")
class Instance(core.Resource):
    """
    (Optional) OpsWorks agent to install. Default is `INHERIT`.
    """

    agent_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) AMI to use for the instance.  If an AMI is specified, `os` must be `Custom`.
    """
    ami_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Machine architecture for created instances.  Valid values are `x86_64` or `i386`. The def
    ault is `x86_64`.
    """
    architecture: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Creates load-based or time-based instances.  Valid values are `load`, `timer`.
    """
    auto_scaling_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the availability zone where instances will be created by default.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Time that the instance was created.
    """
    created_at: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Whether to delete EBS volume on deletion. Default is `true`.
    """
    delete_ebs: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether to delete the Elastic IP on deletion.
    """
    delete_eip: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Configuration block for additional EBS block devices to attach to the instance. See [Bloc
    k Devices](#block-devices) below.
    """
    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.attr(
        EbsBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Whether the launched EC2 instance will be EBS-optimized.
    """
    ebs_optimized: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    EC2 instance ID.
    """
    ec2_instance_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ECS cluster's ARN for container instances.
    """
    ecs_cluster_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Instance Elastic IP address.
    """
    elastic_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block for ephemeral (also known as "Instance Store") volumes on the instanc
    e. See [Block Devices](#block-devices) below.
    """
    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] | None = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    """
    (Optional) Instance's host name.
    """
    hostname: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    ID of the OpsWorks instance.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) For registered instances, infrastructure class: ec2 or on-premises.
    """
    infrastructure_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Controls where to install OS and package updates when the instance boots.  Default is `tr
    ue`.
    """
    install_updates_on_boot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) ARN of the instance's IAM profile.
    """
    instance_profile_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Type of instance to start.
    """
    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    ID of the last service error.
    """
    last_service_error_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) List of the layers the instance will belong to.
    """
    layer_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) Name of operating system that will be installed.
    """
    os: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Instance's platform.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    Private DNS name assigned to the instance. Can only be used inside the Amazon EC2, and only availabl
    e if you've enabled DNS hostnames for your VPC.
    """
    private_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    Private IP address assigned to the instance.
    """
    private_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    Public DNS name assigned to the instance. For EC2-VPC, this is only available if you've enabled DNS
    hostnames for your VPC.
    """
    public_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    Public IP address assigned to the instance, if applicable.
    """
    public_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    For registered instances, who performed the registration.
    """
    registered_by: str | core.StringOut = core.attr(str, computed=True)

    """
    Instance's reported AWS OpsWorks Stacks agent version.
    """
    reported_agent_version: str | core.StringOut = core.attr(str, computed=True)

    """
    For registered instances, the reported operating system family.
    """
    reported_os_family: str | core.StringOut = core.attr(str, computed=True)

    """
    For registered instances, the reported operating system name.
    """
    reported_os_name: str | core.StringOut = core.attr(str, computed=True)

    """
    For registered instances, the reported operating system version.
    """
    reported_os_version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for the root block device of the instance. See [Block Devices](#block
    devices) below.
    """
    root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] | None = core.attr(
        RootBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Name of the type of root device instances will have by default. Valid values are `ebs` or
    instance-store`.
    """
    root_device_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Root device volume ID.
    """
    root_device_volume_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Associated security groups.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    SSH key's Deep Security Agent (DSA) fingerprint.
    """
    ssh_host_dsa_key_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    """
    SSH key's RSA fingerprint.
    """
    ssh_host_rsa_key_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Name of the SSH keypair that instances will have by default.
    """
    ssh_key_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Identifier of the stack the instance will belong to.
    """
    stack_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Desired state of the instance. Valid values are `running` or `stopped`.
    """
    state: str | core.StringOut | None = core.attr(str, default=None)

    """
    Instance status. Will be one of `booting`, `connection_lost`, `online`, `pending`, `rebooting`, `req
    uested`, `running_setup`, `setup_failed`, `shutting_down`, `start_failed`, `stop_failed`, `stopped`,
    stopping`, `terminated`, or `terminating`.
    """
    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Subnet ID to attach to.
    """
    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Instance tenancy to use. Valid values are `default`, `dedicated` or `host`.
    """
    tenancy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Keyword to choose what virtualization mode created instances will use. Valid values are `
    paravirtual` or `hvm`.
    """
    virtualization_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        layer_ids: list[str] | core.ArrayOut[core.StringOut],
        stack_id: str | core.StringOut,
        agent_version: str | core.StringOut | None = None,
        ami_id: str | core.StringOut | None = None,
        architecture: str | core.StringOut | None = None,
        auto_scaling_type: str | core.StringOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        created_at: str | core.StringOut | None = None,
        delete_ebs: bool | core.BoolOut | None = None,
        delete_eip: bool | core.BoolOut | None = None,
        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = None,
        ebs_optimized: bool | core.BoolOut | None = None,
        ecs_cluster_arn: str | core.StringOut | None = None,
        elastic_ip: str | core.StringOut | None = None,
        ephemeral_block_device: list[EphemeralBlockDevice]
        | core.ArrayOut[EphemeralBlockDevice]
        | None = None,
        hostname: str | core.StringOut | None = None,
        infrastructure_class: str | core.StringOut | None = None,
        install_updates_on_boot: bool | core.BoolOut | None = None,
        instance_profile_arn: str | core.StringOut | None = None,
        instance_type: str | core.StringOut | None = None,
        os: str | core.StringOut | None = None,
        root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] | None = None,
        root_device_type: str | core.StringOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ssh_key_name: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tenancy: str | core.StringOut | None = None,
        virtualization_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Instance.Args(
                layer_ids=layer_ids,
                stack_id=stack_id,
                agent_version=agent_version,
                ami_id=ami_id,
                architecture=architecture,
                auto_scaling_type=auto_scaling_type,
                availability_zone=availability_zone,
                created_at=created_at,
                delete_ebs=delete_ebs,
                delete_eip=delete_eip,
                ebs_block_device=ebs_block_device,
                ebs_optimized=ebs_optimized,
                ecs_cluster_arn=ecs_cluster_arn,
                elastic_ip=elastic_ip,
                ephemeral_block_device=ephemeral_block_device,
                hostname=hostname,
                infrastructure_class=infrastructure_class,
                install_updates_on_boot=install_updates_on_boot,
                instance_profile_arn=instance_profile_arn,
                instance_type=instance_type,
                os=os,
                root_block_device=root_block_device,
                root_device_type=root_device_type,
                security_group_ids=security_group_ids,
                ssh_key_name=ssh_key_name,
                state=state,
                status=status,
                subnet_id=subnet_id,
                tenancy=tenancy,
                virtualization_type=virtualization_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        agent_version: str | core.StringOut | None = core.arg(default=None)

        ami_id: str | core.StringOut | None = core.arg(default=None)

        architecture: str | core.StringOut | None = core.arg(default=None)

        auto_scaling_type: str | core.StringOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        created_at: str | core.StringOut | None = core.arg(default=None)

        delete_ebs: bool | core.BoolOut | None = core.arg(default=None)

        delete_eip: bool | core.BoolOut | None = core.arg(default=None)

        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.arg(
            default=None
        )

        ebs_optimized: bool | core.BoolOut | None = core.arg(default=None)

        ecs_cluster_arn: str | core.StringOut | None = core.arg(default=None)

        elastic_ip: str | core.StringOut | None = core.arg(default=None)

        ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
            EphemeralBlockDevice
        ] | None = core.arg(default=None)

        hostname: str | core.StringOut | None = core.arg(default=None)

        infrastructure_class: str | core.StringOut | None = core.arg(default=None)

        install_updates_on_boot: bool | core.BoolOut | None = core.arg(default=None)

        instance_profile_arn: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        layer_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        os: str | core.StringOut | None = core.arg(default=None)

        root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] | None = core.arg(
            default=None
        )

        root_device_type: str | core.StringOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        ssh_key_name: str | core.StringOut | None = core.arg(default=None)

        stack_id: str | core.StringOut = core.arg()

        state: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tenancy: str | core.StringOut | None = core.arg(default=None)

        virtualization_type: str | core.StringOut | None = core.arg(default=None)
