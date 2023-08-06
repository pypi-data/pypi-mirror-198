import terrascript.core as core


@core.data(type="aws_cloudfront_function", namespace="cloudfront")
class DsFunction(core.Data):
    """
    Amazon Resource Name (ARN) identifying your CloudFront Function.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Source code of the function
    """
    code: str | core.StringOut = core.attr(str, computed=True)

    """
    Comment.
    """
    comment: str | core.StringOut = core.attr(str, computed=True)

    """
    ETag hash of the function
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    When this resource was last modified.
    """
    last_modified_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the CloudFront function.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Identifier of the function's runtime.
    """
    runtime: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The function’s stage, either `DEVELOPMENT` or `LIVE`.
    """
    stage: str | core.StringOut = core.attr(str)

    """
    Status of the function. Can be `UNPUBLISHED`, `UNASSOCIATED` or `ASSOCIATED`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        stage: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsFunction.Args(
                name=name,
                stage=stage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        stage: str | core.StringOut = core.arg()
