import terrascript.core as core


@core.schema
class InstanceMetadataOptions(core.Schema):

    http_put_response_hop_limit: int | core.IntOut = core.attr(int, computed=True)

    http_tokens: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        http_put_response_hop_limit: int | core.IntOut,
        http_tokens: str | core.StringOut,
    ):
        super().__init__(
            args=InstanceMetadataOptions.Args(
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_put_response_hop_limit: int | core.IntOut = core.arg()

        http_tokens: str | core.StringOut = core.arg()


@core.schema
class S3Logs(core.Schema):

    s3_bucket_name: str | core.StringOut = core.attr(str, computed=True)

    s3_key_prefix: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        s3_bucket_name: str | core.StringOut,
        s3_key_prefix: str | core.StringOut,
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

        s3_key_prefix: str | core.StringOut = core.arg()


@core.schema
class Logging(core.Schema):

    s3_logs: list[S3Logs] | core.ArrayOut[S3Logs] = core.attr(
        S3Logs, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        s3_logs: list[S3Logs] | core.ArrayOut[S3Logs],
    ):
        super().__init__(
            args=Logging.Args(
                s3_logs=s3_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_logs: list[S3Logs] | core.ArrayOut[S3Logs] = core.arg()


@core.data(type="aws_imagebuilder_infrastructure_configuration", namespace="imagebuilder")
class DsInfrastructureConfiguration(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the infrastructure configuration.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    Date the infrastructure configuration was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    date_updated: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the infrastructure configuration.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Nested list of instance metadata options for the HTTP requests that pipeline builds use to launch EC
    2 build and test instances.
    """
    instance_metadata_options: list[InstanceMetadataOptions] | core.ArrayOut[
        InstanceMetadataOptions
    ] = core.attr(InstanceMetadataOptions, computed=True, kind=core.Kind.array)

    """
    Name of the IAM Instance Profile associated with the configuration.
    """
    instance_profile_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of EC2 Instance Types associated with the configuration.
    """
    instance_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Name of the EC2 Key Pair associated with the configuration.
    """
    key_pair: str | core.StringOut = core.attr(str, computed=True)

    """
    Nested list of logging settings.
    """
    logging: list[Logging] | core.ArrayOut[Logging] = core.attr(
        Logging, computed=True, kind=core.Kind.array
    )

    """
    Name of the infrastructure configuration.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags for the infrastructure created by the infrastructure configuration.
    """
    resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Set of EC2 Security Group identifiers associated with the configuration.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Amazon Resource Name (ARN) of the SNS Topic associated with the configuration.
    """
    sns_topic_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the EC2 Subnet associated with the configuration.
    """
    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags for the infrastructure configuration.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Whether instances are terminated on failure.
    """
    terminate_instance_on_failure: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInfrastructureConfiguration.Args(
                arn=arn,
                resource_tags=resource_tags,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
