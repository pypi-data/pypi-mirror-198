import terrascript.core as core


@core.data(type="aws_prometheus_workspace", namespace="amp")
class DsPrometheusWorkspace(core.Data):
    """
    The Prometheus workspace alias.
    """

    alias: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the Prometheus workspace.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation date of the Prometheus workspace.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The endpoint of the Prometheus workspace.
    """
    prometheus_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of the Prometheus workspace.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The tags assigned to the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The Prometheus workspace ID.
    """
    workspace_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        workspace_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPrometheusWorkspace.Args(
                workspace_id=workspace_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        workspace_id: str | core.StringOut = core.arg()
