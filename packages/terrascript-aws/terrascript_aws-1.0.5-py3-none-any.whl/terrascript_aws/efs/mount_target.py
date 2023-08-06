import terrascript.core as core


@core.resource(type="aws_efs_mount_target", namespace="efs")
class MountTarget(core.Resource):
    """
    The unique and consistent identifier of the Availability Zone (AZ) that the mount target resides in.
    """

    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the Availability Zone (AZ) that the mount target resides in.
    """
    availability_zone_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The DNS name for the EFS file system.
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name of the file system.
    """
    file_system_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the file system for which the mount target is intended.
    """
    file_system_id: str | core.StringOut = core.attr(str)

    """
    The ID of the mount target.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The address (within the address range of the specified subnet) at
    """
    ip_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/late
    st/ug/mounting-fs-mount-cmd-dns-name.html).
    """
    mount_target_dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the network interface that Amazon EFS created when it created the mount target.
    """
    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    AWS account ID that owns the resource.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of up to 5 VPC security group IDs (that must
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Required) The ID of the subnet to add the mount target in.
    """
    subnet_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        file_system_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
        ip_address: str | core.StringOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MountTarget.Args(
                file_system_id=file_system_id,
                subnet_id=subnet_id,
                ip_address=ip_address,
                security_groups=security_groups,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        file_system_id: str | core.StringOut = core.arg()

        ip_address: str | core.StringOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        subnet_id: str | core.StringOut = core.arg()
