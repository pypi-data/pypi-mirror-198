import terrascript.core as core


@core.resource(type="aws_lambda_provisioned_concurrency_config", namespace="lambda_")
class ProvisionedConcurrencyConfig(core.Resource):

    function_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    provisioned_concurrent_executions: int | core.IntOut = core.attr(int)

    qualifier: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: str | core.StringOut,
        provisioned_concurrent_executions: int | core.IntOut,
        qualifier: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProvisionedConcurrencyConfig.Args(
                function_name=function_name,
                provisioned_concurrent_executions=provisioned_concurrent_executions,
                qualifier=qualifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        function_name: str | core.StringOut = core.arg()

        provisioned_concurrent_executions: int | core.IntOut = core.arg()

        qualifier: str | core.StringOut = core.arg()
