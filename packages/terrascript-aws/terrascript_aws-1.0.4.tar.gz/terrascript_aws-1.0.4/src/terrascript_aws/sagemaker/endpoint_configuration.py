import terrascript.core as core


@core.schema
class CaptureOptions(core.Schema):

    capture_mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        capture_mode: str | core.StringOut,
    ):
        super().__init__(
            args=CaptureOptions.Args(
                capture_mode=capture_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capture_mode: str | core.StringOut = core.arg()


@core.schema
class CaptureContentTypeHeader(core.Schema):

    csv_content_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    json_content_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        csv_content_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        json_content_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=CaptureContentTypeHeader.Args(
                csv_content_types=csv_content_types,
                json_content_types=json_content_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        csv_content_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        json_content_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class DataCaptureConfig(core.Schema):

    capture_content_type_header: CaptureContentTypeHeader | None = core.attr(
        CaptureContentTypeHeader, default=None
    )

    capture_options: list[CaptureOptions] | core.ArrayOut[CaptureOptions] = core.attr(
        CaptureOptions, kind=core.Kind.array
    )

    destination_s3_uri: str | core.StringOut = core.attr(str)

    enable_capture: bool | core.BoolOut | None = core.attr(bool, default=None)

    initial_sampling_percentage: int | core.IntOut = core.attr(int)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        capture_options: list[CaptureOptions] | core.ArrayOut[CaptureOptions],
        destination_s3_uri: str | core.StringOut,
        initial_sampling_percentage: int | core.IntOut,
        capture_content_type_header: CaptureContentTypeHeader | None = None,
        enable_capture: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DataCaptureConfig.Args(
                capture_options=capture_options,
                destination_s3_uri=destination_s3_uri,
                initial_sampling_percentage=initial_sampling_percentage,
                capture_content_type_header=capture_content_type_header,
                enable_capture=enable_capture,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capture_content_type_header: CaptureContentTypeHeader | None = core.arg(default=None)

        capture_options: list[CaptureOptions] | core.ArrayOut[CaptureOptions] = core.arg()

        destination_s3_uri: str | core.StringOut = core.arg()

        enable_capture: bool | core.BoolOut | None = core.arg(default=None)

        initial_sampling_percentage: int | core.IntOut = core.arg()

        kms_key_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ServerlessConfig(core.Schema):

    max_concurrency: int | core.IntOut = core.attr(int)

    memory_size_in_mb: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        max_concurrency: int | core.IntOut,
        memory_size_in_mb: int | core.IntOut,
    ):
        super().__init__(
            args=ServerlessConfig.Args(
                max_concurrency=max_concurrency,
                memory_size_in_mb=memory_size_in_mb,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_concurrency: int | core.IntOut = core.arg()

        memory_size_in_mb: int | core.IntOut = core.arg()


@core.schema
class ProductionVariants(core.Schema):

    accelerator_type: str | core.StringOut | None = core.attr(str, default=None)

    initial_instance_count: int | core.IntOut | None = core.attr(int, default=None)

    initial_variant_weight: float | core.FloatOut | None = core.attr(float, default=None)

    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    model_name: str | core.StringOut = core.attr(str)

    serverless_config: ServerlessConfig | None = core.attr(ServerlessConfig, default=None)

    variant_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        model_name: str | core.StringOut,
        accelerator_type: str | core.StringOut | None = None,
        initial_instance_count: int | core.IntOut | None = None,
        initial_variant_weight: float | core.FloatOut | None = None,
        instance_type: str | core.StringOut | None = None,
        serverless_config: ServerlessConfig | None = None,
        variant_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProductionVariants.Args(
                model_name=model_name,
                accelerator_type=accelerator_type,
                initial_instance_count=initial_instance_count,
                initial_variant_weight=initial_variant_weight,
                instance_type=instance_type,
                serverless_config=serverless_config,
                variant_name=variant_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accelerator_type: str | core.StringOut | None = core.arg(default=None)

        initial_instance_count: int | core.IntOut | None = core.arg(default=None)

        initial_variant_weight: float | core.FloatOut | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        model_name: str | core.StringOut = core.arg()

        serverless_config: ServerlessConfig | None = core.arg(default=None)

        variant_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NotificationConfig(core.Schema):

    error_topic: str | core.StringOut | None = core.attr(str, default=None)

    success_topic: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        error_topic: str | core.StringOut | None = None,
        success_topic: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NotificationConfig.Args(
                error_topic=error_topic,
                success_topic=success_topic,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_topic: str | core.StringOut | None = core.arg(default=None)

        success_topic: str | core.StringOut | None = core.arg(default=None)


@core.schema
class OutputConfig(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    notification_config: NotificationConfig | None = core.attr(NotificationConfig, default=None)

    s3_output_path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        s3_output_path: str | core.StringOut,
        kms_key_id: str | core.StringOut | None = None,
        notification_config: NotificationConfig | None = None,
    ):
        super().__init__(
            args=OutputConfig.Args(
                s3_output_path=s3_output_path,
                kms_key_id=kms_key_id,
                notification_config=notification_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        notification_config: NotificationConfig | None = core.arg(default=None)

        s3_output_path: str | core.StringOut = core.arg()


@core.schema
class ClientConfig(core.Schema):

    max_concurrent_invocations_per_instance: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max_concurrent_invocations_per_instance: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ClientConfig.Args(
                max_concurrent_invocations_per_instance=max_concurrent_invocations_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_concurrent_invocations_per_instance: int | core.IntOut | None = core.arg(default=None)


@core.schema
class AsyncInferenceConfig(core.Schema):

    client_config: ClientConfig | None = core.attr(ClientConfig, default=None)

    output_config: OutputConfig = core.attr(OutputConfig)

    def __init__(
        self,
        *,
        output_config: OutputConfig,
        client_config: ClientConfig | None = None,
    ):
        super().__init__(
            args=AsyncInferenceConfig.Args(
                output_config=output_config,
                client_config=client_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_config: ClientConfig | None = core.arg(default=None)

        output_config: OutputConfig = core.arg()


@core.resource(type="aws_sagemaker_endpoint_configuration", namespace="sagemaker")
class EndpointConfiguration(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies configuration for how an endpoint performs asynchronous inference.
    """
    async_inference_config: AsyncInferenceConfig | None = core.attr(
        AsyncInferenceConfig, default=None
    )

    """
    (Optional) Specifies the parameters to capture input/output of SageMaker models endpoints. Fields ar
    e documented below.
    """
    data_capture_config: DataCaptureConfig | None = core.attr(DataCaptureConfig, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses
    to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the endpoint configuration. If omitted, Terraform will assign a random, uniqu
    e name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Fields are documented below.
    """
    production_variants: list[ProductionVariants] | core.ArrayOut[ProductionVariants] = core.attr(
        ProductionVariants, kind=core.Kind.array
    )

    """
    (Optional) A mapping of tags to assign to the resource. If configured with a provider [`default_tags
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tag
    s-configuration-block) present, tags with matching keys will overwrite those defined at the provider
    level.
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

    def __init__(
        self,
        resource_name: str,
        *,
        production_variants: list[ProductionVariants] | core.ArrayOut[ProductionVariants],
        async_inference_config: AsyncInferenceConfig | None = None,
        data_capture_config: DataCaptureConfig | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointConfiguration.Args(
                production_variants=production_variants,
                async_inference_config=async_inference_config,
                data_capture_config=data_capture_config,
                kms_key_arn=kms_key_arn,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        async_inference_config: AsyncInferenceConfig | None = core.arg(default=None)

        data_capture_config: DataCaptureConfig | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        production_variants: list[ProductionVariants] | core.ArrayOut[
            ProductionVariants
        ] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
