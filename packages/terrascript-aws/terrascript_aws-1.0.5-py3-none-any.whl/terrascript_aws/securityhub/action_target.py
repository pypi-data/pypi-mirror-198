import terrascript.core as core


@core.resource(type="aws_securityhub_action_target", namespace="securityhub")
class ActionTarget(core.Resource):
    """
    Amazon Resource Name (ARN) of the Security Hub custom action target.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the custom action target.
    """
    description: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID for the custom action target.
    """
    identifier: str | core.StringOut = core.attr(str)

    """
    (Required) The description for the custom action target.
    """
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
