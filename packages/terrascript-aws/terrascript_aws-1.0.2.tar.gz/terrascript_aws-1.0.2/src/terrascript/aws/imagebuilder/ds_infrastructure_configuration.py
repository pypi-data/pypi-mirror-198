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


@core.data(type="aws_imagebuilder_infrastructure_configuration", namespace="aws_imagebuilder")
class DsInfrastructureConfiguration(core.Data):

    arn: str | core.StringOut = core.attr(str)

    date_created: str | core.StringOut = core.attr(str, computed=True)

    date_updated: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_metadata_options: list[InstanceMetadataOptions] | core.ArrayOut[
        InstanceMetadataOptions
    ] = core.attr(InstanceMetadataOptions, computed=True, kind=core.Kind.array)

    instance_profile_name: str | core.StringOut = core.attr(str, computed=True)

    instance_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    key_pair: str | core.StringOut = core.attr(str, computed=True)

    logging: list[Logging] | core.ArrayOut[Logging] = core.attr(
        Logging, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    sns_topic_arn: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
