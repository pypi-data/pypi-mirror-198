import terrascript.core as core


@core.schema
class MappingRule(core.Schema):

    claim: str | core.StringOut = core.attr(str)

    match_type: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        claim: str | core.StringOut,
        match_type: str | core.StringOut,
        role_arn: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=MappingRule.Args(
                claim=claim,
                match_type=match_type,
                role_arn=role_arn,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        claim: str | core.StringOut = core.arg()

        match_type: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class RoleMapping(core.Schema):

    ambiguous_role_resolution: str | core.StringOut | None = core.attr(str, default=None)

    identity_provider: str | core.StringOut = core.attr(str)

    mapping_rule: list[MappingRule] | core.ArrayOut[MappingRule] | None = core.attr(
        MappingRule, default=None, kind=core.Kind.array
    )

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        identity_provider: str | core.StringOut,
        type: str | core.StringOut,
        ambiguous_role_resolution: str | core.StringOut | None = None,
        mapping_rule: list[MappingRule] | core.ArrayOut[MappingRule] | None = None,
    ):
        super().__init__(
            args=RoleMapping.Args(
                identity_provider=identity_provider,
                type=type,
                ambiguous_role_resolution=ambiguous_role_resolution,
                mapping_rule=mapping_rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ambiguous_role_resolution: str | core.StringOut | None = core.arg(default=None)

        identity_provider: str | core.StringOut = core.arg()

        mapping_rule: list[MappingRule] | core.ArrayOut[MappingRule] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_cognito_identity_pool_roles_attachment", namespace="cognito_identity")
class PoolRolesAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_pool_id: str | core.StringOut = core.attr(str)

    role_mapping: list[RoleMapping] | core.ArrayOut[RoleMapping] | None = core.attr(
        RoleMapping, default=None, kind=core.Kind.array
    )

    roles: dict[str, str] | core.MapOut[core.StringOut] = core.attr(str, kind=core.Kind.map)

    def __init__(
        self,
        resource_name: str,
        *,
        identity_pool_id: str | core.StringOut,
        roles: dict[str, str] | core.MapOut[core.StringOut],
        role_mapping: list[RoleMapping] | core.ArrayOut[RoleMapping] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PoolRolesAttachment.Args(
                identity_pool_id=identity_pool_id,
                roles=roles,
                role_mapping=role_mapping,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity_pool_id: str | core.StringOut = core.arg()

        role_mapping: list[RoleMapping] | core.ArrayOut[RoleMapping] | None = core.arg(default=None)

        roles: dict[str, str] | core.MapOut[core.StringOut] = core.arg()
