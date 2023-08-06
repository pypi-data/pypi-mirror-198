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


@core.resource(type="aws_cloudformation_stack_set", namespace="cloudformation")
class StackSet(core.Resource):
    """
    (Optional) Amazon Resource Number (ARN) of the IAM Role in the administrator account. This must be d
    efined when using the `SELF_MANAGED` permission model.
    """

    administration_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    Amazon Resource Name (ARN) of the StackSet.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block containing the auto-deployment model for your StackSet. This can only
    be defined when using the `SERVICE_MANAGED` permission model.
    """
    auto_deployment: AutoDeployment | None = core.attr(AutoDeployment, default=None)

    """
    (Optional) Specifies whether you are acting as an account administrator in the organization's manage
    ment account or as a delegated administrator in a member account. Valid values: `SELF` (default), `D
    ELEGATED_ADMIN`.
    """
    call_as: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILI
    TY_AUTO_EXPAND`.
    """
    capabilities: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Description of the StackSet.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSClou
    dFormationStackSetExecutionRole` when using the `SELF_MANAGED` permission model. This should not be
    defined when using the `SERVICE_MANAGED` permission model.
    """
    execution_role_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Name of the StackSet.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the StackSet. The name must be unique in the region where you create your StackSe
    t. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start wit
    h an alphabetic character and cannot be longer than 128 characters.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Preferences for how AWS CloudFormation performs a stack set update.
    """
    operation_preferences: OperationPreferences | None = core.attr(
        OperationPreferences, default=None
    )

    """
    (Optional) Key-value map of input parameters for the StackSet template. All template parameters, inc
    luding those with a `Default`, must be configured or ignored with `lifecycle` configuration block `i
    gnore_changes` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` confi
    guration block `ignore_changes` argument.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Describes how the IAM roles required for your StackSet are created. Valid values: `SELF_M
    ANAGED` (default), `SERVICE_MANAGED`.
    """
    permission_model: str | core.StringOut | None = core.attr(str, default=None)

    """
    Unique identifier of the StackSet.
    """
    stack_set_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS
    CloudFormation also propagates these tags to supported resources that are created in the Stacks. A
    maximum number of 50 tags can be specified. If configured with a provider [`default_tags` configurat
    ion block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurat
    ion-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Optional) String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts
    with `template_url`.
    """
    template_body: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) String containing the location of a file containing the CloudFormation template body. The
    URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 46
    0,800 bytes. Conflicts with `template_body`.
    """
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
