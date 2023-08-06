import terrascript.core as core


@core.resource(type="aws_devicefarm_instance_profile", namespace="aws_devicefarm")
class InstanceProfile(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    exclude_app_packages_from_cleanup: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    package_cleanup: bool | core.BoolOut | None = core.attr(bool, default=None)

    reboot_after_use: bool | core.BoolOut | None = core.attr(bool, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        exclude_app_packages_from_cleanup: list[str] | core.ArrayOut[core.StringOut] | None = None,
        package_cleanup: bool | core.BoolOut | None = None,
        reboot_after_use: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceProfile.Args(
                name=name,
                description=description,
                exclude_app_packages_from_cleanup=exclude_app_packages_from_cleanup,
                package_cleanup=package_cleanup,
                reboot_after_use=reboot_after_use,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        exclude_app_packages_from_cleanup: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        package_cleanup: bool | core.BoolOut | None = core.arg(default=None)

        reboot_after_use: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
