import terrascript.core as core


@core.data(type="aws_lambda_alias", namespace="aws_lambda_")
class DsAlias(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    function_name: str | core.StringOut = core.attr(str)

    function_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    invoke_arn: str | core.StringOut = core.attr(str, computed=True)

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
