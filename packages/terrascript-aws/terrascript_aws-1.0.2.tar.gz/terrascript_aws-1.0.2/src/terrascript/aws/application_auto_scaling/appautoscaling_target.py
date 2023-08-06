import terrascript.core as core


@core.resource(type="aws_appautoscaling_target", namespace="aws_application_auto_scaling")
class AppautoscalingTarget(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    max_capacity: int | core.IntOut = core.attr(int)

    min_capacity: int | core.IntOut = core.attr(int)

    resource_id: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    scalable_dimension: str | core.StringOut = core.attr(str)

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
