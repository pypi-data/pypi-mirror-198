import terrascript.core as core


@core.schema
class ProvisioningParameters(core.Schema):

    key: str | core.StringOut = core.attr(str)

    use_previous_value: bool | core.BoolOut | None = core.attr(bool, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        use_previous_value: bool | core.BoolOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProvisioningParameters.Args(
                key=key,
                use_previous_value=use_previous_value,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        use_previous_value: bool | core.BoolOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Outputs(core.Schema):

    description: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        description: str | core.StringOut,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Outputs.Args(
                description=description,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class StackSetProvisioningPreferences(core.Schema):

    accounts: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    failure_tolerance_count: int | core.IntOut | None = core.attr(int, default=None)

    failure_tolerance_percentage: int | core.IntOut | None = core.attr(int, default=None)

    max_concurrency_count: int | core.IntOut | None = core.attr(int, default=None)

    max_concurrency_percentage: int | core.IntOut | None = core.attr(int, default=None)

    regions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        accounts: list[str] | core.ArrayOut[core.StringOut] | None = None,
        failure_tolerance_count: int | core.IntOut | None = None,
        failure_tolerance_percentage: int | core.IntOut | None = None,
        max_concurrency_count: int | core.IntOut | None = None,
        max_concurrency_percentage: int | core.IntOut | None = None,
        regions: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=StackSetProvisioningPreferences.Args(
                accounts=accounts,
                failure_tolerance_count=failure_tolerance_count,
                failure_tolerance_percentage=failure_tolerance_percentage,
                max_concurrency_count=max_concurrency_count,
                max_concurrency_percentage=max_concurrency_percentage,
                regions=regions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accounts: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        failure_tolerance_count: int | core.IntOut | None = core.arg(default=None)

        failure_tolerance_percentage: int | core.IntOut | None = core.arg(default=None)

        max_concurrency_count: int | core.IntOut | None = core.arg(default=None)

        max_concurrency_percentage: int | core.IntOut | None = core.arg(default=None)

        regions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_servicecatalog_provisioned_product", namespace="aws_servicecatalog")
class ProvisionedProduct(core.Resource):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    cloudwatch_dashboard_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    created_time: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ignore_errors: bool | core.BoolOut | None = core.attr(bool, default=None)

    last_provisioning_record_id: str | core.StringOut = core.attr(str, computed=True)

    last_record_id: str | core.StringOut = core.attr(str, computed=True)

    last_successful_provisioning_record_id: str | core.StringOut = core.attr(str, computed=True)

    launch_role_arn: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    notification_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    outputs: list[Outputs] | core.ArrayOut[Outputs] = core.attr(
        Outputs, computed=True, kind=core.Kind.array
    )

    path_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    path_name: str | core.StringOut | None = core.attr(str, default=None)

    product_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    product_name: str | core.StringOut | None = core.attr(str, default=None)

    provisioning_artifact_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    provisioning_artifact_name: str | core.StringOut | None = core.attr(str, default=None)

    provisioning_parameters: list[ProvisioningParameters] | core.ArrayOut[
        ProvisioningParameters
    ] | None = core.attr(ProvisioningParameters, default=None, kind=core.Kind.array)

    retain_physical_resources: bool | core.BoolOut | None = core.attr(bool, default=None)

    stack_set_provisioning_preferences: StackSetProvisioningPreferences | None = core.attr(
        StackSetProvisioningPreferences, default=None
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    status_message: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        ignore_errors: bool | core.BoolOut | None = None,
        notification_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        path_id: str | core.StringOut | None = None,
        path_name: str | core.StringOut | None = None,
        product_id: str | core.StringOut | None = None,
        product_name: str | core.StringOut | None = None,
        provisioning_artifact_id: str | core.StringOut | None = None,
        provisioning_artifact_name: str | core.StringOut | None = None,
        provisioning_parameters: list[ProvisioningParameters]
        | core.ArrayOut[ProvisioningParameters]
        | None = None,
        retain_physical_resources: bool | core.BoolOut | None = None,
        stack_set_provisioning_preferences: StackSetProvisioningPreferences | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProvisionedProduct.Args(
                name=name,
                accept_language=accept_language,
                ignore_errors=ignore_errors,
                notification_arns=notification_arns,
                path_id=path_id,
                path_name=path_name,
                product_id=product_id,
                product_name=product_name,
                provisioning_artifact_id=provisioning_artifact_id,
                provisioning_artifact_name=provisioning_artifact_name,
                provisioning_parameters=provisioning_parameters,
                retain_physical_resources=retain_physical_resources,
                stack_set_provisioning_preferences=stack_set_provisioning_preferences,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        ignore_errors: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        notification_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        path_id: str | core.StringOut | None = core.arg(default=None)

        path_name: str | core.StringOut | None = core.arg(default=None)

        product_id: str | core.StringOut | None = core.arg(default=None)

        product_name: str | core.StringOut | None = core.arg(default=None)

        provisioning_artifact_id: str | core.StringOut | None = core.arg(default=None)

        provisioning_artifact_name: str | core.StringOut | None = core.arg(default=None)

        provisioning_parameters: list[ProvisioningParameters] | core.ArrayOut[
            ProvisioningParameters
        ] | None = core.arg(default=None)

        retain_physical_resources: bool | core.BoolOut | None = core.arg(default=None)

        stack_set_provisioning_preferences: StackSetProvisioningPreferences | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
