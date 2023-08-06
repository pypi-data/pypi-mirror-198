import terrascript.core as core


@core.schema
class Certificate(core.Schema):

    certificate_name: str | core.StringOut = core.attr(str)

    domain_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        certificate_name: str | core.StringOut,
        domain_names: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Certificate.Args(
                certificate_name=certificate_name,
                domain_names=domain_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_name: str | core.StringOut = core.arg()

        domain_names: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class PublicDomainNames(core.Schema):

    certificate: list[Certificate] | core.ArrayOut[Certificate] = core.attr(
        Certificate, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        certificate: list[Certificate] | core.ArrayOut[Certificate],
    ):
        super().__init__(
            args=PublicDomainNames.Args(
                certificate=certificate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: list[Certificate] | core.ArrayOut[Certificate] = core.arg()


@core.resource(type="aws_lightsail_container_service", namespace="lightsail")
class ContainerService(core.Resource):
    """
    The Amazon Resource Name (ARN) of the container service.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Availability Zone. Follows the format us-east-2a (case-sensitive).
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    Same as `name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A Boolean value indicating whether the container service is disabled. Defaults to `false`
    .
    """
    is_disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The name for the container service. Names must be of length 1 to 63, and be
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The power specification for the container service. The power specifies the amount of memo
    ry,
    """
    power: str | core.StringOut = core.attr(str)

    """
    The ID of the power of the container service.
    """
    power_id: str | core.StringOut = core.attr(str, computed=True)

    principal_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The private domain name of the container service. The private domain name is accessible only
    """
    private_domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The public domain names to use with the container service, such as example.com
    """
    public_domain_names: PublicDomainNames | None = core.attr(PublicDomainNames, default=None)

    """
    The Lightsail resource type of the container service (i.e., ContainerService).
    """
    resource_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The scale specification for the container service. The scale specifies the allocated comp
    ute
    """
    scale: int | core.IntOut = core.attr(int)

    """
    The current state of the container service.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Map of container service tags. To tag at launch, specify the tags in the Launch Template.
    If
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The publicly accessible URL of the container service. If no public endpoint is specified in the
    """
    url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        power: str | core.StringOut,
        scale: int | core.IntOut,
        is_disabled: bool | core.BoolOut | None = None,
        public_domain_names: PublicDomainNames | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContainerService.Args(
                name=name,
                power=power,
                scale=scale,
                is_disabled=is_disabled,
                public_domain_names=public_domain_names,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        is_disabled: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        power: str | core.StringOut = core.arg()

        public_domain_names: PublicDomainNames | None = core.arg(default=None)

        scale: int | core.IntOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
