import terrascript.core as core


@core.resource(type="aws_s3_bucket_policy", namespace="s3")
class BucketPolicy(core.Resource):
    """
    (Required) The name of the bucket to which to apply the policy.
    """

    bucket: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The text of the policy. Although this is a bucket policy rather than an IAM policy, the [
    aws_iam_policy_document`](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-so
    urces/iam_policy_document) data source may be used, so long as it specifies a principal. For more in
    formation about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document G
    uide](https://learn.hashicorp.com/terraform/aws/iam-policy). Note: Bucket policies are limited to 20
    KB in size.
    """
    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketPolicy.Args(
                bucket=bucket,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
