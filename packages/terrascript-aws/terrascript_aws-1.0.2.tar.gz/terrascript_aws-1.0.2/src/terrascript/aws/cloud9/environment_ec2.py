import terrascript.core as core


@core.resource(type="aws_cloud9_environment_ec2", namespace="aws_cloud9")
class EnvironmentEc2(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    automatic_stop_time_minutes: int | core.IntOut | None = core.attr(int, default=None)

    connection_type: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_id: str | core.StringOut | None = core.attr(str, default=None)

    instance_type: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    owner_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_type: str | core.StringOut,
        name: str | core.StringOut,
        automatic_stop_time_minutes: int | core.IntOut | None = None,
        connection_type: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        image_id: str | core.StringOut | None = None,
        owner_arn: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EnvironmentEc2.Args(
                instance_type=instance_type,
                name=name,
                automatic_stop_time_minutes=automatic_stop_time_minutes,
                connection_type=connection_type,
                description=description,
                image_id=image_id,
                owner_arn=owner_arn,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        automatic_stop_time_minutes: int | core.IntOut | None = core.arg(default=None)

        connection_type: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        image_id: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        owner_arn: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
