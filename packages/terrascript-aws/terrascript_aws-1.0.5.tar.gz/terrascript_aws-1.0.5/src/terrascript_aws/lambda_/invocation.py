import terrascript.core as core


@core.resource(type="aws_lambda_invocation", namespace="lambda_")
class Invocation(core.Resource):
    """
    (Required) Name of the lambda function.
    """

    function_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) JSON payload to the lambda function.
    """
    input: str | core.StringOut = core.attr(str)

    """
    (Optional) Qualifier (i.e., version) of the lambda function. Defaults to `$LATEST`.
    """
    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    String result of the lambda function invocation.
    """
    result: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Map of arbitrary keys and values that, when changed, will trigger a re-invocation. To for
    ce a re-invocation without changing these keys/values, use the [`terraform taint` command](https://w
    ww.terraform.io/docs/commands/taint.html).
    """
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
