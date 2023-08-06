import terrascript.core as core


@core.schema
class S3(core.Schema):

    bucket_arn: str | core.StringOut = core.attr(str)

    file_key: str | core.StringOut = core.attr(str)

    object_version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        file_key: str | core.StringOut,
        object_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3.Args(
                bucket_arn=bucket_arn,
                file_key=file_key,
                object_version=object_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: str | core.StringOut = core.arg()

        file_key: str | core.StringOut = core.arg()

        object_version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Location(core.Schema):

    s3: S3 = core.attr(S3)

    def __init__(
        self,
        *,
        s3: S3,
    ):
        super().__init__(
            args=Location.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: S3 = core.arg()


@core.resource(type="aws_mskconnect_custom_plugin", namespace="managed_streaming_for_kafka_connect")
class MskconnectCustomPlugin(core.Resource):
    """
    the Amazon Resource Name (ARN) of the custom plugin.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of the plugin file. Allowed values are `ZIP` and `JAR`.
    """
    content_type: str | core.StringOut = core.attr(str)

    """
    (Optional) A summary description of the custom plugin.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    an ID of the latest successfully created revision of the custom plugin.
    """
    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) Information about the location of a custom plugin. See below.
    """
    location: Location = core.attr(Location)

    """
    (Required) The name of the custom plugin..
    """
    name: str | core.StringOut = core.attr(str)

    """
    the state of the custom plugin.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        content_type: str | core.StringOut,
        location: Location,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskconnectCustomPlugin.Args(
                content_type=content_type,
                location=location,
                name=name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_type: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        location: Location = core.arg()

        name: str | core.StringOut = core.arg()
