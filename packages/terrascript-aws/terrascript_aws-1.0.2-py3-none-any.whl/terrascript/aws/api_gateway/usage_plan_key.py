import terrascript.core as core


@core.resource(type="aws_api_gateway_usage_plan_key", namespace="aws_api_gateway")
class UsagePlanKey(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    key_id: str | core.StringOut = core.attr(str)

    key_type: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str, computed=True)

    usage_plan_id: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        key_id: str | core.StringOut,
        key_type: str | core.StringOut,
        usage_plan_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UsagePlanKey.Args(
                key_id=key_id,
                key_type=key_type,
                usage_plan_id=usage_plan_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_id: str | core.StringOut = core.arg()

        key_type: str | core.StringOut = core.arg()

        usage_plan_id: str | core.StringOut = core.arg()
