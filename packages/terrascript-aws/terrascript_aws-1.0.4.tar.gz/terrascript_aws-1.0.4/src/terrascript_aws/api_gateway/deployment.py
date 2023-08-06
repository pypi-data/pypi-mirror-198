import terrascript.core as core


@core.resource(type="aws_api_gateway_deployment", namespace="api_gateway")
class Deployment(core.Resource):
    """
    The creation date of the deployment
    """

    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the deployment
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The execution ARN to be used in [`lambda_permission`](/docs/providers/aws/r/lambda_permission.html)'
    s `source_arn`
    """
    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the deployment
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The URL to invoke the API pointing to the stage,
    """
    invoke_url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) REST API identifier.
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Description to set on the stage managed by the `stage_name` argument.
    """
    stage_description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the stage to create with this deployment. If the specified stage already exists,
    it will be updated to point to the new deployment. We recommend using the [`aws_api_gateway_stage` r
    esource](api_gateway_stage.html) instead to manage stages.
    """
    stage_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Map of arbitrary keys and values that, when changed, will trigger a redeployment. To forc
    e a redeployment without changing these keys/values, use the [`terraform taint` command](https://www
    .terraform.io/docs/commands/taint.html).
    """
    triggers: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Map to set on the stage managed by the `stage_name` argument.
    """
    variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        rest_api_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        stage_description: str | core.StringOut | None = None,
        stage_name: str | core.StringOut | None = None,
        triggers: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Deployment.Args(
                rest_api_id=rest_api_id,
                description=description,
                stage_description=stage_description,
                stage_name=stage_name,
                triggers=triggers,
                variables=variables,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        rest_api_id: str | core.StringOut = core.arg()

        stage_description: str | core.StringOut | None = core.arg(default=None)

        stage_name: str | core.StringOut | None = core.arg(default=None)

        triggers: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
