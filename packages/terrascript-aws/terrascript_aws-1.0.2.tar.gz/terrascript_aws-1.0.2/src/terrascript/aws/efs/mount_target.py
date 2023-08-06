import terrascript.core as core


@core.resource(type="aws_efs_mount_target", namespace="aws_efs")
class MountTarget(core.Resource):

    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    availability_zone_name: str | core.StringOut = core.attr(str, computed=True)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    file_system_arn: str | core.StringOut = core.attr(str, computed=True)

    file_system_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    mount_target_dns_name: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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
