import terrascript.core as core


@core.resource(type="aws_cloudfront_key_group", namespace="aws_cloudfront")
class KeyGroup(core.Resource):

    comment: str | core.StringOut | None = core.attr(str, default=None)

    etag: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    items: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        items: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=KeyGroup.Args(
                items=items,
                name=name,
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        items: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()
