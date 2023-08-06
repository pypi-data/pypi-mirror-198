import terrascript.core as core


@core.schema
class Destination(core.Schema):

    region: str | core.StringOut = core.attr(str)

    registry_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        region: str | core.StringOut,
        registry_id: str | core.StringOut,
    ):
        super().__init__(
            args=Destination.Args(
                region=region,
                registry_id=registry_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: str | core.StringOut = core.arg()

        registry_id: str | core.StringOut = core.arg()


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

    destination: list[Destination] | core.ArrayOut[Destination] = core.attr(
        Destination, kind=core.Kind.array
    )

    repository_filter: list[RepositoryFilter] | core.ArrayOut[RepositoryFilter] | None = core.attr(
        RepositoryFilter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        destination: list[Destination] | core.ArrayOut[Destination],
        repository_filter: list[RepositoryFilter] | core.ArrayOut[RepositoryFilter] | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                destination=destination,
                repository_filter=repository_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: list[Destination] | core.ArrayOut[Destination] = core.arg()

        repository_filter: list[RepositoryFilter] | core.ArrayOut[
            RepositoryFilter
        ] | None = core.arg(default=None)


@core.schema
class ReplicationConfigurationBlk(core.Schema):

    rule: list[Rule] | core.ArrayOut[Rule] = core.attr(Rule, kind=core.Kind.array)

    def __init__(
        self,
        *,
        rule: list[Rule] | core.ArrayOut[Rule],
    ):
        super().__init__(
            args=ReplicationConfigurationBlk.Args(
                rule=rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule: list[Rule] | core.ArrayOut[Rule] = core.arg()


@core.resource(type="aws_ecr_replication_configuration", namespace="ecr")
class ReplicationConfiguration(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The account ID of the destination registry to replicate to.
    """
    registry_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Replication configuration for a registry. See [Replication Configuration](#replication-co
    nfiguration).
    """
    replication_configuration: ReplicationConfigurationBlk | None = core.attr(
        ReplicationConfigurationBlk, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        replication_configuration: ReplicationConfigurationBlk | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationConfiguration.Args(
                replication_configuration=replication_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        replication_configuration: ReplicationConfigurationBlk | None = core.arg(default=None)
