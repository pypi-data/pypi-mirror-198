import terrascript.core as core


@core.resource(type="aws_redshift_snapshot_schedule", namespace="aws_redshift")
class SnapshotSchedule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    definitions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    description: str | core.StringOut | None = core.attr(str, default=None)

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    identifier_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
