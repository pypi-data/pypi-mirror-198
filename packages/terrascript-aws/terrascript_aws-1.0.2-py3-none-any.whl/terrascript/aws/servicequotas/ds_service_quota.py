import terrascript.core as core


@core.data(type="aws_servicequotas_service_quota", namespace="aws_servicequotas")
class DsServiceQuota(core.Data):

    adjustable: bool | core.BoolOut = core.attr(bool, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_value: float | core.FloatOut = core.attr(float, computed=True)

    global_quota: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    quota_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    quota_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    service_code: str | core.StringOut = core.attr(str)

    service_name: str | core.StringOut = core.attr(str, computed=True)

    value: float | core.FloatOut = core.attr(float, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        service_code: str | core.StringOut,
        quota_code: str | core.StringOut | None = None,
        quota_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServiceQuota.Args(
                service_code=service_code,
                quota_code=quota_code,
                quota_name=quota_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        quota_code: str | core.StringOut | None = core.arg(default=None)

        quota_name: str | core.StringOut | None = core.arg(default=None)

        service_code: str | core.StringOut = core.arg()
