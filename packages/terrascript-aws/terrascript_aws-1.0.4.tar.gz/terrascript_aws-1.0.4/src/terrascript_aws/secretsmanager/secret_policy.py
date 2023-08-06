import terrascript.core as core


@core.resource(type="aws_secretsmanager_secret_policy", namespace="secretsmanager")
class SecretPolicy(core.Resource):
    """
    (Optional) Makes an optional API call to Zelkova to validate the Resource Policy to prevent broad ac
    cess to your secret.
    """

    block_public_policy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Amazon Resource Name (ARN) of the secret.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsm
    anager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about bu
    ilding AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://lear
    n.hashicorp.com/terraform/aws/iam-policy). Unlike `aws_secretsmanager_secret`, where `policy` can be
    set to `"{}"` to delete the policy, `"{}"` is not a valid policy since `policy` is required.
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) Secret ARN.
    """
    secret_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        secret_arn: str | core.StringOut,
        block_public_policy: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecretPolicy.Args(
                policy=policy,
                secret_arn=secret_arn,
                block_public_policy=block_public_policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_public_policy: bool | core.BoolOut | None = core.arg(default=None)

        policy: str | core.StringOut = core.arg()

        secret_arn: str | core.StringOut = core.arg()
