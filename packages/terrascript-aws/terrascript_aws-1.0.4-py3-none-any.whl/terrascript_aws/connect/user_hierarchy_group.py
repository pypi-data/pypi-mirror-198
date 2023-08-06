import terrascript.core as core


@core.schema
class LevelFour(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=LevelFour.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class LevelFive(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=LevelFive.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class LevelOne(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=LevelOne.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class LevelTwo(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=LevelTwo.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class LevelThree(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=LevelThree.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class HierarchyPath(core.Schema):

    level_five: list[LevelFive] | core.ArrayOut[LevelFive] = core.attr(
        LevelFive, computed=True, kind=core.Kind.array
    )

    level_four: list[LevelFour] | core.ArrayOut[LevelFour] = core.attr(
        LevelFour, computed=True, kind=core.Kind.array
    )

    level_one: list[LevelOne] | core.ArrayOut[LevelOne] = core.attr(
        LevelOne, computed=True, kind=core.Kind.array
    )

    level_three: list[LevelThree] | core.ArrayOut[LevelThree] = core.attr(
        LevelThree, computed=True, kind=core.Kind.array
    )

    level_two: list[LevelTwo] | core.ArrayOut[LevelTwo] = core.attr(
        LevelTwo, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        level_five: list[LevelFive] | core.ArrayOut[LevelFive],
        level_four: list[LevelFour] | core.ArrayOut[LevelFour],
        level_one: list[LevelOne] | core.ArrayOut[LevelOne],
        level_three: list[LevelThree] | core.ArrayOut[LevelThree],
        level_two: list[LevelTwo] | core.ArrayOut[LevelTwo],
    ):
        super().__init__(
            args=HierarchyPath.Args(
                level_five=level_five,
                level_four=level_four,
                level_one=level_one,
                level_three=level_three,
                level_two=level_two,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        level_five: list[LevelFive] | core.ArrayOut[LevelFive] = core.arg()

        level_four: list[LevelFour] | core.ArrayOut[LevelFour] = core.arg()

        level_one: list[LevelOne] | core.ArrayOut[LevelOne] = core.arg()

        level_three: list[LevelThree] | core.ArrayOut[LevelThree] = core.arg()

        level_two: list[LevelTwo] | core.ArrayOut[LevelTwo] = core.arg()


@core.resource(type="aws_connect_user_hierarchy_group", namespace="connect")
class UserHierarchyGroup(core.Resource):
    """
    The Amazon Resource Name (ARN) of the hierarchy group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier for the hierarchy group.
    """
    hierarchy_group_id: str | core.StringOut = core.attr(str, computed=True)

    """
    A block that contains information about the levels in the hierarchy group. The `hierarchy_path` bloc
    k is documented below.
    """
    hierarchy_path: list[HierarchyPath] | core.ArrayOut[HierarchyPath] = core.attr(
        HierarchyPath, computed=True, kind=core.Kind.array
    )

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the hierarchy group
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    The identifier of the level in the hierarchy group.
    """
    level_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the user hierarchy group. Must not be more than 100 characters.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The identifier for the parent hierarchy group. The user hierarchy is created at level one
    if the parent group ID is null.
    """
    parent_group_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Tags to apply to the hierarchy group. If configured with a provider
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
        parent_group_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserHierarchyGroup.Args(
                instance_id=instance_id,
                name=name,
                parent_group_id=parent_group_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        parent_group_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
