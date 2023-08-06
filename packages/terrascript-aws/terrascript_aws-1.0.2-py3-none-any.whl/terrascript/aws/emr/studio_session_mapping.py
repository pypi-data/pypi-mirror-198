import terrascript.core as core


@core.resource(type="aws_emr_studio_session_mapping", namespace="aws_emr")
class StudioSessionMapping(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    identity_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    identity_type: str | core.StringOut = core.attr(str)

    session_policy_arn: str | core.StringOut = core.attr(str)

    studio_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        identity_type: str | core.StringOut,
        session_policy_arn: str | core.StringOut,
        studio_id: str | core.StringOut,
        identity_id: str | core.StringOut | None = None,
        identity_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StudioSessionMapping.Args(
                identity_type=identity_type,
                session_policy_arn=session_policy_arn,
                studio_id=studio_id,
                identity_id=identity_id,
                identity_name=identity_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity_id: str | core.StringOut | None = core.arg(default=None)

        identity_name: str | core.StringOut | None = core.arg(default=None)

        identity_type: str | core.StringOut = core.arg()

        session_policy_arn: str | core.StringOut = core.arg()

        studio_id: str | core.StringOut = core.arg()
