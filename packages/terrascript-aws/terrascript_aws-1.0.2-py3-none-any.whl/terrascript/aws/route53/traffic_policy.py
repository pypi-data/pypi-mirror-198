import terrascript.core as core


@core.resource(type="aws_route53_traffic_policy", namespace="aws_route53")
class TrafficPolicy(core.Resource):

    comment: str | core.StringOut | None = core.attr(str, default=None)

    document: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str, computed=True)

    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        document: str | core.StringOut,
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TrafficPolicy.Args(
                document=document,
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

        document: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
