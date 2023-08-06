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


@core.data(type="aws_availability_zone", namespace="aws_ec2")
class DsAvailabilityZone(core.Data):

    all_availability_zones: bool | core.BoolOut | None = core.attr(bool, default=None)

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    group_name: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_suffix: str | core.StringOut = core.attr(str, computed=True)

    network_border_group: str | core.StringOut = core.attr(str, computed=True)

    opt_in_status: str | core.StringOut = core.attr(str, computed=True)

    parent_zone_id: str | core.StringOut = core.attr(str, computed=True)

    parent_zone_name: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    zone_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        all_availability_zones: bool | core.BoolOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        name: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        zone_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAvailabilityZone.Args(
                all_availability_zones=all_availability_zones,
                filter=filter,
                name=name,
                state=state,
                zone_id=zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_availability_zones: bool | core.BoolOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        zone_id: str | core.StringOut | None = core.arg(default=None)
