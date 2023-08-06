import terrascript.core as core


@core.schema
class User(core.Schema):

    console_access: bool | core.BoolOut = core.attr(bool, computed=True)

    groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        console_access: bool | core.BoolOut,
        groups: list[str] | core.ArrayOut[core.StringOut],
        username: str | core.StringOut,
    ):
        super().__init__(
            args=User.Args(
                console_access=console_access,
                groups=groups,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        console_access: bool | core.BoolOut = core.arg()

        groups: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class Logs(core.Schema):

    audit: str | core.StringOut = core.attr(str, computed=True)

    general: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        audit: str | core.StringOut,
        general: bool | core.BoolOut,
    ):
        super().__init__(
            args=Logs.Args(
                audit=audit,
                general=general,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audit: str | core.StringOut = core.arg()

        general: bool | core.BoolOut = core.arg()


@core.schema
class MaintenanceWindowStartTime(core.Schema):

    day_of_week: str | core.StringOut = core.attr(str, computed=True)

    time_of_day: str | core.StringOut = core.attr(str, computed=True)

    time_zone: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        day_of_week: str | core.StringOut,
        time_of_day: str | core.StringOut,
        time_zone: str | core.StringOut,
    ):
        super().__init__(
            args=MaintenanceWindowStartTime.Args(
                day_of_week=day_of_week,
                time_of_day=time_of_day,
                time_zone=time_zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        day_of_week: str | core.StringOut = core.arg()

        time_of_day: str | core.StringOut = core.arg()

        time_zone: str | core.StringOut = core.arg()


@core.schema
class Instances(core.Schema):

    console_url: str | core.StringOut = core.attr(str, computed=True)

    endpoints: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    ip_address: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        console_url: str | core.StringOut,
        endpoints: list[str] | core.ArrayOut[core.StringOut],
        ip_address: str | core.StringOut,
    ):
        super().__init__(
            args=Instances.Args(
                console_url=console_url,
                endpoints=endpoints,
                ip_address=ip_address,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        console_url: str | core.StringOut = core.arg()

        endpoints: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        ip_address: str | core.StringOut = core.arg()


@core.schema
class EncryptionOptions(core.Schema):

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    use_aws_owned_key: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        kms_key_id: str | core.StringOut,
        use_aws_owned_key: bool | core.BoolOut,
    ):
        super().__init__(
            args=EncryptionOptions.Args(
                kms_key_id=kms_key_id,
                use_aws_owned_key=use_aws_owned_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut = core.arg()

        use_aws_owned_key: bool | core.BoolOut = core.arg()


@core.schema
class Configuration(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    revision: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        revision: int | core.IntOut,
    ):
        super().__init__(
            args=Configuration.Args(
                id=id,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        revision: int | core.IntOut = core.arg()


@core.schema
class LdapServerMetadata(core.Schema):

    hosts: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    role_base: str | core.StringOut = core.attr(str, computed=True)

    role_name: str | core.StringOut = core.attr(str, computed=True)

    role_search_matching: str | core.StringOut = core.attr(str, computed=True)

    role_search_subtree: bool | core.BoolOut = core.attr(bool, computed=True)

    service_account_password: str | core.StringOut = core.attr(str, computed=True)

    service_account_username: str | core.StringOut = core.attr(str, computed=True)

    user_base: str | core.StringOut = core.attr(str, computed=True)

    user_role_name: str | core.StringOut = core.attr(str, computed=True)

    user_search_matching: str | core.StringOut = core.attr(str, computed=True)

    user_search_subtree: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        hosts: list[str] | core.ArrayOut[core.StringOut],
        role_base: str | core.StringOut,
        role_name: str | core.StringOut,
        role_search_matching: str | core.StringOut,
        role_search_subtree: bool | core.BoolOut,
        service_account_password: str | core.StringOut,
        service_account_username: str | core.StringOut,
        user_base: str | core.StringOut,
        user_role_name: str | core.StringOut,
        user_search_matching: str | core.StringOut,
        user_search_subtree: bool | core.BoolOut,
    ):
        super().__init__(
            args=LdapServerMetadata.Args(
                hosts=hosts,
                role_base=role_base,
                role_name=role_name,
                role_search_matching=role_search_matching,
                role_search_subtree=role_search_subtree,
                service_account_password=service_account_password,
                service_account_username=service_account_username,
                user_base=user_base,
                user_role_name=user_role_name,
                user_search_matching=user_search_matching,
                user_search_subtree=user_search_subtree,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hosts: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        role_base: str | core.StringOut = core.arg()

        role_name: str | core.StringOut = core.arg()

        role_search_matching: str | core.StringOut = core.arg()

        role_search_subtree: bool | core.BoolOut = core.arg()

        service_account_password: str | core.StringOut = core.arg()

        service_account_username: str | core.StringOut = core.arg()

        user_base: str | core.StringOut = core.arg()

        user_role_name: str | core.StringOut = core.arg()

        user_search_matching: str | core.StringOut = core.arg()

        user_search_subtree: bool | core.BoolOut = core.arg()


@core.data(type="aws_mq_broker", namespace="mq")
class DsBroker(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_strategy: str | core.StringOut = core.attr(str, computed=True)

    auto_minor_version_upgrade: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) The unique id of the mq broker.
    """
    broker_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The unique name of the mq broker.
    """
    broker_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    configuration: list[Configuration] | core.ArrayOut[Configuration] = core.attr(
        Configuration, computed=True, kind=core.Kind.array
    )

    deployment_mode: str | core.StringOut = core.attr(str, computed=True)

    encryption_options: list[EncryptionOptions] | core.ArrayOut[EncryptionOptions] = core.attr(
        EncryptionOptions, computed=True, kind=core.Kind.array
    )

    engine_type: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    host_instance_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instances: list[Instances] | core.ArrayOut[Instances] = core.attr(
        Instances, computed=True, kind=core.Kind.array
    )

    ldap_server_metadata: list[LdapServerMetadata] | core.ArrayOut[LdapServerMetadata] = core.attr(
        LdapServerMetadata, computed=True, kind=core.Kind.array
    )

    logs: list[Logs] | core.ArrayOut[Logs] = core.attr(Logs, computed=True, kind=core.Kind.array)

    maintenance_window_start_time: list[MaintenanceWindowStartTime] | core.ArrayOut[
        MaintenanceWindowStartTime
    ] = core.attr(MaintenanceWindowStartTime, computed=True, kind=core.Kind.array)

    publicly_accessible: bool | core.BoolOut = core.attr(bool, computed=True)

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    storage_type: str | core.StringOut = core.attr(str, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user: list[User] | core.ArrayOut[User] = core.attr(User, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        broker_id: str | core.StringOut | None = None,
        broker_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBroker.Args(
                broker_id=broker_id,
                broker_name=broker_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        broker_id: str | core.StringOut | None = core.arg(default=None)

        broker_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
