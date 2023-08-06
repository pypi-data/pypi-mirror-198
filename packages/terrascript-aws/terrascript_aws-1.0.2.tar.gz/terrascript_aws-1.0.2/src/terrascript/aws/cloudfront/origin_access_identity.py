import terrascript.core as core


@core.resource(type="aws_cloudfront_origin_access_identity", namespace="aws_cloudfront")
class OriginAccessIdentity(core.Resource):

    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    cloudfront_access_identity_path: str | core.StringOut = core.attr(str, computed=True)

    comment: str | core.StringOut | None = core.attr(str, default=None)

    etag: str | core.StringOut = core.attr(str, computed=True)

    iam_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

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
