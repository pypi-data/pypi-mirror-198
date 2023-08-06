import terrascript.core as core


@core.schema
class SourceData(core.Schema):

    acm_pca_arn: str | core.StringOut | None = core.attr(str, default=None)

    x509_certificate_data: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        acm_pca_arn: str | core.StringOut | None = None,
        x509_certificate_data: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SourceData.Args(
                acm_pca_arn=acm_pca_arn,
                x509_certificate_data=x509_certificate_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acm_pca_arn: str | core.StringOut | None = core.arg(default=None)

        x509_certificate_data: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Source(core.Schema):

    source_data: SourceData = core.attr(SourceData)

    source_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        source_data: SourceData,
        source_type: str | core.StringOut,
    ):
        super().__init__(
            args=Source.Args(
                source_data=source_data,
                source_type=source_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source_data: SourceData = core.arg()

        source_type: str | core.StringOut = core.arg()


@core.resource(type="aws_rolesanywhere_trust_anchor", namespace="rolesanywhere")
class TrustAnchor(core.Resource):
    """
    Amazon Resource Name (ARN) of the Trust Anchor
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether or not the Trust Anchor should be enabled.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The Trust Anchor ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Trust Anchor.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The source of trust, documented below
    """
    source: Source = core.attr(Source)

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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        source: Source,
        enabled: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TrustAnchor.Args(
                name=name,
                source=source,
                enabled=enabled,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        source: Source = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
