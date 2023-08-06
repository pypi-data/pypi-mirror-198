import terrascript.core as core


@core.resource(type="aws_cognito_user", namespace="aws_cognito")
class User(core.Resource):

    attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    client_metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    desired_delivery_mediums: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    force_alias_creation: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_modified_date: str | core.StringOut = core.attr(str, computed=True)

    message_action: str | core.StringOut | None = core.attr(str, default=None)

    mfa_setting_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    password: str | core.StringOut | None = core.attr(str, default=None)

    preferred_mfa_setting: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    sub: str | core.StringOut = core.attr(str, computed=True)

    temporary_password: str | core.StringOut | None = core.attr(str, default=None)

    user_pool_id: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

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
