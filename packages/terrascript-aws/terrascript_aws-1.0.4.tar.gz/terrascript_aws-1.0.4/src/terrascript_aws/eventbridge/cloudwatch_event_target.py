import terrascript.core as core


@core.schema
class DeadLetterConfig(core.Schema):

    arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DeadLetterConfig.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class HttpTarget(core.Schema):

    header_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    path_parameter_values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    query_string_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        header_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        path_parameter_values: list[str] | core.ArrayOut[core.StringOut] | None = None,
        query_string_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=HttpTarget.Args(
                header_parameters=header_parameters,
                path_parameter_values=path_parameter_values,
                query_string_parameters=query_string_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        path_parameter_values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        query_string_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class NetworkConfiguration(core.Schema):

    assign_public_ip: bool | core.BoolOut | None = core.attr(bool, default=None)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        subnets: list[str] | core.ArrayOut[core.StringOut],
        assign_public_ip: bool | core.BoolOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                subnets=subnets,
                assign_public_ip=assign_public_ip,
                security_groups=security_groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        assign_public_ip: bool | core.BoolOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class PlacementConstraint(core.Schema):

    expression: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        expression: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PlacementConstraint.Args(
                type=type,
                expression=expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        expression: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class EcsTarget(core.Schema):

    enable_ecs_managed_tags: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_execute_command: bool | core.BoolOut | None = core.attr(bool, default=None)

    group: str | core.StringOut | None = core.attr(str, default=None)

    launch_type: str | core.StringOut | None = core.attr(str, default=None)

    network_configuration: NetworkConfiguration | None = core.attr(
        NetworkConfiguration, default=None
    )

    placement_constraint: list[PlacementConstraint] | core.ArrayOut[
        PlacementConstraint
    ] | None = core.attr(PlacementConstraint, default=None, kind=core.Kind.array)

    platform_version: str | core.StringOut | None = core.attr(str, default=None)

    propagate_tags: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    task_count: int | core.IntOut | None = core.attr(int, default=None)

    task_definition_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        task_definition_arn: str | core.StringOut,
        enable_ecs_managed_tags: bool | core.BoolOut | None = None,
        enable_execute_command: bool | core.BoolOut | None = None,
        group: str | core.StringOut | None = None,
        launch_type: str | core.StringOut | None = None,
        network_configuration: NetworkConfiguration | None = None,
        placement_constraint: list[PlacementConstraint]
        | core.ArrayOut[PlacementConstraint]
        | None = None,
        platform_version: str | core.StringOut | None = None,
        propagate_tags: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        task_count: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=EcsTarget.Args(
                task_definition_arn=task_definition_arn,
                enable_ecs_managed_tags=enable_ecs_managed_tags,
                enable_execute_command=enable_execute_command,
                group=group,
                launch_type=launch_type,
                network_configuration=network_configuration,
                placement_constraint=placement_constraint,
                platform_version=platform_version,
                propagate_tags=propagate_tags,
                tags=tags,
                task_count=task_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_ecs_managed_tags: bool | core.BoolOut | None = core.arg(default=None)

        enable_execute_command: bool | core.BoolOut | None = core.arg(default=None)

        group: str | core.StringOut | None = core.arg(default=None)

        launch_type: str | core.StringOut | None = core.arg(default=None)

        network_configuration: NetworkConfiguration | None = core.arg(default=None)

        placement_constraint: list[PlacementConstraint] | core.ArrayOut[
            PlacementConstraint
        ] | None = core.arg(default=None)

        platform_version: str | core.StringOut | None = core.arg(default=None)

        propagate_tags: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        task_count: int | core.IntOut | None = core.arg(default=None)

        task_definition_arn: str | core.StringOut = core.arg()


@core.schema
class RedshiftTarget(core.Schema):

    database: str | core.StringOut = core.attr(str)

    db_user: str | core.StringOut | None = core.attr(str, default=None)

    secrets_manager_arn: str | core.StringOut | None = core.attr(str, default=None)

    sql: str | core.StringOut | None = core.attr(str, default=None)

    statement_name: str | core.StringOut | None = core.attr(str, default=None)

    with_event: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        database: str | core.StringOut,
        db_user: str | core.StringOut | None = None,
        secrets_manager_arn: str | core.StringOut | None = None,
        sql: str | core.StringOut | None = None,
        statement_name: str | core.StringOut | None = None,
        with_event: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=RedshiftTarget.Args(
                database=database,
                db_user=db_user,
                secrets_manager_arn=secrets_manager_arn,
                sql=sql,
                statement_name=statement_name,
                with_event=with_event,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: str | core.StringOut = core.arg()

        db_user: str | core.StringOut | None = core.arg(default=None)

        secrets_manager_arn: str | core.StringOut | None = core.arg(default=None)

        sql: str | core.StringOut | None = core.arg(default=None)

        statement_name: str | core.StringOut | None = core.arg(default=None)

        with_event: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class RetryPolicy(core.Schema):

    maximum_event_age_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    maximum_retry_attempts: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        maximum_event_age_in_seconds: int | core.IntOut | None = None,
        maximum_retry_attempts: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=RetryPolicy.Args(
                maximum_event_age_in_seconds=maximum_event_age_in_seconds,
                maximum_retry_attempts=maximum_retry_attempts,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        maximum_event_age_in_seconds: int | core.IntOut | None = core.arg(default=None)

        maximum_retry_attempts: int | core.IntOut | None = core.arg(default=None)


@core.schema
class RunCommandTargets(core.Schema):

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=RunCommandTargets.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class BatchTarget(core.Schema):

    array_size: int | core.IntOut | None = core.attr(int, default=None)

    job_attempts: int | core.IntOut | None = core.attr(int, default=None)

    job_definition: str | core.StringOut = core.attr(str)

    job_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        job_definition: str | core.StringOut,
        job_name: str | core.StringOut,
        array_size: int | core.IntOut | None = None,
        job_attempts: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=BatchTarget.Args(
                job_definition=job_definition,
                job_name=job_name,
                array_size=array_size,
                job_attempts=job_attempts,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        array_size: int | core.IntOut | None = core.arg(default=None)

        job_attempts: int | core.IntOut | None = core.arg(default=None)

        job_definition: str | core.StringOut = core.arg()

        job_name: str | core.StringOut = core.arg()


@core.schema
class InputTransformer(core.Schema):

    input_paths: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    input_template: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        input_template: str | core.StringOut,
        input_paths: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=InputTransformer.Args(
                input_template=input_template,
                input_paths=input_paths,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_paths: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        input_template: str | core.StringOut = core.arg()


@core.schema
class SqsTarget(core.Schema):

    message_group_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message_group_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SqsTarget.Args(
                message_group_id=message_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message_group_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class KinesisTarget(core.Schema):

    partition_key_path: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        partition_key_path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=KinesisTarget.Args(
                partition_key_path=partition_key_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        partition_key_path: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_cloudwatch_event_target", namespace="eventbridge")
class CloudwatchEventTarget(core.Resource):
    """
    (Required) The Amazon Resource Name (ARN) of the target.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented bel
    ow. A maximum of 1 are allowed.
    """
    batch_target: BatchTarget | None = core.attr(BatchTarget, default=None)

    """
    (Optional)  Parameters used when you are providing a dead letter config. Documented below. A maximum
    of 1 are allowed.
    """
    dead_letter_config: DeadLetterConfig | None = core.attr(DeadLetterConfig, default=None)

    """
    (Optional) Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below.
    A maximum of 1 are allowed.
    """
    ecs_target: EcsTarget | None = core.attr(EcsTarget, default=None)

    """
    (Optional) The event bus to associate with the rule. If you omit this, the `default` event bus is us
    ed.
    """
    event_bus_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Parameters used when you are using the rule to invoke an API Gateway REST endpoint. Docum
    ented below. A maximum of 1 is allowed.
    """
    http_target: HttpTarget | None = core.attr(HttpTarget, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Valid JSON text passed to the target. Conflicts with `input_path` and `input_transformer`
    .
    """
    input: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The value of the [JSONPath](http://goessner.net/articles/JsonPath/) that is used for extr
    acting part of the matched event when passing it to the target. Conflicts with `input` and `input_tr
    ansformer`.
    """
    input_path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Parameters used when you are providing a custom input to a target based on certain event
    data. Conflicts with `input` and `input_path`.
    """
    input_transformer: InputTransformer | None = core.attr(InputTransformer, default=None)

    """
    (Optional) Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documente
    d below. A maximum of 1 are allowed.
    """
    kinesis_target: KinesisTarget | None = core.attr(KinesisTarget, default=None)

    """
    (Optional) Parameters used when you are using the rule to invoke an Amazon Redshift Statement. Docum
    ented below. A maximum of 1 are allowed.
    """
    redshift_target: RedshiftTarget | None = core.attr(RedshiftTarget, default=None)

    """
    (Optional)  Parameters used when you are providing retry policies. Documented below. A maximum of 1
    are allowed.
    """
    retry_policy: RetryPolicy | None = core.attr(RetryPolicy, default=None)

    """
    (Optional) The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule i
    s triggered. Required if `ecs_target` is used or target in `arn` is EC2 instance, Kinesis data strea
    m, Step Functions state machine, or Event Bus in different account or region.
    """
    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the rule you want to add targets to.
    """
    rule: str | core.StringOut = core.attr(str)

    """
    (Optional) Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented
    below. A maximum of 5 are allowed.
    """
    run_command_targets: list[RunCommandTargets] | core.ArrayOut[
        RunCommandTargets
    ] | None = core.attr(RunCommandTargets, default=None, kind=core.Kind.array)

    """
    (Optional) Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented bel
    ow. A maximum of 1 are allowed.
    """
    sqs_target: SqsTarget | None = core.attr(SqsTarget, default=None)

    """
    (Optional) The unique target assignment ID.  If missing, will generate a random, unique id.
    """
    target_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        arn: str | core.StringOut,
        rule: str | core.StringOut,
        batch_target: BatchTarget | None = None,
        dead_letter_config: DeadLetterConfig | None = None,
        ecs_target: EcsTarget | None = None,
        event_bus_name: str | core.StringOut | None = None,
        http_target: HttpTarget | None = None,
        input: str | core.StringOut | None = None,
        input_path: str | core.StringOut | None = None,
        input_transformer: InputTransformer | None = None,
        kinesis_target: KinesisTarget | None = None,
        redshift_target: RedshiftTarget | None = None,
        retry_policy: RetryPolicy | None = None,
        role_arn: str | core.StringOut | None = None,
        run_command_targets: list[RunCommandTargets]
        | core.ArrayOut[RunCommandTargets]
        | None = None,
        sqs_target: SqsTarget | None = None,
        target_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventTarget.Args(
                arn=arn,
                rule=rule,
                batch_target=batch_target,
                dead_letter_config=dead_letter_config,
                ecs_target=ecs_target,
                event_bus_name=event_bus_name,
                http_target=http_target,
                input=input,
                input_path=input_path,
                input_transformer=input_transformer,
                kinesis_target=kinesis_target,
                redshift_target=redshift_target,
                retry_policy=retry_policy,
                role_arn=role_arn,
                run_command_targets=run_command_targets,
                sqs_target=sqs_target,
                target_id=target_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: str | core.StringOut = core.arg()

        batch_target: BatchTarget | None = core.arg(default=None)

        dead_letter_config: DeadLetterConfig | None = core.arg(default=None)

        ecs_target: EcsTarget | None = core.arg(default=None)

        event_bus_name: str | core.StringOut | None = core.arg(default=None)

        http_target: HttpTarget | None = core.arg(default=None)

        input: str | core.StringOut | None = core.arg(default=None)

        input_path: str | core.StringOut | None = core.arg(default=None)

        input_transformer: InputTransformer | None = core.arg(default=None)

        kinesis_target: KinesisTarget | None = core.arg(default=None)

        redshift_target: RedshiftTarget | None = core.arg(default=None)

        retry_policy: RetryPolicy | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        rule: str | core.StringOut = core.arg()

        run_command_targets: list[RunCommandTargets] | core.ArrayOut[
            RunCommandTargets
        ] | None = core.arg(default=None)

        sqs_target: SqsTarget | None = core.arg(default=None)

        target_id: str | core.StringOut | None = core.arg(default=None)
