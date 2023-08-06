import terrascript.core as core


@core.resource(type="aws_iam_policy_attachment", namespace="iam")
class PolicyAttachment(core.Resource):

    groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The policy's ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the attachment.
    """
    name: str | core.StringOut = core.attr(str)

    policy_arn: str | core.StringOut = core.attr(str)

    roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    users: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        policy_arn: str | core.StringOut,
        groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        roles: list[str] | core.ArrayOut[core.StringOut] | None = None,
        users: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PolicyAttachment.Args(
                name=name,
                policy_arn=policy_arn,
                groups=groups,
                roles=roles,
                users=users,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        policy_arn: str | core.StringOut = core.arg()

        roles: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        users: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
