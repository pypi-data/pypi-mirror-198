import terrascript.core as core


@core.resource(type="aws_codeartifact_domain", namespace="codeartifact")
class Domain(core.Resource):
    """
    The ARN of the Domain.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The total size of all assets in the domain.
    """
    asset_size_bytes: int | core.IntOut = core.attr(int, computed=True)

    """
    A timestamp that represents the date and time the domain was created in [RFC3339 format](https://too
    ls.ietf.org/html/rfc3339#section-5.8).
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the domain to create. All domain names in an AWS Region that are in the same
    AWS account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensi
    tive information in a domain name because it is publicly discoverable.
    """
    domain: str | core.StringOut = core.attr(str)

    """
    (Optional) The encryption key for the domain. This is used to encrypt content stored in a domain. Th
    e KMS Key Amazon Resource Name (ARN). The default aws/codeartifact AWS KMS master key is used if thi
    s element is absent.
    """
    encryption_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ARN of the Domain.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS account ID that owns the domain.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of repositories in the domain.
    """
    repository_count: int | core.IntOut = core.attr(int, computed=True)

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
        domain: str | core.StringOut,
        encryption_key: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Domain.Args(
                domain=domain,
                encryption_key=encryption_key,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain: str | core.StringOut = core.arg()

        encryption_key: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
