import terrascript.core as core


@core.schema
class EvaluateOnExit(core.Schema):

    action: str | core.StringOut = core.attr(str)

    on_exit_code: str | core.StringOut | None = core.attr(str, default=None)

    on_reason: str | core.StringOut | None = core.attr(str, default=None)

    on_status_reason: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        action: str | core.StringOut,
        on_exit_code: str | core.StringOut | None = None,
        on_reason: str | core.StringOut | None = None,
        on_status_reason: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EvaluateOnExit.Args(
                action=action,
                on_exit_code=on_exit_code,
                on_reason=on_reason,
                on_status_reason=on_status_reason,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut = core.arg()

        on_exit_code: str | core.StringOut | None = core.arg(default=None)

        on_reason: str | core.StringOut | None = core.arg(default=None)

        on_status_reason: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RetryStrategy(core.Schema):

    attempts: int | core.IntOut | None = core.attr(int, default=None)

    evaluate_on_exit: list[EvaluateOnExit] | core.ArrayOut[EvaluateOnExit] | None = core.attr(
        EvaluateOnExit, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        attempts: int | core.IntOut | None = None,
        evaluate_on_exit: list[EvaluateOnExit] | core.ArrayOut[EvaluateOnExit] | None = None,
    ):
        super().__init__(
            args=RetryStrategy.Args(
                attempts=attempts,
                evaluate_on_exit=evaluate_on_exit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attempts: int | core.IntOut | None = core.arg(default=None)

        evaluate_on_exit: list[EvaluateOnExit] | core.ArrayOut[EvaluateOnExit] | None = core.arg(
            default=None
        )


@core.schema
class Timeout(core.Schema):

    attempt_duration_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        attempt_duration_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Timeout.Args(
                attempt_duration_seconds=attempt_duration_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attempt_duration_seconds: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_batch_job_definition", namespace="batch")
class JobDefinition(core.Resource):
    """
    The Amazon Resource Name of the job definition.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_R
    egisterJobDefinition.html)
    """
    container_properties: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the name of the job definition.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies the parameter substitution placeholders to set in the job definition.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) The platform capabilities required by the job definition. If no value is specified, it de
    faults to `EC2`. To run the job on Fargate resources, specify `FARGATE`.
    """
    platform_capabilities: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Specifies whether to propagate the tags from the job definition to the corresponding Amaz
    on ECS task. Default is `false`.
    """
    propagate_tags: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies the retry strategy to use for failed jobs that are submitted with this job defi
    nition.
    """
    retry_strategy: RetryStrategy | None = core.attr(RetryStrategy, default=None)

    """
    The revision of the job definition.
    """
    revision: int | core.IntOut = core.attr(int, computed=True)

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

    """
    (Optional) Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job
    . Maximum number of `timeout` is `1`. Defined below.
    """
    timeout: Timeout | None = core.attr(Timeout, default=None)

    """
    (Required) The type of job definition.  Must be `container`.
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
        container_properties: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        platform_capabilities: list[str] | core.ArrayOut[core.StringOut] | None = None,
        propagate_tags: bool | core.BoolOut | None = None,
        retry_strategy: RetryStrategy | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timeout: Timeout | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=JobDefinition.Args(
                name=name,
                type=type,
                container_properties=container_properties,
                parameters=parameters,
                platform_capabilities=platform_capabilities,
                propagate_tags=propagate_tags,
                retry_strategy=retry_strategy,
                tags=tags,
                tags_all=tags_all,
                timeout=timeout,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_properties: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        platform_capabilities: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        propagate_tags: bool | core.BoolOut | None = core.arg(default=None)

        retry_strategy: RetryStrategy | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        timeout: Timeout | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
