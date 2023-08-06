import terrascript.core as core


@core.resource(type="aws_ssoadmin_permission_set", namespace="aws_ssoadmin")
class PermissionSet(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_arn: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    relay_state: str | core.StringOut | None = core.attr(str, default=None)

    session_duration: str | core.StringOut | None = core.attr(str, default=None)

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
        instance_arn: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        relay_state: str | core.StringOut | None = None,
        session_duration: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PermissionSet.Args(
                instance_arn=instance_arn,
                name=name,
                description=description,
                relay_state=relay_state,
                session_duration=session_duration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        instance_arn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        relay_state: str | core.StringOut | None = core.arg(default=None)

        session_duration: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
