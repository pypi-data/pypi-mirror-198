import terrascript.core as core


@core.data(type="aws_servicequotas_service_quota", namespace="servicequotas")
class DsServiceQuota(core.Data):
    """
    Whether the service quota is adjustable.
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
    Whether the service quota is global for the AWS account.
    """
    global_quota: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Amazon Resource Name (ARN) of the service quota.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Quota code within the service. When configured, the data source directly looks up the ser
    vice quota. Available values can be found with the [AWS CLI service-quotas list-service-quotas comma
    nd](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html). One o
    f `quota_code` or `quota_name` must be specified.
    """
    quota_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Quota name within the service. When configured, the data source searches through all serv
    ice quotas to find the matching quota name. Available values can be found with the [AWS CLI service-
    quotas list-service-quotas command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/
    list-service-quotas.html). One of `quota_name` or `quota_code` must be specified.
    """
    quota_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Service code for the quota. Available values can be found with the [`aws_servicequotas_se
    rvice` data source](/docs/providers/aws/d/servicequotas_service.html) or [AWS CLI service-quotas lis
    t-services command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.ht
    ml).
    """
    service_code: str | core.StringOut = core.attr(str)

    """
    Name of the service.
    """
    service_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Current value of the service quota.
    """
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
