import terrascript.core as core


@core.schema
class SmsConfiguration(core.Schema):

    external_id: str | core.StringOut = core.attr(str)

    sns_caller_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        external_id: str | core.StringOut,
        sns_caller_arn: str | core.StringOut,
    ):
        super().__init__(
            args=SmsConfiguration.Args(
                external_id=external_id,
                sns_caller_arn=sns_caller_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        external_id: str | core.StringOut = core.arg()

        sns_caller_arn: str | core.StringOut = core.arg()


@core.schema
class NumberAttributeConstraints(core.Schema):

    max_value: str | core.StringOut | None = core.attr(str, default=None)

    min_value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_value: str | core.StringOut | None = None,
        min_value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NumberAttributeConstraints.Args(
                max_value=max_value,
                min_value=min_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_value: str | core.StringOut | None = core.arg(default=None)

        min_value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class StringAttributeConstraints(core.Schema):

    max_length: str | core.StringOut | None = core.attr(str, default=None)

    min_length: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_length: str | core.StringOut | None = None,
        min_length: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StringAttributeConstraints.Args(
                max_length=max_length,
                min_length=min_length,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_length: str | core.StringOut | None = core.arg(default=None)

        min_length: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Schema(core.Schema):

    attribute_data_type: str | core.StringOut = core.attr(str)

    developer_only_attribute: bool | core.BoolOut | None = core.attr(bool, default=None)

    mutable: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut = core.attr(str)

    number_attribute_constraints: NumberAttributeConstraints | None = core.attr(
        NumberAttributeConstraints, default=None
    )

    required: bool | core.BoolOut | None = core.attr(bool, default=None)

    string_attribute_constraints: StringAttributeConstraints | None = core.attr(
        StringAttributeConstraints, default=None
    )

    def __init__(
        self,
        *,
        attribute_data_type: str | core.StringOut,
        name: str | core.StringOut,
        developer_only_attribute: bool | core.BoolOut | None = None,
        mutable: bool | core.BoolOut | None = None,
        number_attribute_constraints: NumberAttributeConstraints | None = None,
        required: bool | core.BoolOut | None = None,
        string_attribute_constraints: StringAttributeConstraints | None = None,
    ):
        super().__init__(
            args=Schema.Args(
                attribute_data_type=attribute_data_type,
                name=name,
                developer_only_attribute=developer_only_attribute,
                mutable=mutable,
                number_attribute_constraints=number_attribute_constraints,
                required=required,
                string_attribute_constraints=string_attribute_constraints,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute_data_type: str | core.StringOut = core.arg()

        developer_only_attribute: bool | core.BoolOut | None = core.arg(default=None)

        mutable: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        number_attribute_constraints: NumberAttributeConstraints | None = core.arg(default=None)

        required: bool | core.BoolOut | None = core.arg(default=None)

        string_attribute_constraints: StringAttributeConstraints | None = core.arg(default=None)


@core.schema
class PasswordPolicy(core.Schema):

    minimum_length: int | core.IntOut | None = core.attr(int, default=None)

    require_lowercase: bool | core.BoolOut | None = core.attr(bool, default=None)

    require_numbers: bool | core.BoolOut | None = core.attr(bool, default=None)

    require_symbols: bool | core.BoolOut | None = core.attr(bool, default=None)

    require_uppercase: bool | core.BoolOut | None = core.attr(bool, default=None)

    temporary_password_validity_days: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        minimum_length: int | core.IntOut | None = None,
        require_lowercase: bool | core.BoolOut | None = None,
        require_numbers: bool | core.BoolOut | None = None,
        require_symbols: bool | core.BoolOut | None = None,
        require_uppercase: bool | core.BoolOut | None = None,
        temporary_password_validity_days: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=PasswordPolicy.Args(
                minimum_length=minimum_length,
                require_lowercase=require_lowercase,
                require_numbers=require_numbers,
                require_symbols=require_symbols,
                require_uppercase=require_uppercase,
                temporary_password_validity_days=temporary_password_validity_days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minimum_length: int | core.IntOut | None = core.arg(default=None)

        require_lowercase: bool | core.BoolOut | None = core.arg(default=None)

        require_numbers: bool | core.BoolOut | None = core.arg(default=None)

        require_symbols: bool | core.BoolOut | None = core.arg(default=None)

        require_uppercase: bool | core.BoolOut | None = core.arg(default=None)

        temporary_password_validity_days: int | core.IntOut | None = core.arg(default=None)


@core.schema
class EmailConfiguration(core.Schema):

    configuration_set: str | core.StringOut | None = core.attr(str, default=None)

    email_sending_account: str | core.StringOut | None = core.attr(str, default=None)

    from_email_address: str | core.StringOut | None = core.attr(str, default=None)

    reply_to_email_address: str | core.StringOut | None = core.attr(str, default=None)

    source_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        configuration_set: str | core.StringOut | None = None,
        email_sending_account: str | core.StringOut | None = None,
        from_email_address: str | core.StringOut | None = None,
        reply_to_email_address: str | core.StringOut | None = None,
        source_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EmailConfiguration.Args(
                configuration_set=configuration_set,
                email_sending_account=email_sending_account,
                from_email_address=from_email_address,
                reply_to_email_address=reply_to_email_address,
                source_arn=source_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        configuration_set: str | core.StringOut | None = core.arg(default=None)

        email_sending_account: str | core.StringOut | None = core.arg(default=None)

        from_email_address: str | core.StringOut | None = core.arg(default=None)

        reply_to_email_address: str | core.StringOut | None = core.arg(default=None)

        source_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DeviceConfiguration(core.Schema):

    challenge_required_on_new_device: bool | core.BoolOut | None = core.attr(bool, default=None)

    device_only_remembered_on_user_prompt: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        challenge_required_on_new_device: bool | core.BoolOut | None = None,
        device_only_remembered_on_user_prompt: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=DeviceConfiguration.Args(
                challenge_required_on_new_device=challenge_required_on_new_device,
                device_only_remembered_on_user_prompt=device_only_remembered_on_user_prompt,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        challenge_required_on_new_device: bool | core.BoolOut | None = core.arg(default=None)

        device_only_remembered_on_user_prompt: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class UserPoolAddOns(core.Schema):

    advanced_security_mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        advanced_security_mode: str | core.StringOut,
    ):
        super().__init__(
            args=UserPoolAddOns.Args(
                advanced_security_mode=advanced_security_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        advanced_security_mode: str | core.StringOut = core.arg()


@core.schema
class InviteMessageTemplate(core.Schema):

    email_message: str | core.StringOut | None = core.attr(str, default=None)

    email_subject: str | core.StringOut | None = core.attr(str, default=None)

    sms_message: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        email_message: str | core.StringOut | None = None,
        email_subject: str | core.StringOut | None = None,
        sms_message: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InviteMessageTemplate.Args(
                email_message=email_message,
                email_subject=email_subject,
                sms_message=sms_message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        email_message: str | core.StringOut | None = core.arg(default=None)

        email_subject: str | core.StringOut | None = core.arg(default=None)

        sms_message: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AdminCreateUserConfig(core.Schema):

    allow_admin_create_user_only: bool | core.BoolOut | None = core.attr(bool, default=None)

    invite_message_template: InviteMessageTemplate | None = core.attr(
        InviteMessageTemplate, default=None
    )

    def __init__(
        self,
        *,
        allow_admin_create_user_only: bool | core.BoolOut | None = None,
        invite_message_template: InviteMessageTemplate | None = None,
    ):
        super().__init__(
            args=AdminCreateUserConfig.Args(
                allow_admin_create_user_only=allow_admin_create_user_only,
                invite_message_template=invite_message_template,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_admin_create_user_only: bool | core.BoolOut | None = core.arg(default=None)

        invite_message_template: InviteMessageTemplate | None = core.arg(default=None)


@core.schema
class UsernameConfiguration(core.Schema):

    case_sensitive: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        case_sensitive: bool | core.BoolOut,
    ):
        super().__init__(
            args=UsernameConfiguration.Args(
                case_sensitive=case_sensitive,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        case_sensitive: bool | core.BoolOut = core.arg()


@core.schema
class CustomSmsSender(core.Schema):

    lambda_arn: str | core.StringOut = core.attr(str)

    lambda_version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        lambda_arn: str | core.StringOut,
        lambda_version: str | core.StringOut,
    ):
        super().__init__(
            args=CustomSmsSender.Args(
                lambda_arn=lambda_arn,
                lambda_version=lambda_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_arn: str | core.StringOut = core.arg()

        lambda_version: str | core.StringOut = core.arg()


@core.schema
class CustomEmailSender(core.Schema):

    lambda_arn: str | core.StringOut = core.attr(str)

    lambda_version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        lambda_arn: str | core.StringOut,
        lambda_version: str | core.StringOut,
    ):
        super().__init__(
            args=CustomEmailSender.Args(
                lambda_arn=lambda_arn,
                lambda_version=lambda_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_arn: str | core.StringOut = core.arg()

        lambda_version: str | core.StringOut = core.arg()


@core.schema
class LambdaConfig(core.Schema):

    create_auth_challenge: str | core.StringOut | None = core.attr(str, default=None)

    custom_email_sender: CustomEmailSender | None = core.attr(
        CustomEmailSender, default=None, computed=True
    )

    custom_message: str | core.StringOut | None = core.attr(str, default=None)

    custom_sms_sender: CustomSmsSender | None = core.attr(
        CustomSmsSender, default=None, computed=True
    )

    define_auth_challenge: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    post_authentication: str | core.StringOut | None = core.attr(str, default=None)

    post_confirmation: str | core.StringOut | None = core.attr(str, default=None)

    pre_authentication: str | core.StringOut | None = core.attr(str, default=None)

    pre_sign_up: str | core.StringOut | None = core.attr(str, default=None)

    pre_token_generation: str | core.StringOut | None = core.attr(str, default=None)

    user_migration: str | core.StringOut | None = core.attr(str, default=None)

    verify_auth_challenge_response: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        create_auth_challenge: str | core.StringOut | None = None,
        custom_email_sender: CustomEmailSender | None = None,
        custom_message: str | core.StringOut | None = None,
        custom_sms_sender: CustomSmsSender | None = None,
        define_auth_challenge: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        post_authentication: str | core.StringOut | None = None,
        post_confirmation: str | core.StringOut | None = None,
        pre_authentication: str | core.StringOut | None = None,
        pre_sign_up: str | core.StringOut | None = None,
        pre_token_generation: str | core.StringOut | None = None,
        user_migration: str | core.StringOut | None = None,
        verify_auth_challenge_response: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LambdaConfig.Args(
                create_auth_challenge=create_auth_challenge,
                custom_email_sender=custom_email_sender,
                custom_message=custom_message,
                custom_sms_sender=custom_sms_sender,
                define_auth_challenge=define_auth_challenge,
                kms_key_id=kms_key_id,
                post_authentication=post_authentication,
                post_confirmation=post_confirmation,
                pre_authentication=pre_authentication,
                pre_sign_up=pre_sign_up,
                pre_token_generation=pre_token_generation,
                user_migration=user_migration,
                verify_auth_challenge_response=verify_auth_challenge_response,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        create_auth_challenge: str | core.StringOut | None = core.arg(default=None)

        custom_email_sender: CustomEmailSender | None = core.arg(default=None)

        custom_message: str | core.StringOut | None = core.arg(default=None)

        custom_sms_sender: CustomSmsSender | None = core.arg(default=None)

        define_auth_challenge: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        post_authentication: str | core.StringOut | None = core.arg(default=None)

        post_confirmation: str | core.StringOut | None = core.arg(default=None)

        pre_authentication: str | core.StringOut | None = core.arg(default=None)

        pre_sign_up: str | core.StringOut | None = core.arg(default=None)

        pre_token_generation: str | core.StringOut | None = core.arg(default=None)

        user_migration: str | core.StringOut | None = core.arg(default=None)

        verify_auth_challenge_response: str | core.StringOut | None = core.arg(default=None)


@core.schema
class VerificationMessageTemplate(core.Schema):

    default_email_option: str | core.StringOut | None = core.attr(str, default=None)

    email_message: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    email_message_by_link: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    email_subject: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    email_subject_by_link: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    sms_message: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        default_email_option: str | core.StringOut | None = None,
        email_message: str | core.StringOut | None = None,
        email_message_by_link: str | core.StringOut | None = None,
        email_subject: str | core.StringOut | None = None,
        email_subject_by_link: str | core.StringOut | None = None,
        sms_message: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=VerificationMessageTemplate.Args(
                default_email_option=default_email_option,
                email_message=email_message,
                email_message_by_link=email_message_by_link,
                email_subject=email_subject,
                email_subject_by_link=email_subject_by_link,
                sms_message=sms_message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_email_option: str | core.StringOut | None = core.arg(default=None)

        email_message: str | core.StringOut | None = core.arg(default=None)

        email_message_by_link: str | core.StringOut | None = core.arg(default=None)

        email_subject: str | core.StringOut | None = core.arg(default=None)

        email_subject_by_link: str | core.StringOut | None = core.arg(default=None)

        sms_message: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SoftwareTokenMfaConfiguration(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=SoftwareTokenMfaConfiguration.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class RecoveryMechanism(core.Schema):

    name: str | core.StringOut = core.attr(str)

    priority: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        priority: int | core.IntOut,
    ):
        super().__init__(
            args=RecoveryMechanism.Args(
                name=name,
                priority=priority,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        priority: int | core.IntOut = core.arg()


@core.schema
class AccountRecoverySetting(core.Schema):

    recovery_mechanism: list[RecoveryMechanism] | core.ArrayOut[RecoveryMechanism] = core.attr(
        RecoveryMechanism, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        recovery_mechanism: list[RecoveryMechanism] | core.ArrayOut[RecoveryMechanism],
    ):
        super().__init__(
            args=AccountRecoverySetting.Args(
                recovery_mechanism=recovery_mechanism,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        recovery_mechanism: list[RecoveryMechanism] | core.ArrayOut[RecoveryMechanism] = core.arg()


@core.resource(type="aws_cognito_user_pool", namespace="cognito")
class UserPool(core.Resource):

    account_recovery_setting: AccountRecoverySetting | None = core.attr(
        AccountRecoverySetting, default=None
    )

    admin_create_user_config: AdminCreateUserConfig | None = core.attr(
        AdminCreateUserConfig, default=None, computed=True
    )

    alias_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_verified_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    custom_domain: str | core.StringOut = core.attr(str, computed=True)

    device_configuration: DeviceConfiguration | None = core.attr(DeviceConfiguration, default=None)

    domain: str | core.StringOut = core.attr(str, computed=True)

    email_configuration: EmailConfiguration | None = core.attr(EmailConfiguration, default=None)

    email_verification_message: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    email_verification_subject: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    estimated_number_of_users: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    lambda_config: LambdaConfig | None = core.attr(LambdaConfig, default=None)

    last_modified_date: str | core.StringOut = core.attr(str, computed=True)

    mfa_configuration: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    password_policy: PasswordPolicy | None = core.attr(PasswordPolicy, default=None, computed=True)

    schema: list[Schema] | core.ArrayOut[Schema] | None = core.attr(
        Schema, default=None, kind=core.Kind.array
    )

    sms_authentication_message: str | core.StringOut | None = core.attr(str, default=None)

    sms_configuration: SmsConfiguration | None = core.attr(
        SmsConfiguration, default=None, computed=True
    )

    sms_verification_message: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    software_token_mfa_configuration: SoftwareTokenMfaConfiguration | None = core.attr(
        SoftwareTokenMfaConfiguration, default=None
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_pool_add_ons: UserPoolAddOns | None = core.attr(UserPoolAddOns, default=None)

    username_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    username_configuration: UsernameConfiguration | None = core.attr(
        UsernameConfiguration, default=None
    )

    verification_message_template: VerificationMessageTemplate | None = core.attr(
        VerificationMessageTemplate, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        account_recovery_setting: AccountRecoverySetting | None = None,
        admin_create_user_config: AdminCreateUserConfig | None = None,
        alias_attributes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        auto_verified_attributes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        device_configuration: DeviceConfiguration | None = None,
        email_configuration: EmailConfiguration | None = None,
        email_verification_message: str | core.StringOut | None = None,
        email_verification_subject: str | core.StringOut | None = None,
        lambda_config: LambdaConfig | None = None,
        mfa_configuration: str | core.StringOut | None = None,
        password_policy: PasswordPolicy | None = None,
        schema: list[Schema] | core.ArrayOut[Schema] | None = None,
        sms_authentication_message: str | core.StringOut | None = None,
        sms_configuration: SmsConfiguration | None = None,
        sms_verification_message: str | core.StringOut | None = None,
        software_token_mfa_configuration: SoftwareTokenMfaConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_pool_add_ons: UserPoolAddOns | None = None,
        username_attributes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        username_configuration: UsernameConfiguration | None = None,
        verification_message_template: VerificationMessageTemplate | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserPool.Args(
                name=name,
                account_recovery_setting=account_recovery_setting,
                admin_create_user_config=admin_create_user_config,
                alias_attributes=alias_attributes,
                auto_verified_attributes=auto_verified_attributes,
                device_configuration=device_configuration,
                email_configuration=email_configuration,
                email_verification_message=email_verification_message,
                email_verification_subject=email_verification_subject,
                lambda_config=lambda_config,
                mfa_configuration=mfa_configuration,
                password_policy=password_policy,
                schema=schema,
                sms_authentication_message=sms_authentication_message,
                sms_configuration=sms_configuration,
                sms_verification_message=sms_verification_message,
                software_token_mfa_configuration=software_token_mfa_configuration,
                tags=tags,
                tags_all=tags_all,
                user_pool_add_ons=user_pool_add_ons,
                username_attributes=username_attributes,
                username_configuration=username_configuration,
                verification_message_template=verification_message_template,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_recovery_setting: AccountRecoverySetting | None = core.arg(default=None)

        admin_create_user_config: AdminCreateUserConfig | None = core.arg(default=None)

        alias_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        auto_verified_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        device_configuration: DeviceConfiguration | None = core.arg(default=None)

        email_configuration: EmailConfiguration | None = core.arg(default=None)

        email_verification_message: str | core.StringOut | None = core.arg(default=None)

        email_verification_subject: str | core.StringOut | None = core.arg(default=None)

        lambda_config: LambdaConfig | None = core.arg(default=None)

        mfa_configuration: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        password_policy: PasswordPolicy | None = core.arg(default=None)

        schema: list[Schema] | core.ArrayOut[Schema] | None = core.arg(default=None)

        sms_authentication_message: str | core.StringOut | None = core.arg(default=None)

        sms_configuration: SmsConfiguration | None = core.arg(default=None)

        sms_verification_message: str | core.StringOut | None = core.arg(default=None)

        software_token_mfa_configuration: SoftwareTokenMfaConfiguration | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_pool_add_ons: UserPoolAddOns | None = core.arg(default=None)

        username_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        username_configuration: UsernameConfiguration | None = core.arg(default=None)

        verification_message_template: VerificationMessageTemplate | None = core.arg(default=None)
