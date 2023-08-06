import terrascript.core as core


@core.resource(type="aws_emr_studio", namespace="emr")
class Studio(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auth_mode: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon S3 location to back up Amazon EMR Studio Workspaces and notebook files.
    """
    default_s3_location: str | core.StringOut = core.attr(str)

    """
    (Optional) A detailed description of the Amazon EMR Studio.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the Amazon EMR Studio Engine security group. The Engine security group allows i
    nbound network traffic from the Workspace security group, and it must be in the same VPC specified b
    y `vpc_id`.
    """
    engine_security_group_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The authentication endpoint of your identity provider (IdP). Specify this value when you
    use IAM authentication and want to let federated users log in to a Studio with the Studio URL and cr
    edentials from your IdP. Amazon EMR Studio redirects users to this endpoint to enter credentials.
    """
    idp_auth_url: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name that your identity provider (IdP) uses for its RelayState parameter. For example
    , RelayState or TargetSource. Specify this value when you use IAM authentication and want to let fed
    erated users log in to a Studio using the Studio URL. The RelayState parameter differs by IdP.
    """
    idp_relay_state_parameter_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A descriptive name for the Amazon EMR Studio.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The IAM role that the Amazon EMR Studio assumes. The service role provides a way for Amaz
    on EMR Studio to interoperate with other Amazon Web Services services.
    """
    service_role: str | core.StringOut = core.attr(str)

    """
    (Required) A list of subnet IDs to associate with the Amazon EMR Studio. A Studio can have a maximum
    of 5 subnets. The subnets must belong to the VPC specified by `vpc_id`. Studio users can create a W
    orkspace in any of the specified subnets.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) list of tags to apply to the EMR Cluster. If configured with a provider [`default_tags` c
    onfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-c
    onfiguration-block) present, tags with matching keys will overwrite those defined at the provider-le
    vel.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The unique access URL of the Amazon EMR Studio.
    """
    url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) - The IAM user role that users and groups assume when logged in to an Amazon EMR Studio.
    Only specify a User Role when you use Amazon Web Services SSO authentication. The permissions attach
    ed to the User Role can be scoped down for each user or group using session policies.
    """
    user_role: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the Amazon EMR Studio Workspace security group. The Workspace security group al
    lows outbound network traffic to resources in the Engine security group, and it must be in the same
    VPC specified by `vpc_id`.
    """
    workspace_security_group_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        auth_mode: str | core.StringOut,
        default_s3_location: str | core.StringOut,
        engine_security_group_id: str | core.StringOut,
        name: str | core.StringOut,
        service_role: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
        workspace_security_group_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        idp_auth_url: str | core.StringOut | None = None,
        idp_relay_state_parameter_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_role: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Studio.Args(
                auth_mode=auth_mode,
                default_s3_location=default_s3_location,
                engine_security_group_id=engine_security_group_id,
                name=name,
                service_role=service_role,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
                workspace_security_group_id=workspace_security_group_id,
                description=description,
                idp_auth_url=idp_auth_url,
                idp_relay_state_parameter_name=idp_relay_state_parameter_name,
                tags=tags,
                tags_all=tags_all,
                user_role=user_role,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth_mode: str | core.StringOut = core.arg()

        default_s3_location: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        engine_security_group_id: str | core.StringOut = core.arg()

        idp_auth_url: str | core.StringOut | None = core.arg(default=None)

        idp_relay_state_parameter_name: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        service_role: str | core.StringOut = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_role: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()

        workspace_security_group_id: str | core.StringOut = core.arg()
