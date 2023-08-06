import terrascript.core as core


@core.resource(type="aws_cloudformation_stack", namespace="aws_cloudformation")
class Stack(core.Resource):

    capabilities: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    disable_rollback: bool | core.BoolOut | None = core.attr(bool, default=None)

    iam_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    notification_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    on_failure: str | core.StringOut | None = core.attr(str, default=None)

    outputs: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    policy_body: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    policy_url: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    template_body: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    template_url: str | core.StringOut | None = core.attr(str, default=None)

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
