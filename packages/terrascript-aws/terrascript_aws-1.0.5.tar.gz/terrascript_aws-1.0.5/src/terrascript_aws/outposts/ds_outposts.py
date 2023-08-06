import terrascript.core as core


@core.data(type="aws_outposts_outposts", namespace="outposts")
class DsOutposts(core.Data):
    """
    Set of Amazon Resource Names (ARNs).
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Availability Zone name.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Availability Zone identifier.
    """
    availability_zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    AWS Region.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of identifiers.
    """
    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) AWS Account identifier of the Outpost owner.
    """
    owner_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Site identifier.
    """
    site_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        availability_zone: str | core.StringOut | None = None,
        availability_zone_id: str | core.StringOut | None = None,
        owner_id: str | core.StringOut | None = None,
        site_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOutposts.Args(
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                owner_id=owner_id,
                site_id=site_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        availability_zone_id: str | core.StringOut | None = core.arg(default=None)

        owner_id: str | core.StringOut | None = core.arg(default=None)

        site_id: str | core.StringOut | None = core.arg(default=None)
