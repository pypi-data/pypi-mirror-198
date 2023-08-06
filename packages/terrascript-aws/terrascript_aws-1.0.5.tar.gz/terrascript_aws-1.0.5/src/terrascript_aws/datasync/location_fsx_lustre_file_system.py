import terrascript.core as core


@core.resource(type="aws_datasync_location_fsx_lustre_file_system", namespace="datasync")
class LocationFsxLustreFileSystem(core.Resource):
    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The time that the FSx for Lustre location was created.
    """
    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) for the FSx for Lustre file system.
    """
    fsx_filesystem_arn: str | core.StringOut = core.attr(str)

    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Names (ARNs) of the security groups that are to use to configure the
    FSx for Lustre file system.
    """
    security_group_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) Subdirectory to perform actions as source or destination.
    """
    subdirectory: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Key-value pairs of resource tags to assign to the DataSync Location. If configured with a
    provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws
    /latest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those
    defined at the provider-level.
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
    The URL of the FSx for Lustre location that was described.
    """
    uri: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        fsx_filesystem_arn: str | core.StringOut,
        security_group_arns: list[str] | core.ArrayOut[core.StringOut],
        subdirectory: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationFsxLustreFileSystem.Args(
                fsx_filesystem_arn=fsx_filesystem_arn,
                security_group_arns=security_group_arns,
                subdirectory=subdirectory,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        fsx_filesystem_arn: str | core.StringOut = core.arg()

        security_group_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subdirectory: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
