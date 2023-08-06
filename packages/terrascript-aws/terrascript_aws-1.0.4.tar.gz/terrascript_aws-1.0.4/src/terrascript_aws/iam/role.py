import terrascript.core as core


@core.schema
class InlinePolicy(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    policy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InlinePolicy.Args(
                name=name,
                policy=policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_iam_role", namespace="iam")
class Role(core.Resource):
    """
    Amazon Resource Name (ARN) specifying the role.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Policy that grants an entity permission to assume the role.
    """
    assume_role_policy: str | core.StringOut = core.attr(str)

    """
    Creation date of the IAM role.
    """
    create_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the role.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether to force detaching any policies the role has before destroying it. Defaults to `f
    alse`.
    """
    force_detach_policies: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Name of the role.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block defining an exclusive set of IAM inline policies associated with the
    IAM role. See below. If no blocks are configured, Terraform will not manage any inline policies in t
    his resource. Configuring one empty block (i.e., `inline_policy {}`) will cause Terraform to remove
    _all_ inline policies added out of band on `apply`.
    """
    inline_policy: list[InlinePolicy] | core.ArrayOut[InlinePolicy] | None = core.attr(
        InlinePolicy, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Set of exclusive IAM managed policy ARNs to attach to the IAM role. If this attribute is
    not configured, Terraform will ignore policy attachments to this resource. When configured, Terrafor
    m will align the role's managed policy attachments with this set by attaching or detaching managed p
    olicies. Configuring an empty set (i.e., `managed_policy_arns = []`) will cause Terraform to remove
    _all_ managed policy attachments.
    """
    managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Maximum session duration (in seconds) that you want to set for the specified role. If you
    do not specify a value for this setting, the default maximum of one hour is applied. This setting c
    an have a value from 1 hour to 12 hours.
    """
    max_session_duration: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Forces new resource) Friendly name of the role. If omitted, Terraform will assign a rando
    m, unique name. See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identif
    iers.html) for more information.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique friendly name beginning with the specified prefix.
    Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Path to the role. See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/
    Using_Identifiers.html) for more information.
    """
    path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) ARN of the policy that is used to set the permissions boundary for the role.
    """
    permissions_boundary: str | core.StringOut | None = core.attr(str, default=None)

    """
    Key-value mapping of tags for the IAM role. If configured with a provider [`default_tags` configurat
    ion block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurat
    ion-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    Stable and unique string identifying the role.
    """
    unique_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        assume_role_policy: str | core.StringOut,
        description: str | core.StringOut | None = None,
        force_detach_policies: bool | core.BoolOut | None = None,
        inline_policy: list[InlinePolicy] | core.ArrayOut[InlinePolicy] | None = None,
        managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        max_session_duration: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
        permissions_boundary: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Role.Args(
                assume_role_policy=assume_role_policy,
                description=description,
                force_detach_policies=force_detach_policies,
                inline_policy=inline_policy,
                managed_policy_arns=managed_policy_arns,
                max_session_duration=max_session_duration,
                name=name,
                name_prefix=name_prefix,
                path=path,
                permissions_boundary=permissions_boundary,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        assume_role_policy: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        force_detach_policies: bool | core.BoolOut | None = core.arg(default=None)

        inline_policy: list[InlinePolicy] | core.ArrayOut[InlinePolicy] | None = core.arg(
            default=None
        )

        managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        max_session_duration: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        permissions_boundary: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
