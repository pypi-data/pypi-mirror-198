import terrascript.core as core


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


@core.resource(type="aws_spot_instance_request", namespace="ec2")
class SpotInstanceRequest(core.Resource):

    ami: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    associate_public_ip_address: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The required duration for the Spot instances, in minutes. This value must be a multiple o
    f 60 (60, 120, 180, 240, 300, or 360).
    """
    block_duration_minutes: int | core.IntOut | None = core.attr(int, default=None)

    capacity_reservation_specification: CapacityReservationSpecification | None = core.attr(
        CapacityReservationSpecification, default=None, computed=True
    )

    cpu_core_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    cpu_threads_per_core: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    credit_specification: CreditSpecification | None = core.attr(CreditSpecification, default=None)

    disable_api_stop: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    disable_api_termination: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.attr(
        EbsBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    ebs_optimized: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    enclave_options: EnclaveOptions | None = core.attr(EnclaveOptions, default=None, computed=True)

    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] | None = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    get_password_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    hibernation: bool | core.BoolOut | None = core.attr(bool, default=None)

    host_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    iam_instance_profile: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Spot Instance Request ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    instance_initiated_shutdown_behavior: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Indicates Spot instance behavior when it is interrupted. Valid values are `terminate`, `s
    top`, or `hibernate`. Default value is `terminate`.
    """
    instance_interruption_behavior: str | core.StringOut | None = core.attr(str, default=None)

    instance_state: str | core.StringOut = core.attr(str, computed=True)

    instance_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ipv6_address_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    key_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A launch group is a group of spot instances that launch together and terminate together.
    """
    launch_group: str | core.StringOut | None = core.attr(str, default=None)

    launch_template: LaunchTemplate | None = core.attr(LaunchTemplate, default=None)

    maintenance_options: MaintenanceOptions | None = core.attr(
        MaintenanceOptions, default=None, computed=True
    )

    metadata_options: MetadataOptions | None = core.attr(
        MetadataOptions, default=None, computed=True
    )

    monitoring: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface] | None = core.attr(
        NetworkInterface, default=None, computed=True, kind=core.Kind.array
    )

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    password_data: str | core.StringOut = core.attr(str, computed=True)

    placement_group: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    placement_partition_number: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    primary_network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The private DNS name assigned to the instance. Can only be
    """
    private_dns: str | core.StringOut = core.attr(str, computed=True)

    private_dns_name_options: PrivateDnsNameOptions | None = core.attr(
        PrivateDnsNameOptions, default=None, computed=True
    )

    """
    The private IP address assigned to the instance
    """
    private_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The public DNS name assigned to the instance. For EC2-VPC, this
    """
    public_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    The public IP address assigned to the instance, if applicable.
    """
    public_ip: str | core.StringOut = core.attr(str, computed=True)

    root_block_device: RootBlockDevice | None = core.attr(
        RootBlockDevice, default=None, computed=True
    )

    secondary_private_ips: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    source_dest_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The current [bid
    """
    spot_bid_status: str | core.StringOut = core.attr(str, computed=True)

    """
    The Instance ID (if any) that is currently fulfilling
    """
    spot_instance_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional; Default: On-demand price) The maximum price to request on the spot market.
    """
    spot_price: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    spot_request_state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional; Default: `persistent`) If set to `one-time`, after
    """
    spot_type: str | core.StringOut | None = core.attr(str, default=None)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the Spot Instance Request. These tags are not automatically ap
    plied to the launched Instance. If configured with a provider [`default_tags` configuration block](h
    ttps://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-block) p
    resent, tags with matching keys will overwrite those defined at the provider-level.
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

    tenancy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    user_data: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    user_data_base64: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    user_data_replace_on_change: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3
    339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the r
    equest immediately.
    """
    valid_from: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc333
    9#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance reques
    ts are placed or enabled to fulfill the request. The default end date is 7 days from the current dat
    e.
    """
    valid_until: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    volume_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional; Default: false) If set, Terraform will
    """
    wait_for_fulfillment: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        ami: str | core.StringOut | None = None,
        associate_public_ip_address: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        block_duration_minutes: int | core.IntOut | None = None,
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
        instance_interruption_behavior: str | core.StringOut | None = None,
        instance_type: str | core.StringOut | None = None,
        ipv6_address_count: int | core.IntOut | None = None,
        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        key_name: str | core.StringOut | None = None,
        launch_group: str | core.StringOut | None = None,
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
        spot_price: str | core.StringOut | None = None,
        spot_type: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tenancy: str | core.StringOut | None = None,
        user_data: str | core.StringOut | None = None,
        user_data_base64: str | core.StringOut | None = None,
        user_data_replace_on_change: bool | core.BoolOut | None = None,
        valid_from: str | core.StringOut | None = None,
        valid_until: str | core.StringOut | None = None,
        volume_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        wait_for_fulfillment: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SpotInstanceRequest.Args(
                ami=ami,
                associate_public_ip_address=associate_public_ip_address,
                availability_zone=availability_zone,
                block_duration_minutes=block_duration_minutes,
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
                instance_interruption_behavior=instance_interruption_behavior,
                instance_type=instance_type,
                ipv6_address_count=ipv6_address_count,
                ipv6_addresses=ipv6_addresses,
                key_name=key_name,
                launch_group=launch_group,
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
                spot_price=spot_price,
                spot_type=spot_type,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                tenancy=tenancy,
                user_data=user_data,
                user_data_base64=user_data_base64,
                user_data_replace_on_change=user_data_replace_on_change,
                valid_from=valid_from,
                valid_until=valid_until,
                volume_tags=volume_tags,
                vpc_security_group_ids=vpc_security_group_ids,
                wait_for_fulfillment=wait_for_fulfillment,
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

        block_duration_minutes: int | core.IntOut | None = core.arg(default=None)

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

        instance_interruption_behavior: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        ipv6_address_count: int | core.IntOut | None = core.arg(default=None)

        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        key_name: str | core.StringOut | None = core.arg(default=None)

        launch_group: str | core.StringOut | None = core.arg(default=None)

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

        spot_price: str | core.StringOut | None = core.arg(default=None)

        spot_type: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tenancy: str | core.StringOut | None = core.arg(default=None)

        user_data: str | core.StringOut | None = core.arg(default=None)

        user_data_base64: str | core.StringOut | None = core.arg(default=None)

        user_data_replace_on_change: bool | core.BoolOut | None = core.arg(default=None)

        valid_from: str | core.StringOut | None = core.arg(default=None)

        valid_until: str | core.StringOut | None = core.arg(default=None)

        volume_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        wait_for_fulfillment: bool | core.BoolOut | None = core.arg(default=None)
