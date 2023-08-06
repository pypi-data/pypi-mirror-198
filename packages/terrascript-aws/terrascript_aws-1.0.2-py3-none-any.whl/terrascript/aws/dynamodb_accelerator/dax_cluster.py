import terrascript.core as core


@core.schema
class ServerSideEncryption(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ServerSideEncryption.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Nodes(core.Schema):

    address: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        availability_zone: str | core.StringOut,
        id: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Nodes.Args(
                address=address,
                availability_zone=availability_zone,
                id=id,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut = core.arg()

        availability_zone: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.resource(type="aws_dax_cluster", namespace="aws_dynamodb_accelerator")
class DaxCluster(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cluster_address: str | core.StringOut = core.attr(str, computed=True)

    cluster_endpoint_encryption_type: str | core.StringOut | None = core.attr(str, default=None)

    cluster_name: str | core.StringOut = core.attr(str)

    configuration_endpoint: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    iam_role_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    node_type: str | core.StringOut = core.attr(str)

    nodes: list[Nodes] | core.ArrayOut[Nodes] = core.attr(
        Nodes, computed=True, kind=core.Kind.array
    )

    notification_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    replication_factor: int | core.IntOut = core.attr(int)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    server_side_encryption: ServerSideEncryption | None = core.attr(
        ServerSideEncryption, default=None
    )

    subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: str | core.StringOut,
        iam_role_arn: str | core.StringOut,
        node_type: str | core.StringOut,
        replication_factor: int | core.IntOut,
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        cluster_endpoint_encryption_type: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        maintenance_window: str | core.StringOut | None = None,
        notification_topic_arn: str | core.StringOut | None = None,
        parameter_group_name: str | core.StringOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        server_side_encryption: ServerSideEncryption | None = None,
        subnet_group_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DaxCluster.Args(
                cluster_name=cluster_name,
                iam_role_arn=iam_role_arn,
                node_type=node_type,
                replication_factor=replication_factor,
                availability_zones=availability_zones,
                cluster_endpoint_encryption_type=cluster_endpoint_encryption_type,
                description=description,
                maintenance_window=maintenance_window,
                notification_topic_arn=notification_topic_arn,
                parameter_group_name=parameter_group_name,
                security_group_ids=security_group_ids,
                server_side_encryption=server_side_encryption,
                subnet_group_name=subnet_group_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        cluster_endpoint_encryption_type: str | core.StringOut | None = core.arg(default=None)

        cluster_name: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        iam_role_arn: str | core.StringOut = core.arg()

        maintenance_window: str | core.StringOut | None = core.arg(default=None)

        node_type: str | core.StringOut = core.arg()

        notification_topic_arn: str | core.StringOut | None = core.arg(default=None)

        parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        replication_factor: int | core.IntOut = core.arg()

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        server_side_encryption: ServerSideEncryption | None = core.arg(default=None)

        subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
