import terrascript.core as core


@core.resource(type="aws_iot_authorizer", namespace="iot")
class Authorizer(core.Resource):
    """
    The ARN of the authorizer.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN of the authorizer's Lambda function.
    """
    authorizer_function_arn: str | core.StringOut = core.attr(str)

    enable_caching_for_http: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the authorizer.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies whether AWS IoT validates the token signature in an authorization request. Defa
    ult: `false`.
    """
    signing_disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The status of Authorizer request at creation. Valid values: `ACTIVE`, `INACTIVE`. Default
    : `ACTIVE`.
    """
    status: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the token key used to extract the token from the HTTP headers. This value is
    required if signing is enabled in your authorizer.
    """
    token_key_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The public keys used to verify the digital signature returned by your custom authenticati
    on service. This value is required if signing is enabled in your authorizer.
    """
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
