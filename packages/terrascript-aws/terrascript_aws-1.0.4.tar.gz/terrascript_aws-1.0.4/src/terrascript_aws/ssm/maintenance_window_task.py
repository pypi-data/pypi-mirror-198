import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class AutomationParameters(core.Schema):

    document_version: str | core.StringOut | None = core.attr(str, default=None)

    parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        document_version: str | core.StringOut | None = None,
        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = None,
    ):
        super().__init__(
            args=AutomationParameters.Args(
                document_version=document_version,
                parameter=parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        document_version: str | core.StringOut | None = core.arg(default=None)

        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.arg(default=None)


@core.schema
class LambdaParameters(core.Schema):

    client_context: str | core.StringOut | None = core.attr(str, default=None)

    payload: str | core.StringOut | None = core.attr(str, default=None)

    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        client_context: str | core.StringOut | None = None,
        payload: str | core.StringOut | None = None,
        qualifier: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LambdaParameters.Args(
                client_context=client_context,
                payload=payload,
                qualifier=qualifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_context: str | core.StringOut | None = core.arg(default=None)

        payload: str | core.StringOut | None = core.arg(default=None)

        qualifier: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NotificationConfig(core.Schema):

    notification_arn: str | core.StringOut | None = core.attr(str, default=None)

    notification_events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    notification_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        notification_arn: str | core.StringOut | None = None,
        notification_events: list[str] | core.ArrayOut[core.StringOut] | None = None,
        notification_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NotificationConfig.Args(
                notification_arn=notification_arn,
                notification_events=notification_events,
                notification_type=notification_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notification_arn: str | core.StringOut | None = core.arg(default=None)

        notification_events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        notification_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CloudwatchConfig(core.Schema):

    cloudwatch_log_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    cloudwatch_output_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        cloudwatch_log_group_name: str | core.StringOut | None = None,
        cloudwatch_output_enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=CloudwatchConfig.Args(
                cloudwatch_log_group_name=cloudwatch_log_group_name,
                cloudwatch_output_enabled=cloudwatch_output_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group_name: str | core.StringOut | None = core.arg(default=None)

        cloudwatch_output_enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class RunCommandParameters(core.Schema):

    cloudwatch_config: CloudwatchConfig | None = core.attr(CloudwatchConfig, default=None)

    comment: str | core.StringOut | None = core.attr(str, default=None)

    document_hash: str | core.StringOut | None = core.attr(str, default=None)

    document_hash_type: str | core.StringOut | None = core.attr(str, default=None)

    document_version: str | core.StringOut | None = core.attr(str, default=None)

    notification_config: NotificationConfig | None = core.attr(NotificationConfig, default=None)

    output_s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    output_s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    service_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    timeout_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cloudwatch_config: CloudwatchConfig | None = None,
        comment: str | core.StringOut | None = None,
        document_hash: str | core.StringOut | None = None,
        document_hash_type: str | core.StringOut | None = None,
        document_version: str | core.StringOut | None = None,
        notification_config: NotificationConfig | None = None,
        output_s3_bucket: str | core.StringOut | None = None,
        output_s3_key_prefix: str | core.StringOut | None = None,
        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = None,
        service_role_arn: str | core.StringOut | None = None,
        timeout_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=RunCommandParameters.Args(
                cloudwatch_config=cloudwatch_config,
                comment=comment,
                document_hash=document_hash,
                document_hash_type=document_hash_type,
                document_version=document_version,
                notification_config=notification_config,
                output_s3_bucket=output_s3_bucket,
                output_s3_key_prefix=output_s3_key_prefix,
                parameter=parameter,
                service_role_arn=service_role_arn,
                timeout_seconds=timeout_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_config: CloudwatchConfig | None = core.arg(default=None)

        comment: str | core.StringOut | None = core.arg(default=None)

        document_hash: str | core.StringOut | None = core.arg(default=None)

        document_hash_type: str | core.StringOut | None = core.arg(default=None)

        document_version: str | core.StringOut | None = core.arg(default=None)

        notification_config: NotificationConfig | None = core.arg(default=None)

        output_s3_bucket: str | core.StringOut | None = core.arg(default=None)

        output_s3_key_prefix: str | core.StringOut | None = core.arg(default=None)

        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.arg(default=None)

        service_role_arn: str | core.StringOut | None = core.arg(default=None)

        timeout_seconds: int | core.IntOut | None = core.arg(default=None)


@core.schema
class StepFunctionsParameters(core.Schema):

    input: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        input: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StepFunctionsParameters.Args(
                input=input,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TaskInvocationParameters(core.Schema):

    automation_parameters: AutomationParameters | None = core.attr(
        AutomationParameters, default=None
    )

    lambda_parameters: LambdaParameters | None = core.attr(LambdaParameters, default=None)

    run_command_parameters: RunCommandParameters | None = core.attr(
        RunCommandParameters, default=None
    )

    step_functions_parameters: StepFunctionsParameters | None = core.attr(
        StepFunctionsParameters, default=None
    )

    def __init__(
        self,
        *,
        automation_parameters: AutomationParameters | None = None,
        lambda_parameters: LambdaParameters | None = None,
        run_command_parameters: RunCommandParameters | None = None,
        step_functions_parameters: StepFunctionsParameters | None = None,
    ):
        super().__init__(
            args=TaskInvocationParameters.Args(
                automation_parameters=automation_parameters,
                lambda_parameters=lambda_parameters,
                run_command_parameters=run_command_parameters,
                step_functions_parameters=step_functions_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        automation_parameters: AutomationParameters | None = core.arg(default=None)

        lambda_parameters: LambdaParameters | None = core.arg(default=None)

        run_command_parameters: RunCommandParameters | None = core.arg(default=None)

        step_functions_parameters: StepFunctionsParameters | None = core.arg(default=None)


@core.schema
class Targets(core.Schema):

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Targets.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_ssm_maintenance_window_task", namespace="ssm")
class MaintenanceWindowTask(core.Resource):
    """
    The ARN of the maintenance window task.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether tasks should continue to run after the cutoff time specified in the mai
    ntenance windows is reached. Valid values are `CONTINUE_TASK` and `CANCEL_TASK`.
    """
    cutoff_behavior: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The description of the maintenance window task.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the maintenance window task.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The maximum number of targets this task can be run for in parallel.
    """
    max_concurrency: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The maximum number of errors allowed before this task stops being scheduled.
    """
    max_errors: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The name of the maintenance window task.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The priority of the task in the Maintenance Window, the lower the number the higher the p
    riority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same
    priority scheduled in parallel.
    """
    priority: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The role that should be assumed when executing the task. If a role is not provided, Syste
    ms Manager uses your account's service-linked role. If no service-linked role for Systems Manager ex
    ists in your account, it is created for you.
    """
    service_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The targets (either instances or window target ids). Instances are specified using Key=In
    stanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,
    Values=window target id1, window target id2.
    """
    targets: list[Targets] | core.ArrayOut[Targets] | None = core.attr(
        Targets, default=None, kind=core.Kind.array
    )

    """
    (Required) The ARN of the task to execute.
    """
    task_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block with parameters for task execution.
    """
    task_invocation_parameters: TaskInvocationParameters | None = core.attr(
        TaskInvocationParameters, default=None
    )

    """
    (Required) The type of task being registered. Valid values: `AUTOMATION`, `LAMBDA`, `RUN_COMMAND` or
    STEP_FUNCTIONS`.
    """
    task_type: str | core.StringOut = core.attr(str)

    """
    (Required) The Id of the maintenance window to register the task with.
    """
    window_id: str | core.StringOut = core.attr(str)

    """
    The ID of the maintenance window task.
    """
    window_task_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        task_arn: str | core.StringOut,
        task_type: str | core.StringOut,
        window_id: str | core.StringOut,
        cutoff_behavior: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        max_concurrency: str | core.StringOut | None = None,
        max_errors: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        priority: int | core.IntOut | None = None,
        service_role_arn: str | core.StringOut | None = None,
        targets: list[Targets] | core.ArrayOut[Targets] | None = None,
        task_invocation_parameters: TaskInvocationParameters | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MaintenanceWindowTask.Args(
                task_arn=task_arn,
                task_type=task_type,
                window_id=window_id,
                cutoff_behavior=cutoff_behavior,
                description=description,
                max_concurrency=max_concurrency,
                max_errors=max_errors,
                name=name,
                priority=priority,
                service_role_arn=service_role_arn,
                targets=targets,
                task_invocation_parameters=task_invocation_parameters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cutoff_behavior: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        max_concurrency: str | core.StringOut | None = core.arg(default=None)

        max_errors: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        priority: int | core.IntOut | None = core.arg(default=None)

        service_role_arn: str | core.StringOut | None = core.arg(default=None)

        targets: list[Targets] | core.ArrayOut[Targets] | None = core.arg(default=None)

        task_arn: str | core.StringOut = core.arg()

        task_invocation_parameters: TaskInvocationParameters | None = core.arg(default=None)

        task_type: str | core.StringOut = core.arg()

        window_id: str | core.StringOut = core.arg()
