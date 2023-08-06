import terrascript.core as core


@core.data(type="aws_cloudfront_origin_access_identities", namespace="aws_cloudfront")
class DsOriginAccessIdentities(core.Data):

    comments: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    iam_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

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
