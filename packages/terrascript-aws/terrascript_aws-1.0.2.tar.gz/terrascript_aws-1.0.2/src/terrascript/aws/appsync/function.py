import terrascript.core as core


@core.schema
class LambdaConflictHandlerConfig(core.Schema):

    lambda_conflict_handler_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        lambda_conflict_handler_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LambdaConflictHandlerConfig.Args(
                lambda_conflict_handler_arn=lambda_conflict_handler_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_conflict_handler_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SyncConfig(core.Schema):

    conflict_detection: str | core.StringOut | None = core.attr(str, default=None)

    conflict_handler: str | core.StringOut | None = core.attr(str, default=None)

    lambda_conflict_handler_config: LambdaConflictHandlerConfig | None = core.attr(
        LambdaConflictHandlerConfig, default=None
    )

    def __init__(
        self,
        *,
        conflict_detection: str | core.StringOut | None = None,
        conflict_handler: str | core.StringOut | None = None,
        lambda_conflict_handler_config: LambdaConflictHandlerConfig | None = None,
    ):
        super().__init__(
            args=SyncConfig.Args(
                conflict_detection=conflict_detection,
                conflict_handler=conflict_handler,
                lambda_conflict_handler_config=lambda_conflict_handler_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        conflict_detection: str | core.StringOut | None = core.arg(default=None)

        conflict_handler: str | core.StringOut | None = core.arg(default=None)

        lambda_conflict_handler_config: LambdaConflictHandlerConfig | None = core.arg(default=None)


@core.resource(type="aws_appsync_function", namespace="aws_appsync")
class Function(core.Resource):

    api_id: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    data_source: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    function_id: str | core.StringOut = core.attr(str, computed=True)

    function_version: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    max_batch_size: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut = core.attr(str)

    request_mapping_template: str | core.StringOut = core.attr(str)

    response_mapping_template: str | core.StringOut = core.attr(str)

    sync_config: SyncConfig | None = core.attr(SyncConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        data_source: str | core.StringOut,
        name: str | core.StringOut,
        request_mapping_template: str | core.StringOut,
        response_mapping_template: str | core.StringOut,
        description: str | core.StringOut | None = None,
        function_version: str | core.StringOut | None = None,
        max_batch_size: int | core.IntOut | None = None,
        sync_config: SyncConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Function.Args(
                api_id=api_id,
                data_source=data_source,
                name=name,
                request_mapping_template=request_mapping_template,
                response_mapping_template=response_mapping_template,
                description=description,
                function_version=function_version,
                max_batch_size=max_batch_size,
                sync_config=sync_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        data_source: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        function_version: str | core.StringOut | None = core.arg(default=None)

        max_batch_size: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        request_mapping_template: str | core.StringOut = core.arg()

        response_mapping_template: str | core.StringOut = core.arg()

        sync_config: SyncConfig | None = core.arg(default=None)
