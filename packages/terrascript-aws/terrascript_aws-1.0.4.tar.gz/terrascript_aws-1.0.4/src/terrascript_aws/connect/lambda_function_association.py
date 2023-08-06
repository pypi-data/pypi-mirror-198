import terrascript.core as core


@core.resource(type="aws_connect_lambda_function_association", namespace="connect")
class LambdaFunctionAssociation(core.Resource):

    function_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        function_arn: str | core.StringOut,
        instance_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LambdaFunctionAssociation.Args(
                function_arn=function_arn,
                instance_id=instance_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        function_arn: str | core.StringOut = core.arg()

        instance_id: str | core.StringOut = core.arg()
