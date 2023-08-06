import terrascript.core as core


@core.resource(type="aws_organizations_policy", namespace="organizations")
class Policy(core.Resource):
    """
    Amazon Resource Name (ARN) of the policy.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The policy content to add to the new policy. For example, if you create a [service contro
    l policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.
    html), this string must be JSON text that specifies the permissions that admins in attached accounts
    can delegate to their users, groups, and roles. For more information about the SCP syntax, see the
    [Service Control Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userg
    uide/orgs_reference_scp-syntax.html) and for more information on the Tag Policy syntax, see the [Tag
    Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage
    _policies_example-tag-policies.html).
    """
    content: str | core.StringOut = core.attr(str)

    """
    (Optional) A description to assign to the policy.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The unique identifier (ID) of the policy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The friendly name to assign to the policy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) The type of policy to create. Valid values are `AISERVICES_OPT_OUT_POLICY`, `BACKUP_POLIC
    Y`, `SERVICE_CONTROL_POLICY` (SCP), and `TAG_POLICY`. Defaults to `SERVICE_CONTROL_POLICY`.
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        content: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Policy.Args(
                content=content,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
