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


@core.resource(type="aws_config_config_rule", namespace="config")
class ConfigRule(core.Resource):
    """
    The ARN of the config rule
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the rule
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A string in JSON format that is passed to the AWS Config rule Lambda function.
    """
    input_parameters: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The maximum frequency with which AWS Config runs evaluations for a rule.
    """
    maximum_execution_frequency: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the rule
    """
    name: str | core.StringOut = core.attr(str)

    """
    The ID of the config rule
    """
    rule_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Scope defines which resources can trigger an evaluation for the rule. See [Source](#sourc
    e) Below.
    """
    scope: Scope | None = core.attr(Scope, default=None)

    """
    (Required) Source specifies the rule owner, the rule identifier, and the notifications that cause th
    e function to evaluate your AWS resources. See [Scope](#scope) Below.
    """
    source: Source = core.attr(Source)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
