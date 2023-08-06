import terrascript.core as core


@core.resource(type="aws_sagemaker_image_version", namespace="sagemaker")
class ImageVersion(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this Image Version.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The registry path of the container image on which this image version is based.
    """
    base_image: str | core.StringOut = core.attr(str)

    """
    The registry path of the container image that contains this image version.
    """
    container_image: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the Image.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    image_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the image. Must be unique to your account.
    """
    image_name: str | core.StringOut = core.attr(str)

    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        base_image: str | core.StringOut,
        image_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ImageVersion.Args(
                base_image=base_image,
                image_name=image_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        base_image: str | core.StringOut = core.arg()

        image_name: str | core.StringOut = core.arg()
