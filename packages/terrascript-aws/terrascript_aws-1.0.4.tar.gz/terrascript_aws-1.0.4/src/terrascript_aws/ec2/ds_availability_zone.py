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


@core.data(type="aws_availability_zone", namespace="ec2")
class DsAvailabilityZone(core.Data):
    """
    (Optional) Set to `true` to include all Availability Zones and Local Zones regardless of your opt in
    status.
    """

    all_availability_zones: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    For Availability Zones, this is the same value as the Region name. For Local Zones, the name of the
    associated group, for example `us-west-2-lax-1`.
    """
    group_name: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The full name of the availability zone to select.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The part of the AZ name that appears after the region name, uniquely identifying the AZ within its r
    egion.
    """
    name_suffix: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the location from which the address is advertised.
    """
    network_border_group: str | core.StringOut = core.attr(str, computed=True)

    """
    For Availability Zones, this always has the value of `opt-in-not-required`. For Local Zones, this is
    the opt in status. The possible values are `opted-in` and `not-opted-in`.
    """
    opt_in_status: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the zone that handles some of the Local Zone or Wavelength Zone control plane operations,
    such as API calls.
    """
    parent_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the zone that handles some of the Local Zone or Wavelength Zone control plane operations
    , such as API calls.
    """
    parent_zone_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The region where the selected availability zone resides. This is always the region selected on the p
    rovider, since this data source searches only within that region.
    """
    region: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A specific availability zone state to require. May be any of `"available"`, `"information
    "` or `"impaired"`.
    """
    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The zone ID of the availability zone to select.
    """
    zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The type of zone. Values are `availability-zone`, `local-zone`, and `wavelength-zone`.
    """
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
