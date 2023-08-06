import terrascript.core as core


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


@core.resource(type="aws_mq_broker", namespace="mq")
class Broker(core.Resource):
    """
    (Optional) Specifies whether any broker modifications are applied immediately, or during the next ma
    intenance window. Default is `false`.
    """

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    ARN of the broker.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Authentication strategy used to secure the broker. Valid values are `simple` and `ldap`.
    ldap` is not supported for `engine_type` `RabbitMQ`.
    """
    authentication_strategy: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Whether to automatically upgrade to new minor versions of brokers as Amazon MQ makes rele
    ases available.
    """
    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Name of the broker.
    """
    broker_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block for broker configuration. Applies to `engine_type` of `ActiveMQ` only
    . Detailed below.
    """
    configuration: Configuration | None = core.attr(Configuration, default=None, computed=True)

    """
    (Optional) Deployment mode of the broker. Valid values are `SINGLE_INSTANCE`, `ACTIVE_STANDBY_MULTI_
    AZ`, and `CLUSTER_MULTI_AZ`. Default is `SINGLE_INSTANCE`.
    """
    deployment_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block containing encryption options. Detailed below.
    """
    encryption_options: EncryptionOptions | None = core.attr(EncryptionOptions, default=None)

    """
    (Required) Type of broker engine. Valid values are `ActiveMQ` and `RabbitMQ`.
    """
    engine_type: str | core.StringOut = core.attr(str)

    """
    (Required) Version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amaz
    on.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions. For example, `5.
    15.0`.
    """
    engine_version: str | core.StringOut = core.attr(str)

    """
    (Required) Broker's instance type. For example, `mq.t3.micro`, `mq.m5.large`.
    """
    host_instance_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The Configuration ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of information about allocated brokers (both active & standby).
    """
    instances: list[Instances] | core.ArrayOut[Instances] = core.attr(
        Instances, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block for the LDAP server used to authenticate and authorize connections to
    the broker. Not supported for `engine_type` `RabbitMQ`. Detailed below. (Currently, AWS may not pro
    cess changes to LDAP server metadata.)
    """
    ldap_server_metadata: LdapServerMetadata | None = core.attr(LdapServerMetadata, default=None)

    """
    (Optional) Configuration block for the logging configuration of the broker. Detailed below.
    """
    logs: Logs | None = core.attr(Logs, default=None)

    """
    (Optional) Configuration block for the maintenance window start time. Detailed below.
    """
    maintenance_window_start_time: MaintenanceWindowStartTime | None = core.attr(
        MaintenanceWindowStartTime, default=None, computed=True
    )

    """
    (Optional) Whether to enable connections from applications outside of the VPC that hosts the broker'
    s subnets.
    """
    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) List of security group IDs assigned to the broker.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Storage type of the broker. For `engine_type` `ActiveMQ`, the valid values are `efs` and
    ebs`, and the AWS-default is `efs`. For `engine_type` `RabbitMQ`, only `ebs` is supported. When usi
    ng `ebs`, only the `mq.m5` broker instance type family is supported.
    """
    storage_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) List of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires
    one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires multiple subnets.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Map of tags to assign to the broker. If configured with a provider [`default_tags` config
    uration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-config
    uration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Required) Configuration block for broker users. For `engine_type` of `RabbitMQ`, Amazon MQ does not
    return broker users preventing this resource from making user updates and drift detection. Detailed
    below.
    """
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
