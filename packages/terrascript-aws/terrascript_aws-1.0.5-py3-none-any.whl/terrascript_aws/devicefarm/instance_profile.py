import terrascript.core as core


@core.resource(type="aws_devicefarm_instance_profile", namespace="devicefarm")
class InstanceProfile(core.Resource):
    """
    The Amazon Resource Name of this instance profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the instance profile.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) An array of strings that specifies the list of app packages that should not be cleaned up
    from the device after a test run.
    """
    exclude_app_packages_from_cleanup: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for the instance profile.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) When set to `true`, Device Farm removes app packages after a test run. The default value
    is `false` for private devices.
    """
    package_cleanup: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) When set to `true`, Device Farm reboots the instance after a test run. The default value
    is `true`.
    """
    reboot_after_use: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
