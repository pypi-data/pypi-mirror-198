import terrascript.core as core


@core.schema
class OperationPreferences(core.Schema):

    failure_tolerance_count: int | core.IntOut | None = core.attr(int, default=None)

    failure_tolerance_percentage: int | core.IntOut | None = core.attr(int, default=None)

    max_concurrent_count: int | core.IntOut | None = core.attr(int, default=None)

    max_concurrent_percentage: int | core.IntOut | None = core.attr(int, default=None)

    region_concurrency_type: str | core.StringOut | None = core.attr(str, default=None)

    region_order: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        failure_tolerance_count: int | core.IntOut | None = None,
        failure_tolerance_percentage: int | core.IntOut | None = None,
        max_concurrent_count: int | core.IntOut | None = None,
        max_concurrent_percentage: int | core.IntOut | None = None,
        region_concurrency_type: str | core.StringOut | None = None,
        region_order: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=OperationPreferences.Args(
                failure_tolerance_count=failure_tolerance_count,
                failure_tolerance_percentage=failure_tolerance_percentage,
                max_concurrent_count=max_concurrent_count,
                max_concurrent_percentage=max_concurrent_percentage,
                region_concurrency_type=region_concurrency_type,
                region_order=region_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failure_tolerance_count: int | core.IntOut | None = core.arg(default=None)

        failure_tolerance_percentage: int | core.IntOut | None = core.arg(default=None)

        max_concurrent_count: int | core.IntOut | None = core.arg(default=None)

        max_concurrent_percentage: int | core.IntOut | None = core.arg(default=None)

        region_concurrency_type: str | core.StringOut | None = core.arg(default=None)

        region_order: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AutoDeployment(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    retain_stacks_on_account_removal: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        retain_stacks_on_account_removal: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=AutoDeployment.Args(
                enabled=enabled,
                retain_stacks_on_account_removal=retain_stacks_on_account_removal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        retain_stacks_on_account_removal: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_cloudformation_stack_set", namespace="aws_cloudformation")
class StackSet(core.Resource):

    administration_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_deployment: AutoDeployment | None = core.attr(AutoDeployment, default=None)

    call_as: str | core.StringOut | None = core.attr(str, default=None)

    capabilities: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    execution_role_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    operation_preferences: OperationPreferences | None = core.attr(
        OperationPreferences, default=None
    )

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    permission_model: str | core.StringOut | None = core.attr(str, default=None)

    stack_set_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    template_body: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    template_url: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        administration_role_arn: str | core.StringOut | None = None,
        auto_deployment: AutoDeployment | None = None,
        call_as: str | core.StringOut | None = None,
        capabilities: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        execution_role_name: str | core.StringOut | None = None,
        operation_preferences: OperationPreferences | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        permission_model: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        template_body: str | core.StringOut | None = None,
        template_url: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StackSet.Args(
                name=name,
                administration_role_arn=administration_role_arn,
                auto_deployment=auto_deployment,
                call_as=call_as,
                capabilities=capabilities,
                description=description,
                execution_role_name=execution_role_name,
                operation_preferences=operation_preferences,
                parameters=parameters,
                permission_model=permission_model,
                tags=tags,
                tags_all=tags_all,
                template_body=template_body,
                template_url=template_url,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        administration_role_arn: str | core.StringOut | None = core.arg(default=None)

        auto_deployment: AutoDeployment | None = core.arg(default=None)

        call_as: str | core.StringOut | None = core.arg(default=None)

        capabilities: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        execution_role_name: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        operation_preferences: OperationPreferences | None = core.arg(default=None)

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        permission_model: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        template_body: str | core.StringOut | None = core.arg(default=None)

        template_url: str | core.StringOut | None = core.arg(default=None)
