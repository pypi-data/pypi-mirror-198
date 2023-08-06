import terrascript.core as core


@core.resource(type="aws_securityhub_action_target", namespace="aws_securityhub")
class ActionTarget(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    identifier: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut,
        identifier: str | core.StringOut,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ActionTarget.Args(
                description=description,
                identifier=identifier,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut = core.arg()

        identifier: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
