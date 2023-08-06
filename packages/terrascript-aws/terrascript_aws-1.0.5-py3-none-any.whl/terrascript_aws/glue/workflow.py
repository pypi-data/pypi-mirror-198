import terrascript.core as core


@core.resource(type="aws_glue_workflow", namespace="glue")
class Workflow(core.Resource):
    """
    Amazon Resource Name (ARN) of Glue Workflow
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_run_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Workflow name
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If
    you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
    """
    max_concurrent_runs: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        default_run_properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        max_concurrent_runs: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workflow.Args(
                default_run_properties=default_run_properties,
                description=description,
                max_concurrent_runs=max_concurrent_runs,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_run_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        description: str | core.StringOut | None = core.arg(default=None)

        max_concurrent_runs: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
