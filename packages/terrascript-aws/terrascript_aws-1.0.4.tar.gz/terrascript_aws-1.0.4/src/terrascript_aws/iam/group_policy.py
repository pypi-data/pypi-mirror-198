import terrascript.core as core


@core.resource(type="aws_iam_group_policy", namespace="iam")
class GroupPolicy(core.Resource):
    """
    (Required) The IAM group to attach to the policy.
    """

    group: str | core.StringOut = core.attr(str)

    """
    The group policy ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the policy. If omitted, Terraform will
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The policy document. This is a JSON formatted string. For more information about building
    IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicor
    p.com/terraform/aws/iam-policy)
    """
    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group: str | core.StringOut,
        policy: str | core.StringOut,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupPolicy.Args(
                group=group,
                policy=policy,
                name=name,
                name_prefix=name_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut = core.arg()
