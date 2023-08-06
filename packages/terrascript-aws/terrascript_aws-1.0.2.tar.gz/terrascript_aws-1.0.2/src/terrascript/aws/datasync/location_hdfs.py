import terrascript.core as core


@core.schema
class QopConfiguration(core.Schema):

    data_transfer_protection: str | core.StringOut | None = core.attr(str, default=None)

    rpc_protection: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        data_transfer_protection: str | core.StringOut | None = None,
        rpc_protection: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=QopConfiguration.Args(
                data_transfer_protection=data_transfer_protection,
                rpc_protection=rpc_protection,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_transfer_protection: str | core.StringOut | None = core.arg(default=None)

        rpc_protection: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NameNode(core.Schema):

    hostname: str | core.StringOut = core.attr(str)

    port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        hostname: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=NameNode.Args(
                hostname=hostname,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hostname: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.resource(type="aws_datasync_location_hdfs", namespace="aws_datasync")
class LocationHdfs(core.Resource):

    agent_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_type: str | core.StringOut | None = core.attr(str, default=None)

    block_size: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kerberos_keytab: str | core.StringOut | None = core.attr(str, default=None)

    kerberos_krb5_conf: str | core.StringOut | None = core.attr(str, default=None)

    kerberos_principal: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_provider_uri: str | core.StringOut | None = core.attr(str, default=None)

    name_node: list[NameNode] | core.ArrayOut[NameNode] = core.attr(NameNode, kind=core.Kind.array)

    qop_configuration: QopConfiguration | None = core.attr(QopConfiguration, default=None)

    replication_factor: int | core.IntOut | None = core.attr(int, default=None)

    simple_user: str | core.StringOut | None = core.attr(str, default=None)

    subdirectory: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    uri: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        agent_arns: list[str] | core.ArrayOut[core.StringOut],
        name_node: list[NameNode] | core.ArrayOut[NameNode],
        authentication_type: str | core.StringOut | None = None,
        block_size: int | core.IntOut | None = None,
        kerberos_keytab: str | core.StringOut | None = None,
        kerberos_krb5_conf: str | core.StringOut | None = None,
        kerberos_principal: str | core.StringOut | None = None,
        kms_key_provider_uri: str | core.StringOut | None = None,
        qop_configuration: QopConfiguration | None = None,
        replication_factor: int | core.IntOut | None = None,
        simple_user: str | core.StringOut | None = None,
        subdirectory: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationHdfs.Args(
                agent_arns=agent_arns,
                name_node=name_node,
                authentication_type=authentication_type,
                block_size=block_size,
                kerberos_keytab=kerberos_keytab,
                kerberos_krb5_conf=kerberos_krb5_conf,
                kerberos_principal=kerberos_principal,
                kms_key_provider_uri=kms_key_provider_uri,
                qop_configuration=qop_configuration,
                replication_factor=replication_factor,
                simple_user=simple_user,
                subdirectory=subdirectory,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        agent_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        authentication_type: str | core.StringOut | None = core.arg(default=None)

        block_size: int | core.IntOut | None = core.arg(default=None)

        kerberos_keytab: str | core.StringOut | None = core.arg(default=None)

        kerberos_krb5_conf: str | core.StringOut | None = core.arg(default=None)

        kerberos_principal: str | core.StringOut | None = core.arg(default=None)

        kms_key_provider_uri: str | core.StringOut | None = core.arg(default=None)

        name_node: list[NameNode] | core.ArrayOut[NameNode] = core.arg()

        qop_configuration: QopConfiguration | None = core.arg(default=None)

        replication_factor: int | core.IntOut | None = core.arg(default=None)

        simple_user: str | core.StringOut | None = core.arg(default=None)

        subdirectory: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
