import terrascript.core as core


@core.resource(type="aws_config_organization_custom_rule", namespace="aws_config")
class OrganizationCustomRule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    excluded_accounts: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    input_parameters: str | core.StringOut | None = core.attr(str, default=None)

    lambda_function_arn: str | core.StringOut = core.attr(str)

    maximum_execution_frequency: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    resource_id_scope: str | core.StringOut | None = core.attr(str, default=None)

    resource_types_scope: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tag_key_scope: str | core.StringOut | None = core.attr(str, default=None)

    tag_value_scope: str | core.StringOut | None = core.attr(str, default=None)

    trigger_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        lambda_function_arn: str | core.StringOut,
        name: str | core.StringOut,
        trigger_types: list[str] | core.ArrayOut[core.StringOut],
        description: str | core.StringOut | None = None,
        excluded_accounts: list[str] | core.ArrayOut[core.StringOut] | None = None,
        input_parameters: str | core.StringOut | None = None,
        maximum_execution_frequency: str | core.StringOut | None = None,
        resource_id_scope: str | core.StringOut | None = None,
        resource_types_scope: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tag_key_scope: str | core.StringOut | None = None,
        tag_value_scope: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationCustomRule.Args(
                lambda_function_arn=lambda_function_arn,
                name=name,
                trigger_types=trigger_types,
                description=description,
                excluded_accounts=excluded_accounts,
                input_parameters=input_parameters,
                maximum_execution_frequency=maximum_execution_frequency,
                resource_id_scope=resource_id_scope,
                resource_types_scope=resource_types_scope,
                tag_key_scope=tag_key_scope,
                tag_value_scope=tag_value_scope,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        excluded_accounts: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        input_parameters: str | core.StringOut | None = core.arg(default=None)

        lambda_function_arn: str | core.StringOut = core.arg()

        maximum_execution_frequency: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        resource_id_scope: str | core.StringOut | None = core.arg(default=None)

        resource_types_scope: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tag_key_scope: str | core.StringOut | None = core.arg(default=None)

        tag_value_scope: str | core.StringOut | None = core.arg(default=None)

        trigger_types: list[str] | core.ArrayOut[core.StringOut] = core.arg()
