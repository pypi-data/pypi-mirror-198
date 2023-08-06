import terrascript.core as core


@core.resource(type="aws_cloudfront_origin_access_identity", namespace="cloudfront")
class OriginAccessIdentity(core.Resource):
    """
    Internal value used by CloudFront to allow future
    """

    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    """
    A shortcut to the full path for the
    """
    cloudfront_access_identity_path: str | core.StringOut = core.attr(str, computed=True)

    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    The current version of the origin access identity's information.
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    A pre-generated ARN for use in S3 bucket policies (see below).
    """
    iam_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier for the distribution. For example: `EDFDVBD632BHDS5`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon S3 canonical user ID for the origin
    """
    s3_canonical_user_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        comment: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OriginAccessIdentity.Args(
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)
