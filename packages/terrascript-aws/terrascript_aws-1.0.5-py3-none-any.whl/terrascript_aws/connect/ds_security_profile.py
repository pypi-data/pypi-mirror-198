import terrascript.core as core


@core.data(type="aws_connect_security_profile", namespace="connect")
class DsSecurityProfile(core.Data):
    """
    The Amazon Resource Name (ARN) of the Security Profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the description of the Security Profile.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Security Profile separat
    ed by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Returns information on a specific Security Profile by name
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The organization resource identifier for the security profile.
    """
    organization_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies a list of permissions assigned to the security profile.
    """
    permissions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Returns information on a specific Security Profile by Security Profile id
    """
    security_profile_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A map of tags to assign to the Security Profile.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        name: str | core.StringOut | None = None,
        security_profile_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSecurityProfile.Args(
                instance_id=instance_id,
                name=name,
                security_profile_id=security_profile_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        security_profile_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
