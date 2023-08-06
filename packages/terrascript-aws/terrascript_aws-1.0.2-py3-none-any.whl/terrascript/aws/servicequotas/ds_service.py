import terrascript.core as core


@core.data(type="aws_servicequotas_service", namespace="aws_servicequotas")
class DsService(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    service_code: str | core.StringOut = core.attr(str, computed=True)

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
