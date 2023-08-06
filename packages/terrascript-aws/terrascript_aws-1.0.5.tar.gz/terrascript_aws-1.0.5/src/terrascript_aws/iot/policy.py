import terrascript.core as core


@core.resource(type="aws_iot_policy", namespace="iot")
class Policy(core.Resource):
    """
    The ARN assigned by AWS to this policy.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The default version of this policy.
    """
    default_version_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the policy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The policy document. This is a JSON formatted string. Use the [IoT Developer Guide](http:
    //docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Polic
    ies. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM P
    olicy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-policy).
    """
    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Policy.Args(
                name=name,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
