import terrascript.core as core


@core.resource(type="aws_ec2_host", namespace="ec2")
class Host(core.Resource):
    """
    The ARN of the Dedicated Host.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether the host accepts any untargeted instance launches that match its instan
    ce type configuration, or if it only accepts Host tenancy instance launches that specify its unique
    host ID. Valid values: `on`, `off`. Default: `on`.
    """
    auto_placement: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The Availability Zone in which to allocate the Dedicated Host.
    """
    availability_zone: str | core.StringOut = core.attr(str)

    """
    (Optional) Indicates whether to enable or disable host recovery for the Dedicated Host. Valid values
    : `on`, `off`. Default: `off`.
    """
    host_recovery: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the allocated Dedicated Host. This is used to launch an instance onto a specific host.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the instance family to be supported by the Dedicated Hosts. If you specify an i
    nstance family, the Dedicated Hosts support multiple instance types within that instance family. Exa
    ctly one of `instance_family` or `instance_type` must be specified.
    """
    instance_family: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the instance type to be supported by the Dedicated Hosts. If you specify an ins
    tance type, the Dedicated Hosts support instances of the specified instance type only. Exactly one o
    f `instance_family` or `instance_type` must be specified.
    """
    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The Amazon Resource Name (ARN) of the AWS Outpost on which to allocate the Dedicated Host
    .
    """
    outpost_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the AWS account that owns the Dedicated Host.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Map of tags to assign to this resource. If configured with a provider [`default_tags` con
    figuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-con
    figuration-block) present, tags with matching keys will overwrite those defined at the provider-leve
    l.
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
        availability_zone: str | core.StringOut,
        auto_placement: str | core.StringOut | None = None,
        host_recovery: str | core.StringOut | None = None,
        instance_family: str | core.StringOut | None = None,
        instance_type: str | core.StringOut | None = None,
        outpost_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Host.Args(
                availability_zone=availability_zone,
                auto_placement=auto_placement,
                host_recovery=host_recovery,
                instance_family=instance_family,
                instance_type=instance_type,
                outpost_arn=outpost_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_placement: str | core.StringOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut = core.arg()

        host_recovery: str | core.StringOut | None = core.arg(default=None)

        instance_family: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        outpost_arn: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
