import terrascript.core as core


@core.resource(type="aws_servicequotas_service_quota", namespace="aws_servicequotas")
class ServiceQuota(core.Resource):

    adjustable: bool | core.BoolOut = core.attr(bool, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_value: float | core.FloatOut = core.attr(float, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    quota_code: str | core.StringOut = core.attr(str)

    quota_name: str | core.StringOut = core.attr(str, computed=True)

    request_id: str | core.StringOut = core.attr(str, computed=True)

    request_status: str | core.StringOut = core.attr(str, computed=True)

    service_code: str | core.StringOut = core.attr(str)

    service_name: str | core.StringOut = core.attr(str, computed=True)

    value: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        resource_name: str,
        *,
        quota_code: str | core.StringOut,
        service_code: str | core.StringOut,
        value: float | core.FloatOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceQuota.Args(
                quota_code=quota_code,
                service_code=service_code,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        quota_code: str | core.StringOut = core.arg()

        service_code: str | core.StringOut = core.arg()

        value: float | core.FloatOut = core.arg()
