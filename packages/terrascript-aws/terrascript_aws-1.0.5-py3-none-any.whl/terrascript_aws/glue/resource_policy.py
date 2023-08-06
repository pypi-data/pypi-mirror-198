import terrascript.core as core


@core.resource(type="aws_glue_resource_policy", namespace="glue")
class ResourcePolicy(core.Resource):
    """
    (Optional) Indicates that you are using both methods to grant cross-account. Valid values are `TRUE`
    and `FALSE`. Note the terraform will not perform drift detetction on this field as its not return o
    n read.
    """

    enable_hybrid: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        enable_hybrid: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourcePolicy.Args(
                policy=policy,
                enable_hybrid=enable_hybrid,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enable_hybrid: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut = core.arg()
