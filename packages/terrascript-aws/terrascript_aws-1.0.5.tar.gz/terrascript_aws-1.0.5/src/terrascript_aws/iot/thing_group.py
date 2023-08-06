import terrascript.core as core


@core.schema
class RootToParentGroups(core.Schema):

    group_arn: str | core.StringOut = core.attr(str, computed=True)

    group_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        group_arn: str | core.StringOut,
        group_name: str | core.StringOut,
    ):
        super().__init__(
            args=RootToParentGroups.Args(
                group_arn=group_arn,
                group_name=group_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_arn: str | core.StringOut = core.arg()

        group_name: str | core.StringOut = core.arg()


@core.schema
class Metadata(core.Schema):

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    parent_group_name: str | core.StringOut = core.attr(str, computed=True)

    root_to_parent_groups: list[RootToParentGroups] | core.ArrayOut[RootToParentGroups] = core.attr(
        RootToParentGroups, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        creation_date: str | core.StringOut,
        parent_group_name: str | core.StringOut,
        root_to_parent_groups: list[RootToParentGroups] | core.ArrayOut[RootToParentGroups],
    ):
        super().__init__(
            args=Metadata.Args(
                creation_date=creation_date,
                parent_group_name=parent_group_name,
                root_to_parent_groups=root_to_parent_groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        creation_date: str | core.StringOut = core.arg()

        parent_group_name: str | core.StringOut = core.arg()

        root_to_parent_groups: list[RootToParentGroups] | core.ArrayOut[
            RootToParentGroups
        ] = core.arg()


@core.schema
class AttributePayload(core.Schema):

    attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        attributes: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AttributePayload.Args(
                attributes=attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Properties(core.Schema):

    attribute_payload: AttributePayload | None = core.attr(AttributePayload, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        attribute_payload: AttributePayload | None = None,
        description: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Properties.Args(
                attribute_payload=attribute_payload,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute_payload: AttributePayload | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_iot_thing_group", namespace="iot")
class ThingGroup(core.Resource):
    """
    The ARN of the Thing Group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Thing Group ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    metadata: list[Metadata] | core.ArrayOut[Metadata] = core.attr(
        Metadata, computed=True, kind=core.Kind.array
    )

    """
    (Required) The name of the Thing Group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of the parent Thing Group.
    """
    parent_group_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The Thing Group properties. Defined below.
    """
    properties: Properties | None = core.attr(Properties, default=None)

    """
    (Optional) Key-value mapping of resource tags
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The current version of the Thing Group record in the registry.
    """
    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        parent_group_name: str | core.StringOut | None = None,
        properties: Properties | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ThingGroup.Args(
                name=name,
                parent_group_name=parent_group_name,
                properties=properties,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        parent_group_name: str | core.StringOut | None = core.arg(default=None)

        properties: Properties | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
