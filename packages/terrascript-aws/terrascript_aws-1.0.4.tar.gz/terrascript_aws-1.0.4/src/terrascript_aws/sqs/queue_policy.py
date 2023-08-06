import terrascript.core as core


@core.resource(type="aws_sqs_queue_policy", namespace="sqs")
class QueuePolicy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The JSON policy for the SQS queue. For more information about building AWS IAM policy doc
    uments with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform
    /aws/iam-policy).
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) The URL of the SQS Queue to which to attach the policy
    """
    queue_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        queue_url: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=QueuePolicy.Args(
                policy=policy,
                queue_url=queue_url,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()

        queue_url: str | core.StringOut = core.arg()
