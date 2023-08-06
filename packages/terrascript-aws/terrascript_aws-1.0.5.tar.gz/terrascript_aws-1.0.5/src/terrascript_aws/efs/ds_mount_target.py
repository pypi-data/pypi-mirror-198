import terrascript.core as core


@core.data(type="aws_efs_mount_target", namespace="efs")
class DsMountTarget(core.Data):
    """
    (Optional) ID or ARN of the access point whose mount target that you want to find. It must be includ
    ed if a `file_system_id` and `mount_target_id` are not included.
    """

    access_point_id: str | core.StringOut | None = core.attr(str, default=None)

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
    Amazon Resource Name of the file system for which the mount target is intended.
    """
    file_system_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ID or ARN of the file system whose mount target that you want to find. It must be include
    d if an `access_point_id` and `mount_target_id` are not included.
    """
    file_system_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Address at which the file system may be mounted via the mount target.
    """
    ip_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/late
    st/ug/mounting-fs-mount-cmd-dns-name.html).
    """
    mount_target_dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ID or ARN of the mount target that you want to find. It must be included in your request
    if an `access_point_id` and `file_system_id` are not included.
    """
    mount_target_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the network interface that Amazon EFS created when it created the mount target.
    """
    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    AWS account ID that owns the resource.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of VPC security group IDs attached to the mount target.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    ID of the mount target's subnet.
    """
    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        access_point_id: str | core.StringOut | None = None,
        file_system_id: str | core.StringOut | None = None,
        mount_target_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMountTarget.Args(
                access_point_id=access_point_id,
                file_system_id=file_system_id,
                mount_target_id=mount_target_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_point_id: str | core.StringOut | None = core.arg(default=None)

        file_system_id: str | core.StringOut | None = core.arg(default=None)

        mount_target_id: str | core.StringOut | None = core.arg(default=None)
