import terrascript.core as core


@core.schema
class PolicyAttribute(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PolicyAttribute.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_load_balancer_policy", namespace="elb_classic")
class LoadBalancerPolicy(core.Resource):
    """
    The ID of the policy.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The load balancer on which the policy is defined.
    """
    load_balancer_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Policy attribute to apply to the policy.
    """
    policy_attribute: list[PolicyAttribute] | core.ArrayOut[PolicyAttribute] | None = core.attr(
        PolicyAttribute, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Required) The name of the load balancer policy.
    """
    policy_name: str | core.StringOut = core.attr(str)

    """
    (Required) The policy type.
    """
    policy_type_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        load_balancer_name: str | core.StringOut,
        policy_name: str | core.StringOut,
        policy_type_name: str | core.StringOut,
        policy_attribute: list[PolicyAttribute] | core.ArrayOut[PolicyAttribute] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LoadBalancerPolicy.Args(
                load_balancer_name=load_balancer_name,
                policy_name=policy_name,
                policy_type_name=policy_type_name,
                policy_attribute=policy_attribute,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        load_balancer_name: str | core.StringOut = core.arg()

        policy_attribute: list[PolicyAttribute] | core.ArrayOut[PolicyAttribute] | None = core.arg(
            default=None
        )

        policy_name: str | core.StringOut = core.arg()

        policy_type_name: str | core.StringOut = core.arg()
