import terrascript.core as core


@core.data(type="aws_cloudfront_origin_access_identity", namespace="cloudfront")
class DsOriginAccessIdentity(core.Data):
    """
    Internal value used by CloudFront to allow future
    """

    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    """
    A shortcut to the full path for the
    """
    cloudfront_access_identity_path: str | core.StringOut = core.attr(str, computed=True)

    """
    An optional comment for the origin access identity.
    """
    comment: str | core.StringOut = core.attr(str, computed=True)

    """
    The current version of the origin access identity's information.
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    A pre-generated ARN for use in S3 bucket policies (see below).
    """
    iam_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str)

    """
    The Amazon S3 canonical user ID for the origin
    """
    s3_canonical_user_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsOriginAccessIdentity.Args(
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()
