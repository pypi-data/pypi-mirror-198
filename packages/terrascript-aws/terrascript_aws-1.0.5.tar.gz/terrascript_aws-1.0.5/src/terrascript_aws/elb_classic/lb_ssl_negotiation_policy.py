import terrascript.core as core


@core.schema
class Attribute(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Attribute.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_lb_ssl_negotiation_policy", namespace="elb_classic")
class LbSslNegotiationPolicy(core.Resource):
    """
    (Optional) An SSL Negotiation policy attribute. Each has two properties:
    """

    attribute: list[Attribute] | core.ArrayOut[Attribute] | None = core.attr(
        Attribute, default=None, kind=core.Kind.array
    )

    """
    The ID of the policy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The load balancer port to which the policy
    """
    lb_port: int | core.IntOut = core.attr(int)

    """
    (Required) The load balancer to which the policy
    """
    load_balancer: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the SSL negotiation policy.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        lb_port: int | core.IntOut,
        load_balancer: str | core.StringOut,
        name: str | core.StringOut,
        attribute: list[Attribute] | core.ArrayOut[Attribute] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbSslNegotiationPolicy.Args(
                lb_port=lb_port,
                load_balancer=load_balancer,
                name=name,
                attribute=attribute,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attribute: list[Attribute] | core.ArrayOut[Attribute] | None = core.arg(default=None)

        lb_port: int | core.IntOut = core.arg()

        load_balancer: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
