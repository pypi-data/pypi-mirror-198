import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    resource_value: str | core.StringOut | None = core.attr(str, default=None)

    static_value: str | core.StringOut | None = core.attr(str, default=None)

    static_values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        resource_value: str | core.StringOut | None = None,
        static_value: str | core.StringOut | None = None,
        static_values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                resource_value=resource_value,
                static_value=static_value,
                static_values=static_values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        resource_value: str | core.StringOut | None = core.arg(default=None)

        static_value: str | core.StringOut | None = core.arg(default=None)

        static_values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class SsmControls(core.Schema):

    concurrent_execution_rate_percentage: int | core.IntOut | None = core.attr(int, default=None)

    error_percentage: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        concurrent_execution_rate_percentage: int | core.IntOut | None = None,
        error_percentage: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=SsmControls.Args(
                concurrent_execution_rate_percentage=concurrent_execution_rate_percentage,
                error_percentage=error_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        concurrent_execution_rate_percentage: int | core.IntOut | None = core.arg(default=None)

        error_percentage: int | core.IntOut | None = core.arg(default=None)


@core.schema
class ExecutionControls(core.Schema):

    ssm_controls: SsmControls | None = core.attr(SsmControls, default=None)

    def __init__(
        self,
        *,
        ssm_controls: SsmControls | None = None,
    ):
        super().__init__(
            args=ExecutionControls.Args(
                ssm_controls=ssm_controls,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ssm_controls: SsmControls | None = core.arg(default=None)


@core.resource(type="aws_config_remediation_configuration", namespace="config")
class RemediationConfiguration(core.Resource):
    """
    ARN of the Config Remediation Configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Remediation is triggered automatically if `true`.
    """
    automatic: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Name of the AWS Config rule.
    """
    config_rule_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block for execution controls. See below.
    """
    execution_controls: ExecutionControls | None = core.attr(ExecutionControls, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Maximum number of failed attempts for auto-remediation. If you do not select a number, th
    e default is 5.
    """
    maximum_automatic_attempts: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Can be specified multiple times for each parameter. Each parameter block supports argumen
    ts below.
    """
    parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    """
    (Optional) Type of resource.
    """
    resource_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a num
    ber, the default is 60 seconds.
    """
    retry_attempt_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) Target ID is the name of the public document.
    """
    target_id: str | core.StringOut = core.attr(str)

    """
    (Required) Type of the target. Target executes remediation. For example, SSM document.
    """
    target_type: str | core.StringOut = core.attr(str)

    """
    (Optional) Version of the target. For example, version of the SSM document
    """
    target_version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        config_rule_name: str | core.StringOut,
        target_id: str | core.StringOut,
        target_type: str | core.StringOut,
        automatic: bool | core.BoolOut | None = None,
        execution_controls: ExecutionControls | None = None,
        maximum_automatic_attempts: int | core.IntOut | None = None,
        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = None,
        resource_type: str | core.StringOut | None = None,
        retry_attempt_seconds: int | core.IntOut | None = None,
        target_version: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RemediationConfiguration.Args(
                config_rule_name=config_rule_name,
                target_id=target_id,
                target_type=target_type,
                automatic=automatic,
                execution_controls=execution_controls,
                maximum_automatic_attempts=maximum_automatic_attempts,
                parameter=parameter,
                resource_type=resource_type,
                retry_attempt_seconds=retry_attempt_seconds,
                target_version=target_version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        automatic: bool | core.BoolOut | None = core.arg(default=None)

        config_rule_name: str | core.StringOut = core.arg()

        execution_controls: ExecutionControls | None = core.arg(default=None)

        maximum_automatic_attempts: int | core.IntOut | None = core.arg(default=None)

        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.arg(default=None)

        resource_type: str | core.StringOut | None = core.arg(default=None)

        retry_attempt_seconds: int | core.IntOut | None = core.arg(default=None)

        target_id: str | core.StringOut = core.arg()

        target_type: str | core.StringOut = core.arg()

        target_version: str | core.StringOut | None = core.arg(default=None)
