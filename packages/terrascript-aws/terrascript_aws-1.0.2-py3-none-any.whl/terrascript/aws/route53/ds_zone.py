import terrascript.core as core


@core.data(type="aws_route53_zone", namespace="aws_route53")
class DsZone(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    comment: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    linked_service_description: str | core.StringOut = core.attr(str, computed=True)

    linked_service_principal: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    private_zone: bool | core.BoolOut | None = core.attr(bool, default=None)

    resource_record_set_count: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
