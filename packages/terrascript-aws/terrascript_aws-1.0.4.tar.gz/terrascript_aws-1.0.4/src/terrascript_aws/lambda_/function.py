import terrascript.core as core


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


@core.resource(type="aws_lambda_function", namespace="lambda_")
class Function(core.Resource):
    """
    (Optional) Instruction set architecture for your Lambda function. Valid values are `["x86_64"]` and
    ["arm64"]`. Default is `["x86_64"]`. Removing this attribute, function's architecture stay the same
    .
    """

    architectures: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Required) Amazon Resource Name (ARN) of the Amazon EFS Access Point that provides access to the fil
    e system.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) To enable code signing for this function, specify the ARN of a code-signing configuration
    . A code-signing configuration includes a set of signing profiles, which define the trusted publishe
    rs for this function.
    """
    code_signing_config_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block. Detailed below.
    """
    dead_letter_config: DeadLetterConfig | None = core.attr(DeadLetterConfig, default=None)

    """
    (Optional) Description of what your Lambda Function does.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block. Detailed below.
    """
    environment: Environment | None = core.attr(Environment, default=None)

    """
    (Optional) The amount of Ephemeral storage(`/tmp`) to allocate for the Lambda Function in MB. This p
    arameter is used to expand the total amount of Ephemeral storage available, beyond the default amoun
    t of `512`MB. Detailed below.
    """
    ephemeral_storage: EphemeralStorage | None = core.attr(
        EphemeralStorage, default=None, computed=True
    )

    """
    (Optional) Configuration block. Detailed below.
    """
    file_system_config: FileSystemConfig | None = core.attr(FileSystemConfig, default=None)

    """
    (Optional) Path to the function's deployment package within the local filesystem. Conflicts with `im
    age_uri`, `s3_bucket`, `s3_key`, and `s3_object_version`.
    """
    filename: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Unique name for your Lambda Function.
    """
    function_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Function [entrypoint][3] in your code.
    """
    handler: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block. Detailed below.
    """
    image_config: ImageConfig | None = core.attr(ImageConfig, default=None)

    """
    (Optional) ECR image URI containing the function's deployment package. Conflicts with `filename`, `s
    3_bucket`, `s3_key`, and `s3_object_version`.
    """
    image_uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws_api_gateway_integ
    ration`](/docs/providers/aws/r/api_gateway_integration.html)'s `uri`.
    """
    invoke_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key that is used to en
    crypt environment variables. If this configuration is not provided when environment variables are in
    use, AWS Lambda uses a default service key. If this configuration is provided when environment vari
    ables are not in use, the AWS Lambda API does not save this configuration and Terraform will show a
    perpetual difference of adding the key. To fix the perpetual difference, remove this configuration.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    Date this resource was last modified.
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [
    Lambda Layers][10]
    """
    layers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [L
    imits][5]
    """
    memory_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Lambda deployment package type. Valid values are `Zip` and `Image`. Defaults to `Zip`.
    """
    package_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
    """
    publish: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    ARN identifying your Lambda Function Version (if versioning is enabled via `publish = true`).
    """
    qualified_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amount of reserved concurrent executions for this lambda function. A value of `0` disable
    s lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved C
    oncurrency Limits `-1`. See [Managing Concurrency][9]
    """
    reserved_concurrent_executions: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) Amazon Resource Name (ARN) of the function's execution role. The role provides the functi
    on's identity and access to AWS services and resources.
    """
    role: str | core.StringOut = core.attr(str)

    """
    (Optional) Identifier of the function's runtime. See [Runtimes][6] for valid values.
    """
    runtime: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) S3 bucket location containing the function's deployment package. Conflicts with `filename
    and `image_uri`. This bucket must reside in the same AWS region where you are creating the Lambda
    function.
    """
    s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) S3 key of an object containing the function's deployment package. Conflicts with `filenam
    e` and `image_uri`.
    """
    s3_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Object version containing the function's deployment package. Conflicts with `filename` an
    d `image_uri`.
    """
    s3_object_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    ARN of the signing job.
    """
    signing_job_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the signing profile version.
    """
    signing_profile_version_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file
    specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.z
    ip")` (Terraform 0.11.12 and later) or `base64sha256(file("file.zip"))` (Terraform 0.11.11 and earli
    er), where "file.zip" is the local filename of the lambda function source archive.
    """
    source_code_hash: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Size in bytes of the function .zip file.
    """
    source_code_size: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Map of tags to assign to the object. If configured with a provider [`default_tags` config
    uration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-config
    uration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) Amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][
    5].
    """
    timeout: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Configuration block. Detailed below.
    """
    tracing_config: TracingConfig | None = core.attr(TracingConfig, default=None, computed=True)

    """
    Latest published version of your Lambda Function.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block. Detailed below.
    """
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
