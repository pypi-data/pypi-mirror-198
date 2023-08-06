import terrascript.core as core


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
class MetadataOptions(core.Schema):

    http_endpoint: str | core.StringOut = core.attr(str, computed=True)

    http_put_response_hop_limit: int | core.IntOut = core.attr(int, computed=True)

    http_tokens: str | core.StringOut = core.attr(str, computed=True)

    instance_metadata_tags: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        http_endpoint: str | core.StringOut,
        http_put_response_hop_limit: int | core.IntOut,
        http_tokens: str | core.StringOut,
        instance_metadata_tags: str | core.StringOut,
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
        http_endpoint: str | core.StringOut = core.arg()

        http_put_response_hop_limit: int | core.IntOut = core.arg()

        http_tokens: str | core.StringOut = core.arg()

        instance_metadata_tags: str | core.StringOut = core.arg()


@core.schema
class PrivateDnsNameOptions(core.Schema):

    enable_resource_name_dns_a_record: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_resource_name_dns_aaaa_record: bool | core.BoolOut = core.attr(bool, computed=True)

    hostname_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enable_resource_name_dns_a_record: bool | core.BoolOut,
        enable_resource_name_dns_aaaa_record: bool | core.BoolOut,
        hostname_type: str | core.StringOut,
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
        enable_resource_name_dns_a_record: bool | core.BoolOut = core.arg()

        enable_resource_name_dns_aaaa_record: bool | core.BoolOut = core.arg()

        hostname_type: str | core.StringOut = core.arg()


