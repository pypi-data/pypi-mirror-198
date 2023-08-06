import terrascript.core as core


@core.resource(type="aws_cloudfront_function", namespace="cloudfront")
class Function(core.Resource):
    """
    Amazon Resource Name (ARN) identifying your CloudFront Function.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Source code of the function
    """
    code: str | core.StringOut = core.attr(str)

    """
    (Optional) Comment.
    """
    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    ETag hash of the function. This is the value for the `DEVELOPMENT` stage of the function.
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    ETag hash of any `LIVE` stage of the function.
    """
    live_stage_etag: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Unique name for your CloudFront Function.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether to publish creation/change as Live CloudFront Function Version. Defaults to `true
    .
    """
    publish: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Identifier of the function's runtime. Currently only `cloudfront-js-1.0` is valid.
    """
    runtime: str | core.StringOut = core.attr(str)

    """
    Status of the function. Can be `UNPUBLISHED`, `UNASSOCIATED` or `ASSOCIATED`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        code: str | core.StringOut,
        name: str | core.StringOut,
        runtime: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        publish: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Function.Args(
                code=code,
                name=name,
                runtime=runtime,
                comment=comment,
                publish=publish,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        code: str | core.StringOut = core.arg()

        comment: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        publish: bool | core.BoolOut | None = core.arg(default=None)

        runtime: str | core.StringOut = core.arg()
