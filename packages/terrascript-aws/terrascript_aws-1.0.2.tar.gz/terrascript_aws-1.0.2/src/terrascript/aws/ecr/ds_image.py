import terrascript.core as core


@core.data(type="aws_ecr_image", namespace="aws_ecr")
class DsImage(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    image_digest: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    image_pushed_at: int | core.IntOut = core.attr(int, computed=True)

    image_size_in_bytes: int | core.IntOut = core.attr(int, computed=True)

    image_tag: str | core.StringOut | None = core.attr(str, default=None)

    image_tags: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    registry_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
