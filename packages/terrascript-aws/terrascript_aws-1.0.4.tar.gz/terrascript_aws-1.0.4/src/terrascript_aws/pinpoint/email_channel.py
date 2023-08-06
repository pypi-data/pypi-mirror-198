import terrascript.core as core


@core.resource(type="aws_pinpoint_email_channel", namespace="pinpoint")
class EmailChannel(core.Resource):

    application_id: str | core.StringOut = core.attr(str)

    configuration_set: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    from_address: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity: str | core.StringOut = core.attr(str)

    messages_per_second: int | core.IntOut = core.attr(int, computed=True)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: str | core.StringOut,
        from_address: str | core.StringOut,
        identity: str | core.StringOut,
        configuration_set: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EmailChannel.Args(
                application_id=application_id,
                from_address=from_address,
                identity=identity,
                configuration_set=configuration_set,
                enabled=enabled,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        configuration_set: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        from_address: str | core.StringOut = core.arg()

        identity: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)
