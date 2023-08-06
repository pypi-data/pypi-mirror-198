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

    ip_family: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    service_ipv4_cidr: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        ip_family: str | core.StringOut | None = None,
        service_ipv4_cidr: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=KubernetesNetworkConfig.Args(
                ip_family=ip_family,
                service_ipv4_cidr=service_ipv4_cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_family: str | core.StringOut | None = core.arg(default=None)

        service_ipv4_cidr: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Provider(core.Schema):

    key_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key_arn: str | core.StringOut,
    ):
        super().__init__(
            args=Provider.Args(
                key_arn=key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_arn: str | core.StringOut = core.arg()


@core.schema
class EncryptionConfig(core.Schema):

    provider: Provider = core.attr(Provider)

    resources: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        provider: Provider,
        resources: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=EncryptionConfig.Args(
                provider=provider,
                resources=resources,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        provider: Provider = core.arg()

        resources: list[str] | core.ArrayOut[core.StringOut] = core.arg()


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

    endpoint_private_access: bool | core.BoolOut | None = core.attr(bool, default=None)

    endpoint_public_access: bool | core.BoolOut | None = core.attr(bool, default=None)

    public_access_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cluster_security_group_id: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
        endpoint_private_access: bool | core.BoolOut | None = None,
        endpoint_public_access: bool | core.BoolOut | None = None,
        public_access_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                cluster_security_group_id=cluster_security_group_id,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
                endpoint_private_access=endpoint_private_access,
                endpoint_public_access=endpoint_public_access,
                public_access_cidrs=public_access_cidrs,
                security_group_ids=security_group_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_security_group_id: str | core.StringOut = core.arg()

        endpoint_private_access: bool | core.BoolOut | None = core.arg(default=None)

        endpoint_public_access: bool | core.BoolOut | None = core.arg(default=None)

        public_access_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.resource(type="aws_eks_cluster", namespace="aws_eks")
class Cluster(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_authority: list[CertificateAuthority] | core.ArrayOut[
        CertificateAuthority
    ] = core.attr(CertificateAuthority, computed=True, kind=core.Kind.array)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    enabled_cluster_log_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    encryption_config: EncryptionConfig | None = core.attr(EncryptionConfig, default=None)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity: list[Identity] | core.ArrayOut[Identity] = core.attr(
        Identity, computed=True, kind=core.Kind.array
    )

    kubernetes_network_config: KubernetesNetworkConfig | None = core.attr(
        KubernetesNetworkConfig, default=None, computed=True
    )

    name: str | core.StringOut = core.attr(str)

    platform_version: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    vpc_config: VpcConfig = core.attr(VpcConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        vpc_config: VpcConfig,
        enabled_cluster_log_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        encryption_config: EncryptionConfig | None = None,
        kubernetes_network_config: KubernetesNetworkConfig | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        version: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                name=name,
                role_arn=role_arn,
                vpc_config=vpc_config,
                enabled_cluster_log_types=enabled_cluster_log_types,
                encryption_config=encryption_config,
                kubernetes_network_config=kubernetes_network_config,
                tags=tags,
                tags_all=tags_all,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled_cluster_log_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        encryption_config: EncryptionConfig | None = core.arg(default=None)

        kubernetes_network_config: KubernetesNetworkConfig | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)

        vpc_config: VpcConfig = core.arg()
