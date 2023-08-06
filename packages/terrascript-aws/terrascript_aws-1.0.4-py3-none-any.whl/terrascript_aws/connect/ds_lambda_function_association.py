import terrascript.core as core


@core.data(type="aws_connect_lambda_function_association", namespace="connect")
class DsLambdaFunctionAssociation(core.Data):

    function_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        function_arn: str | core.StringOut,
        instance_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsLambdaFunctionAssociation.Args(
                function_arn=function_arn,
                instance_id=instance_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: str | core.StringOut = core.arg()

        instance_id: str | core.StringOut = core.arg()
