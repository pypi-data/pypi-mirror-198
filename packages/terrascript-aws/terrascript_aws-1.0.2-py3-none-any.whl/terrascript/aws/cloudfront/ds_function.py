import terrascript.core as core


@core.data(type="aws_cloudfront_function", namespace="aws_cloudfront")
class DsFunction(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    code: str | core.StringOut = core.attr(str, computed=True)

    comment: str | core.StringOut = core.attr(str, computed=True)

    etag: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_modified_time: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    runtime: str | core.StringOut = core.attr(str, computed=True)

    stage: str | core.StringOut = core.attr(str)

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
