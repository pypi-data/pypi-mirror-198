import terrascript.core as core


@core.schema
class Oidc(core.Schema):

    issuer: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        issuer: str | core.StringOut,
    ):
        super().__init__(
            args=Oidc.Args(
                issuer=issuer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        issuer: str | core.StringOut = core.arg()


@core.schema
class Identity(core.Schema):

    oidc: list[Oidc] | core.ArrayOut[Oidc] = core.attr(Oidc, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        oidc: list[Oidc] | core.ArrayOut[Oidc],
    ):
        super().__init__(
            args=Identity.Args(
                oidc=oidc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        oidc: list[Oidc] | core.ArrayOut[Oidc] = core.arg()


@core.schema
class KubernetesNetworkConfig(core.Schema):

    ip_family: str | core.StringOut = core.attr(str, computed=True)

    service_ipv4_cidr: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ip_family: str | core.StringOut,
        service_ipv4_cidr: str | core.StringOut,
    ):
        super().__init__(
            args=KubernetesNetworkConfig.Args(
                ip_family=ip_family,
                service_ipv4_cidr=service_ipv4_cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_family: str | core.StringOut = core.arg()

        service_ipv4_cidr: str | core.StringOut = core.arg()


@core.schema
class CertificateAuthority(core.Schema):

    data: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        data: str | core.StringOut,
    ):
        super().__init__(
            args=CertificateAuthority.Args(
                data=data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data: str | core.StringOut = core.arg()


@core.schema
class VpcConfig(core.Schema):

    cluster_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    endpoint_private_access: bool | core.BoolOut = core.attr(bool, computed=True)

    endpoint_public_access: bool | core.BoolOut = core.attr(bool, computed=True)

    public_access_cidrs: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cluster_security_group_id: str | core.StringOut,
        endpoint_private_access: bool | core.BoolOut,
        endpoint_public_access: bool | core.BoolOut,
        public_access_cidrs: list[str] | core.ArrayOut[core.StringOut],
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcConfig.Args(
                cluster_security_group_id=cluster_security_group_id,
                endpoint_private_access=endpoint_private_access,
                endpoint_public_access=endpoint_public_access,
                public_access_cidrs=public_access_cidrs,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_security_group_id: str | core.StringOut = core.arg()

        endpoint_private_access: bool | core.BoolOut = core.arg()

        endpoint_public_access: bool | core.BoolOut = core.arg()

        public_access_cidrs: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.data(type="aws_eks_cluster", namespace="aws_eks")
class DsCluster(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_authority: list[CertificateAuthority] | core.ArrayOut[
        CertificateAuthority
    ] = core.attr(CertificateAuthority, computed=True, kind=core.Kind.array)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    enabled_cluster_log_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity: list[Identity] | core.ArrayOut[Identity] = core.attr(
        Identity, computed=True, kind=core.Kind.array
    )

    kubernetes_network_config: list[KubernetesNetworkConfig] | core.ArrayOut[
        KubernetesNetworkConfig
    ] = core.attr(KubernetesNetworkConfig, computed=True, kind=core.Kind.array)

    name: str | core.StringOut = core.attr(str)

    platform_version: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: str | core.StringOut = core.attr(str, computed=True)

    vpc_config: list[VpcConfig] | core.ArrayOut[VpcConfig] = core.attr(
        VpcConfig, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
