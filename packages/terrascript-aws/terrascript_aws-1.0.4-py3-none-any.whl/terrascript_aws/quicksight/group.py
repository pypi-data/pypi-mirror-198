import terrascript.core as core


@core.resource(type="aws_quicksight_group", namespace="quicksight")
class Group(core.Resource):
    """
    Amazon Resource Name (ARN) of group
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID for the AWS account that the group is in. Currently, you use the ID for the AWS ac
    count that contains your Amazon QuickSight account.
    """
    aws_account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A description for the group.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A name for the group.
    """
    group_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The namespace. Currently, you should set this to `default`.
    """
    namespace: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        group_name: str | core.StringOut,
        aws_account_id: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        namespace: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Group.Args(
                group_name=group_name,
                aws_account_id=aws_account_id,
                description=description,
                namespace=namespace,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_account_id: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        group_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut | None = core.arg(default=None)
