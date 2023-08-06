import terrascript.core as core


@core.resource(type="aws_rolesanywhere_profile", namespace="aws_rolesanywhere")
class Profile(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    duration_seconds: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    require_instance_properties: bool | core.BoolOut | None = core.attr(bool, default=None)

    role_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    session_policy: str | core.StringOut | None = core.attr(str, default=None)

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
        name: str | core.StringOut,
        role_arns: list[str] | core.ArrayOut[core.StringOut],
        duration_seconds: int | core.IntOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        require_instance_properties: bool | core.BoolOut | None = None,
        session_policy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Profile.Args(
                name=name,
                role_arns=role_arns,
                duration_seconds=duration_seconds,
                enabled=enabled,
                managed_policy_arns=managed_policy_arns,
                require_instance_properties=require_instance_properties,
                session_policy=session_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        duration_seconds: int | core.IntOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        require_instance_properties: bool | core.BoolOut | None = core.arg(default=None)

        role_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        session_policy: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
