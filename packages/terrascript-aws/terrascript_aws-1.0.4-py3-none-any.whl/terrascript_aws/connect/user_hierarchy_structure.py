import terrascript.core as core


@core.schema
class LevelThree(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

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

    name: str | core.StringOut = core.attr(str)

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

    name: str | core.StringOut = core.attr(str)

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

    name: str | core.StringOut = core.attr(str)

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

    name: str | core.StringOut = core.attr(str)

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
class HierarchyStructure(core.Schema):

    level_five: LevelFive | None = core.attr(LevelFive, default=None, computed=True)

    level_four: LevelFour | None = core.attr(LevelFour, default=None, computed=True)

    level_one: LevelOne | None = core.attr(LevelOne, default=None, computed=True)

    level_three: LevelThree | None = core.attr(LevelThree, default=None, computed=True)

    level_two: LevelTwo | None = core.attr(LevelTwo, default=None, computed=True)

    def __init__(
        self,
        *,
        level_five: LevelFive | None = None,
        level_four: LevelFour | None = None,
        level_one: LevelOne | None = None,
        level_three: LevelThree | None = None,
        level_two: LevelTwo | None = None,
    ):
        super().__init__(
            args=HierarchyStructure.Args(
                level_five=level_five,
                level_four=level_four,
                level_one=level_one,
                level_three=level_three,
                level_two=level_two,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        level_five: LevelFive | None = core.arg(default=None)

        level_four: LevelFour | None = core.arg(default=None)

        level_one: LevelOne | None = core.arg(default=None)

        level_three: LevelThree | None = core.arg(default=None)

        level_two: LevelTwo | None = core.arg(default=None)


@core.resource(type="aws_connect_user_hierarchy_structure", namespace="connect")
class UserHierarchyStructure(core.Resource):
    """
    (Required) A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is
    documented below.
    """

    hierarchy_structure: HierarchyStructure = core.attr(HierarchyStructure)

    """
    The identifier of the hosting Amazon Connect Instance.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        hierarchy_structure: HierarchyStructure,
        instance_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserHierarchyStructure.Args(
                hierarchy_structure=hierarchy_structure,
                instance_id=instance_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hierarchy_structure: HierarchyStructure = core.arg()

        instance_id: str | core.StringOut = core.arg()
