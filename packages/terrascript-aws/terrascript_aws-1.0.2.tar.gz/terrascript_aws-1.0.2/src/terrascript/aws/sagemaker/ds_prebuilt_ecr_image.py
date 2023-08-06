import terrascript.core as core


@core.data(type="aws_sagemaker_prebuilt_ecr_image", namespace="aws_sagemaker")
class DsPrebuiltEcrImage(core.Data):

    dns_suffix: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_tag: str | core.StringOut | None = core.attr(str, default=None)

    region: str | core.StringOut | None = core.attr(str, default=None)

    registry_id: str | core.StringOut = core.attr(str, computed=True)

    registry_path: str | core.StringOut = core.attr(str, computed=True)

    repository_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        repository_name: str | core.StringOut,
        dns_suffix: str | core.StringOut | None = None,
        image_tag: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPrebuiltEcrImage.Args(
                repository_name=repository_name,
                dns_suffix=dns_suffix,
                image_tag=image_tag,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_suffix: str | core.StringOut | None = core.arg(default=None)

        image_tag: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        repository_name: str | core.StringOut = core.arg()
