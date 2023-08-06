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


@core.resource(type="aws_cloudhsm_v2_cluster", namespace="cloudhsm")
class V2Cluster(core.Resource):
    """
    The list of cluster certificates.
    """

    cluster_certificates: list[ClusterCertificates] | core.ArrayOut[
        ClusterCertificates
    ] = core.attr(ClusterCertificates, computed=True, kind=core.Kind.array)

    """
    The id of the CloudHSM cluster.
    """
    cluster_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the CloudHSM cluster.
    """
    cluster_state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of HSM module in the cluster. Currently, only `hsm1.medium` is supported.
    """
    hsm_type: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the security group associated with the CloudHSM cluster.
    """
    security_group_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The id of Cloud HSM v2 cluster backup to be restored.
    """
    source_backup_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The IDs of subnets in which cluster will operate.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
    The id of the VPC that the CloudHSM cluster resides in.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        hsm_type: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        source_backup_identifier: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2Cluster.Args(
                hsm_type=hsm_type,
                subnet_ids=subnet_ids,
                source_backup_identifier=source_backup_identifier,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hsm_type: str | core.StringOut = core.arg()

        source_backup_identifier: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
