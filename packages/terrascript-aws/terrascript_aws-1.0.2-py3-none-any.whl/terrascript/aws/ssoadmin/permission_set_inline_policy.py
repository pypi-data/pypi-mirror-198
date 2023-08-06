import terrascript.core as core


@core.resource(type="aws_ssoadmin_permission_set_inline_policy", namespace="aws_ssoadmin")
class PermissionSetInlinePolicy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    inline_policy: str | core.StringOut = core.attr(str)

    instance_arn: str | core.StringOut = core.attr(str)

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
