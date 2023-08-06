import terrascript.core as core


@core.resource(type="aws_shield_protection_group", namespace="shield")
class ProtectionGroup(core.Resource):
    """
    (Required) Defines how AWS Shield combines resource data for the group in order to detect, mitigate,
    and report events.
    """

    aggregation: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Names (ARNs) of the resources to include in the protection group. You
    must set this when you set `pattern` to ARBITRARY and you must not set it for any other `pattern` s
    etting.
    """
    members: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The criteria to use to choose the protected resources for inclusion in the group.
    """
    pattern: str | core.StringOut = core.attr(str)

    """
    The ARN (Amazon Resource Name) of the protection group.
    """
    protection_group_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the protection group.
    """
    protection_group_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The resource type to include in the protection group. You must set this when you set `pat
    tern` to BY_RESOURCE_TYPE and you must not set it for any other `pattern` setting.
    """
    resource_type: str | core.StringOut | None = core.attr(str, default=None)

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

    def __init__(
        self,
        resource_name: str,
        *,
        aggregation: str | core.StringOut,
        pattern: str | core.StringOut,
        protection_group_id: str | core.StringOut,
        members: list[str] | core.ArrayOut[core.StringOut] | None = None,
        resource_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProtectionGroup.Args(
                aggregation=aggregation,
                pattern=pattern,
                protection_group_id=protection_group_id,
                members=members,
                resource_type=resource_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aggregation: str | core.StringOut = core.arg()

        members: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        pattern: str | core.StringOut = core.arg()

        protection_group_id: str | core.StringOut = core.arg()

        resource_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
