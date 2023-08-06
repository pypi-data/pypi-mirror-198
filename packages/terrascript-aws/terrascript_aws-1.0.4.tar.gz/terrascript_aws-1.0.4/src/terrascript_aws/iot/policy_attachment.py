import terrascript.core as core


@core.resource(type="aws_iot_policy_attachment", namespace="iot")
class PolicyAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the policy to attach.
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) The identity to which the policy is attached.
    """
    target: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        target: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PolicyAttachment.Args(
                policy=policy,
                target=target,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()

        target: str | core.StringOut = core.arg()
