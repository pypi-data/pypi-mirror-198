import terrascript.core as core


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


@core.resource(type="aws_eks_cluster", namespace="eks")
class Cluster(core.Resource):
    """
    ARN of the cluster.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Attribute block containing `certificate-authority-data` for your cluster. Detailed below.
    """
    certificate_authority: list[CertificateAuthority] | core.ArrayOut[
        CertificateAuthority
    ] = core.attr(CertificateAuthority, computed=True, kind=core.Kind.array)

    """
    Unix epoch timestamp in seconds for when the cluster was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of the desired control plane logging to enable. For more information, see [Amazon EK
    S Control Plane Logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).
    """
    enabled_cluster_log_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block with encryption configuration for the cluster. Only available on Kube
    rnetes 1.13 and above clusters created after March 6, 2020. Detailed below.
    """
    encryption_config: EncryptionConfig | None = core.attr(EncryptionConfig, default=None)

    """
    Endpoint for your Kubernetes API server.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the cluster.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Attribute block containing identity provider information for your cluster. Only available on Kuberne
    tes version 1.13 and 1.14 clusters created or upgraded on or after September 3, 2019. Detailed below
    .
    """
    identity: list[Identity] | core.ArrayOut[Identity] = core.attr(
        Identity, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block with kubernetes network configuration for the cluster. Detailed below
    . If removed, Terraform will only perform drift detection if a configuration value is provided.
    """
    kubernetes_network_config: KubernetesNetworkConfig | None = core.attr(
        KubernetesNetworkConfig, default=None, computed=True
    )

    name: str | core.StringOut = core.attr(str)

    """
    Platform version for the cluster.
    """
    platform_version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ARN of the IAM role that provides permissions for the Kubernetes control plane to make ca
    lls to AWS API operations on your behalf. Ensure the resource configuration includes explicit depend
    encies on the IAM Role permissions by adding [`depends_on`](https://www.terraform.io/docs/configurat
    ion/meta-arguments/depends_on.html) if using the [`aws_iam_role_policy` resource](/docs/providers/aw
    s/r/iam_role_policy.html) or [`aws_iam_role_policy_attachment` resource](/docs/providers/aws/r/iam_r
    ole_policy_attachment.html), otherwise EKS cannot delete EKS managed EC2 infrastructure such as Secu
    rity Groups on EKS Cluster deletion.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    Status of the EKS cluster. One of `CREATING`, `ACTIVE`, `DELETING`, `FAILED`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Configuration block for the VPC associated with your cluster. Amazon EKS VPC resources ha
    ve specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Co
    nsiderations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Secur
    ity Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in t
    he Amazon EKS User Guide. Detailed below. Also contains attributes detailed in the Attributes sectio
    n.
    """
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
