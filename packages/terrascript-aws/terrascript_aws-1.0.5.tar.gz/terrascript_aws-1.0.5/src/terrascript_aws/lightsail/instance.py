import terrascript.core as core


@core.resource(type="aws_lightsail_instance", namespace="lightsail")
class Instance(core.Resource):
    """
    The ARN of the Lightsail instance (matches `id`).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Availability Zone in which to create your
    """
    availability_zone: str | core.StringOut = core.attr(str)

    """
    (Required) The ID for a virtual private server image. A list of available blueprint IDs can be obtai
    ned using the AWS CLI command: `aws lightsail get-blueprints`
    """
    blueprint_id: str | core.StringOut = core.attr(str)

    """
    (Required) The bundle of specification information (see list below)
    """
    bundle_id: str | core.StringOut = core.attr(str)

    """
    The number of vCPUs the instance has.
    """
    cpu_count: int | core.IntOut = core.attr(int, computed=True)

    """
    The timestamp when the instance was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the Lightsail instance (matches `arn`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (**Deprecated**) The first IPv6 address of the Lightsail instance. Use `ipv6_addresses` attribute in
    stead.
    """
    ipv6_address: str | core.StringOut = core.attr(str, computed=True)

    """
    List of IPv6 addresses for the Lightsail instance.
    """
    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    A Boolean value indicating whether this instance has a static IP assigned to it.
    """
    is_static_ip: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) The name of your key pair. Created in the
    """
    key_pair_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the Lightsail Instance. Names be unique within each AWS Region in your Lights
    ail account.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The private IP address of the instance.
    """
    private_ip_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The public IP address of the instance.
    """
    public_ip_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The amount of RAM in GB on the instance (e.g., 1.0).
    """
    ram_size: float | core.FloatOut = core.attr(float, computed=True)

    """
    (Optional) A map of tags to assign to the resource. To create a key-only tag, use an empty string as
    the value. If configured with a provider [`default_tags` configuration block](https://registry.terr
    aform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-block) present, tags with ma
    tching keys will overwrite those defined at the provider-level.
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
    (Optional) launch script to configure server with additional user data
    """
    user_data: str | core.StringOut | None = core.attr(str, default=None)

    """
    The user name for connecting to the instance (e.g., ec2-user).
    """
    username: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: str | core.StringOut,
        blueprint_id: str | core.StringOut,
        bundle_id: str | core.StringOut,
        name: str | core.StringOut,
        key_pair_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_data: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Instance.Args(
                availability_zone=availability_zone,
                blueprint_id=blueprint_id,
                bundle_id=bundle_id,
                name=name,
                key_pair_name=key_pair_name,
                tags=tags,
                tags_all=tags_all,
                user_data=user_data,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: str | core.StringOut = core.arg()

        blueprint_id: str | core.StringOut = core.arg()

        bundle_id: str | core.StringOut = core.arg()

        key_pair_name: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_data: str | core.StringOut | None = core.arg(default=None)
