import terrascript.core as core


@core.data(type="aws_lambda_alias", namespace="lambda_")
class DsAlias(core.Data):
    """
    The Amazon Resource Name (ARN) identifying the Lambda function alias.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of alias.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the aliased Lambda function.
    """
    function_name: str | core.StringOut = core.attr(str)

    """
    Lambda function version which the alias uses.
    """
    function_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN to be used for invoking Lambda Function from API Gateway - to be used in aws_api_gateway_int
    egration's `uri`.
    """
    invoke_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the Lambda alias.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        function_name: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsAlias.Args(
                function_name=function_name,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
