import terrascript.core as core


@core.resource(type="aws_codeartifact_repository_permissions_policy", namespace="codeartifact")
class RepositoryPermissionsPolicy(core.Resource):
    """
    (Required) The name of the domain on which to set the resource policy.
    """

    domain: str | core.StringOut = core.attr(str)

    """
    (Optional) The account number of the AWS account that owns the domain.
    """
    domain_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ARN of the resource associated with the resource policy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A JSON policy string to be set as the access control resource policy on the provided doma
    in.
    """
    policy_document: str | core.StringOut = core.attr(str)

    """
    (Optional) The current revision of the resource policy to be set. This revision is used for optimist
    ic locking, which prevents others from overwriting your changes to the domain's resource policy.
    """
    policy_revision: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name of the repository to set the resource policy on.
    """
    repository: str | core.StringOut = core.attr(str)

    """
    The ARN of the resource associated with the resource policy.
    """
    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain: str | core.StringOut,
        policy_document: str | core.StringOut,
        repository: str | core.StringOut,
        domain_owner: str | core.StringOut | None = None,
        policy_revision: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RepositoryPermissionsPolicy.Args(
                domain=domain,
                policy_document=policy_document,
                repository=repository,
                domain_owner=domain_owner,
                policy_revision=policy_revision,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain: str | core.StringOut = core.arg()

        domain_owner: str | core.StringOut | None = core.arg(default=None)

        policy_document: str | core.StringOut = core.arg()

        policy_revision: str | core.StringOut | None = core.arg(default=None)

        repository: str | core.StringOut = core.arg()
