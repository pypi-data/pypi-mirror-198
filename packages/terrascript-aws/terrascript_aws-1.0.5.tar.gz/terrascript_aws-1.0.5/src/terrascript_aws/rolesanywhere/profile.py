import terrascript.core as core


@core.resource(type="aws_rolesanywhere_profile", namespace="rolesanywhere")
class Profile(core.Resource):
    """
    Amazon Resource Name (ARN) of the Profile
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The number of seconds the vended session credentials are valid for. Defaults to 3600.
    """
    duration_seconds: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Whether or not the Profile is enabled.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Profile ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of managed policy ARNs that apply to the vended session credentials.
    """
    managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The name of the Profile.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies whether instance properties are required in [CreateSession](https://docs.aws.am
    azon.com/rolesanywhere/latest/APIReference/API_CreateSession.html) requests with this profile.
    """
    require_instance_properties: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) A list of IAM roles that this profile can assume
    """
    role_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) A session policy that applies to the trust boundary of the vended session credentials.
    """
    session_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
        name: str | core.StringOut,
        role_arns: list[str] | core.ArrayOut[core.StringOut],
        duration_seconds: int | core.IntOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        require_instance_properties: bool | core.BoolOut | None = None,
        session_policy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Profile.Args(
                name=name,
                role_arns=role_arns,
                duration_seconds=duration_seconds,
                enabled=enabled,
                managed_policy_arns=managed_policy_arns,
                require_instance_properties=require_instance_properties,
                session_policy=session_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        duration_seconds: int | core.IntOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        require_instance_properties: bool | core.BoolOut | None = core.arg(default=None)

        role_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        session_policy: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
