import terrascript.core as core


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class EphemeralStorage(core.Schema):

    size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        size: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=EphemeralStorage.Args(
                size=size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        size: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Environment(core.Schema):

    variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Environment.Args(
                variables=variables,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class ImageConfig(core.Schema):

    command: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    entry_point: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    working_directory: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        command: list[str] | core.ArrayOut[core.StringOut] | None = None,
        entry_point: list[str] | core.ArrayOut[core.StringOut] | None = None,
        working_directory: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ImageConfig.Args(
                command=command,
                entry_point=entry_point,
                working_directory=working_directory,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        command: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        entry_point: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        working_directory: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TracingConfig(core.Schema):

    mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        mode: str | core.StringOut,
    ):
        super().__init__(
            args=TracingConfig.Args(
                mode=mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mode: str | core.StringOut = core.arg()


@core.schema
class FileSystemConfig(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    local_mount_path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        local_mount_path: str | core.StringOut,
    ):
        super().__init__(
            args=FileSystemConfig.Args(
                arn=arn,
                local_mount_path=local_mount_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        local_mount_path: str | core.StringOut = core.arg()


@core.schema
class DeadLetterConfig(core.Schema):

    target_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        target_arn: str | core.StringOut,
    ):
        super().__init__(
            args=DeadLetterConfig.Args(
                target_arn=target_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_lambda_function", namespace="aws_lambda_")
class Function(core.Resource):

    architectures: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    code_signing_config_arn: str | core.StringOut | None = core.attr(str, default=None)

    dead_letter_config: DeadLetterConfig | None = core.attr(DeadLetterConfig, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    environment: Environment | None = core.attr(Environment, default=None)

    ephemeral_storage: EphemeralStorage | None = core.attr(
        EphemeralStorage, default=None, computed=True
    )

    file_system_config: FileSystemConfig | None = core.attr(FileSystemConfig, default=None)

    filename: str | core.StringOut | None = core.attr(str, default=None)

    function_name: str | core.StringOut = core.attr(str)

    handler: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_config: ImageConfig | None = core.attr(ImageConfig, default=None)

    image_uri: str | core.StringOut | None = core.attr(str, default=None)

    invoke_arn: str | core.StringOut = core.attr(str, computed=True)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    last_modified: str | core.StringOut = core.attr(str, computed=True)

    layers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    memory_size: int | core.IntOut | None = core.attr(int, default=None)

    package_type: str | core.StringOut | None = core.attr(str, default=None)

    publish: bool | core.BoolOut | None = core.attr(bool, default=None)

    qualified_arn: str | core.StringOut = core.attr(str, computed=True)

    reserved_concurrent_executions: int | core.IntOut | None = core.attr(int, default=None)

    role: str | core.StringOut = core.attr(str)

    runtime: str | core.StringOut | None = core.attr(str, default=None)

    s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    s3_key: str | core.StringOut | None = core.attr(str, default=None)

    s3_object_version: str | core.StringOut | None = core.attr(str, default=None)

    signing_job_arn: str | core.StringOut = core.attr(str, computed=True)

    signing_profile_version_arn: str | core.StringOut = core.attr(str, computed=True)

    source_code_hash: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    source_code_size: int | core.IntOut = core.attr(int, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout: int | core.IntOut | None = core.attr(int, default=None)

    tracing_config: TracingConfig | None = core.attr(TracingConfig, default=None, computed=True)

    version: str | core.StringOut = core.attr(str, computed=True)

    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: str | core.StringOut,
        role: str | core.StringOut,
        architectures: list[str] | core.ArrayOut[core.StringOut] | None = None,
        code_signing_config_arn: str | core.StringOut | None = None,
        dead_letter_config: DeadLetterConfig | None = None,
        description: str | core.StringOut | None = None,
        environment: Environment | None = None,
        ephemeral_storage: EphemeralStorage | None = None,
        file_system_config: FileSystemConfig | None = None,
        filename: str | core.StringOut | None = None,
        handler: str | core.StringOut | None = None,
        image_config: ImageConfig | None = None,
        image_uri: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        layers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        memory_size: int | core.IntOut | None = None,
        package_type: str | core.StringOut | None = None,
        publish: bool | core.BoolOut | None = None,
        reserved_concurrent_executions: int | core.IntOut | None = None,
        runtime: str | core.StringOut | None = None,
        s3_bucket: str | core.StringOut | None = None,
        s3_key: str | core.StringOut | None = None,
        s3_object_version: str | core.StringOut | None = None,
        source_code_hash: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timeout: int | core.IntOut | None = None,
        tracing_config: TracingConfig | None = None,
        vpc_config: VpcConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Function.Args(
                function_name=function_name,
                role=role,
                architectures=architectures,
                code_signing_config_arn=code_signing_config_arn,
                dead_letter_config=dead_letter_config,
                description=description,
                environment=environment,
                ephemeral_storage=ephemeral_storage,
                file_system_config=file_system_config,
                filename=filename,
                handler=handler,
                image_config=image_config,
                image_uri=image_uri,
                kms_key_arn=kms_key_arn,
                layers=layers,
                memory_size=memory_size,
                package_type=package_type,
                publish=publish,
                reserved_concurrent_executions=reserved_concurrent_executions,
                runtime=runtime,
                s3_bucket=s3_bucket,
                s3_key=s3_key,
                s3_object_version=s3_object_version,
                source_code_hash=source_code_hash,
                tags=tags,
                tags_all=tags_all,
                timeout=timeout,
                tracing_config=tracing_config,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        architectures: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        code_signing_config_arn: str | core.StringOut | None = core.arg(default=None)

        dead_letter_config: DeadLetterConfig | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        environment: Environment | None = core.arg(default=None)

        ephemeral_storage: EphemeralStorage | None = core.arg(default=None)

        file_system_config: FileSystemConfig | None = core.arg(default=None)

        filename: str | core.StringOut | None = core.arg(default=None)

        function_name: str | core.StringOut = core.arg()

        handler: str | core.StringOut | None = core.arg(default=None)

        image_config: ImageConfig | None = core.arg(default=None)

        image_uri: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        layers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        memory_size: int | core.IntOut | None = core.arg(default=None)

        package_type: str | core.StringOut | None = core.arg(default=None)

        publish: bool | core.BoolOut | None = core.arg(default=None)

        reserved_concurrent_executions: int | core.IntOut | None = core.arg(default=None)

        role: str | core.StringOut = core.arg()

        runtime: str | core.StringOut | None = core.arg(default=None)

        s3_bucket: str | core.StringOut | None = core.arg(default=None)

        s3_key: str | core.StringOut | None = core.arg(default=None)

        s3_object_version: str | core.StringOut | None = core.arg(default=None)

        source_code_hash: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        timeout: int | core.IntOut | None = core.arg(default=None)

        tracing_config: TracingConfig | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)
