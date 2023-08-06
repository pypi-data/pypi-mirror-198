import terrascript.core as core


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
class HierarchyStructure(core.Schema):

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
        level_five: list[LevelFive] | core.ArrayOut[LevelFive] = core.arg()

        level_four: list[LevelFour] | core.ArrayOut[LevelFour] = core.arg()

        level_one: list[LevelOne] | core.ArrayOut[LevelOne] = core.arg()

        level_three: list[LevelThree] | core.ArrayOut[LevelThree] = core.arg()

        level_two: list[LevelTwo] | core.ArrayOut[LevelTwo] = core.arg()


@core.data(type="aws_connect_user_hierarchy_structure", namespace="connect")
class DsUserHierarchyStructure(core.Data):
    """
    A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is documented
    below.
    """

    hierarchy_structure: list[HierarchyStructure] | core.ArrayOut[HierarchyStructure] = core.attr(
        HierarchyStructure, computed=True, kind=core.Kind.array
    )

    """
    The identifier of the hierarchy level.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsUserHierarchyStructure.Args(
                instance_id=instance_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: str | core.StringOut = core.arg()
