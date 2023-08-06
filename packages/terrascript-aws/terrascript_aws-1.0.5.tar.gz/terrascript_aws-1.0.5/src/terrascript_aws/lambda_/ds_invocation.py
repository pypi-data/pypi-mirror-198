import terrascript.core as core


@core.data(type="aws_lambda_invocation", namespace="lambda_")
class DsInvocation(core.Data):
    """
    (Required) The name of the lambda function.
    """

    function_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A string in JSON format that is passed as payload to the lambda function.
    """
    input: str | core.StringOut = core.attr(str)

    """
    (Optional) The qualifier (a.k.a version) of the lambda function. Defaults
    """
    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    String result of the lambda function invocation.
    """
    result: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        function_name: str | core.StringOut,
        input: str | core.StringOut,
        qualifier: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInvocation.Args(
                function_name=function_name,
                input=input,
                qualifier=qualifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_name: str | core.StringOut = core.arg()

        input: str | core.StringOut = core.arg()

        qualifier: str | core.StringOut | None = core.arg(default=None)
