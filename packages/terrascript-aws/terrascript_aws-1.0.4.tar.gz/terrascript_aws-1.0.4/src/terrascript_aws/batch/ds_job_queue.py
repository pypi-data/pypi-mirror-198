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


@core.data(type="aws_batch_job_queue", namespace="batch")
class DsJobQueue(core.Data):
    """
    The ARN of the job queue.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The compute environments that are attached to the job queue and the order in
    """
    compute_environment_order: list[ComputeEnvironmentOrder] | core.ArrayOut[
        ComputeEnvironmentOrder
    ] = core.attr(ComputeEnvironmentOrder, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the job queue.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The priority of the job queue. Job queues with a higher priority are evaluated first when
    """
    priority: int | core.IntOut = core.attr(int, computed=True)

    """
    The ARN of the fair share scheduling policy. If this attribute has a value, the job queue uses a fai
    r share scheduling policy. If this attribute does not have a value, the job queue uses a first in, f
    irst out (FIFO) scheduling policy.
    """
    scheduling_policy_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Describes the ability of the queue to accept new jobs (for example, `ENABLED` or `DISABLED`).
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    The current status of the job queue (for example, `CREATING` or `VALID`).
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    A short, human-readable string to provide additional details about the current status
    """
    status_reason: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags
    """
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
