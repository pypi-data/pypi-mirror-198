import terrascript.core as core


@core.resource(type="aws_batch_job_queue", namespace="aws_batch")
class JobQueue(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    compute_environments: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    priority: int | core.IntOut = core.attr(int)

    scheduling_policy_arn: str | core.StringOut | None = core.attr(str, default=None)

    state: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
