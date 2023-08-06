import terrascript.core as core


@core.resource(type="aws_cognito_user", namespace="cognito")
class User(core.Resource):
    """
    (Optional) A map that contains user attributes and attribute values to be set for the user.
    """

    attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) A map of custom key-value pairs that you can provide as input for any custom workflows th
    at user creation triggers. Amazon Cognito does not store the `client_metadata` value. This data is a
    vailable only to Lambda triggers that are assigned to a user pool to support custom workflows. If yo
    ur user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose
    . For more information, see [Customizing User Pool Workflows with Lambda Triggers](https://docs.aws.
    amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-trigger
    s.html).
    """
    client_metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of mediums to the welcome message will be sent through. Allowed values are `EMAIL`
    and `SMS`. If it's provided, make sure you have also specified `email` attribute for the `EMAIL` me
    dium and `phone_number` for the `SMS`. More than one value can be specified. Amazon Cognito does not
    store the `desired_delivery_mediums` value. Defaults to `["SMS"]`.
    """
    desired_delivery_mediums: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Specifies whether the user should be enabled after creation. The welcome message will be
    sent regardless of the `enabled` value. The behavior can be changed with `message_action` argument.
    Defaults to `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) If this parameter is set to True and the `phone_number` or `email` address specified in t
    he `attributes` parameter already exists as an alias with a different user, Amazon Cognito will migr
    ate the alias from the previous user to the newly created user. The previous user will no longer be
    able to log in using that alias. Amazon Cognito does not store the `force_alias_creation` value. Def
    aults to `false`.
    """
    force_alias_creation: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_modified_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set to `RESEND` to resend the invitation message to a user that already exists and reset
    the expiration limit on the user's account. Set to `SUPPRESS` to suppress sending the message. Only
    one value can be specified. Amazon Cognito does not store the `message_action` value.
    """
    message_action: str | core.StringOut | None = core.attr(str, default=None)

    mfa_setting_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The user's permanent password. This password must conform to the password policy specifie
    d by user pool the user belongs to. The welcome message always contains only `temporary_password` va
    lue. You can suppress sending the welcome message with the `message_action` argument. Amazon Cognito
    does not store the `password` value. Conflicts with `temporary_password`.
    """
    password: str | core.StringOut | None = core.attr(str, default=None)

    preferred_mfa_setting: str | core.StringOut = core.attr(str, computed=True)

    """
    current user status.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    unique user id that is never reassignable to another user.
    """
    sub: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The user's temporary password. Conflicts with `password`.
    """
    temporary_password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The user pool ID for the user pool where the user will be created.
    """
    user_pool_id: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    """
    (Optional) The user's validation data. This is an array of name-value pairs that contain user attrib
    utes and attribute values that you can use for custom validation, such as restricting the types of u
    ser accounts that can be registered. Amazon Cognito does not store the `validation_data` value. For
    more information, see [Customizing User Pool Workflows with Lambda Triggers](https://docs.aws.amazon
    .com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html
    ).
    """
    validation_data: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        user_pool_id: str | core.StringOut,
        username: str | core.StringOut,
        attributes: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        client_metadata: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        desired_delivery_mediums: list[str] | core.ArrayOut[core.StringOut] | None = None,
        enabled: bool | core.BoolOut | None = None,
        force_alias_creation: bool | core.BoolOut | None = None,
        message_action: str | core.StringOut | None = None,
        password: str | core.StringOut | None = None,
        temporary_password: str | core.StringOut | None = None,
        validation_data: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                user_pool_id=user_pool_id,
                username=username,
                attributes=attributes,
                client_metadata=client_metadata,
                desired_delivery_mediums=desired_delivery_mediums,
                enabled=enabled,
                force_alias_creation=force_alias_creation,
                message_action=message_action,
                password=password,
                temporary_password=temporary_password,
                validation_data=validation_data,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        client_metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        desired_delivery_mediums: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        force_alias_creation: bool | core.BoolOut | None = core.arg(default=None)

        message_action: str | core.StringOut | None = core.arg(default=None)

        password: str | core.StringOut | None = core.arg(default=None)

        temporary_password: str | core.StringOut | None = core.arg(default=None)

        user_pool_id: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()

        validation_data: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )
