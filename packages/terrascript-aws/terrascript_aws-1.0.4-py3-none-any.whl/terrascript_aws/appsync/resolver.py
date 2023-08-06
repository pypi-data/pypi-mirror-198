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


@core.schema
class PipelineConfig(core.Schema):

    functions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        functions: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=PipelineConfig.Args(
                functions=functions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        functions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class CachingConfig(core.Schema):

    caching_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ttl: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        caching_keys: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ttl: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CachingConfig.Args(
                caching_keys=caching_keys,
                ttl=ttl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        caching_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ttl: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_appsync_resolver", namespace="appsync")
class Resolver(core.Resource):
    """
    (Required) The API ID for the GraphQL API.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    The ARN
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The CachingConfig.
    """
    caching_config: CachingConfig | None = core.attr(CachingConfig, default=None)

    """
    (Optional) The data source name.
    """
    data_source: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The field name from the schema defined in the GraphQL API.
    """
    field: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    kind: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The maximum batching size for a resolver. Valid values are between `0` and `2000`.
    """
    max_batch_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The PipelineConfig.
    """
    pipeline_config: PipelineConfig | None = core.attr(PipelineConfig, default=None)

    """
    (Optional) The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE
    resolver. Required for non-Lambda resolvers.
    """
    request_template: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE
    resolver. Required for non-Lambda resolvers.
    """
    response_template: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Describes a Sync configuration for a resolver. See [Sync Config](#sync-config).
    """
    sync_config: SyncConfig | None = core.attr(SyncConfig, default=None)

    """
    (Required) The type name from the schema defined in the GraphQL API.
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        field: str | core.StringOut,
        type: str | core.StringOut,
        caching_config: CachingConfig | None = None,
        data_source: str | core.StringOut | None = None,
        kind: str | core.StringOut | None = None,
        max_batch_size: int | core.IntOut | None = None,
        pipeline_config: PipelineConfig | None = None,
        request_template: str | core.StringOut | None = None,
        response_template: str | core.StringOut | None = None,
        sync_config: SyncConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Resolver.Args(
                api_id=api_id,
                field=field,
                type=type,
                caching_config=caching_config,
                data_source=data_source,
                kind=kind,
                max_batch_size=max_batch_size,
                pipeline_config=pipeline_config,
                request_template=request_template,
                response_template=response_template,
                sync_config=sync_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        caching_config: CachingConfig | None = core.arg(default=None)

        data_source: str | core.StringOut | None = core.arg(default=None)

        field: str | core.StringOut = core.arg()

        kind: str | core.StringOut | None = core.arg(default=None)

        max_batch_size: int | core.IntOut | None = core.arg(default=None)

        pipeline_config: PipelineConfig | None = core.arg(default=None)

        request_template: str | core.StringOut | None = core.arg(default=None)

        response_template: str | core.StringOut | None = core.arg(default=None)

        sync_config: SyncConfig | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
