import terrascript.core as core


@core.resource(type="aws_acmpca_policy", namespace="acmpca")
class Policy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) JSON-formatted IAM policy to attach to the specified private CA resource.
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) Amazon Resource Name (ARN) of the private CA to associate with the policy.
    """
    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        resource_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Policy.Args(
                policy=policy,
                resource_arn=resource_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()
