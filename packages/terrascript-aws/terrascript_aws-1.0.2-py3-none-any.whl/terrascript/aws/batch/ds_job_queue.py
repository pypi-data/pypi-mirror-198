import terrascript.core as core


@core.schema
class ComputeEnvironmentOrder(core.Schema):

    compute_environment: str | core.StringOut = core.attr(str, computed=True)

    order: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        compute_environment: str | core.StringOut,
        order: int | core.IntOut,
    ):
        super().__init__(
            args=ComputeEnvironmentOrder.Args(
                compute_environment=compute_environment,
                order=order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_environment: str | core.StringOut = core.arg()

        order: int | core.IntOut = core.arg()


@core.data(type="aws_batch_job_queue", namespace="aws_batch")
class DsJobQueue(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    compute_environment_order: list[ComputeEnvironmentOrder] | core.ArrayOut[
        ComputeEnvironmentOrder
    ] = core.attr(ComputeEnvironmentOrder, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    priority: int | core.IntOut = core.attr(int, computed=True)

    scheduling_policy_arn: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    status_reason: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsJobQueue.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
