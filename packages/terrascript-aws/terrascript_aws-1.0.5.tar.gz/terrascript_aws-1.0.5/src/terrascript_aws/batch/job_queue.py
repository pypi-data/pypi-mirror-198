import terrascript.core as core


@core.resource(type="aws_batch_job_queue", namespace="batch")
class JobQueue(core.Resource):
    """
    The Amazon Resource Name of the job queue.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the set of compute environments
    """
    compute_environments: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the name of the job queue.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The priority of the job queue. Job queues with a higher priority
    """
    priority: int | core.IntOut = core.attr(int)

    """
    (Optional) The ARN of the fair share scheduling policy. If this parameter is specified, the job queu
    e uses a fair share scheduling policy. If this parameter isn't specified, the job queue uses a first
    in, first out (FIFO) scheduling policy. After a job queue is created, you can replace but can't rem
    ove the fair share scheduling policy.
    """
    scheduling_policy_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
    """
    state: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        compute_environments: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        priority: int | core.IntOut,
        state: str | core.StringOut,
        scheduling_policy_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=JobQueue.Args(
                compute_environments=compute_environments,
                name=name,
                priority=priority,
                state=state,
                scheduling_policy_arn=scheduling_policy_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_environments: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()

        priority: int | core.IntOut = core.arg()

        scheduling_policy_arn: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
