import terrascript.core as core


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


@core.resource(type="aws_config_configuration_aggregator", namespace="config")
class ConfigurationAggregator(core.Resource):
    """
    (Optional) The account(s) to aggregate config data from as documented below.
    """

    account_aggregation_source: AccountAggregationSource | None = core.attr(
        AccountAggregationSource, default=None
    )

    """
    The ARN of the aggregator
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the configuration aggregator.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The organization to aggregate config data from as documented below.
    """
    organization_aggregation_source: OrganizationAggregationSource | None = core.attr(
        OrganizationAggregationSource, default=None
    )

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
