import terrascript.core as core


@core.schema
class EnclaveOptions(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=EnclaveOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    device_name: str | core.StringOut = core.attr(str)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        volume_id: str | core.StringOut,
        delete_on_termination: bool | core.BoolOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        throughput: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                device_name=device_name,
                volume_id=volume_id,
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
                tags=tags,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut | None = core.arg(default=None)

        device_name: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_id: str | core.StringOut = core.arg()

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NetworkInterface(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    device_index: int | core.IntOut = core.attr(int)

    network_card_index: int | core.IntOut | None = core.attr(int, default=None)

    network_interface_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        device_index: int | core.IntOut,
        network_interface_id: str | core.StringOut,
        delete_on_termination: bool | core.BoolOut | None = None,
        network_card_index: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=NetworkInterface.Args(
                device_index=device_index,
                network_interface_id=network_interface_id,
                delete_on_termination=delete_on_termination,
                network_card_index=network_card_index,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut | None = core.arg(default=None)

        device_index: int | core.IntOut = core.arg()

        network_card_index: int | core.IntOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut = core.arg()


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: str | core.StringOut = core.attr(str)

    no_device: bool | core.BoolOut | None = core.attr(bool, default=None)

    virtual_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        no_device: bool | core.BoolOut | None = None,
        virtual_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        no_device: bool | core.BoolOut | None = core.arg(default=None)

        virtual_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    device_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        volume_id: str | core.StringOut,
        delete_on_termination: bool | core.BoolOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        throughput: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                device_name=device_name,
                volume_id=volume_id,
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                tags=tags,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut | None = core.arg(default=None)

        device_name: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_id: str | core.StringOut = core.arg()

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class PrivateDnsNameOptions(core.Schema):

    enable_resource_name_dns_a_record: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    enable_resource_name_dns_aaaa_record: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    hostname_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        enable_resource_name_dns_a_record: bool | core.BoolOut | None = None,
        enable_resource_name_dns_aaaa_record: bool | core.BoolOut | None = None,
        hostname_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PrivateDnsNameOptions.Args(
                enable_resource_name_dns_a_record=enable_resource_name_dns_a_record,
                enable_resource_name_dns_aaaa_record=enable_resource_name_dns_aaaa_record,
                hostname_type=hostname_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_resource_name_dns_a_record: bool | core.BoolOut | None = core.arg(default=None)

        enable_resource_name_dns_aaaa_record: bool | core.BoolOut | None = core.arg(default=None)

        hostname_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MaintenanceOptions(core.Schema):

    auto_recovery: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        auto_recovery: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MaintenanceOptions.Args(
                auto_recovery=auto_recovery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_recovery: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    http_put_response_hop_limit: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    http_tokens: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    instance_metadata_tags: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_endpoint: str | core.StringOut | None = None,
        http_put_response_hop_limit: int | core.IntOut | None = None,
        http_tokens: str | core.StringOut | None = None,
        instance_metadata_tags: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MetadataOptions.Args(
                http_endpoint=http_endpoint,
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
                instance_metadata_tags=instance_metadata_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint: str | core.StringOut | None = core.arg(default=None)

        http_put_response_hop_limit: int | core.IntOut | None = core.arg(default=None)

        http_tokens: str | core.StringOut | None = core.arg(default=None)

        instance_metadata_tags: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LaunchTemplate(core.Schema):

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                id=id,
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CapacityReservationTarget(core.Schema):

    capacity_reservation_id: str | core.StringOut | None = core.attr(str, default=None)

    capacity_reservation_resource_group_arn: str | core.StringOut | None = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        capacity_reservation_id: str | core.StringOut | None = None,
        capacity_reservation_resource_group_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CapacityReservationTarget.Args(
                capacity_reservation_id=capacity_reservation_id,
                capacity_reservation_resource_group_arn=capacity_reservation_resource_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_reservation_id: str | core.StringOut | None = core.arg(default=None)

        capacity_reservation_resource_group_arn: str | core.StringOut | None = core.arg(
            default=None
        )


@core.schema
class CapacityReservationSpecification(core.Schema):

    capacity_reservation_preference: str | core.StringOut | None = core.attr(str, default=None)

    capacity_reservation_target: CapacityReservationTarget | None = core.attr(
        CapacityReservationTarget, default=None
    )

    def __init__(
        self,
        *,
        capacity_reservation_preference: str | core.StringOut | None = None,
        capacity_reservation_target: CapacityReservationTarget | None = None,
    ):
        super().__init__(
            args=CapacityReservationSpecification.Args(
                capacity_reservation_preference=capacity_reservation_preference,
                capacity_reservation_target=capacity_reservation_target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_reservation_preference: str | core.StringOut | None = core.arg(default=None)

        capacity_reservation_target: CapacityReservationTarget | None = core.arg(default=None)


@core.schema
class CreditSpecification(core.Schema):

    cpu_credits: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cpu_credits: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CreditSpecification.Args(
                cpu_credits=cpu_credits,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_credits: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_instance", namespace="ec2")
class Instance(core.Resource):
    """
    (Optional) AMI to use for the instance. Required unless `launch_template` is specified and the Launc
    h Template specifes an AMI. If an AMI is specified in the Launch Template, setting `ami` will overri
    de the AMI specified in the Launch Template.
    """

    ami: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ARN of the instance.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to associate a public IP address with an instance in a VPC.
    """
    associate_public_ip_address: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) AZ to start the instance in.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Describes an instance's Capacity Reservation targeting option. See [Capacity Reservation
    Specification](#capacity-reservation-specification) below for more details.
    """
    capacity_reservation_specification: CapacityReservationSpecification | None = core.attr(
        CapacityReservationSpecification, default=None, computed=True
    )

    """
    (Optional) Sets the number of CPU cores for an instance. This option is only supported on creation o
    f instance type that support CPU Options [CPU Cores and Threads Per CPU Core Per Instance Type](http
    s://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-ins
    tances-values) - specifying this option for unsupported instance types will return an error from the
    EC2 API.
    """
    cpu_core_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional - has no effect unless `cpu_core_count` is also set)  If set to to 1, hyperthreading is di
    sabled on the launched instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs
    .aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.
    """
    cpu_threads_per_core: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Configuration block for customizing the credit specification of the instance. See [Credit
    Specification](#credit-specification) below for more details. Terraform will only perform drift det
    ection of its value when present in a configuration. Removing this configuration on existing instanc
    es will only stop managing it. It will not change the configuration back to the default for the inst
    ance type.
    """
    credit_specification: CreditSpecification | None = core.attr(CreditSpecification, default=None)

    """
    (Optional) If true, enables [EC2 Instance Stop Protection](https://docs.aws.amazon.com/AWSEC2/latest
    /UserGuide/Stop_Start.html#Using_StopProtection).
    """
    disable_api_stop: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) If true, enables [EC2 Instance Termination Protection](https://docs.aws.amazon.com/AWSEC2
    /latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination).
    """
    disable_api_termination: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) One or more configuration blocks with additional EBS block devices to attach to the insta
    nce. Block device configurations only apply on resource creation. See [Block Devices](#ebs-ephemeral
    and-root-block-devices) below for details on attributes and drift detection. When accessing this as
    an attribute reference, it is a set of objects.
    """
    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.attr(
        EbsBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) If true, the launched EC2 instance will be EBS-optimized. Note that if this is not set on
    an instance type that is optimized by default then this will show as disabled but if the instance t
    ype is optimized by default then there is no need to set this and there is no effect to disabling it
    . See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.h
    tml) of the AWS User Guide for more information.
    """
    ebs_optimized: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Enable Nitro Enclaves on launched instances. See [Enclave Options](#enclave-options) belo
    w for more details.
    """
    enclave_options: EnclaveOptions | None = core.attr(EnclaveOptions, default=None, computed=True)

    """
    (Optional) One or more configuration blocks to customize Ephemeral (also known as "Instance Store")
    volumes on the instance. See [Block Devices](#ebs-ephemeral-and-root-block-devices) below for detail
    s. When accessing this as an attribute reference, it is a set of objects.
    """
    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] | None = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    """
    (Optional) If true, wait for password data to become available and retrieve it. Useful for getting t
    he administrator password for instances running Microsoft Windows. The password data is exported to
    the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIRe
    ference/API_GetPasswordData.html) for more information.
    """
    get_password_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) If true, the launched EC2 instance will support hibernation.
    """
    hibernation: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) ID of a dedicated host that the instance will be assigned to. Use when an instance is to
    be launched on a specific dedicated host.
    """
    host_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) IAM Instance Profile to launch the instance with. Specified as the name of the Instance P
    rofile. Ensure your credentials have the correct permission to assign the instance profile according
    to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role
    ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.
    """
    iam_instance_profile: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the launch template. Conflicts with `name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Shutdown behavior for the instance. Amazon defaults this to `stop` for EBS-backed instanc
    es and `terminate` for instance-store instances. Cannot be set on instance-store instances. See [Shu
    tdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using
    _ChangingInstanceInitiatedShutdownBehavior) for more information.
    """
    instance_initiated_shutdown_behavior: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The state of the instance. One of: `pending`, `running`, `shutting-down`, `terminated`, `stopping`,
    stopped`. See [Instance Lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance
    lifecycle.html) for more information.
    """
    instance_state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The instance type to use for the instance. Updates to this field will trigger a stop/star
    t of the EC2 instance.
    """
    instance_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ipv6_address_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Specify one or more IPv6 addresses from the range of the subnet to associate with the pri
    mary network interface
    """
    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Key name of the Key Pair to use for the instance; which can be managed using [the `aws_ke
    y_pair` resource](key_pair.html).
    """
    key_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies a Launch Template to configure the instance. Parameters configured on this reso
    urce will override the corresponding parameters in the Launch Template.
    """
    launch_template: LaunchTemplate | None = core.attr(LaunchTemplate, default=None)

    """
    (Optional) The maintenance and recovery options for the instance. See [Maintenance Options](#mainten
    ance-options) below for more details.
    """
    maintenance_options: MaintenanceOptions | None = core.attr(
        MaintenanceOptions, default=None, computed=True
    )

    """
    (Optional) Customize the metadata options of the instance. See [Metadata Options](#metadata-options)
    below for more details.
    """
    metadata_options: MetadataOptions | None = core.attr(
        MetadataOptions, default=None, computed=True
    )

    """
    (Optional) If true, the launched EC2 instance will have detailed monitoring enabled. (Available sinc
    e v0.6.0)
    """
    monitoring: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Customize network interfaces to be attached at instance boot time. See [Network Interface
    s](#network-interfaces) below for more details.
    """
    network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface] | None = core.attr(
        NetworkInterface, default=None, computed=True, kind=core.Kind.array
    )

    """
    The ARN of the Outpost the instance is assigned to.
    """
    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Base-64 encoded encrypted password data for the instance. Useful for getting the administrator passw
    ord for instances running Microsoft Windows. This attribute is only exported if `get_password_data`
    is true. Note that this encrypted value will be stored in the state file, as with all exported attri
    butes. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordD
    ata.html) for more information.
    """
    password_data: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Placement Group to start the instance in.
    """
    placement_group: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The number of the partition the instance is in. Valid only if [the `aws_placement_group`
    resource's](placement_group.html) `strategy` argument is set to `"partition"`.
    """
    placement_partition_number: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    The ID of the instance's primary network interface.
    """
    primary_network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The private DNS name assigned to the instance. Can only be used inside the Amazon EC2, and only avai
    lable if you've enabled DNS hostnames for your VPC.
    """
    private_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The options for the instance hostname. The default values are inherited from the subnet.
    See [Private DNS Name Options](#private-dns-name-options) below for more details.
    """
    private_dns_name_options: PrivateDnsNameOptions | None = core.attr(
        PrivateDnsNameOptions, default=None, computed=True
    )

    """
    (Optional) Private IP address to associate with the instance in a VPC.
    """
    private_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The public DNS name assigned to the instance. For EC2-VPC, this is only available if you've enabled
    DNS hostnames for your VPC.
    """
    public_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    The public IP address assigned to the instance, if applicable. **NOTE**: If you are using an [`aws_e
    ip`](/docs/providers/aws/r/eip.html) with your instance, you should refer to the EIP's address direc
    tly and not use `public_ip` as this field will change after the EIP is attached.
    """
    public_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block to customize details about the root block device of the instance. See
    [Block Devices](#ebs-ephemeral-and-root-block-devices) below for details. When accessing this as an
    attribute reference, it is a list containing one object.
    """
    root_block_device: RootBlockDevice | None = core.attr(
        RootBlockDevice, default=None, computed=True
    )

    """
    (Optional) A list of secondary private IPv4 addresses to assign to the instance's primary network in
    terface (eth0) in a VPC. Can only be assigned to the primary network interface (eth0) attached at in
    stance creation, not a pre-existing network interface i.e., referenced in a `network_interface` bloc
    k. Refer to the [Elastic network interfaces documentation](https://docs.aws.amazon.com/AWSEC2/latest
    /UserGuide/using-eni.html#AvailableIpPerENI) to see the maximum number of private IP addresses allow
    ed per instance type.
    """
    secondary_private_ips: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional, EC2-Classic and default VPC only) A list of security group names to associate with.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Controls if traffic is routed to the instance when the destination address does not match
    the instance. Used for NAT or VPNs. Defaults true.
    """
    source_dest_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) VPC Subnet ID to launch in.
    """
    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the resource. Note that these tags apply to the instance and n
    ot block storage devices. If configured with a provider [`default_tags` configuration block](https:/
    /registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-block) present
    , tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) Tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy
    of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-insta
    nce command.
    """
    tenancy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) User data to provide when launching the instance. Do not pass gzip-compressed data via th
    is argument; see `user_data_base64` instead. Updates to this field will trigger a stop/start of the
    EC2 instance by default. If the `user_data_replace_on_change` is set then updates to this field will
    trigger a destroy and recreate.
    """
    user_data: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this
    instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded use
    r data must be base64-encoded and passed via this argument to avoid corruption. Updates to this fiel
    d will trigger a stop/start of the EC2 instance by default. If the `user_data_replace_on_change` is
    set then updates to this field will trigger a destroy and recreate.
    """
    user_data_base64: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) When used in combination with `user_data` or `user_data_base64` will trigger a destroy an
    d recreate when set to `true`. Defaults to `false` if not set.
    """
    user_data_replace_on_change: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A map of tags to assign, at instance-creation time, to root and EBS volumes.
    """
    volume_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional, VPC only) A list of security group IDs to associate with.
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        ami: str | core.StringOut | None = None,
        associate_public_ip_address: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        capacity_reservation_specification: CapacityReservationSpecification | None = None,
        cpu_core_count: int | core.IntOut | None = None,
        cpu_threads_per_core: int | core.IntOut | None = None,
        credit_specification: CreditSpecification | None = None,
        disable_api_stop: bool | core.BoolOut | None = None,
        disable_api_termination: bool | core.BoolOut | None = None,
        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = None,
        ebs_optimized: bool | core.BoolOut | None = None,
        enclave_options: EnclaveOptions | None = None,
        ephemeral_block_device: list[EphemeralBlockDevice]
        | core.ArrayOut[EphemeralBlockDevice]
        | None = None,
        get_password_data: bool | core.BoolOut | None = None,
        hibernation: bool | core.BoolOut | None = None,
        host_id: str | core.StringOut | None = None,
        iam_instance_profile: str | core.StringOut | None = None,
        instance_initiated_shutdown_behavior: str | core.StringOut | None = None,
        instance_type: str | core.StringOut | None = None,
        ipv6_address_count: int | core.IntOut | None = None,
        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        key_name: str | core.StringOut | None = None,
        launch_template: LaunchTemplate | None = None,
        maintenance_options: MaintenanceOptions | None = None,
        metadata_options: MetadataOptions | None = None,
        monitoring: bool | core.BoolOut | None = None,
        network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface] | None = None,
        placement_group: str | core.StringOut | None = None,
        placement_partition_number: int | core.IntOut | None = None,
        private_dns_name_options: PrivateDnsNameOptions | None = None,
        private_ip: str | core.StringOut | None = None,
        root_block_device: RootBlockDevice | None = None,
        secondary_private_ips: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        source_dest_check: bool | core.BoolOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tenancy: str | core.StringOut | None = None,
        user_data: str | core.StringOut | None = None,
        user_data_base64: str | core.StringOut | None = None,
        user_data_replace_on_change: bool | core.BoolOut | None = None,
        volume_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Instance.Args(
                ami=ami,
                associate_public_ip_address=associate_public_ip_address,
                availability_zone=availability_zone,
                capacity_reservation_specification=capacity_reservation_specification,
                cpu_core_count=cpu_core_count,
                cpu_threads_per_core=cpu_threads_per_core,
                credit_specification=credit_specification,
                disable_api_stop=disable_api_stop,
                disable_api_termination=disable_api_termination,
                ebs_block_device=ebs_block_device,
                ebs_optimized=ebs_optimized,
                enclave_options=enclave_options,
                ephemeral_block_device=ephemeral_block_device,
                get_password_data=get_password_data,
                hibernation=hibernation,
                host_id=host_id,
                iam_instance_profile=iam_instance_profile,
                instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior,
                instance_type=instance_type,
                ipv6_address_count=ipv6_address_count,
                ipv6_addresses=ipv6_addresses,
                key_name=key_name,
                launch_template=launch_template,
                maintenance_options=maintenance_options,
                metadata_options=metadata_options,
                monitoring=monitoring,
                network_interface=network_interface,
                placement_group=placement_group,
                placement_partition_number=placement_partition_number,
                private_dns_name_options=private_dns_name_options,
                private_ip=private_ip,
                root_block_device=root_block_device,
                secondary_private_ips=secondary_private_ips,
                security_groups=security_groups,
                source_dest_check=source_dest_check,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                tenancy=tenancy,
                user_data=user_data,
                user_data_base64=user_data_base64,
                user_data_replace_on_change=user_data_replace_on_change,
                volume_tags=volume_tags,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ami: str | core.StringOut | None = core.arg(default=None)

        associate_public_ip_address: bool | core.BoolOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        capacity_reservation_specification: CapacityReservationSpecification | None = core.arg(
            default=None
        )

        cpu_core_count: int | core.IntOut | None = core.arg(default=None)

        cpu_threads_per_core: int | core.IntOut | None = core.arg(default=None)

        credit_specification: CreditSpecification | None = core.arg(default=None)

        disable_api_stop: bool | core.BoolOut | None = core.arg(default=None)

        disable_api_termination: bool | core.BoolOut | None = core.arg(default=None)

        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.arg(
            default=None
        )

        ebs_optimized: bool | core.BoolOut | None = core.arg(default=None)

        enclave_options: EnclaveOptions | None = core.arg(default=None)

        ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
            EphemeralBlockDevice
        ] | None = core.arg(default=None)

        get_password_data: bool | core.BoolOut | None = core.arg(default=None)

        hibernation: bool | core.BoolOut | None = core.arg(default=None)

        host_id: str | core.StringOut | None = core.arg(default=None)

        iam_instance_profile: str | core.StringOut | None = core.arg(default=None)

        instance_initiated_shutdown_behavior: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        ipv6_address_count: int | core.IntOut | None = core.arg(default=None)

        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        key_name: str | core.StringOut | None = core.arg(default=None)

        launch_template: LaunchTemplate | None = core.arg(default=None)

        maintenance_options: MaintenanceOptions | None = core.arg(default=None)

        metadata_options: MetadataOptions | None = core.arg(default=None)

        monitoring: bool | core.BoolOut | None = core.arg(default=None)

        network_interface: list[NetworkInterface] | core.ArrayOut[
            NetworkInterface
        ] | None = core.arg(default=None)

        placement_group: str | core.StringOut | None = core.arg(default=None)

        placement_partition_number: int | core.IntOut | None = core.arg(default=None)

        private_dns_name_options: PrivateDnsNameOptions | None = core.arg(default=None)

        private_ip: str | core.StringOut | None = core.arg(default=None)

        root_block_device: RootBlockDevice | None = core.arg(default=None)

        secondary_private_ips: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        source_dest_check: bool | core.BoolOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tenancy: str | core.StringOut | None = core.arg(default=None)

        user_data: str | core.StringOut | None = core.arg(default=None)

        user_data_base64: str | core.StringOut | None = core.arg(default=None)

        user_data_replace_on_change: bool | core.BoolOut | None = core.arg(default=None)

        volume_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
