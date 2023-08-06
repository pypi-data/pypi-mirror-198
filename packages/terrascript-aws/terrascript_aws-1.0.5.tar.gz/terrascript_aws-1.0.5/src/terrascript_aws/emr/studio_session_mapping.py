import terrascript.core as core


@core.resource(type="aws_emr_studio_session_mapping", namespace="emr")
class StudioSessionMapping(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The name of the user or group from the Amazon Web Services SSO Identity Store.
    """
    identity_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Specifies whether the identity to map to the Amazon EMR Studio is a `USER` or a `GROUP`.
    """
    identity_type: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) for the session policy that will be applied to the user or
    group. You should specify the ARN for the session policy that you want to apply, not the ARN of you
    r user role.
    """
    session_policy_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the Amazon EMR Studio to which the user or group will be mapped.
    """
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
