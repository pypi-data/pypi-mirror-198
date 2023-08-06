import terrascript.core as core


@core.schema
class OrganizationAggregationSource(core.Schema):

    all_regions: bool | core.BoolOut | None = core.attr(bool, default=None)

    regions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        all_regions: bool | core.BoolOut | None = None,
        regions: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=OrganizationAggregationSource.Args(
                role_arn=role_arn,
                all_regions=all_regions,
                regions=regions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_regions: bool | core.BoolOut | None = core.arg(default=None)

        regions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()


@core.schema
class AccountAggregationSource(core.Schema):

    account_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    all_regions: bool | core.BoolOut | None = core.attr(bool, default=None)

    regions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        account_ids: list[str] | core.ArrayOut[core.StringOut],
        all_regions: bool | core.BoolOut | None = None,
        regions: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AccountAggregationSource.Args(
                account_ids=account_ids,
                all_regions=all_regions,
                regions=regions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        all_regions: bool | core.BoolOut | None = core.arg(default=None)

        regions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_config_configuration_aggregator", namespace="aws_config")
class ConfigurationAggregator(core.Resource):

    account_aggregation_source: AccountAggregationSource | None = core.attr(
        AccountAggregationSource, default=None
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    organization_aggregation_source: OrganizationAggregationSource | None = core.attr(
        OrganizationAggregationSource, default=None
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        account_aggregation_source: AccountAggregationSource | None = None,
        organization_aggregation_source: OrganizationAggregationSource | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationAggregator.Args(
                name=name,
                account_aggregation_source=account_aggregation_source,
                organization_aggregation_source=organization_aggregation_source,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_aggregation_source: AccountAggregationSource | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        organization_aggregation_source: OrganizationAggregationSource | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
