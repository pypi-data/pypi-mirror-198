import terrascript.core as core


@core.data(type="aws_service", namespace="meta_data_sources")
class DsService(core.Data):
    """
    (Optional) DNS name of the service (_e.g.,_ `rds.us-east-1.amazonaws.com`). One of `dns_name`, `reve
    rse_dns_name`, or `service_id` is required.
    """

    dns_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Partition corresponding to the region.
    """
    partition: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Region of the service (_e.g.,_ `us-west-2`, `ap-northeast-1`).
    """
    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Reverse DNS name of the service (_e.g.,_ `com.amazonaws.us-west-2.s3`). One of `dns_name`
    , `reverse_dns_name`, or `service_id` is required.
    """
    reverse_dns_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Prefix of the service (_e.g.,_ `com.amazonaws` in AWS Commercial, `cn.com.amazonaws` in A
    WS China).
    """
    reverse_dns_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Service (_e.g.,_ `s3`, `rds`, `ec2`). One of `dns_name`, `reverse_dns_name`, or `service_
    id` is required.
    """
    service_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Whether the service is supported in the region's partition. New services may not be listed immediate
    ly as supported.
    """
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
