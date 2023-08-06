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


@core.data(type="aws_availability_zones", namespace="ec2")
class DsAvailabilityZones(core.Data):
    """
    (Optional) Set to `true` to include all Availability Zones and Local Zones regardless of your opt in
    status.
    """

    all_availability_zones: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) List of Availability Zone names to exclude.
    """
    exclude_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) List of Availability Zone IDs to exclude.
    """
    exclude_zone_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    group_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Region of the Availability Zones.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of the Availability Zone names available to the account.
    """
    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Allows to filter list of Availability Zones based on their
    """
    state: str | core.StringOut | None = core.attr(str, default=None)

    """
    A list of the Availability Zone IDs available to the account.
    """
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
