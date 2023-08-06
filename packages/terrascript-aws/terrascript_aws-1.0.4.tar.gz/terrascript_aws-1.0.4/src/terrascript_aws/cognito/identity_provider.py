import terrascript.core as core


@core.resource(type="aws_cognito_identity_provider", namespace="cognito")
class IdentityProvider(core.Resource):

    attribute_mapping: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    idp_identifiers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    provider_details: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, kind=core.Kind.map
    )

    provider_name: str | core.StringOut = core.attr(str)

    provider_type: str | core.StringOut = core.attr(str)

    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        provider_details: dict[str, str] | core.MapOut[core.StringOut],
        provider_name: str | core.StringOut,
        provider_type: str | core.StringOut,
        user_pool_id: str | core.StringOut,
        attribute_mapping: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        idp_identifiers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=IdentityProvider.Args(
                provider_details=provider_details,
                provider_name=provider_name,
                provider_type=provider_type,
                user_pool_id=user_pool_id,
                attribute_mapping=attribute_mapping,
                idp_identifiers=idp_identifiers,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attribute_mapping: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        idp_identifiers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        provider_details: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        provider_name: str | core.StringOut = core.arg()

        provider_type: str | core.StringOut = core.arg()

        user_pool_id: str | core.StringOut = core.arg()
