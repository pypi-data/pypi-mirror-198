import terrascript.core as core


@core.schema
class TracingConfig(core.Schema):

    mode: str | core.StringOut = core.attr(str, computed=True)

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
class DeadLetterConfig(core.Schema):

    target_arn: str | core.StringOut = core.attr(str, computed=True)

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


@core.schema
class EphemeralStorage(core.Schema):

    size: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        size: int | core.IntOut,
    ):
        super().__init__(
            args=EphemeralStorage.Args(
                size=size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        size: int | core.IntOut = core.arg()


@core.schema
class Environment(core.Schema):

    variables: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        variables: dict[str, str] | core.MapOut[core.StringOut],
    ):
        super().__init__(
            args=Environment.Args(
                variables=variables,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        variables: dict[str, str] | core.MapOut[core.StringOut] = core.arg()


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

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
class FileSystemConfig(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    local_mount_path: str | core.StringOut = core.attr(str, computed=True)

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


@core.data(type="aws_lambda_function", namespace="aws_lambda_")
class DsFunction(core.Data):

    architectures: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    code_signing_config_arn: str | core.StringOut = core.attr(str, computed=True)

    dead_letter_config: list[DeadLetterConfig] | core.ArrayOut[DeadLetterConfig] = core.attr(
        DeadLetterConfig, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut = core.attr(str, computed=True)

    environment: list[Environment] | core.ArrayOut[Environment] = core.attr(
        Environment, computed=True, kind=core.Kind.array
    )

    ephemeral_storage: list[EphemeralStorage] | core.ArrayOut[EphemeralStorage] = core.attr(
        EphemeralStorage, computed=True, kind=core.Kind.array
    )

    file_system_config: list[FileSystemConfig] | core.ArrayOut[FileSystemConfig] = core.attr(
        FileSystemConfig, computed=True, kind=core.Kind.array
    )

    function_name: str | core.StringOut = core.attr(str)

    handler: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_uri: str | core.StringOut = core.attr(str, computed=True)

    invoke_arn: str | core.StringOut = core.attr(str, computed=True)

    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    last_modified: str | core.StringOut = core.attr(str, computed=True)

    layers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    memory_size: int | core.IntOut = core.attr(int, computed=True)

    qualified_arn: str | core.StringOut = core.attr(str, computed=True)

    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    reserved_concurrent_executions: int | core.IntOut = core.attr(int, computed=True)

    role: str | core.StringOut = core.attr(str, computed=True)

    runtime: str | core.StringOut = core.attr(str, computed=True)

    signing_job_arn: str | core.StringOut = core.attr(str, computed=True)

    signing_profile_version_arn: str | core.StringOut = core.attr(str, computed=True)

    source_code_hash: str | core.StringOut = core.attr(str, computed=True)

    source_code_size: int | core.IntOut = core.attr(int, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout: int | core.IntOut = core.attr(int, computed=True)

    tracing_config: list[TracingConfig] | core.ArrayOut[TracingConfig] = core.attr(
        TracingConfig, computed=True, kind=core.Kind.array
    )

    version: str | core.StringOut = core.attr(str, computed=True)

    vpc_config: list[VpcConfig] | core.ArrayOut[VpcConfig] = core.attr(
        VpcConfig, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        function_name: str | core.StringOut,
        qualifier: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFunction.Args(
                function_name=function_name,
                qualifier=qualifier,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_name: str | core.StringOut = core.arg()

        qualifier: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
