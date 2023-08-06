import terrascript.core as core


@core.resource(type="aws_acmpca_permission", namespace="aws_acmpca")
class Permission(core.Resource):

    actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    certificate_authority_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str, computed=True)

    principal: str | core.StringOut = core.attr(str)

    source_account: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        actions: list[str] | core.ArrayOut[core.StringOut],
        certificate_authority_arn: str | core.StringOut,
        principal: str | core.StringOut,
        source_account: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permission.Args(
                actions=actions,
                certificate_authority_arn=certificate_authority_arn,
                principal=principal,
                source_account=source_account,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        certificate_authority_arn: str | core.StringOut = core.arg()

        principal: str | core.StringOut = core.arg()

        source_account: str | core.StringOut | None = core.arg(default=None)
