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


@core.resource(type="aws_config_remediation_configuration", namespace="aws_config")
class RemediationConfiguration(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    automatic: bool | core.BoolOut | None = core.attr(bool, default=None)

    config_rule_name: str | core.StringOut = core.attr(str)

    execution_controls: ExecutionControls | None = core.attr(ExecutionControls, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    maximum_automatic_attempts: int | core.IntOut | None = core.attr(int, default=None)

    parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    resource_type: str | core.StringOut | None = core.attr(str, default=None)

    retry_attempt_seconds: int | core.IntOut | None = core.attr(int, default=None)

    target_id: str | core.StringOut = core.attr(str)

    target_type: str | core.StringOut = core.attr(str)

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
