import terrascript.core as core


@core.schema
class Error(core.Schema):

    error_code: str | core.StringOut = core.attr(str, computed=True)

    error_message: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        error_code: str | core.StringOut,
        error_message: str | core.StringOut,
    ):
        super().__init__(
            args=Error.Args(
                error_code=error_code,
                error_message=error_message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_code: str | core.StringOut = core.arg()

        error_message: str | core.StringOut = core.arg()


@core.schema
class LastUpdated(core.Schema):

    created_at: str | core.StringOut = core.attr(str, computed=True)

    error: list[Error] | core.ArrayOut[Error] = core.attr(
        Error, computed=True, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        created_at: str | core.StringOut,
        error: list[Error] | core.ArrayOut[Error],
        status: str | core.StringOut,
    ):
        super().__init__(
            args=LastUpdated.Args(
                created_at=created_at,
                error=error,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        created_at: str | core.StringOut = core.arg()

        error: list[Error] | core.ArrayOut[Error] = core.arg()

        status: str | core.StringOut = core.arg()


@core.schema
class NetworkConfiguration(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class DagProcessingLogs(core.Schema):

    cloud_watch_log_group_arn: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    log_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        log_level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DagProcessingLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        log_level: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SchedulerLogs(core.Schema):

    cloud_watch_log_group_arn: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    log_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        log_level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SchedulerLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        log_level: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TaskLogs(core.Schema):

    cloud_watch_log_group_arn: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    log_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        log_level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TaskLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        log_level: str | core.StringOut | None = core.arg(default=None)


@core.schema
class WebserverLogs(core.Schema):

    cloud_watch_log_group_arn: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    log_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        log_level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=WebserverLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        log_level: str | core.StringOut | None = core.arg(default=None)


@core.schema
class WorkerLogs(core.Schema):

    cloud_watch_log_group_arn: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    log_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        log_level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=WorkerLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        log_level: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LoggingConfiguration(core.Schema):

    dag_processing_logs: DagProcessingLogs | None = core.attr(
        DagProcessingLogs, default=None, computed=True
    )

    scheduler_logs: SchedulerLogs | None = core.attr(SchedulerLogs, default=None, computed=True)

    task_logs: TaskLogs | None = core.attr(TaskLogs, default=None, computed=True)

    webserver_logs: WebserverLogs | None = core.attr(WebserverLogs, default=None, computed=True)

    worker_logs: WorkerLogs | None = core.attr(WorkerLogs, default=None, computed=True)

    def __init__(
        self,
        *,
        dag_processing_logs: DagProcessingLogs | None = None,
        scheduler_logs: SchedulerLogs | None = None,
        task_logs: TaskLogs | None = None,
        webserver_logs: WebserverLogs | None = None,
        worker_logs: WorkerLogs | None = None,
    ):
        super().__init__(
            args=LoggingConfiguration.Args(
                dag_processing_logs=dag_processing_logs,
                scheduler_logs=scheduler_logs,
                task_logs=task_logs,
                webserver_logs=webserver_logs,
                worker_logs=worker_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dag_processing_logs: DagProcessingLogs | None = core.arg(default=None)

        scheduler_logs: SchedulerLogs | None = core.arg(default=None)

        task_logs: TaskLogs | None = core.arg(default=None)

        webserver_logs: WebserverLogs | None = core.arg(default=None)

        worker_logs: WorkerLogs | None = core.arg(default=None)


@core.resource(type="aws_mwaa_environment", namespace="aws_mwaa")
class Environment(core.Resource):

    airflow_configuration_options: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    airflow_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    dag_s3_path: str | core.StringOut = core.attr(str)

    environment_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    execution_role_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key: str | core.StringOut | None = core.attr(str, default=None)

    last_updated: list[LastUpdated] | core.ArrayOut[LastUpdated] = core.attr(
        LastUpdated, computed=True, kind=core.Kind.array
    )

    logging_configuration: LoggingConfiguration | None = core.attr(
        LoggingConfiguration, default=None, computed=True
    )

    max_workers: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    min_workers: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    network_configuration: NetworkConfiguration = core.attr(NetworkConfiguration)

    plugins_s3_object_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    plugins_s3_path: str | core.StringOut | None = core.attr(str, default=None)

    requirements_s3_object_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    requirements_s3_path: str | core.StringOut | None = core.attr(str, default=None)

    schedulers: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    service_role_arn: str | core.StringOut = core.attr(str, computed=True)

    source_bucket_arn: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    webserver_access_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    webserver_url: str | core.StringOut = core.attr(str, computed=True)

    weekly_maintenance_window_start: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        dag_s3_path: str | core.StringOut,
        execution_role_arn: str | core.StringOut,
        name: str | core.StringOut,
        network_configuration: NetworkConfiguration,
        source_bucket_arn: str | core.StringOut,
        airflow_configuration_options: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        airflow_version: str | core.StringOut | None = None,
        environment_class: str | core.StringOut | None = None,
        kms_key: str | core.StringOut | None = None,
        logging_configuration: LoggingConfiguration | None = None,
        max_workers: int | core.IntOut | None = None,
        min_workers: int | core.IntOut | None = None,
        plugins_s3_object_version: str | core.StringOut | None = None,
        plugins_s3_path: str | core.StringOut | None = None,
        requirements_s3_object_version: str | core.StringOut | None = None,
        requirements_s3_path: str | core.StringOut | None = None,
        schedulers: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        webserver_access_mode: str | core.StringOut | None = None,
        weekly_maintenance_window_start: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Environment.Args(
                dag_s3_path=dag_s3_path,
                execution_role_arn=execution_role_arn,
                name=name,
                network_configuration=network_configuration,
                source_bucket_arn=source_bucket_arn,
                airflow_configuration_options=airflow_configuration_options,
                airflow_version=airflow_version,
                environment_class=environment_class,
                kms_key=kms_key,
                logging_configuration=logging_configuration,
                max_workers=max_workers,
                min_workers=min_workers,
                plugins_s3_object_version=plugins_s3_object_version,
                plugins_s3_path=plugins_s3_path,
                requirements_s3_object_version=requirements_s3_object_version,
                requirements_s3_path=requirements_s3_path,
                schedulers=schedulers,
                tags=tags,
                tags_all=tags_all,
                webserver_access_mode=webserver_access_mode,
                weekly_maintenance_window_start=weekly_maintenance_window_start,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        airflow_configuration_options: dict[str, str] | core.MapOut[
            core.StringOut
        ] | None = core.arg(default=None)

        airflow_version: str | core.StringOut | None = core.arg(default=None)

        dag_s3_path: str | core.StringOut = core.arg()

        environment_class: str | core.StringOut | None = core.arg(default=None)

        execution_role_arn: str | core.StringOut = core.arg()

        kms_key: str | core.StringOut | None = core.arg(default=None)

        logging_configuration: LoggingConfiguration | None = core.arg(default=None)

        max_workers: int | core.IntOut | None = core.arg(default=None)

        min_workers: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        network_configuration: NetworkConfiguration = core.arg()

        plugins_s3_object_version: str | core.StringOut | None = core.arg(default=None)

        plugins_s3_path: str | core.StringOut | None = core.arg(default=None)

        requirements_s3_object_version: str | core.StringOut | None = core.arg(default=None)

        requirements_s3_path: str | core.StringOut | None = core.arg(default=None)

        schedulers: int | core.IntOut | None = core.arg(default=None)

        source_bucket_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        webserver_access_mode: str | core.StringOut | None = core.arg(default=None)

        weekly_maintenance_window_start: str | core.StringOut | None = core.arg(default=None)
