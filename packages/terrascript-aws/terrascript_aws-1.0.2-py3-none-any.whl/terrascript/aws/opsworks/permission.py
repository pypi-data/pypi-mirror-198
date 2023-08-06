import terrascript.core as core


@core.resource(type="aws_opsworks_permission", namespace="aws_opsworks")
class Permission(core.Resource):

    allow_ssh: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    allow_sudo: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    stack_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    user_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_arn: str | core.StringOut,
        allow_ssh: bool | core.BoolOut | None = None,
        allow_sudo: bool | core.BoolOut | None = None,
        level: str | core.StringOut | None = None,
        stack_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permission.Args(
                user_arn=user_arn,
                allow_ssh=allow_ssh,
                allow_sudo=allow_sudo,
                level=level,
                stack_id=stack_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_ssh: bool | core.BoolOut | None = core.arg(default=None)

        allow_sudo: bool | core.BoolOut | None = core.arg(default=None)

        level: str | core.StringOut | None = core.arg(default=None)

        stack_id: str | core.StringOut | None = core.arg(default=None)

        user_arn: str | core.StringOut = core.arg()
