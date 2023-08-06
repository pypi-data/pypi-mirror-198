import terrascript.core as core


@core.resource(type="aws_ecr_registry_policy", namespace="ecr")
class RegistryPolicy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The policy document. This is a JSON formatted string. For more information about building
    IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicor
    p.com/terraform/aws/iam-policy)
    """
    policy: str | core.StringOut = core.attr(str)

    """
    The registry ID where the registry was created.
    """
    registry_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegistryPolicy.Args(
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()
