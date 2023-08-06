import terrascript.core as core


@core.resource(type="aws_ec2_host", namespace="aws_ec2")
class Host(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_placement: str | core.StringOut | None = core.attr(str, default=None)

    availability_zone: str | core.StringOut = core.attr(str)

    host_recovery: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_family: str | core.StringOut | None = core.attr(str, default=None)

    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    outpost_arn: str | core.StringOut | None = core.attr(str, default=None)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
