import terrascript.core as core


@core.schema
class Ec2Config(core.Schema):

    security_group_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        security_group_arns: list[str] | core.ArrayOut[core.StringOut],
        subnet_arn: str | core.StringOut,
    ):
        super().__init__(
            args=Ec2Config.Args(
                security_group_arns=security_group_arns,
                subnet_arn=subnet_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_datasync_location_efs", namespace="datasync")
class LocationEfs(core.Resource):
    """
    (Optional) Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to access
    the Amazon EFS file system.
    """

    access_point_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block containing EC2 configurations for connecting to the EFS File System.
    """
    ec2_config: Ec2Config = core.attr(Ec2Config)

    """
    (Required) Amazon Resource Name (ARN) of EFS File System.
    """
    efs_file_system_arn: str | core.StringOut = core.attr(str)

    """
    (Optional)  Specifies an Identity and Access Management (IAM) role that DataSync assumes when mounti
    ng the Amazon EFS file system.
    """
    file_system_access_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether you want DataSync to use TLS encryption when transferring data to or fr
    om your Amazon EFS file system. Valid values are `NONE` and `TLS1_2`.
    """
    in_transit_encryption: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Subdirectory to perform actions as source or destination. Default `/`.
    """
    subdirectory: str | core.StringOut | None = core.attr(str, default=None)

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

    uri: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        ec2_config: Ec2Config,
        efs_file_system_arn: str | core.StringOut,
        access_point_arn: str | core.StringOut | None = None,
        file_system_access_role_arn: str | core.StringOut | None = None,
        in_transit_encryption: str | core.StringOut | None = None,
        subdirectory: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationEfs.Args(
                ec2_config=ec2_config,
                efs_file_system_arn=efs_file_system_arn,
                access_point_arn=access_point_arn,
                file_system_access_role_arn=file_system_access_role_arn,
                in_transit_encryption=in_transit_encryption,
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
        access_point_arn: str | core.StringOut | None = core.arg(default=None)

        ec2_config: Ec2Config = core.arg()

        efs_file_system_arn: str | core.StringOut = core.arg()

        file_system_access_role_arn: str | core.StringOut | None = core.arg(default=None)

        in_transit_encryption: str | core.StringOut | None = core.arg(default=None)

        subdirectory: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
