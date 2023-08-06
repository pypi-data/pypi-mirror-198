import terrascript.core as core


@core.data(type="aws_batch_compute_environment", namespace="batch")
class DsComputeEnvironment(core.Data):
    """
    The ARN of the compute environment.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Batch Compute Environment
    """
    compute_environment_name: str | core.StringOut = core.attr(str)

    """
    The ARN of the underlying Amazon ECS cluster used by the compute environment.
    """
    ecs_cluster_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
    """
    service_role: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the compute environment (for example, `ENABLED` or `DISABLED`). If the state is `ENABLE
    D`, then the compute environment accepts jobs from a queue and can scale out automatically based on
    queues.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    The current status of the compute environment (for example, `CREATING` or `VALID`).
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    A short, human-readable string to provide additional details about the current status of the compute
    environment.
    """
    status_reason: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The type of the compute environment (for example, `MANAGED` or `UNMANAGED`).
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        compute_environment_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsComputeEnvironment.Args(
                compute_environment_name=compute_environment_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_environment_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
