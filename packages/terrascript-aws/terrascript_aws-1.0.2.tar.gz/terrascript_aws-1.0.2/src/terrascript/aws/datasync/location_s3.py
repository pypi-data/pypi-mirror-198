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


@core.resource(type="aws_datasync_location_s3", namespace="aws_datasync")
class LocationS3(core.Resource):

    agent_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    s3_bucket_arn: str | core.StringOut = core.attr(str)

    s3_config: S3Config = core.attr(S3Config)

    s3_storage_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subdirectory: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
