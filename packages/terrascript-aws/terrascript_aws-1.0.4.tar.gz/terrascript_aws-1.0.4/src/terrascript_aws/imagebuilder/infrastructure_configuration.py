import terrascript.core as core


@core.schema
class S3Logs(core.Schema):

    s3_bucket_name: str | core.StringOut = core.attr(str)

    s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_bucket_name: str | core.StringOut,
        s3_key_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Logs.Args(
                s3_bucket_name=s3_bucket_name,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_bucket_name: str | core.StringOut = core.arg()

        s3_key_prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Logging(core.Schema):

    s3_logs: S3Logs = core.attr(S3Logs)

    def __init__(
        self,
        *,
        s3_logs: S3Logs,
    ):
        super().__init__(
            args=Logging.Args(
                s3_logs=s3_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_logs: S3Logs = core.arg()


@core.schema
class InstanceMetadataOptions(core.Schema):

    http_put_response_hop_limit: int | core.IntOut | None = core.attr(int, default=None)

    http_tokens: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_put_response_hop_limit: int | core.IntOut | None = None,
        http_tokens: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InstanceMetadataOptions.Args(
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_put_response_hop_limit: int | core.IntOut | None = core.arg(default=None)

        http_tokens: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_imagebuilder_infrastructure_configuration", namespace="imagebuilder")
class InfrastructureConfiguration(core.Resource):
    """
    Amazon Resource Name (ARN) of the configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Date when the configuration was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    Date when the configuration was updated.
    """
    date_updated: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description for the configuration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Amazon Resource Name (ARN) of the configuration.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block with instance metadata options for the HTTP requests that pipeline bu
    ilds use to launch EC2 build and test instances. Detailed below.
    """
    instance_metadata_options: InstanceMetadataOptions | None = core.attr(
        InstanceMetadataOptions, default=None
    )

    """
    (Required) Name of IAM Instance Profile.
    """
    instance_profile_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Set of EC2 Instance Types.
    """
    instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Name of EC2 Key Pair.
    """
    key_pair: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block with logging settings. Detailed below.
    """
    logging: Logging | None = core.attr(Logging, default=None)

    """
    (Required) Name for the configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags to assign to infrastructure created by the configuration.
    """
    resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Set of EC2 Security Group identifiers.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Amazon Resource Name (ARN) of SNS Topic.
    """
    sns_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) EC2 Subnet identifier. Also requires `security_group_ids` argument.
    """
    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags to assign to the configuration. If configured with a provi
    der [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/lates
    t/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those defin
    ed at the provider-level.
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
    (Optional) Enable if the instance should be terminated when the pipeline fails. Defaults to `false`.
    """
    terminate_instance_on_failure: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_profile_name: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        instance_metadata_options: InstanceMetadataOptions | None = None,
        instance_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        key_pair: str | core.StringOut | None = None,
        logging: Logging | None = None,
        resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        sns_topic_arn: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        terminate_instance_on_failure: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InfrastructureConfiguration.Args(
                instance_profile_name=instance_profile_name,
                name=name,
                description=description,
                instance_metadata_options=instance_metadata_options,
                instance_types=instance_types,
                key_pair=key_pair,
                logging=logging,
                resource_tags=resource_tags,
                security_group_ids=security_group_ids,
                sns_topic_arn=sns_topic_arn,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                terminate_instance_on_failure=terminate_instance_on_failure,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        instance_metadata_options: InstanceMetadataOptions | None = core.arg(default=None)

        instance_profile_name: str | core.StringOut = core.arg()

        instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        key_pair: str | core.StringOut | None = core.arg(default=None)

        logging: Logging | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        sns_topic_arn: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        terminate_instance_on_failure: bool | core.BoolOut | None = core.arg(default=None)
