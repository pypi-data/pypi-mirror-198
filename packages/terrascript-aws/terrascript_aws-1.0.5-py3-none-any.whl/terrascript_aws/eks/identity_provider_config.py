import terrascript.core as core


@core.schema
class Oidc(core.Schema):

    client_id: str | core.StringOut = core.attr(str)

    groups_claim: str | core.StringOut | None = core.attr(str, default=None)

    groups_prefix: str | core.StringOut | None = core.attr(str, default=None)

    identity_provider_config_name: str | core.StringOut = core.attr(str)

    issuer_url: str | core.StringOut = core.attr(str)

    required_claims: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    username_claim: str | core.StringOut | None = core.attr(str, default=None)

    username_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        identity_provider_config_name: str | core.StringOut,
        issuer_url: str | core.StringOut,
        groups_claim: str | core.StringOut | None = None,
        groups_prefix: str | core.StringOut | None = None,
        required_claims: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        username_claim: str | core.StringOut | None = None,
        username_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Oidc.Args(
                client_id=client_id,
                identity_provider_config_name=identity_provider_config_name,
                issuer_url=issuer_url,
                groups_claim=groups_claim,
                groups_prefix=groups_prefix,
                required_claims=required_claims,
                username_claim=username_claim,
                username_prefix=username_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: str | core.StringOut = core.arg()

        groups_claim: str | core.StringOut | None = core.arg(default=None)

        groups_prefix: str | core.StringOut | None = core.arg(default=None)

        identity_provider_config_name: str | core.StringOut = core.arg()

        issuer_url: str | core.StringOut = core.arg()

        required_claims: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        username_claim: str | core.StringOut | None = core.arg(default=None)

        username_prefix: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_eks_identity_provider_config", namespace="eks")
class IdentityProviderConfig(core.Resource):
    """
    Amazon Resource Name (ARN) of the EKS Identity Provider Configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    """
    EKS Cluster name and EKS Identity Provider Configuration name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Nested attribute containing [OpenID Connect](https://openid.net/connect/) identity provid
    er information for the cluster. Detailed below.
    """
    oidc: Oidc = core.attr(Oidc)

    """
    Status of the EKS Identity Provider Configuration.
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
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: str | core.StringOut,
        oidc: Oidc,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=IdentityProviderConfig.Args(
                cluster_name=cluster_name,
                oidc=oidc,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_name: str | core.StringOut = core.arg()

        oidc: Oidc = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
