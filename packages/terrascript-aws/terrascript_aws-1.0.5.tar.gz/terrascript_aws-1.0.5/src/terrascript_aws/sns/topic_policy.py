import terrascript.core as core


@core.resource(type="aws_sns_topic_policy", namespace="sns")
class TopicPolicy(core.Resource):
    """
    (Required) The ARN of the SNS topic
    """

    arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS Account ID of the SNS topic owner
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The fully-formed AWS policy as JSON. For more information about building AWS IAM policy d
    ocuments with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terrafo
    rm/aws/iam-policy).
    """
    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        arn: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TopicPolicy.Args(
                arn=arn,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
