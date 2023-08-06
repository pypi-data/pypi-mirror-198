import terrascript.core as core


@core.resource(type="aws_elasticache_user_group", namespace="elasticache")
class UserGroup(core.Resource):

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The current supported value is `REDIS`.
    """
    engine: str | core.StringOut = core.attr(str)

    """
    The user group identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The ID of the user group.
    """
    user_group_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The list of user IDs that belong to the user group.
    """
    user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        engine: str | core.StringOut,
        user_group_id: str | core.StringOut,
        arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserGroup.Args(
                engine=engine,
                user_group_id=user_group_id,
                arn=arn,
                tags=tags,
                tags_all=tags_all,
                user_ids=user_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: str | core.StringOut | None = core.arg(default=None)

        engine: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_group_id: str | core.StringOut = core.arg()

        user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
