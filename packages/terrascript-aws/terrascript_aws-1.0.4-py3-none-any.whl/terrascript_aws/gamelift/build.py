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


@core.resource(type="aws_gamelift_build", namespace="gamelift")
class Build(core.Resource):
    """
    GameLift Build ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    GameLift Build ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the build
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Operating system that the game server binaries are built to run onE.g., `WINDOWS_2012`, `
    AMAZON_LINUX` or `AMAZON_LINUX_2`.
    """
    operating_system: str | core.StringOut = core.attr(str)

    """
    (Required) Information indicating where your game build files are stored. See below.
    """
    storage_location: StorageLocation = core.attr(StorageLocation)

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
    (Optional) Version that is associated with this build.
    """
    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        operating_system: str | core.StringOut,
        storage_location: StorageLocation,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        version: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Build.Args(
                name=name,
                operating_system=operating_system,
                storage_location=storage_location,
                tags=tags,
                tags_all=tags_all,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        operating_system: str | core.StringOut = core.arg()

        storage_location: StorageLocation = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)
