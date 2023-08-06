import terrascript.core as core


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class DomainJoinInfo(core.Schema):

    directory_name: str | core.StringOut | None = core.attr(str, default=None)

    organizational_unit_distinguished_name: str | core.StringOut | None = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        directory_name: str | core.StringOut | None = None,
        organizational_unit_distinguished_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DomainJoinInfo.Args(
                directory_name=directory_name,
                organizational_unit_distinguished_name=organizational_unit_distinguished_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_name: str | core.StringOut | None = core.arg(default=None)

        organizational_unit_distinguished_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AccessEndpoint(core.Schema):

    endpoint_type: str | core.StringOut = core.attr(str)

    vpce_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        endpoint_type: str | core.StringOut,
        vpce_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AccessEndpoint.Args(
                endpoint_type=endpoint_type,
                vpce_id=vpce_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_type: str | core.StringOut = core.arg()

        vpce_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_appstream_image_builder", namespace="appstream")
class ImageBuilder(core.Resource):
    """
    (Optional) Set of interface VPC endpoint (interface endpoint) objects. Maximum of 4. See below.
    """

    access_endpoint: list[AccessEndpoint] | core.ArrayOut[AccessEndpoint] | None = core.attr(
        AccessEndpoint, default=None, kind=core.Kind.array
    )

    """
    (Optional) The version of the AppStream 2.0 agent to use for this image builder.
    """
    appstream_agent_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    ARN of the appstream image builder.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time, in UTC and extended RFC 3339 format, when the image builder was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description to display.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Human-readable friendly name for the AppStream image builder.
    """
    display_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block for the name of the directory and organizational unit (OU) to use to
    join the image builder to a Microsoft Active Directory domain. See below.
    """
    domain_join_info: DomainJoinInfo | None = core.attr(DomainJoinInfo, default=None, computed=True)

    """
    (Optional) Enables or disables default internet access for the image builder.
    """
    enable_default_internet_access: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) ARN of the IAM role to apply to the image builder.
    """
    iam_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The name of the image builder.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Required if `image_name` not provided) ARN of the public, private, or shared image to use
    .
    """
    image_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Required if `image_arn` not provided) Name of the image used to create the image builder.
    """
    image_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The instance type to use when launching the image builder.
    """
    instance_type: str | core.StringOut = core.attr(str)

    """
    (Required) Unique name for the image builder.
    """
    name: str | core.StringOut = core.attr(str)

    """
    State of the image builder. Can be: `PENDING`, `UPDATING_AGENT`, `RUNNING`, `STOPPING`, `STOPPED`, `
    REBOOTING`, `SNAPSHOTTING`, `DELETING`, `FAILED`, `UPDATING`, `PENDING_QUALIFICATION`
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the instance. If configured with a provider [`default_tags` co
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

    """
    (Optional) Configuration block for the VPC configuration for the image builder. See below.
    """
    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_type: str | core.StringOut,
        name: str | core.StringOut,
        access_endpoint: list[AccessEndpoint] | core.ArrayOut[AccessEndpoint] | None = None,
        appstream_agent_version: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        display_name: str | core.StringOut | None = None,
        domain_join_info: DomainJoinInfo | None = None,
        enable_default_internet_access: bool | core.BoolOut | None = None,
        iam_role_arn: str | core.StringOut | None = None,
        image_arn: str | core.StringOut | None = None,
        image_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_config: VpcConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ImageBuilder.Args(
                instance_type=instance_type,
                name=name,
                access_endpoint=access_endpoint,
                appstream_agent_version=appstream_agent_version,
                description=description,
                display_name=display_name,
                domain_join_info=domain_join_info,
                enable_default_internet_access=enable_default_internet_access,
                iam_role_arn=iam_role_arn,
                image_arn=image_arn,
                image_name=image_name,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_endpoint: list[AccessEndpoint] | core.ArrayOut[AccessEndpoint] | None = core.arg(
            default=None
        )

        appstream_agent_version: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        display_name: str | core.StringOut | None = core.arg(default=None)

        domain_join_info: DomainJoinInfo | None = core.arg(default=None)

        enable_default_internet_access: bool | core.BoolOut | None = core.arg(default=None)

        iam_role_arn: str | core.StringOut | None = core.arg(default=None)

        image_arn: str | core.StringOut | None = core.arg(default=None)

        image_name: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)
