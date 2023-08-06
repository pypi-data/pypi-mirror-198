import terrascript.core as core


@core.resource(type="aws_connect_security_profile", namespace="connect")
class SecurityProfile(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Security Profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the description of the Security Profile.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Security Profile separat
    ed by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the name of the Security Profile.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The organization resource identifier for the security profile.
    """
    organization_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies a list of permissions assigned to the security profile.
    """
    permissions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The identifier for the Security Profile.
    """
    security_profile_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Tags to apply to the Security Profile. If configured with a provider
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        instance_id: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        permissions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecurityProfile.Args(
                instance_id=instance_id,
                name=name,
                description=description,
                permissions=permissions,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        permissions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
