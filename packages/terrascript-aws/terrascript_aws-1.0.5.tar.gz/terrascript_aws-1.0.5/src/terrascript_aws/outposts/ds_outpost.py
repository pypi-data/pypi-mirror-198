import terrascript.core as core


@core.data(type="aws_outposts_outpost", namespace="outposts")
class DsOutpost(core.Data):
    """
    (Optional) Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Availability Zone name.
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    Availability Zone identifier.
    """
    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Description.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Identifier of the Outpost.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the Outpost.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) AWS Account identifier of the Outpost owner.
    """
    owner_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Site identifier.
    """
    site_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        owner_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOutpost.Args(
                arn=arn,
                id=id,
                name=name,
                owner_id=owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        owner_id: str | core.StringOut | None = core.arg(default=None)
