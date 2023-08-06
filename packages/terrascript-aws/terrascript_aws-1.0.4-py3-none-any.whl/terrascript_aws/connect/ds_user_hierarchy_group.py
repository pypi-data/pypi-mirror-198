import terrascript.core as core


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


@core.data(type="aws_connect_user_hierarchy_group", namespace="connect")
class DsUserHierarchyGroup(core.Data):
    """
    The Amazon Resource Name (ARN) of the hierarchy group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific hierarchy group by hierarchy group id
    """
    hierarchy_group_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A block that contains information about the levels in the hierarchy group. The `hierarchy_path` bloc
    k is documented below.
    """
    hierarchy_path: list[HierarchyPath] | core.ArrayOut[HierarchyPath] = core.attr(
        HierarchyPath, computed=True, kind=core.Kind.array
    )

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the hierarchy group separate
    d by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    The identifier of the level in the hierarchy group.
    """
    level_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific hierarchy group by name
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A map of tags to assign to the hierarchy group.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        hierarchy_group_id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUserHierarchyGroup.Args(
                instance_id=instance_id,
                hierarchy_group_id=hierarchy_group_id,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hierarchy_group_id: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
