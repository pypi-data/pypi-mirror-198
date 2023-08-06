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


@core.resource(type="aws_datasync_location_hdfs", namespace="datasync")
class LocationHdfs(core.Resource):
    """
    (Required) A list of DataSync Agent ARNs with which this location will be associated.
    """

    agent_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of authentication used to determine the identity of the user. Valid values are `
    SIMPLE` and `KERBEROS`.
    """
    authentication_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The size of data blocks to write into the HDFS cluster. The block size must be a multiple
    of 512 bytes. The default block size is 128 mebibytes (MiB).
    """
    block_size: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Kerberos key table (keytab) that contains mappings between the defined Kerberos princ
    ipal and the encrypted keys. If `KERBEROS` is specified for `authentication_type`, this parameter is
    required.
    """
    kerberos_keytab: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The krb5.conf file that contains the Kerberos configuration information. If `KERBEROS` is
    specified for `authentication_type`, this parameter is required.
    """
    kerberos_krb5_conf: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The Kerberos principal with access to the files and folders on the HDFS cluster. If `KERB
    EROS` is specified for `authentication_type`, this parameter is required.
    """
    kerberos_principal: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The URI of the HDFS cluster's Key Management Server (KMS).
    """
    kms_key_provider_uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required)  The NameNode that manages the HDFS namespace. The NameNode performs operations such as o
    pening, closing, and renaming files and directories. The NameNode contains the information to map bl
    ocks of data to the DataNodes. You can use only one NameNode. See configuration below.
    """
    name_node: list[NameNode] | core.ArrayOut[NameNode] = core.attr(NameNode, kind=core.Kind.array)

    """
    (Optional) The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) a
    nd data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster
    . If `qop_configuration` isn't specified, `rpc_protection` and `data_transfer_protection` default to
    PRIVACY`. If you set RpcProtection or DataTransferProtection, the other parameter assumes the same
    value.  See configuration below.
    """
    qop_configuration: QopConfiguration | None = core.attr(QopConfiguration, default=None)

    """
    (Optional) The number of DataNodes to replicate the data to when writing to the HDFS cluster. By def
    ault, data is replicated to three DataNodes.
    """
    replication_factor: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The user name used to identify the client on the host operating system. If `SIMPLE` is sp
    ecified for `authentication_type`, this parameter is required.
    """
    simple_user: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write
    data to the HDFS cluster. If the subdirectory isn't specified, it will default to /.
    """
    subdirectory: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value pairs of resource tags to assign to the DataSync Location. If configured with a
    provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws
    /latest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those
    defined at the provider-level.
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
