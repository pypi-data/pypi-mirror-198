import terrascript.core as core


@core.resource(type="aws_iam_user_policy", namespace="iam")
class UserPolicy(core.Resource):
    """
    The user policy ID, in the form of `user_name:user_policy_name`.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the policy. If omitted, Terraform will assign a random, unique name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The policy document. This is a JSON formatted string. For more information about building
    AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hash
    icorp.com/terraform/aws/iam-policy).
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) IAM user to which to attach this policy.
    """
    user: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        user: str | core.StringOut,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserPolicy.Args(
                policy=policy,
                user=user,
                name=name,
                name_prefix=name_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut = core.arg()

        user: str | core.StringOut = core.arg()