@core.schema
class MaintenanceOptions(core.Schema):

    auto_recovery: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        auto_recovery: str | core.StringOut,
    ):
        super().__init__(
            args=MaintenanceOptions.Args(
                auto_recovery=auto_recovery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_recovery: str | core.StringOut = core.arg()


@core.schema
class EnclaveOptions(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=EnclaveOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class CreditSpecification(core.Schema):

    cpu_credits: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cpu_credits: str | core.StringOut,
    ):
        super().__init__(
            args=CreditSpecification.Args(
                cpu_credits=cpu_credits,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_credits: str | core.StringOut = core.arg()


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    device_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut,
        device_name: str | core.StringOut,
        encrypted: bool | core.BoolOut,
        iops: int | core.IntOut,
        kms_key_id: str | core.StringOut,
        throughput: int | core.IntOut,
        volume_id: str | core.StringOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                device_name=device_name,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                throughput=throughput,
                volume_id=volume_id,
                volume_size=volume_size,
                volume_type=volume_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut = core.arg()

        device_name: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut = core.arg()

        iops: int | core.IntOut = core.arg()

        kms_key_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput: int | core.IntOut = core.arg()

        volume_id: str | core.StringOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    device_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut,
        device_name: str | core.StringOut,
        encrypted: bool | core.BoolOut,
        iops: int | core.IntOut,
        kms_key_id: str | core.StringOut,
        snapshot_id: str | core.StringOut,
        throughput: int | core.IntOut,
        volume_id: str | core.StringOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                device_name=device_name,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
                throughput=throughput,
                volume_id=volume_id,
                volume_size=volume_size,
                volume_type=volume_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut = core.arg()

        device_name: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut = core.arg()

        iops: int | core.IntOut = core.arg()

        kms_key_id: str | core.StringOut = core.arg()

        snapshot_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput: int | core.IntOut = core.arg()

        volume_id: str | core.StringOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.data(type="aws_instance", namespace="ec2")
class DsInstance(core.Data):
    """
    The ID of the AMI used to launch the instance.
    """

    ami: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the instance.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether or not the Instance is associated with a public IP address or not (Boolean).
    """
    associate_public_ip_address: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The availability zone of the Instance.
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    The credit specification of the Instance.
    """
    credit_specification: list[CreditSpecification] | core.ArrayOut[
        CreditSpecification
    ] = core.attr(CreditSpecification, computed=True, kind=core.Kind.array)

    """
    Whether or not EC2 Instance Stop Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Sto
    p_Start.html#Using_StopProtection) is enabled (Boolean).
    """
    disable_api_stop: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether or not [EC2 Instance Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserG
    uide/terminating-instances.html#Using_ChangingDisableAPITermination) is enabled (Boolean).
    """
    disable_api_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The EBS block device mappings of the Instance.
    """
    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] = core.attr(
        EbsBlockDevice, computed=True, kind=core.Kind.array
    )

    """
    Whether the Instance is EBS optimized or not (Boolean).
    """
    ebs_optimized: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The enclave options of the instance.
    """
    enclave_options: list[EnclaveOptions] | core.ArrayOut[EnclaveOptions] = core.attr(
        EnclaveOptions, computed=True, kind=core.Kind.array
    )

    """
    The ephemeral block device mappings of the Instance.
    """
    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] = core.attr(EphemeralBlockDevice, computed=True, kind=core.Kind.array)

    """
    (Optional) One or more name/value pairs to use as filters. There are
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) If true, wait for password data to become available and retrieve it. Useful for getting t
    he administrator password for instances running Microsoft Windows. The password data is exported to
    the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIRe
    ference/API_GetPasswordData.html) for more information.
    """
    get_password_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Retrieve Base64 encoded User Data contents into the `user_data_base64` attribute. A SHA-1
    hash of the User Data contents will always be present in the `user_data` attribute. Defaults to `fa
    lse`.
    """
    get_user_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Id of the dedicated host the instance will be assigned to.
    """
    host_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the instance profile associated with the Instance.
    """
    iam_instance_profile: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specify the exact Instance ID with which to populate the data source.
    """
    instance_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The state of the instance. One of: `pending`, `running`, `shutting-down`, `terminated`, `stopping`,
    stopped`. See [Instance Lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance
    lifecycle.html) for more information.
    """
    instance_state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags, each pair of which must
    """
    instance_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The type of the Instance.
    """
    instance_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The IPv6 addresses associated to the Instance, if applicable. **NOTE**: Unlike the IPv4 address, thi
    s doesn't change if you attach an EIP to the instance.
    """
    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The key name of the Instance.
    """
    key_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The maintenance and recovery options for the instance.
    """
    maintenance_options: list[MaintenanceOptions] | core.ArrayOut[MaintenanceOptions] = core.attr(
        MaintenanceOptions, computed=True, kind=core.Kind.array
    )

    """
    The metadata options of the Instance.
    """
    metadata_options: list[MetadataOptions] | core.ArrayOut[MetadataOptions] = core.attr(
        MetadataOptions, computed=True, kind=core.Kind.array
    )

    """
    Whether detailed monitoring is enabled or disabled for the Instance (Boolean).
    """
    monitoring: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The ID of the network interface that was created with the Instance.
    """
    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the Outpost.
    """
    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Base-64 encoded encrypted password data for the instance.
    """
    password_data: str | core.StringOut = core.attr(str, computed=True)

    """
    The placement group of the Instance.
    """
    placement_group: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of the partition the instance is in.
    """
    placement_partition_number: int | core.IntOut = core.attr(int, computed=True)

    """
    The private DNS name assigned to the Instance. Can only be
    """
    private_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    The options for the instance hostname.
    """
    private_dns_name_options: list[PrivateDnsNameOptions] | core.ArrayOut[
        PrivateDnsNameOptions
    ] = core.attr(PrivateDnsNameOptions, computed=True, kind=core.Kind.array)

    """
    The private IP address assigned to the Instance.
    """
    private_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    The public DNS name assigned to the Instance. For EC2-VPC, this
    """
    public_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    The public IP address assigned to the Instance, if applicable. **NOTE**: If you are using an [`aws_e
    ip`](/docs/providers/aws/r/eip.html) with your instance, you should refer to the EIP's address direc
    tly and not use `public_ip`, as this field will change after the EIP is attached.
    """
    public_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    The root block device mappings of the Instance
    """
    root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] = core.attr(
        RootBlockDevice, computed=True, kind=core.Kind.array
    )

    """
    The secondary private IPv4 addresses assigned to the instance's primary network interface (eth0) in
    a VPC.
    """
    secondary_private_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The associated security groups.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Whether the network interface performs source/destination checking (Boolean).
    """
    source_dest_check: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The VPC subnet ID.
    """
    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the Instance.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The tenancy of the instance: `dedicated`, `default`, `host`.
    """
    tenancy: str | core.StringOut = core.attr(str, computed=True)

    """
    SHA-1 hash of User Data supplied to the Instance.
    """
    user_data: str | core.StringOut = core.attr(str, computed=True)

    """
    Base64 encoded contents of User Data supplied to the Instance. Valid UTF-8 contents can be decoded w
    ith the [`base64decode` function](https://www.terraform.io/docs/configuration/functions/base64decode
    .html). This attribute is only exported if `get_user_data` is true.
    """
    user_data_base64: str | core.StringOut = core.attr(str, computed=True)

    """
    The associated security groups in a non-default VPC.
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        get_password_data: bool | core.BoolOut | None = None,
        get_user_data: bool | core.BoolOut | None = None,
        instance_id: str | core.StringOut | None = None,
        instance_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInstance.Args(
                filter=filter,
                get_password_data=get_password_data,
                get_user_data=get_user_data,
                instance_id=instance_id,
                instance_tags=instance_tags,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        get_password_data: bool | core.BoolOut | None = core.arg(default=None)

        get_user_data: bool | core.BoolOut | None = core.arg(default=None)

        instance_id: str | core.StringOut | None = core.arg(default=None)

        instance_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
