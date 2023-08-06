import terrascript.core as core


@core.data(type="aws_iam_policy", namespace="iam")
class DsPolicy(core.Data):
    """
    (Optional) The ARN of the IAM policy.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The description of the policy.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the IAM policy.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The path to the policy.
    """
    path: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The prefix of the path to the IAM policy.
    """
    path_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    The policy document of the policy.
    """
    policy: str | core.StringOut = core.attr(str, computed=True)

    """
    The policy's ID.
    """
    policy_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value mapping of tags for the IAM Policy.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        path_prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPolicy.Args(
                arn=arn,
                name=name,
                path_prefix=path_prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        path_prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
