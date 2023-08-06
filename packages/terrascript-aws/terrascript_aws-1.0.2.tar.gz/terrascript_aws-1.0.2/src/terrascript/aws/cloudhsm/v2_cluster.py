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


@core.resource(type="aws_cloudhsm_v2_cluster", namespace="aws_cloudhsm")
class V2Cluster(core.Resource):

    cluster_certificates: list[ClusterCertificates] | core.ArrayOut[
        ClusterCertificates
    ] = core.attr(ClusterCertificates, computed=True, kind=core.Kind.array)

    cluster_id: str | core.StringOut = core.attr(str, computed=True)

    cluster_state: str | core.StringOut = core.attr(str, computed=True)

    hsm_type: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    security_group_id: str | core.StringOut = core.attr(str, computed=True)

    source_backup_identifier: str | core.StringOut | None = core.attr(str, default=None)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
