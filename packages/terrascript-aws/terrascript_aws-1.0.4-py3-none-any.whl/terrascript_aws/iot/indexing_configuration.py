import terrascript.core as core


@core.schema
class CustomField(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomField.Args(
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ManagedField(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ManagedField.Args(
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ThingGroupIndexingConfiguration(core.Schema):

    custom_field: list[CustomField] | core.ArrayOut[CustomField] | None = core.attr(
        CustomField, default=None, kind=core.Kind.array
    )

    managed_field: list[ManagedField] | core.ArrayOut[ManagedField] | None = core.attr(
        ManagedField, default=None, computed=True, kind=core.Kind.array
    )

    thing_group_indexing_mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        thing_group_indexing_mode: str | core.StringOut,
        custom_field: list[CustomField] | core.ArrayOut[CustomField] | None = None,
        managed_field: list[ManagedField] | core.ArrayOut[ManagedField] | None = None,
    ):
        super().__init__(
            args=ThingGroupIndexingConfiguration.Args(
                thing_group_indexing_mode=thing_group_indexing_mode,
                custom_field=custom_field,
                managed_field=managed_field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_field: list[CustomField] | core.ArrayOut[CustomField] | None = core.arg(default=None)

        managed_field: list[ManagedField] | core.ArrayOut[ManagedField] | None = core.arg(
            default=None
        )

        thing_group_indexing_mode: str | core.StringOut = core.arg()


@core.schema
class ThingIndexingConfiguration(core.Schema):

    custom_field: list[CustomField] | core.ArrayOut[CustomField] | None = core.attr(
        CustomField, default=None, kind=core.Kind.array
    )

    device_defender_indexing_mode: str | core.StringOut | None = core.attr(str, default=None)

    managed_field: list[ManagedField] | core.ArrayOut[ManagedField] | None = core.attr(
        ManagedField, default=None, computed=True, kind=core.Kind.array
    )

    named_shadow_indexing_mode: str | core.StringOut | None = core.attr(str, default=None)

    thing_connectivity_indexing_mode: str | core.StringOut | None = core.attr(str, default=None)

    thing_indexing_mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        thing_indexing_mode: str | core.StringOut,
        custom_field: list[CustomField] | core.ArrayOut[CustomField] | None = None,
        device_defender_indexing_mode: str | core.StringOut | None = None,
        managed_field: list[ManagedField] | core.ArrayOut[ManagedField] | None = None,
        named_shadow_indexing_mode: str | core.StringOut | None = None,
        thing_connectivity_indexing_mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ThingIndexingConfiguration.Args(
                thing_indexing_mode=thing_indexing_mode,
                custom_field=custom_field,
                device_defender_indexing_mode=device_defender_indexing_mode,
                managed_field=managed_field,
                named_shadow_indexing_mode=named_shadow_indexing_mode,
                thing_connectivity_indexing_mode=thing_connectivity_indexing_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_field: list[CustomField] | core.ArrayOut[CustomField] | None = core.arg(default=None)

        device_defender_indexing_mode: str | core.StringOut | None = core.arg(default=None)

        managed_field: list[ManagedField] | core.ArrayOut[ManagedField] | None = core.arg(
            default=None
        )

        named_shadow_indexing_mode: str | core.StringOut | None = core.arg(default=None)

        thing_connectivity_indexing_mode: str | core.StringOut | None = core.arg(default=None)

        thing_indexing_mode: str | core.StringOut = core.arg()


@core.resource(type="aws_iot_indexing_configuration", namespace="iot")
class IndexingConfiguration(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Thing group indexing configuration. See below.
    """
    thing_group_indexing_configuration: ThingGroupIndexingConfiguration | None = core.attr(
        ThingGroupIndexingConfiguration, default=None, computed=True
    )

    """
    (Optional) Thing indexing configuration. See below.
    """
    thing_indexing_configuration: ThingIndexingConfiguration | None = core.attr(
        ThingIndexingConfiguration, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        thing_group_indexing_configuration: ThingGroupIndexingConfiguration | None = None,
        thing_indexing_configuration: ThingIndexingConfiguration | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=IndexingConfiguration.Args(
                thing_group_indexing_configuration=thing_group_indexing_configuration,
                thing_indexing_configuration=thing_indexing_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        thing_group_indexing_configuration: ThingGroupIndexingConfiguration | None = core.arg(
            default=None
        )

        thing_indexing_configuration: ThingIndexingConfiguration | None = core.arg(default=None)
