import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_availability_zones", namespace="aws_ec2")
class DsAvailabilityZones(core.Data):

    all_availability_zones: bool | core.BoolOut | None = core.attr(bool, default=None)

    exclude_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    exclude_zone_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    group_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    state: str | core.StringOut | None = core.attr(str, default=None)

    zone_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        all_availability_zones: bool | core.BoolOut | None = None,
        exclude_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        exclude_zone_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        state: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAvailabilityZones.Args(
                all_availability_zones=all_availability_zones,
                exclude_names=exclude_names,
                exclude_zone_ids=exclude_zone_ids,
                filter=filter,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_availability_zones: bool | core.BoolOut | None = core.arg(default=None)

        exclude_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        exclude_zone_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)
