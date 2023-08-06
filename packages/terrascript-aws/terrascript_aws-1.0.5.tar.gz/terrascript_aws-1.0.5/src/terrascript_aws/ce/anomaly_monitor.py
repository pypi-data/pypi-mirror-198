import terrascript.core as core


@core.resource(type="aws_ce_anomaly_monitor", namespace="ce")
class AnomalyMonitor(core.Resource):
    """
    ARN of the anomaly monitor.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Unique ID of the anomaly monitor. Same as `arn`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, if `monitor_type` is `DIMENSIONAL`) The dimensions to evaluate. Valid values: `SERVICE`.
    """
    monitor_dimension: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required, if `monitor_type` is `CUSTOM`) A valid JSON representation for the [Expression](https://d
    ocs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object.
    """
    monitor_specification: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The possible type values. Valid values: `DIMENSIONAL` | `CUSTOM`.
    """
    monitor_type: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the monitor.
    """
    name: str | core.StringOut = core.attr(str)

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
        monitor_type: str | core.StringOut,
        name: str | core.StringOut,
        monitor_dimension: str | core.StringOut | None = None,
        monitor_specification: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AnomalyMonitor.Args(
                monitor_type=monitor_type,
                name=name,
                monitor_dimension=monitor_dimension,
                monitor_specification=monitor_specification,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        monitor_dimension: str | core.StringOut | None = core.arg(default=None)

        monitor_specification: str | core.StringOut | None = core.arg(default=None)

        monitor_type: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
