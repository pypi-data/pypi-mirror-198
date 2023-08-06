import terrascript.core as core


@core.resource(type="aws_lightsail_instance", namespace="aws_lightsail")
class Instance(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str)

    blueprint_id: str | core.StringOut = core.attr(str)

    bundle_id: str | core.StringOut = core.attr(str)

    cpu_count: int | core.IntOut = core.attr(int, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_address: str | core.StringOut = core.attr(str, computed=True)

    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    is_static_ip: bool | core.BoolOut = core.attr(bool, computed=True)

    key_pair_name: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    private_ip_address: str | core.StringOut = core.attr(str, computed=True)

    public_ip_address: str | core.StringOut = core.attr(str, computed=True)

    ram_size: float | core.FloatOut = core.attr(float, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_data: str | core.StringOut | None = core.attr(str, default=None)

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
