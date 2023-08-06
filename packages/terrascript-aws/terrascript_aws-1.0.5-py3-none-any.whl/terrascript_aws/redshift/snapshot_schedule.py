import terrascript.core as core


@core.resource(type="aws_redshift_snapshot_schedule", namespace="redshift")
class SnapshotSchedule(core.Resource):
    """
    Amazon Resource Name (ARN) of the Redshift Snapshot Schedule.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The definition of the snapshot schedule. The definition is made up of schedule expression
    s, for example `cron(30 12 *)` or `rate(12 hours)`.
    """
    definitions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) The description of the snapshot schedule.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether to destroy all associated clusters with this snapshot schedule on deletion. Must
    be enabled and applied before attempting deletion.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The snapshot schedule identifier. If omitted, Terraform will assign
    a random, unique identifier.
    """
    identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique
    """
    identifier_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
        definitions: list[str] | core.ArrayOut[core.StringOut],
        description: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        identifier: str | core.StringOut | None = None,
        identifier_prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SnapshotSchedule.Args(
                definitions=definitions,
                description=description,
                force_destroy=force_destroy,
                identifier=identifier,
                identifier_prefix=identifier_prefix,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        definitions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        identifier: str | core.StringOut | None = core.arg(default=None)

        identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
