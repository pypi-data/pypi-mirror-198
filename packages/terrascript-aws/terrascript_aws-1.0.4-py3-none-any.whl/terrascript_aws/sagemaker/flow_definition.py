import terrascript.core as core


@core.schema
class AmountInUsd(core.Schema):

    cents: int | core.IntOut | None = core.attr(int, default=None)

    dollars: int | core.IntOut | None = core.attr(int, default=None)

    tenth_fractions_of_a_cent: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cents: int | core.IntOut | None = None,
        dollars: int | core.IntOut | None = None,
        tenth_fractions_of_a_cent: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AmountInUsd.Args(
                cents=cents,
                dollars=dollars,
                tenth_fractions_of_a_cent=tenth_fractions_of_a_cent,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cents: int | core.IntOut | None = core.arg(default=None)

        dollars: int | core.IntOut | None = core.arg(default=None)

        tenth_fractions_of_a_cent: int | core.IntOut | None = core.arg(default=None)


@core.schema
class PublicWorkforceTaskPrice(core.Schema):

    amount_in_usd: AmountInUsd | None = core.attr(AmountInUsd, default=None)

    def __init__(
        self,
        *,
        amount_in_usd: AmountInUsd | None = None,
    ):
        super().__init__(
            args=PublicWorkforceTaskPrice.Args(
                amount_in_usd=amount_in_usd,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amount_in_usd: AmountInUsd | None = core.arg(default=None)


@core.schema
class HumanLoopConfig(core.Schema):

    human_task_ui_arn: str | core.StringOut = core.attr(str)

    public_workforce_task_price: PublicWorkforceTaskPrice | None = core.attr(
        PublicWorkforceTaskPrice, default=None
    )

    task_availability_lifetime_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    task_count: int | core.IntOut = core.attr(int)

    task_description: str | core.StringOut = core.attr(str)

    task_keywords: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    task_time_limit_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    task_title: str | core.StringOut = core.attr(str)

    workteam_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        human_task_ui_arn: str | core.StringOut,
        task_count: int | core.IntOut,
        task_description: str | core.StringOut,
        task_title: str | core.StringOut,
        workteam_arn: str | core.StringOut,
        public_workforce_task_price: PublicWorkforceTaskPrice | None = None,
        task_availability_lifetime_in_seconds: int | core.IntOut | None = None,
        task_keywords: list[str] | core.ArrayOut[core.StringOut] | None = None,
        task_time_limit_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=HumanLoopConfig.Args(
                human_task_ui_arn=human_task_ui_arn,
                task_count=task_count,
                task_description=task_description,
                task_title=task_title,
                workteam_arn=workteam_arn,
                public_workforce_task_price=public_workforce_task_price,
                task_availability_lifetime_in_seconds=task_availability_lifetime_in_seconds,
                task_keywords=task_keywords,
                task_time_limit_in_seconds=task_time_limit_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        human_task_ui_arn: str | core.StringOut = core.arg()

        public_workforce_task_price: PublicWorkforceTaskPrice | None = core.arg(default=None)

        task_availability_lifetime_in_seconds: int | core.IntOut | None = core.arg(default=None)

        task_count: int | core.IntOut = core.arg()

        task_description: str | core.StringOut = core.arg()

        task_keywords: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        task_time_limit_in_seconds: int | core.IntOut | None = core.arg(default=None)

        task_title: str | core.StringOut = core.arg()

        workteam_arn: str | core.StringOut = core.arg()


@core.schema
class OutputConfig(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    s3_output_path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        s3_output_path: str | core.StringOut,
        kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=OutputConfig.Args(
                s3_output_path=s3_output_path,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        s3_output_path: str | core.StringOut = core.arg()


@core.schema
class HumanLoopActivationConditionsConfig(core.Schema):

    human_loop_activation_conditions: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        human_loop_activation_conditions: str | core.StringOut,
    ):
        super().__init__(
            args=HumanLoopActivationConditionsConfig.Args(
                human_loop_activation_conditions=human_loop_activation_conditions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        human_loop_activation_conditions: str | core.StringOut = core.arg()


@core.schema
class HumanLoopActivationConfig(core.Schema):

    human_loop_activation_conditions_config: HumanLoopActivationConditionsConfig | None = core.attr(
        HumanLoopActivationConditionsConfig, default=None
    )

    def __init__(
        self,
        *,
        human_loop_activation_conditions_config: HumanLoopActivationConditionsConfig | None = None,
    ):
        super().__init__(
            args=HumanLoopActivationConfig.Args(
                human_loop_activation_conditions_config=human_loop_activation_conditions_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        human_loop_activation_conditions_config: HumanLoopActivationConditionsConfig | None = (
            core.arg(default=None)
        )


@core.schema
class HumanLoopRequestSource(core.Schema):

    aws_managed_human_loop_request_source: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        aws_managed_human_loop_request_source: str | core.StringOut,
    ):
        super().__init__(
            args=HumanLoopRequestSource.Args(
                aws_managed_human_loop_request_source=aws_managed_human_loop_request_source,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_managed_human_loop_request_source: str | core.StringOut = core.arg()


@core.resource(type="aws_sagemaker_flow_definition", namespace="sagemaker")
class FlowDefinition(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this Flow Definition.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of your flow definition.
    """
    flow_definition_name: str | core.StringOut = core.attr(str)

    """
    (Optional) An object containing information about the events that trigger a human workflow. See [Hum
    an Loop Activation Config](#human-loop-activation-config) details below.
    """
    human_loop_activation_config: HumanLoopActivationConfig | None = core.attr(
        HumanLoopActivationConfig, default=None
    )

    """
    (Required)  An object containing information about the tasks the human reviewers will perform. See [
    Human Loop Config](#human-loop-config) details below.
    """
    human_loop_config: HumanLoopConfig = core.attr(HumanLoopConfig)

    """
    (Optional) Container for configuring the source of human task requests. Use to specify if Amazon Rek
    ognition or Amazon Textract is used as an integration source. See [Human Loop Request Source](#human
    loop-request-source) details below.
    """
    human_loop_request_source: HumanLoopRequestSource | None = core.attr(
        HumanLoopRequestSource, default=None
    )

    """
    The name of the Flow Definition.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) An object containing information about where the human review results will be uploaded. S
    ee [Output Config](#output-config) details below.
    """
    output_config: OutputConfig = core.attr(OutputConfig)

    """
    (Required) The Amazon Resource Name (ARN) of the role needed to call other services on your behalf.
    """
    role_arn: str | core.StringOut = core.attr(str)

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
        flow_definition_name: str | core.StringOut,
        human_loop_config: HumanLoopConfig,
        output_config: OutputConfig,
        role_arn: str | core.StringOut,
        human_loop_activation_config: HumanLoopActivationConfig | None = None,
        human_loop_request_source: HumanLoopRequestSource | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FlowDefinition.Args(
                flow_definition_name=flow_definition_name,
                human_loop_config=human_loop_config,
                output_config=output_config,
                role_arn=role_arn,
                human_loop_activation_config=human_loop_activation_config,
                human_loop_request_source=human_loop_request_source,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        flow_definition_name: str | core.StringOut = core.arg()

        human_loop_activation_config: HumanLoopActivationConfig | None = core.arg(default=None)

        human_loop_config: HumanLoopConfig = core.arg()

        human_loop_request_source: HumanLoopRequestSource | None = core.arg(default=None)

        output_config: OutputConfig = core.arg()

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
