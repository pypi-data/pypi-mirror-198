import terrascript.core as core


@core.resource(type="aws_cloudfront_function", namespace="aws_cloudfront")
class Function(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    code: str | core.StringOut = core.attr(str)

    comment: str | core.StringOut | None = core.attr(str, default=None)

    etag: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    live_stage_etag: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    publish: bool | core.BoolOut | None = core.attr(bool, default=None)

    runtime: str | core.StringOut = core.attr(str)

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
