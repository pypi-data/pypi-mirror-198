import terrascript.core as core


@core.resource(type="aws_apigatewayv2_deployment", namespace="apigatewayv2")
class Deployment(core.Resource):
    """
    (Required) The API identifier.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    Whether the deployment was automatically released.
    """
    auto_deployed: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) The description for the deployment resource. Must be less than or equal to 1024 character
    s in length.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The deployment identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of arbitrary keys and values that, when changed, will trigger a redeployment. To fo
    rce a redeployment without changing these keys/values, use the [`terraform taint` command](https://w
    ww.terraform.io/docs/commands/taint.html).
    """
    triggers: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        triggers: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Deployment.Args(
                api_id=api_id,
                description=description,
                triggers=triggers,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        triggers: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
