import terrascript.core as core


@core.resource(type="aws_amplify_webhook", namespace="amplify")
class Webhook(core.Resource):
    """
    (Required) The unique ID for an Amplify app.
    """

    app_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) for the webhook.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for a branch that is part of the Amplify app.
    """
    branch_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The description for a webhook.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The URL of the webhook.
    """
    url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        app_id: str | core.StringOut,
        branch_name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Webhook.Args(
                app_id=app_id,
                branch_name=branch_name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_id: str | core.StringOut = core.arg()

        branch_name: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)
