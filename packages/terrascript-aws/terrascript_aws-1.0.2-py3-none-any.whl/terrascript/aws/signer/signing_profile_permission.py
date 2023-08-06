import terrascript.core as core


@core.resource(type="aws_signer_signing_profile_permission", namespace="aws_signer")
class SigningProfilePermission(core.Resource):

    action: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    principal: str | core.StringOut = core.attr(str)

    profile_name: str | core.StringOut = core.attr(str)

    profile_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    statement_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    statement_id_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        action: str | core.StringOut,
        principal: str | core.StringOut,
        profile_name: str | core.StringOut,
        profile_version: str | core.StringOut | None = None,
        statement_id: str | core.StringOut | None = None,
        statement_id_prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SigningProfilePermission.Args(
                action=action,
                principal=principal,
                profile_name=profile_name,
                profile_version=profile_version,
                statement_id=statement_id,
                statement_id_prefix=statement_id_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: str | core.StringOut = core.arg()

        principal: str | core.StringOut = core.arg()

        profile_name: str | core.StringOut = core.arg()

        profile_version: str | core.StringOut | None = core.arg(default=None)

        statement_id: str | core.StringOut | None = core.arg(default=None)

        statement_id_prefix: str | core.StringOut | None = core.arg(default=None)
