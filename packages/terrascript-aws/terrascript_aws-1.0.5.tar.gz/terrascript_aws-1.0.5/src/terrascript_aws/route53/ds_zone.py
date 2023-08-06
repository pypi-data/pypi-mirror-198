import terrascript.core as core


@core.data(type="aws_route53_zone", namespace="route53")
class DsZone(core.Data):
    """
    The Amazon Resource Name (ARN) of the Hosted Zone.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Caller Reference of the Hosted Zone.
    """
    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    """
    The comment field of the Hosted Zone.
    """
    comment: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The description provided by the service that created the Hosted Zone (e.g., `arn:aws:servicediscover
    y:us-east-1:1234567890:namespace/ns-xxxxxxxxxxxxxxxx`).
    """
    linked_service_description: str | core.StringOut = core.attr(str, computed=True)

    """
    The service that created the Hosted Zone (e.g., `servicediscovery.amazonaws.com`).
    """
    linked_service_principal: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Hosted Zone name of the desired Hosted Zone.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The list of DNS name servers for the Hosted Zone.
    """
    name_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Used with `name` field to get a private Hosted Zone.
    """
    private_zone: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The number of Record Set in the Hosted Zone.
    """
    resource_record_set_count: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) Used with `name` field. A map of tags, each pair of which must exactly match a pair on th
    e desired Hosted Zone.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Used with `name` field to get a private Hosted Zone associated with the vpc_id (in this c
    ase, private_zone is not mandatory).
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The Hosted Zone id of the desired Hosted Zone.
    """
    zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut | None = None,
        private_zone: bool | core.BoolOut | None = None,
        resource_record_set_count: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
        zone_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsZone.Args(
                name=name,
                private_zone=private_zone,
                resource_record_set_count=resource_record_set_count,
                tags=tags,
                vpc_id=vpc_id,
                zone_id=zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        private_zone: bool | core.BoolOut | None = core.arg(default=None)

        resource_record_set_count: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)

        zone_id: str | core.StringOut | None = core.arg(default=None)
