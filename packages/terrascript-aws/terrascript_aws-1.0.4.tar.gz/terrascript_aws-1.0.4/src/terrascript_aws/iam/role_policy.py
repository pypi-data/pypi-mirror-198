import terrascript.core as core


@core.resource(type="aws_iam_role_policy", namespace="iam")
class RolePolicy(core.Resource):
    """
    The role policy ID, in the form of `role_name:role_policy_name`.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the role policy. If omitted, Terraform will
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The inline policy document. This is a JSON formatted string. For more information about b
    uilding IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.h
    ashicorp.com/terraform/aws/iam-policy)
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the IAM role to attach to the policy.
    """
    role: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        role: str | core.StringOut,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RolePolicy.Args(
                policy=policy,
                role=role,
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

        role: str | core.StringOut = core.arg()
