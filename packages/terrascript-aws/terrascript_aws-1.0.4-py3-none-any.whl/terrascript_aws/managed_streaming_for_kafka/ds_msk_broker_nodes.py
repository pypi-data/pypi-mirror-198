import terrascript.core as core


@core.schema
class NodeInfoList(core.Schema):

    attached_eni_id: str | core.StringOut = core.attr(str, computed=True)

    broker_id: float | core.FloatOut = core.attr(float, computed=True)

    client_subnet: str | core.StringOut = core.attr(str, computed=True)

    client_vpc_ip_address: str | core.StringOut = core.attr(str, computed=True)

    endpoints: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    node_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attached_eni_id: str | core.StringOut,
        broker_id: float | core.FloatOut,
        client_subnet: str | core.StringOut,
        client_vpc_ip_address: str | core.StringOut,
        endpoints: list[str] | core.ArrayOut[core.StringOut],
        node_arn: str | core.StringOut,
    ):
        super().__init__(
            args=NodeInfoList.Args(
                attached_eni_id=attached_eni_id,
                broker_id=broker_id,
                client_subnet=client_subnet,
                client_vpc_ip_address=client_vpc_ip_address,
                endpoints=endpoints,
                node_arn=node_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attached_eni_id: str | core.StringOut = core.arg()

        broker_id: float | core.FloatOut = core.arg()

        client_subnet: str | core.StringOut = core.arg()

        client_vpc_ip_address: str | core.StringOut = core.arg()

        endpoints: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        node_arn: str | core.StringOut = core.arg()


@core.data(type="aws_msk_broker_nodes", namespace="managed_streaming_for_kafka")
class DsMskBrokerNodes(core.Data):
    """
    (Required) The ARN of the cluster the nodes belong to.
    """

    cluster_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    node_info_list: list[NodeInfoList] | core.ArrayOut[NodeInfoList] = core.attr(
        NodeInfoList, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_arn: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsMskBrokerNodes.Args(
                cluster_arn=cluster_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_arn: str | core.StringOut = core.arg()
