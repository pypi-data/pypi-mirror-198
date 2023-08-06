import terrascript.core as core


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


@core.resource(type="aws_servicecatalog_provisioned_product", namespace="servicecatalog")
class ProvisionedProduct(core.Resource):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default val
    ue is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    ARN of the provisioned product.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of CloudWatch dashboards that were created when provisioning the product.
    """
    cloudwatch_dashboard_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Time when the provisioned product was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    Provisioned Product ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) _Only applies to deleting._ If set to `true`, AWS Service Catalog stops managing the spec
    ified provisioned product even if it cannot delete the underlying resources. The default value is `f
    alse`.
    """
    ignore_errors: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Record identifier of the last request performed on this provisioned product of the following types:
    ProvisionedProduct`, `UpdateProvisionedProduct`, `ExecuteProvisionedProductPlan`, `TerminateProvisi
    onedProduct`.
    """
    last_provisioning_record_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Record identifier of the last request performed on this provisioned product.
    """
    last_record_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Record identifier of the last successful request performed on this provisioned product of the follow
    ing types: `ProvisionedProduct`, `UpdateProvisionedProduct`, `ExecuteProvisionedProductPlan`, `Termi
    nateProvisionedProduct`.
    """
    last_successful_provisioning_record_id: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the launch role associated with the provisioned product.
    """
    launch_role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) User-friendly name of the provisioned product.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.
    """
    notification_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The set of outputs for the product created.
    """
    outputs: list[Outputs] | core.ArrayOut[Outputs] = core.attr(
        Outputs, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Path identifier of the product. This value is optional if the product has a default path,
    and required if the product has more than one path. To list the paths for a product, use `aws_servi
    cecatalog_launch_paths`. When required, you must provide `path_id` or `path_name`, but not both.
    """
    path_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the path. You must provide `path_id` or `path_name`, but not both.
    """
    path_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Product identifier. For example, `prod-abcdzk7xy33qa`. You must provide `product_id` or `
    product_name`, but not both.
    """
    product_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the product. You must provide `product_id` or `product_name`, but not both.
    """
    product_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Identifier of the provisioning artifact. For example, `pa-4abcdjnxjj6ne`. You must provid
    e the `provisioning_artifact_id` or `provisioning_artifact_name`, but not both.
    """
    provisioning_artifact_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Name of the provisioning artifact. You must provide the `provisioning_artifact_id` or `pr
    ovisioning_artifact_name`, but not both.
    """
    provisioning_artifact_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block with parameters specified by the administrator that are required for
    provisioning the product. See details below.
    """
    provisioning_parameters: list[ProvisioningParameters] | core.ArrayOut[
        ProvisioningParameters
    ] | None = core.attr(ProvisioningParameters, default=None, kind=core.Kind.array)

    """
    (Optional) _Only applies to deleting._ Whether to delete the Service Catalog provisioned product but
    leave the CloudFormation stack, stack set, or the underlying resources of the deleted provisioned p
    roduct. The default value is `false`.
    """
    retain_physical_resources: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Configuration block with information about the provisioning preferences for a stack set.
    See details below.
    """
    stack_set_provisioning_preferences: StackSetProvisioningPreferences | None = core.attr(
        StackSetProvisioningPreferences, default=None
    )

    """
    Current status of the provisioned product. See meanings below.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Current status message of the provisioned product.
    """
    status_message: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Tags to apply to the provisioned product. If configured with a provider [`default_tags` c
    onfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-c
    onfiguration-block) present, tags with matching keys will overwrite those defined at the provider-le
    vel.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Type of provisioned product. Valid values are `CFN_STACK` and `CFN_STACKSET`.
    """
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
