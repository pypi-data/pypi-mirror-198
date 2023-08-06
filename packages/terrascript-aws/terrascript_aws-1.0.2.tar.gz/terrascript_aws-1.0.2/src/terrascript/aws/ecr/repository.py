import terrascript.core as core


@core.schema
class ImageScanningConfiguration(core.Schema):

    scan_on_push: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        scan_on_push: bool | core.BoolOut,
    ):
        super().__init__(
            args=ImageScanningConfiguration.Args(
                scan_on_push=scan_on_push,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        scan_on_push: bool | core.BoolOut = core.arg()


@core.schema
class EncryptionConfiguration(core.Schema):

    encryption_type: str | core.StringOut | None = core.attr(str, default=None)

    kms_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        encryption_type: str | core.StringOut | None = None,
        kms_key: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                encryption_type=encryption_type,
                kms_key=kms_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_type: str | core.StringOut | None = core.arg(default=None)

        kms_key: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ecr_repository", namespace="aws_ecr")
class Repository(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    encryption_configuration: list[EncryptionConfiguration] | core.ArrayOut[
        EncryptionConfiguration
    ] | None = core.attr(EncryptionConfiguration, default=None, kind=core.Kind.array)

    force_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_scanning_configuration: ImageScanningConfiguration | None = core.attr(
        ImageScanningConfiguration, default=None
    )

    image_tag_mutability: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    registry_id: str | core.StringOut = core.attr(str, computed=True)

    repository_url: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        encryption_configuration: list[EncryptionConfiguration]
        | core.ArrayOut[EncryptionConfiguration]
        | None = None,
        force_delete: bool | core.BoolOut | None = None,
        image_scanning_configuration: ImageScanningConfiguration | None = None,
        image_tag_mutability: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Repository.Args(
                name=name,
                encryption_configuration=encryption_configuration,
                force_delete=force_delete,
                image_scanning_configuration=image_scanning_configuration,
                image_tag_mutability=image_tag_mutability,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        encryption_configuration: list[EncryptionConfiguration] | core.ArrayOut[
            EncryptionConfiguration
        ] | None = core.arg(default=None)

        force_delete: bool | core.BoolOut | None = core.arg(default=None)

        image_scanning_configuration: ImageScanningConfiguration | None = core.arg(default=None)

        image_tag_mutability: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
