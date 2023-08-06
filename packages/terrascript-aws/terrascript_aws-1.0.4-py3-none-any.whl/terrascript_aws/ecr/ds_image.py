import terrascript.core as core


@core.data(type="aws_ecr_image", namespace="ecr")
class DsImage(core.Data):
    """
    SHA256 digest of the image manifest.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The sha256 digest of the image manifest. At least one of `image_digest` or `image_tag` mu
    st be specified.
    """
    image_digest: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The date and time, expressed as a unix timestamp, at which the current image was pushed to the repos
    itory.
    """
    image_pushed_at: int | core.IntOut = core.attr(int, computed=True)

    """
    The size, in bytes, of the image in the repository.
    """
    image_size_in_bytes: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) The tag associated with this image. At least one of `image_digest` or `image_tag` must be
    specified.
    """
    image_tag: str | core.StringOut | None = core.attr(str, default=None)

    """
    The list of tags associated with this image.
    """
    image_tags: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The ID of the Registry where the repository resides.
    """
    registry_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name of the ECR Repository.
    """
    repository_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        repository_name: str | core.StringOut,
        image_digest: str | core.StringOut | None = None,
        image_tag: str | core.StringOut | None = None,
        registry_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsImage.Args(
                repository_name=repository_name,
                image_digest=image_digest,
                image_tag=image_tag,
                registry_id=registry_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_digest: str | core.StringOut | None = core.arg(default=None)

        image_tag: str | core.StringOut | None = core.arg(default=None)

        registry_id: str | core.StringOut | None = core.arg(default=None)

        repository_name: str | core.StringOut = core.arg()
