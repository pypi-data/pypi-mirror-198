import terrascript.core as core


@core.resource(type="aws_sagemaker_image", namespace="sagemaker")
class Image(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this Image.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the image.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The display name of the image. When the image is added to a domain (must be unique to the
    domain).
    """
    display_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name of the Image.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the image. Must be unique to your account.
    """
    image_name: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform ta
    sks on your behalf.
    """
    role_arn: str | core.StringOut = core.attr(str)

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
        image_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        description: str | core.StringOut | None = None,
        display_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Image.Args(
                image_name=image_name,
                role_arn=role_arn,
                description=description,
                display_name=display_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        display_name: str | core.StringOut | None = core.arg(default=None)

        image_name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
