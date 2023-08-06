import terrascript.core as core


@core.resource(type="aws_servicequotas_service_quota", namespace="servicequotas")
class ServiceQuota(core.Resource):
    """
    Whether the service quota can be increased.
    """

    adjustable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Amazon Resource Name (ARN) of the service quota.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Default value of the service quota.
    """
    default_value: float | core.FloatOut = core.attr(float, computed=True)

    """
    Service code and quota code, separated by a front slash (`/`)
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Code of the service quota to track. For example: `L-F678F1CE`. Available values can be fo
    und with the [AWS CLI service-quotas list-service-quotas command](https://docs.aws.amazon.com/cli/la
    test/reference/service-quotas/list-service-quotas.html).
    """
    quota_code: str | core.StringOut = core.attr(str)

    """
    Name of the quota.
    """
    quota_name: str | core.StringOut = core.attr(str, computed=True)

    request_id: str | core.StringOut = core.attr(str, computed=True)

    request_status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Code of the service to track. For example: `vpc`. Available values can be found with the
    [AWS CLI service-quotas list-services command](https://docs.aws.amazon.com/cli/latest/reference/serv
    ice-quotas/list-services.html).
    """
    service_code: str | core.StringOut = core.attr(str)

    """
    Name of the service.
    """
    service_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Float specifying the desired value for the service quota. If the desired value is higher
    than the current value, a quota increase request is submitted. When a known request is submitted and
    pending, the value reflects the desired value of the pending request.
    """
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
