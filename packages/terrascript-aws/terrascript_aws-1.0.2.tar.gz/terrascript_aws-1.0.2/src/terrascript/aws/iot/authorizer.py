import terrascript.core as core


@core.resource(type="aws_iot_authorizer", namespace="aws_iot")
class Authorizer(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    authorizer_function_arn: str | core.StringOut = core.attr(str)

    enable_caching_for_http: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    signing_disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    status: str | core.StringOut | None = core.attr(str, default=None)

    token_key_name: str | core.StringOut | None = core.attr(str, default=None)

    token_signing_public_keys: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        authorizer_function_arn: str | core.StringOut,
        name: str | core.StringOut,
        enable_caching_for_http: bool | core.BoolOut | None = None,
        signing_disabled: bool | core.BoolOut | None = None,
        status: str | core.StringOut | None = None,
        token_key_name: str | core.StringOut | None = None,
        token_signing_public_keys: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Authorizer.Args(
                authorizer_function_arn=authorizer_function_arn,
                name=name,
                enable_caching_for_http=enable_caching_for_http,
                signing_disabled=signing_disabled,
                status=status,
                token_key_name=token_key_name,
                token_signing_public_keys=token_signing_public_keys,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authorizer_function_arn: str | core.StringOut = core.arg()

        enable_caching_for_http: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        signing_disabled: bool | core.BoolOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        token_key_name: str | core.StringOut | None = core.arg(default=None)

        token_signing_public_keys: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )
