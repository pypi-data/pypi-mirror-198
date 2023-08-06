import terrascript.core as core


@core.data(type="aws_cloudfront_origin_access_identities", namespace="cloudfront")
class DsOriginAccessIdentities(core.Data):

    comments: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Set of ARNs of the matched origin access identities.
    """
    iam_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of ids of the matched origin access identities.
    """
    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Set of S3 canonical user IDs of the matched origin access identities.
    """
    s3_canonical_user_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        comments: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOriginAccessIdentities.Args(
                comments=comments,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comments: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
