import terrascript.core as core


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


@core.data(type="aws_ecr_repository", namespace="ecr")
class DsRepository(core.Data):
    """
    Full ARN of the repository.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Encryption configuration for the repository. See [Encryption Configuration](#encryption-configuratio
    n) below.
    """
    encryption_configuration: list[EncryptionConfiguration] | core.ArrayOut[
        EncryptionConfiguration
    ] = core.attr(EncryptionConfiguration, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Configuration block that defines image scanning configuration for the repository. See [Image Scannin
    g Configuration](#image-scanning-configuration) below.
    """
    image_scanning_configuration: list[ImageScanningConfiguration] | core.ArrayOut[
        ImageScanningConfiguration
    ] = core.attr(ImageScanningConfiguration, computed=True, kind=core.Kind.array)

    """
    The tag mutability setting for the repository.
    """
    image_tag_mutability: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the ECR Repository.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The registry ID where the repository was created.
    """
    registry_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`)
    .
    """
    repository_url: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the resource.
    """
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
