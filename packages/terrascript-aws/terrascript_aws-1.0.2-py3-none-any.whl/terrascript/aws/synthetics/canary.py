import terrascript.core as core


@core.schema
class Schedule(core.Schema):

    duration_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    expression: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        expression: str | core.StringOut,
        duration_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Schedule.Args(
                expression=expression,
                duration_in_seconds=duration_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration_in_seconds: int | core.IntOut | None = core.arg(default=None)

        expression: str | core.StringOut = core.arg()


@core.schema
class S3Encryption(core.Schema):

    encryption_mode: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_mode: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Encryption.Args(
                encryption_mode=encryption_mode,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_mode: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ArtifactConfig(core.Schema):

    s3_encryption: S3Encryption | None = core.attr(S3Encryption, default=None)

    def __init__(
        self,
        *,
        s3_encryption: S3Encryption | None = None,
    ):
        super().__init__(
            args=ArtifactConfig.Args(
                s3_encryption=s3_encryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_encryption: S3Encryption | None = core.arg(default=None)


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        vpc_id: str | core.StringOut,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                vpc_id=vpc_id,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class Timeline(core.Schema):

    created: str | core.StringOut = core.attr(str, computed=True)

    last_modified: str | core.StringOut = core.attr(str, computed=True)

    last_started: str | core.StringOut = core.attr(str, computed=True)

    last_stopped: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        created: str | core.StringOut,
        last_modified: str | core.StringOut,
        last_started: str | core.StringOut,
        last_stopped: str | core.StringOut,
    ):
        super().__init__(
            args=Timeline.Args(
                created=created,
                last_modified=last_modified,
                last_started=last_started,
                last_stopped=last_stopped,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        created: str | core.StringOut = core.arg()

        last_modified: str | core.StringOut = core.arg()

        last_started: str | core.StringOut = core.arg()

        last_stopped: str | core.StringOut = core.arg()


@core.schema
class RunConfig(core.Schema):

    active_tracing: bool | core.BoolOut | None = core.attr(bool, default=None)

    environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    memory_in_mb: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    timeout_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        active_tracing: bool | core.BoolOut | None = None,
        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        memory_in_mb: int | core.IntOut | None = None,
        timeout_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=RunConfig.Args(
                active_tracing=active_tracing,
                environment_variables=environment_variables,
                memory_in_mb=memory_in_mb,
                timeout_in_seconds=timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_tracing: bool | core.BoolOut | None = core.arg(default=None)

        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        memory_in_mb: int | core.IntOut | None = core.arg(default=None)

        timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_synthetics_canary", namespace="aws_synthetics")
class Canary(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    artifact_config: ArtifactConfig | None = core.attr(ArtifactConfig, default=None)

    artifact_s3_location: str | core.StringOut = core.attr(str)

    delete_lambda: bool | core.BoolOut | None = core.attr(bool, default=None)

    engine_arn: str | core.StringOut = core.attr(str, computed=True)

    execution_role_arn: str | core.StringOut = core.attr(str)

    failure_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    handler: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    run_config: RunConfig | None = core.attr(RunConfig, default=None, computed=True)

    runtime_version: str | core.StringOut = core.attr(str)

    s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    s3_key: str | core.StringOut | None = core.attr(str, default=None)

    s3_version: str | core.StringOut | None = core.attr(str, default=None)

    schedule: Schedule = core.attr(Schedule)

    source_location_arn: str | core.StringOut = core.attr(str, computed=True)

    start_canary: bool | core.BoolOut | None = core.attr(bool, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    success_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeline: list[Timeline] | core.ArrayOut[Timeline] = core.attr(
        Timeline, computed=True, kind=core.Kind.array
    )

    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None)

    zip_file: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        artifact_s3_location: str | core.StringOut,
        execution_role_arn: str | core.StringOut,
        handler: str | core.StringOut,
        name: str | core.StringOut,
        runtime_version: str | core.StringOut,
        schedule: Schedule,
        artifact_config: ArtifactConfig | None = None,
        delete_lambda: bool | core.BoolOut | None = None,
        failure_retention_period: int | core.IntOut | None = None,
        run_config: RunConfig | None = None,
        s3_bucket: str | core.StringOut | None = None,
        s3_key: str | core.StringOut | None = None,
        s3_version: str | core.StringOut | None = None,
        start_canary: bool | core.BoolOut | None = None,
        success_retention_period: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_config: VpcConfig | None = None,
        zip_file: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Canary.Args(
                artifact_s3_location=artifact_s3_location,
                execution_role_arn=execution_role_arn,
                handler=handler,
                name=name,
                runtime_version=runtime_version,
                schedule=schedule,
                artifact_config=artifact_config,
                delete_lambda=delete_lambda,
                failure_retention_period=failure_retention_period,
                run_config=run_config,
                s3_bucket=s3_bucket,
                s3_key=s3_key,
                s3_version=s3_version,
                start_canary=start_canary,
                success_retention_period=success_retention_period,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                zip_file=zip_file,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        artifact_config: ArtifactConfig | None = core.arg(default=None)

        artifact_s3_location: str | core.StringOut = core.arg()

        delete_lambda: bool | core.BoolOut | None = core.arg(default=None)

        execution_role_arn: str | core.StringOut = core.arg()

        failure_retention_period: int | core.IntOut | None = core.arg(default=None)

        handler: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        run_config: RunConfig | None = core.arg(default=None)

        runtime_version: str | core.StringOut = core.arg()

        s3_bucket: str | core.StringOut | None = core.arg(default=None)

        s3_key: str | core.StringOut | None = core.arg(default=None)

        s3_version: str | core.StringOut | None = core.arg(default=None)

        schedule: Schedule = core.arg()

        start_canary: bool | core.BoolOut | None = core.arg(default=None)

        success_retention_period: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)

        zip_file: str | core.StringOut | None = core.arg(default=None)
