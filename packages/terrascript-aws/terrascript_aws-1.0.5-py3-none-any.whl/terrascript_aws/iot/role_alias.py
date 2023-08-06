import terrascript.core as core


@core.resource(type="aws_iot_role_alias", namespace="iot")
class RoleAlias(core.Resource):
    """
    (Required) The name of the role alias.
    """

    alias: str | core.StringOut = core.attr(str)

    """
    The ARN assigned by AWS to this role alias.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The duration of the credential, in seconds. If you do not specify a value for this settin
    g, the default maximum of one hour is applied. This setting can have a value from 900 seconds (15 mi
    nutes) to 43200 seconds (12 hours).
    """
    credential_duration: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identity of the role to which the alias refers.
    """
    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        alias: str | core.StringOut,
        role_arn: str | core.StringOut,
        credential_duration: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoleAlias.Args(
                alias=alias,
                role_arn=role_arn,
                credential_duration=credential_duration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alias: str | core.StringOut = core.arg()

        credential_duration: int | core.IntOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()
