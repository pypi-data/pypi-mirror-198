import terrascript.core as core


@core.resource(type="aws_ecs_account_setting_default", namespace="ecs")
class AccountSettingDefault(core.Resource):
    """
    ARN that identifies the account setting.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the account setting to set. Valid values are `serviceLongArnFormat`, `taskLongArn
    Format`, `containerInstanceLongArnFormat`, `awsvpcTrunking` and `containerInsights`.
    """
    name: str | core.StringOut = core.attr(str)

    principal_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) State of the setting. Valid values are `enabled` and `disabled`.
    """
    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccountSettingDefault.Args(
                name=name,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()
