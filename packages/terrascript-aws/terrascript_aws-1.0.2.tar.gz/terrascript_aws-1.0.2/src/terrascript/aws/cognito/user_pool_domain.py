import terrascript.core as core


@core.resource(type="aws_cognito_user_pool_domain", namespace="aws_cognito")
class UserPoolDomain(core.Resource):
    """
    The AWS account ID for the user pool owner.
    """

    aws_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.
    """
    certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The URL of the CloudFront distribution. This is required to generate the ALIAS `aws_route53_record`
    """
    cloudfront_distribution_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) For custom domains, this is the fully-qualified domain name, such as auth.example.com. Fo
    r Amazon Cognito prefix domains, this is the prefix alone, such as auth.
    """
    domain: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The S3 bucket where the static files for this domain are stored.
    """
    s3_bucket: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The user pool ID.
    """
    user_pool_id: str | core.StringOut = core.attr(str)

    """
    The app version.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain: str | core.StringOut,
        user_pool_id: str | core.StringOut,
        certificate_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserPoolDomain.Args(
                domain=domain,
                user_pool_id=user_pool_id,
                certificate_arn=certificate_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: str | core.StringOut | None = core.arg(default=None)

        domain: str | core.StringOut = core.arg()

        user_pool_id: str | core.StringOut = core.arg()
