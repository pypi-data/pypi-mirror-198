import terrascript.core as core


@core.schema
class DeploymentTargets(core.Schema):

    organizational_unit_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        organizational_unit_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=DeploymentTargets.Args(
                organizational_unit_ids=organizational_unit_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        organizational_unit_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


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


@core.resource(type="aws_cloudformation_stack_set_instance", namespace="cloudformation")
class StackSetInstance(core.Resource):
    """
    (Optional) Target AWS Account ID to create a Stack based on the StackSet. Defaults to current accoun
    t.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies whether you are acting as an account administrator in the organization's manage
    ment account or as a delegated administrator in a member account. Valid values: `SELF` (default), `D
    ELEGATED_ADMIN`.
    """
    call_as: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The AWS Organizations accounts to which StackSets deploys. StackSets doesn't deploy stack
    instances to the organization management account, even if the organization management account is in
    your organization or in an OU in your organization. Drift detection is not possible for this argume
    nt. See [deployment_targets](#deployment_targets-argument-reference) below.
    """
    deployment_targets: DeploymentTargets | None = core.attr(DeploymentTargets, default=None)

    """
    StackSet name, target AWS account ID, and target AWS region separated by commas (`,`)
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Preferences for how AWS CloudFormation performs a stack set operation.
    """
    operation_preferences: OperationPreferences | None = core.attr(
        OperationPreferences, default=None
    )

    """
    The organization root ID or organizational unit (OU) IDs specified for `deployment_targets`.
    """
    organizational_unit_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of input parameters to override from the StackSet for this Instance.
    """
    parameter_overrides: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
    """
    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) During Terraform resource destroy, remove Instance from StackSet while keeping the Stack
    and its associated resources. Must be enabled in Terraform state _before_ destroy operation to take
    effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. D
    efaults to `false`.
    """
    retain_stack: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Stack identifier
    """
    stack_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the StackSet.
    """
    stack_set_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        stack_set_name: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        call_as: str | core.StringOut | None = None,
        deployment_targets: DeploymentTargets | None = None,
        operation_preferences: OperationPreferences | None = None,
        parameter_overrides: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        region: str | core.StringOut | None = None,
        retain_stack: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StackSetInstance.Args(
                stack_set_name=stack_set_name,
                account_id=account_id,
                call_as=call_as,
                deployment_targets=deployment_targets,
                operation_preferences=operation_preferences,
                parameter_overrides=parameter_overrides,
                region=region,
                retain_stack=retain_stack,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        call_as: str | core.StringOut | None = core.arg(default=None)

        deployment_targets: DeploymentTargets | None = core.arg(default=None)

        operation_preferences: OperationPreferences | None = core.arg(default=None)

        parameter_overrides: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        region: str | core.StringOut | None = core.arg(default=None)

        retain_stack: bool | core.BoolOut | None = core.arg(default=None)

        stack_set_name: str | core.StringOut = core.arg()
