import terrascript.core as core


@core.schema
class RepositoryFilter(core.Schema):

    filter: str | core.StringOut = core.attr(str)

    filter_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        filter: str | core.StringOut,
        filter_type: str | core.StringOut,
    ):
        super().__init__(
            args=RepositoryFilter.Args(
                filter=filter,
                filter_type=filter_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: str | core.StringOut = core.arg()

        filter_type: str | core.StringOut = core.arg()


@core.schema
class Rule(core.Schema):

    repository_filter: list[RepositoryFilter] | core.ArrayOut[RepositoryFilter] = core.attr(
        RepositoryFilter, kind=core.Kind.array
    )

    scan_frequency: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        repository_filter: list[RepositoryFilter] | core.ArrayOut[RepositoryFilter],
        scan_frequency: str | core.StringOut,
    ):
        super().__init__(
            args=Rule.Args(
                repository_filter=repository_filter,
                scan_frequency=scan_frequency,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_filter: list[RepositoryFilter] | core.ArrayOut[RepositoryFilter] = core.arg()

        scan_frequency: str | core.StringOut = core.arg()


@core.resource(type="aws_ecr_registry_scanning_configuration", namespace="ecr")
class RegistryScanningConfiguration(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The registry ID the scanning configuration applies to.
    """
    registry_id: str | core.StringOut = core.attr(str, computed=True)

    rule: list[Rule] | core.ArrayOut[Rule] | None = core.attr(
        Rule, default=None, kind=core.Kind.array
    )

    scan_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        scan_type: str | core.StringOut,
        rule: list[Rule] | core.ArrayOut[Rule] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegistryScanningConfiguration.Args(
                scan_type=scan_type,
                rule=rule,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        rule: list[Rule] | core.ArrayOut[Rule] | None = core.arg(default=None)

        scan_type: str | core.StringOut = core.arg()
