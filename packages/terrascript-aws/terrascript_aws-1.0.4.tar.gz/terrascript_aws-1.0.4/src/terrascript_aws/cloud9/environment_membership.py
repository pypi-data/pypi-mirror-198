import terrascript.core as core


@core.resource(type="aws_cloud9_environment_membership", namespace="cloud9")
class EnvironmentMembership(core.Resource):

    environment_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    permissions: str | core.StringOut = core.attr(str)

    user_arn: str | core.StringOut = core.attr(str)

    user_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        environment_id: str | core.StringOut,
        permissions: str | core.StringOut,
        user_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EnvironmentMembership.Args(
                environment_id=environment_id,
                permissions=permissions,
                user_arn=user_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        environment_id: str | core.StringOut = core.arg()

        permissions: str | core.StringOut = core.arg()

        user_arn: str | core.StringOut = core.arg()
