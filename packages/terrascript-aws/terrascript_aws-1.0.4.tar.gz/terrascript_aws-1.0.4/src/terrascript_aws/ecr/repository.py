import terrascript.core as core


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


@core.resource(type="aws_ecr_repository", namespace="ecr")
class Repository(core.Resource):
    """
    Full ARN of the repository.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Encryption configuration for the repository. See [below for schema](#encryption_configura
    tion).
    """
    encryption_configuration: list[EncryptionConfiguration] | core.ArrayOut[
        EncryptionConfiguration
    ] | None = core.attr(EncryptionConfiguration, default=None, kind=core.Kind.array)

    """
    (Optional) If `true`, will delete the repository even if it contains images.
    """
    force_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block that defines image scanning configuration for the repository. By defa
    ult, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com
    /AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
    """
    image_scanning_configuration: ImageScanningConfiguration | None = core.attr(
        ImageScanningConfiguration, default=None
    )

    """
    (Optional) The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`.
    Defaults to `MUTABLE`.
    """
    image_tag_mutability: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name of the repository.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The registry ID where the repository was created.
    """
    registry_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`)
    .
    """
    repository_url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
