import terrascript.core as core


@core.schema
class Command(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    python_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    script_location: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        script_location: str | core.StringOut,
        name: str | core.StringOut | None = None,
        python_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Command.Args(
                script_location=script_location,
                name=name,
                python_version=python_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        python_version: str | core.StringOut | None = core.arg(default=None)

        script_location: str | core.StringOut = core.arg()


@core.schema
class ExecutionProperty(core.Schema):

    max_concurrent_runs: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max_concurrent_runs: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ExecutionProperty.Args(
                max_concurrent_runs=max_concurrent_runs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_concurrent_runs: int | core.IntOut | None = core.arg(default=None)


@core.schema
class NotificationProperty(core.Schema):

    notify_delay_after: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        notify_delay_after: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=NotificationProperty.Args(
                notify_delay_after=notify_delay_after,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notify_delay_after: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_glue_job", namespace="glue")
class Job(core.Resource):
    """
    Amazon Resource Name (ARN) of Glue Job
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    command: Command = core.attr(Command)

    connections: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    default_arguments: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates whether the job is run with a standard or flexible execution class. The standar
    d execution class is ideal for time-sensitive workloads that require fast job startup and dedicated
    resources. Valid value: `FLEX`, `STANDARD`.
    """
    execution_class: str | core.StringOut | None = core.attr(str, default=None)

    execution_property: ExecutionProperty | None = core.attr(
        ExecutionProperty, default=None, computed=True
    )

    """
    (Optional) The version of glue to use, for example "1.0". For information about available versions,
    see the [AWS Glue Release Notes](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
    """
    glue_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Job name
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    max_capacity: float | core.FloatOut | None = core.attr(float, default=None, computed=True)

    max_retries: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The name of the job command. Defaults to `glueetl`. Use `pythonshell` for Python Shell Jo
    b Type, or `gluestreaming` for Streaming Job Type. `max_capacity` needs to be set if `pythonshell` i
    s chosen.
    """
    name: str | core.StringOut = core.attr(str)

    non_overridable_arguments: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Notification property of the job. Defined below.
    """
    notification_property: NotificationProperty | None = core.attr(
        NotificationProperty, default=None, computed=True
    )

    """
    (Optional) The number of workers of a defined workerType that are allocated when a job runs.
    """
    number_of_workers: int | core.IntOut | None = core.attr(int, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of the Security Configuration to be associated with the job.
    """
    security_configuration: str | core.StringOut | None = core.attr(str, default=None)

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

    timeout: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The type of predefined worker that is allocated when a job runs. Accepts a value of Stand
    ard, G.1X, or G.2X.
    """
    worker_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        command: Command,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        connections: list[str] | core.ArrayOut[core.StringOut] | None = None,
        default_arguments: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        execution_class: str | core.StringOut | None = None,
        execution_property: ExecutionProperty | None = None,
        glue_version: str | core.StringOut | None = None,
        max_capacity: float | core.FloatOut | None = None,
        max_retries: int | core.IntOut | None = None,
        non_overridable_arguments: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        notification_property: NotificationProperty | None = None,
        number_of_workers: int | core.IntOut | None = None,
        security_configuration: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timeout: int | core.IntOut | None = None,
        worker_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Job.Args(
                command=command,
                name=name,
                role_arn=role_arn,
                connections=connections,
                default_arguments=default_arguments,
                description=description,
                execution_class=execution_class,
                execution_property=execution_property,
                glue_version=glue_version,
                max_capacity=max_capacity,
                max_retries=max_retries,
                non_overridable_arguments=non_overridable_arguments,
                notification_property=notification_property,
                number_of_workers=number_of_workers,
                security_configuration=security_configuration,
                tags=tags,
                tags_all=tags_all,
                timeout=timeout,
                worker_type=worker_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        command: Command = core.arg()

        connections: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        default_arguments: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        description: str | core.StringOut | None = core.arg(default=None)

        execution_class: str | core.StringOut | None = core.arg(default=None)

        execution_property: ExecutionProperty | None = core.arg(default=None)

        glue_version: str | core.StringOut | None = core.arg(default=None)

        max_capacity: float | core.FloatOut | None = core.arg(default=None)

        max_retries: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        non_overridable_arguments: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        notification_property: NotificationProperty | None = core.arg(default=None)

        number_of_workers: int | core.IntOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        security_configuration: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        timeout: int | core.IntOut | None = core.arg(default=None)

        worker_type: str | core.StringOut | None = core.arg(default=None)
