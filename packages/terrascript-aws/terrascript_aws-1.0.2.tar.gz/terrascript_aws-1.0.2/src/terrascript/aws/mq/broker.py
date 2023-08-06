import terrascript.core as core


@core.schema
class User(core.Schema):

    console_access: bool | core.BoolOut | None = core.attr(bool, default=None)

    groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
        console_access: bool | core.BoolOut | None = None,
        groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=User.Args(
                password=password,
                username=username,
                console_access=console_access,
                groups=groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        console_access: bool | core.BoolOut | None = core.arg(default=None)

        groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class LdapServerMetadata(core.Schema):

    hosts: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_base: str | core.StringOut | None = core.attr(str, default=None)

    role_name: str | core.StringOut | None = core.attr(str, default=None)

    role_search_matching: str | core.StringOut | None = core.attr(str, default=None)

    role_search_subtree: bool | core.BoolOut | None = core.attr(bool, default=None)

    service_account_password: str | core.StringOut | None = core.attr(str, default=None)

    service_account_username: str | core.StringOut | None = core.attr(str, default=None)

    user_base: str | core.StringOut | None = core.attr(str, default=None)

    user_role_name: str | core.StringOut | None = core.attr(str, default=None)

    user_search_matching: str | core.StringOut | None = core.attr(str, default=None)

    user_search_subtree: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        hosts: list[str] | core.ArrayOut[core.StringOut] | None = None,
        role_base: str | core.StringOut | None = None,
        role_name: str | core.StringOut | None = None,
        role_search_matching: str | core.StringOut | None = None,
        role_search_subtree: bool | core.BoolOut | None = None,
        service_account_password: str | core.StringOut | None = None,
        service_account_username: str | core.StringOut | None = None,
        user_base: str | core.StringOut | None = None,
        user_role_name: str | core.StringOut | None = None,
        user_search_matching: str | core.StringOut | None = None,
        user_search_subtree: bool | core.BoolOut | None = None,
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
        hosts: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        role_base: str | core.StringOut | None = core.arg(default=None)

        role_name: str | core.StringOut | None = core.arg(default=None)

        role_search_matching: str | core.StringOut | None = core.arg(default=None)

        role_search_subtree: bool | core.BoolOut | None = core.arg(default=None)

        service_account_password: str | core.StringOut | None = core.arg(default=None)

        service_account_username: str | core.StringOut | None = core.arg(default=None)

        user_base: str | core.StringOut | None = core.arg(default=None)

        user_role_name: str | core.StringOut | None = core.arg(default=None)

        user_search_matching: str | core.StringOut | None = core.arg(default=None)

        user_search_subtree: bool | core.BoolOut | None = core.arg(default=None)


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
class MaintenanceWindowStartTime(core.Schema):

    day_of_week: str | core.StringOut = core.attr(str)

    time_of_day: str | core.StringOut = core.attr(str)

    time_zone: str | core.StringOut = core.attr(str)

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
class EncryptionOptions(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    use_aws_owned_key: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        kms_key_id: str | core.StringOut | None = None,
        use_aws_owned_key: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=EncryptionOptions.Args(
                kms_key_id=kms_key_id,
                use_aws_owned_key=use_aws_owned_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        use_aws_owned_key: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Logs(core.Schema):

    audit: str | core.StringOut | None = core.attr(str, default=None)

    general: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        audit: str | core.StringOut | None = None,
        general: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Logs.Args(
                audit=audit,
                general=general,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audit: str | core.StringOut | None = core.arg(default=None)

        general: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Configuration(core.Schema):

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    revision: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        id: str | core.StringOut | None = None,
        revision: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Configuration.Args(
                id=id,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        revision: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_mq_broker", namespace="aws_mq")
class Broker(core.Resource):

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_strategy: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    broker_name: str | core.StringOut = core.attr(str)

    configuration: Configuration | None = core.attr(Configuration, default=None, computed=True)

    deployment_mode: str | core.StringOut | None = core.attr(str, default=None)

    encryption_options: EncryptionOptions | None = core.attr(EncryptionOptions, default=None)

    engine_type: str | core.StringOut = core.attr(str)

    engine_version: str | core.StringOut = core.attr(str)

    host_instance_type: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    instances: list[Instances] | core.ArrayOut[Instances] = core.attr(
        Instances, computed=True, kind=core.Kind.array
    )

    ldap_server_metadata: LdapServerMetadata | None = core.attr(LdapServerMetadata, default=None)

    logs: Logs | None = core.attr(Logs, default=None)

    maintenance_window_start_time: MaintenanceWindowStartTime | None = core.attr(
        MaintenanceWindowStartTime, default=None, computed=True
    )

    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    storage_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user: list[User] | core.ArrayOut[User] = core.attr(User, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        broker_name: str | core.StringOut,
        engine_type: str | core.StringOut,
        engine_version: str | core.StringOut,
        host_instance_type: str | core.StringOut,
        user: list[User] | core.ArrayOut[User],
        apply_immediately: bool | core.BoolOut | None = None,
        authentication_strategy: str | core.StringOut | None = None,
        auto_minor_version_upgrade: bool | core.BoolOut | None = None,
        configuration: Configuration | None = None,
        deployment_mode: str | core.StringOut | None = None,
        encryption_options: EncryptionOptions | None = None,
        ldap_server_metadata: LdapServerMetadata | None = None,
        logs: Logs | None = None,
        maintenance_window_start_time: MaintenanceWindowStartTime | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        storage_type: str | core.StringOut | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Broker.Args(
                broker_name=broker_name,
                engine_type=engine_type,
                engine_version=engine_version,
                host_instance_type=host_instance_type,
                user=user,
                apply_immediately=apply_immediately,
                authentication_strategy=authentication_strategy,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                configuration=configuration,
                deployment_mode=deployment_mode,
                encryption_options=encryption_options,
                ldap_server_metadata=ldap_server_metadata,
                logs=logs,
                maintenance_window_start_time=maintenance_window_start_time,
                publicly_accessible=publicly_accessible,
                security_groups=security_groups,
                storage_type=storage_type,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        authentication_strategy: str | core.StringOut | None = core.arg(default=None)

        auto_minor_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        broker_name: str | core.StringOut = core.arg()

        configuration: Configuration | None = core.arg(default=None)

        deployment_mode: str | core.StringOut | None = core.arg(default=None)

        encryption_options: EncryptionOptions | None = core.arg(default=None)

        engine_type: str | core.StringOut = core.arg()

        engine_version: str | core.StringOut = core.arg()

        host_instance_type: str | core.StringOut = core.arg()

        ldap_server_metadata: LdapServerMetadata | None = core.arg(default=None)

        logs: Logs | None = core.arg(default=None)

        maintenance_window_start_time: MaintenanceWindowStartTime | None = core.arg(default=None)

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        storage_type: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user: list[User] | core.ArrayOut[User] = core.arg()
