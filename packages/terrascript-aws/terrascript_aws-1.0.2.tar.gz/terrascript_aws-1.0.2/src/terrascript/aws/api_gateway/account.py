import terrascript.core as core


@core.schema
class ThrottleSettings(core.Schema):

    burst_limit: int | core.IntOut = core.attr(int, computed=True)

    rate_limit: float | core.FloatOut = core.attr(float, computed=True)

    def __init__(
        self,
        *,
        burst_limit: int | core.IntOut,
        rate_limit: float | core.FloatOut,
    ):
        super().__init__(
            args=ThrottleSettings.Args(
                burst_limit=burst_limit,
                rate_limit=rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        burst_limit: int | core.IntOut = core.arg()

        rate_limit: float | core.FloatOut = core.arg()


@core.resource(type="aws_api_gateway_account", namespace="aws_api_gateway")
class Account(core.Resource):

    cloudwatch_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    throttle_settings: list[ThrottleSettings] | core.ArrayOut[ThrottleSettings] = core.attr(
        ThrottleSettings, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cloudwatch_role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Account.Args(
                cloudwatch_role_arn=cloudwatch_role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_role_arn: str | core.StringOut | None = core.arg(default=None)
