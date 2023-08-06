import terrascript.core as core


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


@core.resource(type="aws_mwaa_environment", namespace="mwaa")
class Environment(core.Resource):
    """
    (Optional) The `airflow_configuration_options` parameter specifies airflow override options. Check t
    he [Official documentation](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variab
    les.html#configuring-env-variables-reference) for all possible configuration options.
    """

    airflow_configuration_options: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Airflow version of your environment, will be set by default to the latest version that MW
    AA supports.
    """
    airflow_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ARN of the MWAA Environment
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Created At date of the MWAA Environment
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The relative path to the DAG folder on your Amazon S3 storage bucket. For example, dags.
    For more information, see [Importing DAGs on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/us
    erguide/configuring-dag-import.html).
    """
    dag_s3_path: str | core.StringOut = core.attr(str)

    """
    (Optional) Environment class for the cluster. Possible options are `mw1.small`, `mw1.medium`, `mw1.l
    arge`. Will be set by default to `mw1.small`. Please check the [AWS Pricing](https://aws.amazon.com/
    de/managed-workflows-for-apache-airflow/pricing/) for more information about the environment classes
    .
    """
    environment_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) of the task execution role that the Amazon MWAA and its en
    vironment can assume. Check the [official AWS documentation](https://docs.aws.amazon.com/mwaa/latest
    /userguide/mwaa-create-role.html) for the detailed role specification.
    """
    execution_role_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) of your KMS key that you want to use for encryption. Will
    be set to the ARN of the managed KMS key `aws/airflow` by default. Please check the [Official Docume
    ntation](https://docs.aws.amazon.com/mwaa/latest/userguide/custom-keys-certs.html) for more informat
    ion.
    """
    kms_key: str | core.StringOut | None = core.attr(str, default=None)

    last_updated: list[LastUpdated] | core.ArrayOut[LastUpdated] = core.attr(
        LastUpdated, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The Apache Airflow logs you want to send to Amazon CloudWatch Logs.
    """
    logging_configuration: LoggingConfiguration | None = core.attr(
        LoggingConfiguration, default=None, computed=True
    )

    """
    (Optional) The maximum number of workers that can be automatically scaled up. Value need to be betwe
    en `1` and `25`. Will be `10` by default.
    """
    max_workers: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The minimum number of workers that you want to run in your environment. Will be `1` by de
    fault.
    """
    min_workers: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Required) The name of the Apache Airflow Environment
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the network configuration for your Apache Airflow Environment. This includes tw
    o private subnets as well as security groups for the Airflow environment. Each subnet requires inter
    net connection, otherwise the deployment will fail. See [Network configuration](#network-configurati
    on) below for details.
    """
    network_configuration: NetworkConfiguration = core.attr(NetworkConfiguration)

    """
    (Optional) The plugins.zip file version you want to use.
    """
    plugins_s3_object_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The relative path to the plugins.zip file on your Amazon S3 storage bucket. For example,
    plugins.zip. If a relative path is provided in the request, then plugins_s3_object_version is requir
    ed. For more information, see [Importing DAGs on Amazon MWAA](https://docs.aws.amazon.com/mwaa/lates
    t/userguide/configuring-dag-import.html).
    """
    plugins_s3_path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The requirements.txt file version you want to use.
    """
    requirements_s3_object_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The relative path to the requirements.txt file on your Amazon S3 storage bucket. For exam
    ple, requirements.txt. If a relative path is provided in the request, then requirements_s3_object_ve
    rsion is required. For more information, see [Importing DAGs on Amazon MWAA](https://docs.aws.amazon
    .com/mwaa/latest/userguide/configuring-dag-import.html).
    """
    requirements_s3_path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The number of schedulers that you want to run in your environment. v2.0.2 and above accep
    ts `2` - `5`, default `2`. v1.10.12 accepts `1`.
    """
    schedulers: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    The Service Role ARN of the Amazon MWAA Environment
    """
    service_role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) of your Amazon S3 storage bucket. For example, arn:aws:s3:
    ::airflow-mybucketname.
    """
    source_bucket_arn: str | core.StringOut = core.attr(str)

    """
    The status of the Amazon MWAA Environment
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of resource tags to associate with the resource. If configured with a provider [`de
    fault_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#d
    efault_tags-configuration-block) present, tags with matching keys will overwrite those defined at th
    e provider-level.
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
    (Optional) Specifies whether the webserver should be accessible over the internet or via your specif
    ied VPC. Possible options: `PRIVATE_ONLY` (default) and `PUBLIC_ONLY`.
    """
    webserver_access_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The webserver URL of the MWAA Environment
    """
    webserver_url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the start date for the weekly maintenance window.
    """
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
