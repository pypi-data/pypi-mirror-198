import terrascript.core as core


@core.schema
class ClusterCertificates(core.Schema):

    aws_hardware_certificate: str | core.StringOut = core.attr(str, computed=True)

    cluster_certificate: str | core.StringOut = core.attr(str, computed=True)

    cluster_csr: str | core.StringOut = core.attr(str, computed=True)

    hsm_certificate: str | core.StringOut = core.attr(str, computed=True)

    manufacturer_hardware_certificate: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        aws_hardware_certificate: str | core.StringOut,
        cluster_certificate: str | core.StringOut,
        cluster_csr: str | core.StringOut,
        hsm_certificate: str | core.StringOut,
        manufacturer_hardware_certificate: str | core.StringOut,
    ):
        super().__init__(
            args=ClusterCertificates.Args(
                aws_hardware_certificate=aws_hardware_certificate,
                cluster_certificate=cluster_certificate,
                cluster_csr=cluster_csr,
                hsm_certificate=hsm_certificate,
                manufacturer_hardware_certificate=manufacturer_hardware_certificate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_hardware_certificate: str | core.StringOut = core.arg()

        cluster_certificate: str | core.StringOut = core.arg()

        cluster_csr: str | core.StringOut = core.arg()

        hsm_certificate: str | core.StringOut = core.arg()

        manufacturer_hardware_certificate: str | core.StringOut = core.arg()


@core.data(type="aws_cloudhsm_v2_cluster", namespace="cloudhsm")
class DsV2Cluster(core.Data):
    """
    The list of cluster certificates.
    """

    cluster_certificates: list[ClusterCertificates] | core.ArrayOut[
        ClusterCertificates
    ] = core.attr(ClusterCertificates, computed=True, kind=core.Kind.array)

    """
    (Required) The id of Cloud HSM v2 cluster.
    """
    cluster_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The state of the cluster to be found.
    """
    cluster_state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the security group associated with the CloudHSM cluster.
    """
    security_group_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IDs of subnets in which cluster operates.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The id of the VPC that the CloudHSM cluster resides in.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_id: str | core.StringOut,
        cluster_state: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsV2Cluster.Args(
                cluster_id=cluster_id,
                cluster_state=cluster_state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_id: str | core.StringOut = core.arg()

        cluster_state: str | core.StringOut | None = core.arg(default=None)
