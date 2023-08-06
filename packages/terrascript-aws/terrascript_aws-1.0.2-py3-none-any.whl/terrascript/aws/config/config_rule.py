import terrascript.core as core


@core.schema
class Scope(core.Schema):

    compliance_resource_id: str | core.StringOut | None = core.attr(str, default=None)

    compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tag_key: str | core.StringOut | None = core.attr(str, default=None)

    tag_value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        compliance_resource_id: str | core.StringOut | None = None,
        compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tag_key: str | core.StringOut | None = None,
        tag_value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Scope.Args(
                compliance_resource_id=compliance_resource_id,
                compliance_resource_types=compliance_resource_types,
                tag_key=tag_key,
                tag_value=tag_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_resource_id: str | core.StringOut | None = core.arg(default=None)

        compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tag_key: str | core.StringOut | None = core.arg(default=None)

        tag_value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SourceDetail(core.Schema):

    event_source: str | core.StringOut | None = core.attr(str, default=None)

    maximum_execution_frequency: str | core.StringOut | None = core.attr(str, default=None)

    message_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        event_source: str | core.StringOut | None = None,
        maximum_execution_frequency: str | core.StringOut | None = None,
        message_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SourceDetail.Args(
                event_source=event_source,
                maximum_execution_frequency=maximum_execution_frequency,
                message_type=message_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_source: str | core.StringOut | None = core.arg(default=None)

        maximum_execution_frequency: str | core.StringOut | None = core.arg(default=None)

        message_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CustomPolicyDetails(core.Schema):

    enable_debug_log_delivery: bool | core.BoolOut | None = core.attr(bool, default=None)

    policy_runtime: str | core.StringOut = core.attr(str)

    policy_text: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        policy_runtime: str | core.StringOut,
        policy_text: str | core.StringOut,
        enable_debug_log_delivery: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=CustomPolicyDetails.Args(
                policy_runtime=policy_runtime,
                policy_text=policy_text,
                enable_debug_log_delivery=enable_debug_log_delivery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_debug_log_delivery: bool | core.BoolOut | None = core.arg(default=None)

        policy_runtime: str | core.StringOut = core.arg()

        policy_text: str | core.StringOut = core.arg()


@core.schema
class Source(core.Schema):

    custom_policy_details: CustomPolicyDetails | None = core.attr(CustomPolicyDetails, default=None)

    owner: str | core.StringOut = core.attr(str)

    source_detail: list[SourceDetail] | core.ArrayOut[SourceDetail] | None = core.attr(
        SourceDetail, default=None, kind=core.Kind.array
    )

    source_identifier: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        owner: str | core.StringOut,
        custom_policy_details: CustomPolicyDetails | None = None,
        source_detail: list[SourceDetail] | core.ArrayOut[SourceDetail] | None = None,
        source_identifier: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Source.Args(
                owner=owner,
                custom_policy_details=custom_policy_details,
                source_detail=source_detail,
                source_identifier=source_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_policy_details: CustomPolicyDetails | None = core.arg(default=None)

        owner: str | core.StringOut = core.arg()

        source_detail: list[SourceDetail] | core.ArrayOut[SourceDetail] | None = core.arg(
            default=None
        )

        source_identifier: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_config_config_rule", namespace="aws_config")
class ConfigRule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    input_parameters: str | core.StringOut | None = core.attr(str, default=None)

    maximum_execution_frequency: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    rule_id: str | core.StringOut = core.attr(str, computed=True)

    scope: Scope | None = core.attr(Scope, default=None)

    source: Source = core.attr(Source)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        source: Source,
        description: str | core.StringOut | None = None,
        input_parameters: str | core.StringOut | None = None,
        maximum_execution_frequency: str | core.StringOut | None = None,
        scope: Scope | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigRule.Args(
                name=name,
                source=source,
                description=description,
                input_parameters=input_parameters,
                maximum_execution_frequency=maximum_execution_frequency,
                scope=scope,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        input_parameters: str | core.StringOut | None = core.arg(default=None)

        maximum_execution_frequency: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        scope: Scope | None = core.arg(default=None)

        source: Source = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
