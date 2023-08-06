import terrascript.core as core


@core.resource(type="aws_cognito_user_pool_domain", namespace="cognito")
class UserPoolDomain(core.Resource):

    aws_account_id: str | core.StringOut = core.attr(str, computed=True)

    certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    cloudfront_distribution_arn: str | core.StringOut = core.attr(str, computed=True)

    domain: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    s3_bucket: str | core.StringOut = core.attr(str, computed=True)

    user_pool_id: str | core.StringOut = core.attr(str)

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
