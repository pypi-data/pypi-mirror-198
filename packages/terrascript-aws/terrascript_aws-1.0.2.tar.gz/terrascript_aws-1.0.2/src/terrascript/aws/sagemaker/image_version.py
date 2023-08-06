import terrascript.core as core


@core.resource(type="aws_sagemaker_image_version", namespace="aws_sagemaker")
class ImageVersion(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    base_image: str | core.StringOut = core.attr(str)

    container_image: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_arn: str | core.StringOut = core.attr(str, computed=True)

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
