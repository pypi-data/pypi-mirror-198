import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_destination_policy", namespace="aws_cloudwatch")
class LogDestinationPolicy(core.Resource):

    access_policy: str | core.StringOut = core.attr(str)

    destination_name: str | core.StringOut = core.attr(str)

    force_update: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        access_policy: str | core.StringOut,
        destination_name: str | core.StringOut,
        force_update: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogDestinationPolicy.Args(
                access_policy=access_policy,
                destination_name=destination_name,
                force_update=force_update,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policy: str | core.StringOut = core.arg()

        destination_name: str | core.StringOut = core.arg()

        force_update: bool | core.BoolOut | None = core.arg(default=None)
