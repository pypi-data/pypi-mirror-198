import terrascript.core as core


@core.resource(type="aws_appautoscaling_target", namespace="application_auto_scaling")
class AppautoscalingTarget(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The max capacity of the scalable target.
    """
    max_capacity: int | core.IntOut = core.attr(int)

    """
    (Required) The min capacity of the scalable target.
    """
    min_capacity: int | core.IntOut = core.attr(int)

    """
    (Required) The resource type and unique identifier string for the resource associated with the scali
    ng policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scalin
    g API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalab
    leTarget.html#API_RegisterScalableTarget_RequestParameters)
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The ARN of the IAM role that allows Application AutoScaling to modify your scalable targe
    t on your behalf. This defaults to an IAM Service-Linked Role for most services and custom IAM Roles
    are ignored by the API for those namespaces. See the [AWS Application Auto Scaling documentation](h
    ttps://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#secu
    rity_iam_service-with-iam-roles) for more information about how this service interacts with IAM.
    """
    role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The scalable dimension of the scalable target. Documentation can be found in the `Scalabl
    eDimension` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/a
    utoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_Reque
    stParameters)
    """
    scalable_dimension: str | core.StringOut = core.attr(str)

    """
    (Required) The AWS service namespace of the scalable target. Documentation can be found in the `Serv
    iceNamespace` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com
    /autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_Req
    uestParameters)
    """
    service_namespace: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        max_capacity: int | core.IntOut,
        min_capacity: int | core.IntOut,
        resource_id: str | core.StringOut,
        scalable_dimension: str | core.StringOut,
        service_namespace: str | core.StringOut,
        role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppautoscalingTarget.Args(
                max_capacity=max_capacity,
                min_capacity=min_capacity,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                service_namespace=service_namespace,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        max_capacity: int | core.IntOut = core.arg()

        min_capacity: int | core.IntOut = core.arg()

        resource_id: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)

        scalable_dimension: str | core.StringOut = core.arg()

        service_namespace: str | core.StringOut = core.arg()
