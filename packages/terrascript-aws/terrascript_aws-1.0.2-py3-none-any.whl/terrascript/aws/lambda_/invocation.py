import terrascript.core as core


@core.resource(type="aws_lambda_invocation", namespace="aws_lambda_")
class Invocation(core.Resource):

    function_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    input: str | core.StringOut = core.attr(str)

    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    result: str | core.StringOut = core.attr(str, computed=True)

    triggers: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: str | core.StringOut,
        input: str | core.StringOut,
        qualifier: str | core.StringOut | None = None,
        triggers: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Invocation.Args(
                function_name=function_name,
                input=input,
                qualifier=qualifier,
                triggers=triggers,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        function_name: str | core.StringOut = core.arg()

        input: str | core.StringOut = core.arg()

        qualifier: str | core.StringOut | None = core.arg(default=None)

        triggers: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
