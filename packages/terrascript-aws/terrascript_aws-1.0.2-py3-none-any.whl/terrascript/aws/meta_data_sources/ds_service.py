import terrascript.core as core


@core.data(type="aws_service", namespace="aws_meta_data_sources")
class DsService(core.Data):

    dns_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    partition: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    reverse_dns_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    reverse_dns_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    service_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    supported: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        dns_name: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
        reverse_dns_name: str | core.StringOut | None = None,
        reverse_dns_prefix: str | core.StringOut | None = None,
        service_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsService.Args(
                dns_name=dns_name,
                region=region,
                reverse_dns_name=reverse_dns_name,
                reverse_dns_prefix=reverse_dns_prefix,
                service_id=service_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        reverse_dns_name: str | core.StringOut | None = core.arg(default=None)

        reverse_dns_prefix: str | core.StringOut | None = core.arg(default=None)

        service_id: str | core.StringOut | None = core.arg(default=None)
