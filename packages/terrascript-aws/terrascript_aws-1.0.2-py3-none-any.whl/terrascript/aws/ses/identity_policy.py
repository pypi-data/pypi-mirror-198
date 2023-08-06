import terrascript.core as core


@core.resource(type="aws_ses_identity_policy", namespace="aws_ses")
class IdentityPolicy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    identity: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        identity: str | core.StringOut,
        name: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=IdentityPolicy.Args(
                identity=identity,
                name=name,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
