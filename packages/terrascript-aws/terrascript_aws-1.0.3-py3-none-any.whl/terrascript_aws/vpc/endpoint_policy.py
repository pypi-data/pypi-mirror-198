import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_policy", namespace="vpc")
class EndpointPolicy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    vpc_endpoint_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_endpoint_id: str | core.StringOut,
        policy: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointPolicy.Args(
                vpc_endpoint_id=vpc_endpoint_id,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut | None = core.arg(default=None)

        vpc_endpoint_id: str | core.StringOut = core.arg()
