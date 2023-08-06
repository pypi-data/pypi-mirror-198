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


@core.data(type="aws_eks_cluster", namespace="eks")
class DsCluster(core.Data):
    """
    The Amazon Resource Name (ARN) of the cluster.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Nested attribute containing `certificate-authority-data` for your cluster.
    """
    certificate_authority: list[CertificateAuthority] | core.ArrayOut[
        CertificateAuthority
    ] = core.attr(CertificateAuthority, computed=True, kind=core.Kind.array)

    """
    The Unix epoch time stamp in seconds for when the cluster was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    The enabled control plane logs.
    """
    enabled_cluster_log_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The endpoint for your Kubernetes API server.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the cluster
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Nested attribute containing identity provider information for your cluster. Only available on Kubern
    etes version 1.13 and 1.14 clusters created or upgraded on or after September 3, 2019. For an exampl
    e using this information to enable IAM Roles for Service Accounts, see the [`aws_eks_cluster` resour
    ce documentation](/docs/providers/aws/r/eks_cluster.html).
    """
    identity: list[Identity] | core.ArrayOut[Identity] = core.attr(
        Identity, computed=True, kind=core.Kind.array
    )

    """
    Nested list containing Kubernetes Network Configuration.
    """
    kubernetes_network_config: list[KubernetesNetworkConfig] | core.ArrayOut[
        KubernetesNetworkConfig
    ] = core.attr(KubernetesNetworkConfig, computed=True, kind=core.Kind.array)

    """
    (Required) The name of the cluster. Must be between 1-100 characters in length. Must begin with an a
    lphanumeric character, and must only contain alphanumeric characters, dashes and underscores (`^[0-9
    A-Za-z][A-Za-z0-9\-_]+$`).
    """
    name: str | core.StringOut = core.attr(str)

    """
    The platform version for the cluster.
    """
    platform_version: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control
    plane to make calls to AWS API operations on your behalf.
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of the EKS cluster. One of `CREATING`, `ACTIVE`, `DELETING`, `FAILED`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The Kubernetes server version for the cluster.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    """
    Nested list containing VPC configuration for the cluster.
    """
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
