import terrascript.core as core


@core.data(type="aws_route53_resolver_rules", namespace="route53_resolver")
class DsRules(core.Data):
    """
    AWS Region.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A regex string to filter resolver rule names.
    """
    name_regex: str | core.StringOut | None = core.attr(str, default=None)

    owner_id: str | core.StringOut | None = core.attr(str, default=None)

    resolver_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The IDs of the matched resolver rules.
    """
    resolver_rule_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    rule_type: str | core.StringOut | None = core.attr(str, default=None)

    share_status: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name_regex: str | core.StringOut | None = None,
        owner_id: str | core.StringOut | None = None,
        resolver_endpoint_id: str | core.StringOut | None = None,
        rule_type: str | core.StringOut | None = None,
        share_status: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRules.Args(
                name_regex=name_regex,
                owner_id=owner_id,
                resolver_endpoint_id=resolver_endpoint_id,
                rule_type=rule_type,
                share_status=share_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name_regex: str | core.StringOut | None = core.arg(default=None)

        owner_id: str | core.StringOut | None = core.arg(default=None)

        resolver_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        rule_type: str | core.StringOut | None = core.arg(default=None)

        share_status: str | core.StringOut | None = core.arg(default=None)
