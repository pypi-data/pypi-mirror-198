import terrascript.core as core


@core.data(type="aws_datapipeline_pipeline", namespace="datapipeline")
class DsPipeline(core.Data):
    """
    Description of Pipeline.
    """

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of Pipeline.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ID of the pipeline.
    """
    pipeline_id: str | core.StringOut = core.attr(str)

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
        pipeline_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPipeline.Args(
                pipeline_id=pipeline_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pipeline_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
