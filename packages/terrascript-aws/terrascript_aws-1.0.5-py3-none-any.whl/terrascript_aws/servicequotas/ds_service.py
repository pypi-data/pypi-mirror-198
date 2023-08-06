import terrascript.core as core


@core.data(type="aws_servicequotas_service", namespace="servicequotas")
class DsService(core.Data):
    """
    Code of the service.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Code of the service.
    """
    service_code: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Service name to lookup within Service Quotas. Available values can be found with the [AWS
    CLI service-quotas list-services command](https://docs.aws.amazon.com/cli/latest/reference/service-
    quotas/list-services.html).
    """
    service_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        service_name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsService.Args(
                service_name=service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        service_name: str | core.StringOut = core.arg()
