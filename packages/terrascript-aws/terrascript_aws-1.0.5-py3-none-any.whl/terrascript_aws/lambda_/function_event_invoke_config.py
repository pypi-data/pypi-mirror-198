import terrascript.core as core


@core.schema
class OnFailure(core.Schema):

    destination: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        destination: str | core.StringOut,
    ):
        super().__init__(
            args=OnFailure.Args(
                destination=destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: str | core.StringOut = core.arg()


@core.schema
class OnSuccess(core.Schema):

    destination: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        destination: str | core.StringOut,
    ):
        super().__init__(
            args=OnSuccess.Args(
                destination=destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: str | core.StringOut = core.arg()


@core.schema
class DestinationConfig(core.Schema):

    on_failure: OnFailure | None = core.attr(OnFailure, default=None)

    on_success: OnSuccess | None = core.attr(OnSuccess, default=None)

    def __init__(
        self,
        *,
        on_failure: OnFailure | None = None,
        on_success: OnSuccess | None = None,
    ):
        super().__init__(
            args=DestinationConfig.Args(
                on_failure=on_failure,
                on_success=on_success,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_failure: OnFailure | None = core.arg(default=None)

        on_success: OnSuccess | None = core.arg(default=None)


@core.resource(type="aws_lambda_function_event_invoke_config", namespace="lambda_")
class FunctionEventInvokeConfig(core.Resource):
    """
    (Optional) Configuration block with destination configuration. See below for details.
    """

    destination_config: DestinationConfig | None = core.attr(DestinationConfig, default=None)

    """
    (Required) Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias
    qualifier.
    """
    function_name: str | core.StringOut = core.attr(str)

    """
    Fully qualified Lambda Function name or Amazon Resource Name (ARN)
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Maximum age of a request that Lambda sends to a function for processing in seconds. Valid
    values between 60 and 21600.
    """
    maximum_event_age_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Maximum number of times to retry when the function returns an error. Valid values between
    0 and 2. Defaults to 2.
    """
    maximum_retry_attempts: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Lambda Function published version, `$LATEST`, or Lambda Alias name.
    """
    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: str | core.StringOut,
        destination_config: DestinationConfig | None = None,
        maximum_event_age_in_seconds: int | core.IntOut | None = None,
        maximum_retry_attempts: int | core.IntOut | None = None,
        qualifier: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FunctionEventInvokeConfig.Args(
                function_name=function_name,
                destination_config=destination_config,
                maximum_event_age_in_seconds=maximum_event_age_in_seconds,
                maximum_retry_attempts=maximum_retry_attempts,
                qualifier=qualifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_config: DestinationConfig | None = core.arg(default=None)

        function_name: str | core.StringOut = core.arg()

        maximum_event_age_in_seconds: int | core.IntOut | None = core.arg(default=None)

        maximum_retry_attempts: int | core.IntOut | None = core.arg(default=None)

        qualifier: str | core.StringOut | None = core.arg(default=None)
