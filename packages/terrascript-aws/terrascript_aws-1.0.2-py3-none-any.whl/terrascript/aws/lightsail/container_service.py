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


@core.resource(type="aws_lightsail_container_service", namespace="aws_lightsail")
class ContainerService(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    is_disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut = core.attr(str)

    power: str | core.StringOut = core.attr(str)

    power_id: str | core.StringOut = core.attr(str, computed=True)

    principal_arn: str | core.StringOut = core.attr(str, computed=True)

    private_domain_name: str | core.StringOut = core.attr(str, computed=True)

    public_domain_names: PublicDomainNames | None = core.attr(PublicDomainNames, default=None)

    resource_type: str | core.StringOut = core.attr(str, computed=True)

    scale: int | core.IntOut = core.attr(int)

    state: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
