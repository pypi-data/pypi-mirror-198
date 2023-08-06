import terrascript.core as core


@core.resource(type="aws_app_cookie_stickiness_policy", namespace="aws_elb_classic")
class AppCookieStickinessPolicy(core.Resource):

    cookie_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    lb_port: int | core.IntOut = core.attr(int)

    load_balancer: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cookie_name: str | core.StringOut,
        lb_port: int | core.IntOut,
        load_balancer: str | core.StringOut,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppCookieStickinessPolicy.Args(
                cookie_name=cookie_name,
                lb_port=lb_port,
                load_balancer=load_balancer,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cookie_name: str | core.StringOut = core.arg()

        lb_port: int | core.IntOut = core.arg()

        load_balancer: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
