import terrascript.core as core


@core.resource(type="aws_ssm_service_setting", namespace="ssm")
class ServiceSetting(core.Resource):
    """
    ARN of the service setting.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ID of the service setting.
    """
    setting_id: str | core.StringOut = core.attr(str)

    """
    (Required) Value of the service setting.
    """
    setting_value: str | core.StringOut = core.attr(str)

    """
    Status of the service setting. Value can be `Default`, `Customized` or `PendingUpdate`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        setting_id: str | core.StringOut,
        setting_value: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceSetting.Args(
                setting_id=setting_id,
                setting_value=setting_value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        setting_id: str | core.StringOut = core.arg()

        setting_value: str | core.StringOut = core.arg()
