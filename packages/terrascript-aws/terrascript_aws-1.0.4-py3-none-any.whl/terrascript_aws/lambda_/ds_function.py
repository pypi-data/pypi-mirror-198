import terrascript.core as core


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


@core.data(type="aws_lambda_function", namespace="lambda_")
class DsFunction(core.Data):
    """
    The instruction set architecture for the Lambda function.
    """

    architectures: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Unqualified (no `:QUALIFIER` or `:VERSION` suffix) Amazon Resource Name (ARN) identifying your Lambd
    a Function. See also `qualified_arn`.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) for a Code Signing Configuration.
    """
    code_signing_config_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Configure the function's *dead letter queue*.
    """
    dead_letter_config: list[DeadLetterConfig] | core.ArrayOut[DeadLetterConfig] = core.attr(
        DeadLetterConfig, computed=True, kind=core.Kind.array
    )

    """
    Description of what your Lambda Function does.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The Lambda environment's configuration settings.
    """
    environment: list[Environment] | core.ArrayOut[Environment] = core.attr(
        Environment, computed=True, kind=core.Kind.array
    )

    """
    The amount of Ephemeral storage(`/tmp`) allocated for the Lambda Function.
    """
    ephemeral_storage: list[EphemeralStorage] | core.ArrayOut[EphemeralStorage] = core.attr(
        EphemeralStorage, computed=True, kind=core.Kind.array
    )

    """
    The connection settings for an Amazon EFS file system.
    """
    file_system_config: list[FileSystemConfig] | core.ArrayOut[FileSystemConfig] = core.attr(
        FileSystemConfig, computed=True, kind=core.Kind.array
    )

    """
    (Required) Name of the lambda function.
    """
    function_name: str | core.StringOut = core.attr(str)

    """
    The function entrypoint in your code.
    """
    handler: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The URI of the container image.
    """
    image_uri: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN to be used for invoking Lambda Function from API Gateway.
    """
    invoke_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN for the KMS encryption key.
    """
    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date this resource was last modified.
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of Lambda Layer ARNs attached to your Lambda Function.
    """
    layers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Amount of memory in MB your Lambda Function can use at runtime.
    """
    memory_size: int | core.IntOut = core.attr(int, computed=True)

    """
    Qualified (`:QUALIFIER` or `:VERSION` suffix) Amazon Resource Name (ARN) identifying your Lambda Fun
    ction. See also `arn`.
    """
    qualified_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Alias name or version number of the lambda functionE.g., `$LATEST`, `my-alias`, or `1`
    """
    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    The amount of reserved concurrent executions for this lambda function or `-1` if unreserved.
    """
    reserved_concurrent_executions: int | core.IntOut = core.attr(int, computed=True)

    """
    IAM role attached to the Lambda Function.
    """
    role: str | core.StringOut = core.attr(str, computed=True)

    """
    The runtime environment for the Lambda function.
    """
    runtime: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of a signing job.
    """
    signing_job_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) for a signing profile version.
    """
    signing_profile_version_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Base64-encoded representation of raw SHA-256 sum of the zip file.
    """
    source_code_hash: str | core.StringOut = core.attr(str, computed=True)

    """
    The size in bytes of the function .zip file.
    """
    source_code_size: int | core.IntOut = core.attr(int, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The function execution time at which Lambda should terminate the function.
    """
    timeout: int | core.IntOut = core.attr(int, computed=True)

    """
    Tracing settings of the function.
    """
    tracing_config: list[TracingConfig] | core.ArrayOut[TracingConfig] = core.attr(
        TracingConfig, computed=True, kind=core.Kind.array
    )

    """
    The version of the Lambda function.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    """
    VPC configuration associated with your Lambda function.
    """
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
