import terrascript.core as core


@core.resource(type="aws_s3control_bucket_policy", namespace="s3control")
class BucketPolicy(core.Resource):
    """
    (Required) Amazon Resource Name (ARN) of the bucket.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    Amazon Resource Name (ARN) of the bucket.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) JSON string of the resource policy. For more information about building AWS IAM policy do
    cuments with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terrafor
    m/aws/iam-policy).
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
