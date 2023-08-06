import terrascript.core as core


@core.schema
class FieldSelector(core.Schema):

    ends_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    equals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    field: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    not_ends_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    not_equals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    not_starts_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    starts_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ends_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
        equals: list[str] | core.ArrayOut[core.StringOut] | None = None,
        field: str | core.StringOut | None = None,
        not_ends_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
        not_equals: list[str] | core.ArrayOut[core.StringOut] | None = None,
        not_starts_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
        starts_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=FieldSelector.Args(
                ends_with=ends_with,
                equals=equals,
                field=field,
                not_ends_with=not_ends_with,
                not_equals=not_equals,
                not_starts_with=not_starts_with,
                starts_with=starts_with,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ends_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        equals: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        field: str | core.StringOut | None = core.arg(default=None)

        not_ends_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        not_equals: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        not_starts_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        starts_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AdvancedEventSelector(core.Schema):

    field_selector: list[FieldSelector] | core.ArrayOut[FieldSelector] | None = core.attr(
        FieldSelector, default=None, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        field_selector: list[FieldSelector] | core.ArrayOut[FieldSelector] | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AdvancedEventSelector.Args(
                field_selector=field_selector,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_selector: list[FieldSelector] | core.ArrayOut[FieldSelector] | None = core.arg(
            default=None
        )

        name: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_cloudtrail_event_data_store", namespace="cloudtrail")
class EventDataStore(core.Resource):

    advanced_event_selector: list[AdvancedEventSelector] | core.ArrayOut[
        AdvancedEventSelector
    ] | None = core.attr(AdvancedEventSelector, default=None, computed=True, kind=core.Kind.array)

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    multi_region_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut = core.attr(str)

    organization_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    retention_period: int | core.IntOut | None = core.attr(int, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    termination_protection_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        advanced_event_selector: list[AdvancedEventSelector]
        | core.ArrayOut[AdvancedEventSelector]
        | None = None,
        multi_region_enabled: bool | core.BoolOut | None = None,
        organization_enabled: bool | core.BoolOut | None = None,
        retention_period: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        termination_protection_enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventDataStore.Args(
                name=name,
                advanced_event_selector=advanced_event_selector,
                multi_region_enabled=multi_region_enabled,
                organization_enabled=organization_enabled,
                retention_period=retention_period,
                tags=tags,
                tags_all=tags_all,
                termination_protection_enabled=termination_protection_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        advanced_event_selector: list[AdvancedEventSelector] | core.ArrayOut[
            AdvancedEventSelector
        ] | None = core.arg(default=None)

        multi_region_enabled: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        organization_enabled: bool | core.BoolOut | None = core.arg(default=None)

        retention_period: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        termination_protection_enabled: bool | core.BoolOut | None = core.arg(default=None)
