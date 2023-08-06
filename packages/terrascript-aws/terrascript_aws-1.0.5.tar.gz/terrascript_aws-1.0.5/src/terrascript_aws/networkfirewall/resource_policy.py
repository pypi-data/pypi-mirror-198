import terrascript.core as core


@core.resource(type="aws_networkfirewall_resource_policy", namespace="networkfirewall")
class ResourcePolicy(core.Resource):
    """
    The Amazon Resource Name (ARN) of the rule group or firewall policy associated with the resource pol
    icy.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) JSON formatted policy document that controls access to the Network Firewall resource. The
    policy must be provided **without whitespaces**.  We recommend using [jsonencode](https://www.terra
    form.io/docs/configuration/functions/jsonencode.html) for formatting as seen in the examples above.
    For more details, including available policy statement Actions, see the [Policy](https://docs.aws.am
    azon.com/network-firewall/latest/APIReference/API_PutResourcePolicy.html#API_PutResourcePolicy_Reque
    stSyntax) parameter in the AWS API documentation.
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the rule group or firewall policy.
    """
    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        resource_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourcePolicy.Args(
                policy=policy,
                resource_arn=resource_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()
