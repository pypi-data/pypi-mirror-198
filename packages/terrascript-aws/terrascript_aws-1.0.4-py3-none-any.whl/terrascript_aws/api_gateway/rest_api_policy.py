import terrascript.core as core


@core.resource(type="aws_api_gateway_rest_api_policy", namespace="api_gateway")
class RestApiPolicy(core.Resource):
    """
    The ID of the REST API
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) JSON formatted policy document that controls access to the API Gateway. For more informat
    ion about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](
    https://learn.hashicorp.com/terraform/aws/iam-policy)
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the REST API.
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RestApiPolicy.Args(
                policy=policy,
                rest_api_id=rest_api_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()
