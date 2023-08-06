import terrascript.core as core


@core.schema
class PhoneConfig(core.Schema):

    after_contact_work_time_limit: int | core.IntOut | None = core.attr(int, default=None)

    auto_accept: bool | core.BoolOut | None = core.attr(bool, default=None)

    desk_phone_number: str | core.StringOut | None = core.attr(str, default=None)

    phone_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        phone_type: str | core.StringOut,
        after_contact_work_time_limit: int | core.IntOut | None = None,
        auto_accept: bool | core.BoolOut | None = None,
        desk_phone_number: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PhoneConfig.Args(
                phone_type=phone_type,
                after_contact_work_time_limit=after_contact_work_time_limit,
                auto_accept=auto_accept,
                desk_phone_number=desk_phone_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        after_contact_work_time_limit: int | core.IntOut | None = core.arg(default=None)

        auto_accept: bool | core.BoolOut | None = core.arg(default=None)

        desk_phone_number: str | core.StringOut | None = core.arg(default=None)

        phone_type: str | core.StringOut = core.arg()


@core.schema
class IdentityInfo(core.Schema):

    email: str | core.StringOut | None = core.attr(str, default=None)

    first_name: str | core.StringOut | None = core.attr(str, default=None)

    last_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        email: str | core.StringOut | None = None,
        first_name: str | core.StringOut | None = None,
        last_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=IdentityInfo.Args(
                email=email,
                first_name=first_name,
                last_name=last_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        email: str | core.StringOut | None = core.arg(default=None)

        first_name: str | core.StringOut | None = core.arg(default=None)

        last_name: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_connect_user", namespace="connect")
class User(core.Resource):
    """
    The Amazon Resource Name (ARN) of the user.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The identifier of the user account in the directory used for identity management. If Amaz
    on Connect cannot access the directory, you can specify this identifier to authenticate users. If yo
    u include the identifier, we assume that Amazon Connect cannot access the directory. Otherwise, the
    identity information is used to authenticate users from your directory. This parameter is required i
    f you are using an existing directory for identity management in Amazon Connect when Amazon Connect
    cannot access your directory to authenticate users. If you are using SAML for identity management an
    d include this parameter, an error is returned.
    """
    directory_user_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The identifier of the hierarchy group for the user.
    """
    hierarchy_group_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the user
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A block that contains information about the identity of the user. Documented below.
    """
    identity_info: IdentityInfo | None = core.attr(IdentityInfo, default=None)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) The user name for the account. For instances not using SAML for identity management, the
    user name can include up to 20 characters. If you are using SAML for identity management, the user n
    ame can include up to 64 characters from `[a-zA-Z0-9_-.\@]+`.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The password for the user account. A password is required if you are using Amazon Connect
    for identity management. Otherwise, it is an error to include a password.
    """
    password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A block that contains information about the phone settings for the user. Documented below
    .
    """
    phone_config: PhoneConfig = core.attr(PhoneConfig)

    """
    (Required) The identifier of the routing profile for the user.
    """
    routing_profile_id: str | core.StringOut = core.attr(str)

    """
    (Required) A list of identifiers for the security profiles for the user. Specify a minimum of 1 and
    maximum of 10 security profile ids. For more information, see [Best Practices for Security Profiles]
    (https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-best-practices.html) in the
    Amazon Connect Administrator Guide.
    """
    security_profile_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) Tags to apply to the user. If configured with a provider
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The identifier for the user.
    """
    user_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_id: str | core.StringOut,
        name: str | core.StringOut,
        phone_config: PhoneConfig,
        routing_profile_id: str | core.StringOut,
        security_profile_ids: list[str] | core.ArrayOut[core.StringOut],
        directory_user_id: str | core.StringOut | None = None,
        hierarchy_group_id: str | core.StringOut | None = None,
        identity_info: IdentityInfo | None = None,
        password: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                instance_id=instance_id,
                name=name,
                phone_config=phone_config,
                routing_profile_id=routing_profile_id,
                security_profile_ids=security_profile_ids,
                directory_user_id=directory_user_id,
                hierarchy_group_id=hierarchy_group_id,
                identity_info=identity_info,
                password=password,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_user_id: str | core.StringOut | None = core.arg(default=None)

        hierarchy_group_id: str | core.StringOut | None = core.arg(default=None)

        identity_info: IdentityInfo | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        password: str | core.StringOut | None = core.arg(default=None)

        phone_config: PhoneConfig = core.arg()

        routing_profile_id: str | core.StringOut = core.arg()

        security_profile_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
