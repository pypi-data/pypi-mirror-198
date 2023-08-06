import terrascript.core as core


@core.resource(type="aws_quicksight_group_membership", namespace="aws_quicksight")
class GroupMembership(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    aws_account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    group_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    member_name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        group_name: str | core.StringOut,
        member_name: str | core.StringOut,
        aws_account_id: str | core.StringOut | None = None,
        namespace: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupMembership.Args(
                group_name=group_name,
                member_name=member_name,
                aws_account_id=aws_account_id,
                namespace=namespace,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_account_id: str | core.StringOut | None = core.arg(default=None)

        group_name: str | core.StringOut = core.arg()

        member_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut | None = core.arg(default=None)
