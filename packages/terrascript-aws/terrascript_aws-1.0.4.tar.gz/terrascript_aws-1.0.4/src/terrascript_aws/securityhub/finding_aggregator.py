import terrascript.core as core


@core.resource(type="aws_securityhub_finding_aggregator", namespace="securityhub")
class FindingAggregator(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    linking_mode: str | core.StringOut = core.attr(str)

    specified_regions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        linking_mode: str | core.StringOut,
        specified_regions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FindingAggregator.Args(
                linking_mode=linking_mode,
                specified_regions=specified_regions,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        linking_mode: str | core.StringOut = core.arg()

        specified_regions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
