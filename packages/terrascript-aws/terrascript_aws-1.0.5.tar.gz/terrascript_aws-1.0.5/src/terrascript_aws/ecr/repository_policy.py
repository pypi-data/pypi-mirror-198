import terrascript.core as core


@core.resource(type="aws_ecr_repository_policy", namespace="ecr")
class RepositoryPolicy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The policy document. This is a JSON formatted string. For more information about building
    IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicor
    p.com/terraform/aws/iam-policy)
    """
    policy: str | core.StringOut = core.attr(str)

    """
    The registry ID where the repository was created.
    """
    registry_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the repository to apply the policy.
    """
    repository: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        repository: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RepositoryPolicy.Args(
                policy=policy,
                repository=repository,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()

        repository: str | core.StringOut = core.arg()
