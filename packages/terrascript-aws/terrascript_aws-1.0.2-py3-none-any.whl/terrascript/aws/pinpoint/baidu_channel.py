import terrascript.core as core


@core.resource(type="aws_pinpoint_baidu_channel", namespace="aws_pinpoint")
class BaiduChannel(core.Resource):
    """
    (Required) Platform credential API key from Baidu.
    """

    api_key: str | core.StringOut = core.attr(str)

    """
    (Required) The application ID.
    """
    application_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies whether to enable the channel. Defaults to `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Platform credential Secret key from Baidu.
    """
    secret_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_key: str | core.StringOut,
        application_id: str | core.StringOut,
        secret_key: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BaiduChannel.Args(
                api_key=api_key,
                application_id=application_id,
                secret_key=secret_key,
                enabled=enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key: str | core.StringOut = core.arg()

        application_id: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        secret_key: str | core.StringOut = core.arg()
