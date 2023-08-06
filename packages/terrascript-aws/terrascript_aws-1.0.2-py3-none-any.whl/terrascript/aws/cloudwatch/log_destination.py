import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_destination", namespace="aws_cloudwatch")
class LogDestination(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    target_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        target_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogDestination.Args(
                name=name,
                role_arn=role_arn,
                target_arn=target_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        target_arn: str | core.StringOut = core.arg()
