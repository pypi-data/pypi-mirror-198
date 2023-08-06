import terrascript.core as core


@core.resource(type="aws_ssoadmin_permission_set_inline_policy", namespace="ssoadmin")
class PermissionSetInlinePolicy(core.Resource):
    """
    The Amazon Resource Names (ARNs) of the Permission Set and SSO Instance, separated by a comma (`,`).
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The IAM inline policy to attach to a Permission Set.
    """
    inline_policy: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the SSO Instance under which the o
    peration will be executed.
    """
    instance_arn: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the Permission Set.
    """
    permission_set_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        inline_policy: str | core.StringOut,
        instance_arn: str | core.StringOut,
        permission_set_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PermissionSetInlinePolicy.Args(
                inline_policy=inline_policy,
                instance_arn=instance_arn,
                permission_set_arn=permission_set_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        inline_policy: str | core.StringOut = core.arg()

        instance_arn: str | core.StringOut = core.arg()

        permission_set_arn: str | core.StringOut = core.arg()
