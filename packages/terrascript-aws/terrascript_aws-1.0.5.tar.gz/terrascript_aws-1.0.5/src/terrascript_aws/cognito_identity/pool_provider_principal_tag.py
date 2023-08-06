import terrascript.core as core


@core.resource(
    type="aws_cognito_identity_pool_provider_principal_tag", namespace="cognito_identity"
)
class PoolProviderPrincipalTag(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_pool_id: str | core.StringOut = core.attr(str)

    identity_provider_name: str | core.StringOut = core.attr(str)

    principal_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    use_defaults: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        identity_pool_id: str | core.StringOut,
        identity_provider_name: str | core.StringOut,
        principal_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        use_defaults: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PoolProviderPrincipalTag.Args(
                identity_pool_id=identity_pool_id,
                identity_provider_name=identity_provider_name,
                principal_tags=principal_tags,
                use_defaults=use_defaults,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity_pool_id: str | core.StringOut = core.arg()

        identity_provider_name: str | core.StringOut = core.arg()

        principal_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        use_defaults: bool | core.BoolOut | None = core.arg(default=None)
