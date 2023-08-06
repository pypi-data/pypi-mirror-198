import terrascript.core as core


@core.schema
class S3Config(core.Schema):

    bucket_access_role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_access_role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=S3Config.Args(
                bucket_access_role_arn=bucket_access_role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_access_role_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_datasync_location_s3", namespace="datasync")
class LocationS3(core.Resource):
    """
    (Optional) A list of DataSync Agent ARNs with which this location will be associated.
    """

    agent_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Amazon Resource Name (ARN) of the S3 Bucket.
    """
    s3_bucket_arn: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block containing information for connecting to S3.
    """
    s3_config: S3Config = core.attr(S3Config)

    """
    (Optional) The Amazon S3 storage class that you want to store your files in when this location is us
    ed as a task destination. [Valid values](https://docs.aws.amazon.com/datasync/latest/userguide/creat
    e-s3-location.html#using-storage-classes)
    """
    s3_storage_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Prefix to perform actions as source or destination.
    """
    subdirectory: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value pairs of resource tags to assign to the DataSync Location. If configured with a
    provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws
    /latest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those
    defined at the provider-level.
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

    uri: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        s3_bucket_arn: str | core.StringOut,
        s3_config: S3Config,
        subdirectory: str | core.StringOut,
        agent_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        s3_storage_class: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationS3.Args(
                s3_bucket_arn=s3_bucket_arn,
                s3_config=s3_config,
                subdirectory=subdirectory,
                agent_arns=agent_arns,
                s3_storage_class=s3_storage_class,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        agent_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        s3_bucket_arn: str | core.StringOut = core.arg()

        s3_config: S3Config = core.arg()

        s3_storage_class: str | core.StringOut | None = core.arg(default=None)

        subdirectory: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
