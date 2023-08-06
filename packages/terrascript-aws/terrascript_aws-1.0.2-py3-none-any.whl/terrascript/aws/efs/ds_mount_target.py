import terrascript.core as core


@core.data(type="aws_efs_mount_target", namespace="aws_efs")
class DsMountTarget(core.Data):

    access_point_id: str | core.StringOut | None = core.attr(str, default=None)

    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    availability_zone_name: str | core.StringOut = core.attr(str, computed=True)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    file_system_arn: str | core.StringOut = core.attr(str, computed=True)

    file_system_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address: str | core.StringOut = core.attr(str, computed=True)

    mount_target_dns_name: str | core.StringOut = core.attr(str, computed=True)

    mount_target_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

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
