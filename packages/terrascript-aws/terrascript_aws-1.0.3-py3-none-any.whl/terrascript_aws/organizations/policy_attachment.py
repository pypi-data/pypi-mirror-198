import terrascript.core as core


@core.resource(type="aws_organizations_policy_attachment", namespace="organizations")
class PolicyAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    policy_id: str | core.StringOut = core.attr(str)

    target_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy_id: str | core.StringOut,
        target_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PolicyAttachment.Args(
                policy_id=policy_id,
                target_id=target_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy_id: str | core.StringOut = core.arg()

        target_id: str | core.StringOut = core.arg()
