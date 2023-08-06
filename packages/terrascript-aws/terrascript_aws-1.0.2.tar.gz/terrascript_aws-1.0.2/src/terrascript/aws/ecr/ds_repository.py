import terrascript.core as core


@core.schema
class ImageScanningConfiguration(core.Schema):

    scan_on_push: bool | core.BoolOut = core.attr(bool, computed=True)

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

    encryption_type: str | core.StringOut = core.attr(str, computed=True)

    kms_key: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        encryption_type: str | core.StringOut,
        kms_key: str | core.StringOut,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                encryption_type=encryption_type,
                kms_key=kms_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_type: str | core.StringOut = core.arg()

        kms_key: str | core.StringOut = core.arg()


@core.data(type="aws_ecr_repository", namespace="aws_ecr")
class DsRepository(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    encryption_configuration: list[EncryptionConfiguration] | core.ArrayOut[
        EncryptionConfiguration
    ] = core.attr(EncryptionConfiguration, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_scanning_configuration: list[ImageScanningConfiguration] | core.ArrayOut[
        ImageScanningConfiguration
    ] = core.attr(ImageScanningConfiguration, computed=True, kind=core.Kind.array)

    image_tag_mutability: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    registry_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    repository_url: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        registry_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRepository.Args(
                name=name,
                registry_id=registry_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        registry_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
