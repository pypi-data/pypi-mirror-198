import terrascript.core as core


@core.resource(type="aws_redshift_authentication_profile", namespace="aws_redshift")
class AuthenticationProfile(core.Resource):

    authentication_profile_content: str | core.StringOut = core.attr(str)

    authentication_profile_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_profile_content: str | core.StringOut,
        authentication_profile_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AuthenticationProfile.Args(
                authentication_profile_content=authentication_profile_content,
                authentication_profile_name=authentication_profile_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_profile_content: str | core.StringOut = core.arg()

        authentication_profile_name: str | core.StringOut = core.arg()
