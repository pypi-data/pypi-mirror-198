import terrascript.core as core


@core.schema
class StorageLocation(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    object_version: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
        role_arn: str | core.StringOut,
        object_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StorageLocation.Args(
                bucket=bucket,
                key=key,
                role_arn=role_arn,
                object_version=object_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        object_version: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_gamelift_script", namespace="gamelift")
class Script(core.Resource):
    """
    GameLift Script ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    GameLift Script ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the script
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Information indicating where your game script files are stored. See below.
    """
    storage_location: StorageLocation | None = core.attr(
        StorageLocation, default=None, computed=True
    )

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) Version that is associated with this script.
    """
    version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A data object containing your Realtime scripts and dependencies as a zip  file. The zip f
    ile can have one or multiple files. Maximum size of a zip file is 5 MB.
    """
    zip_file: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        storage_location: StorageLocation | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        version: str | core.StringOut | None = None,
        zip_file: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Script.Args(
                name=name,
                storage_location=storage_location,
                tags=tags,
                tags_all=tags_all,
                version=version,
                zip_file=zip_file,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        storage_location: StorageLocation | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)

        zip_file: str | core.StringOut | None = core.arg(default=None)
