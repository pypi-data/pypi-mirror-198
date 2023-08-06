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


@core.resource(type="aws_connect_user", namespace="aws_connect")
class User(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    directory_user_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    hierarchy_group_id: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_info: IdentityInfo | None = core.attr(IdentityInfo, default=None)

    instance_id: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    password: str | core.StringOut | None = core.attr(str, default=None)

    phone_config: PhoneConfig = core.attr(PhoneConfig)

    routing_profile_id: str | core.StringOut = core.attr(str)

    security_profile_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
