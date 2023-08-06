import terrascript.core as core


@core.resource(type="aws_iot_role_alias", namespace="aws_iot")
class RoleAlias(core.Resource):

    alias: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    credential_duration: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        alias: str | core.StringOut,
        role_arn: str | core.StringOut,
        credential_duration: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoleAlias.Args(
                alias=alias,
                role_arn=role_arn,
                credential_duration=credential_duration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alias: str | core.StringOut = core.arg()

        credential_duration: int | core.IntOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()
