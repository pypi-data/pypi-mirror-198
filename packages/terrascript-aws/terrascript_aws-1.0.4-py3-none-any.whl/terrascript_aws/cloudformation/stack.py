import terrascript.core as core


@core.resource(type="aws_cloudformation_stack", namespace="cloudformation")
class Stack(core.Resource):
    """
    (Optional) A list of capabilities.
    """

    capabilities: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Set to true to disable rollback of the stack if stack creation failed.
    """
    disable_rollback: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't
    specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If
    no role is available, AWS CloudFormation uses a temporary session that is generated from your user c
    redentials.
    """
    iam_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    A unique identifier of the stack.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Stack name.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of SNS topic ARNs to publish stack related events.
    """
    notification_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Action to be taken if stack creation fails. This must be
    """
    on_failure: str | core.StringOut | None = core.attr(str, default=None)

    """
    A map of outputs from the stack.
    """
    outputs: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    (Optional) A map of Parameter structures that specify input parameters for the stack.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Structure containing the stack policy body.
    """
    policy_body: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Location of a file containing the stack policy.
    """
    policy_url: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Map of resource tags to associate with this stack. If configured with a provider [`defaul
    t_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#defau
    lt_tags-configuration-block) present, tags with matching keys will overwrite those defined at the pr
    ovider-level.
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
    (Optional) Structure containing the template body (max size: 51,200 bytes).
    """
    template_body: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Location of a file containing the template body (max size: 460,800 bytes).
    """
    template_url: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The amount of time that can pass before the stack status becomes `CREATE_FAILED`.
    """
    timeout_in_minutes: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        capabilities: list[str] | core.ArrayOut[core.StringOut] | None = None,
        disable_rollback: bool | core.BoolOut | None = None,
        iam_role_arn: str | core.StringOut | None = None,
        notification_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        on_failure: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        policy_body: str | core.StringOut | None = None,
        policy_url: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        template_body: str | core.StringOut | None = None,
        template_url: str | core.StringOut | None = None,
        timeout_in_minutes: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stack.Args(
                name=name,
                capabilities=capabilities,
                disable_rollback=disable_rollback,
                iam_role_arn=iam_role_arn,
                notification_arns=notification_arns,
                on_failure=on_failure,
                parameters=parameters,
                policy_body=policy_body,
                policy_url=policy_url,
                tags=tags,
                tags_all=tags_all,
                template_body=template_body,
                template_url=template_url,
                timeout_in_minutes=timeout_in_minutes,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capabilities: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        disable_rollback: bool | core.BoolOut | None = core.arg(default=None)

        iam_role_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        notification_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        on_failure: str | core.StringOut | None = core.arg(default=None)

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        policy_body: str | core.StringOut | None = core.arg(default=None)

        policy_url: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        template_body: str | core.StringOut | None = core.arg(default=None)

        template_url: str | core.StringOut | None = core.arg(default=None)

        timeout_in_minutes: int | core.IntOut | None = core.arg(default=None)
