import terrascript.core as core


@core.schema
class ProvisioningArtifactParameters(core.Schema):

    description: str | core.StringOut | None = core.attr(str, default=None)

    disable_template_validation: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    template_physical_id: str | core.StringOut | None = core.attr(str, default=None)

    template_url: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        description: str | core.StringOut | None = None,
        disable_template_validation: bool | core.BoolOut | None = None,
        name: str | core.StringOut | None = None,
        template_physical_id: str | core.StringOut | None = None,
        template_url: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProvisioningArtifactParameters.Args(
                description=description,
                disable_template_validation=disable_template_validation,
                name=name,
                template_physical_id=template_physical_id,
                template_url=template_url,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut | None = core.arg(default=None)

        disable_template_validation: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        template_physical_id: str | core.StringOut | None = core.arg(default=None)

        template_url: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_servicecatalog_product", namespace="servicecatalog")
class Product(core.Resource):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default val
    ue is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    ARN of the product.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Time when the product was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the product.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Distributor (i.e., vendor) of the product.
    """
    distributor: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Whether the product has a default path. If the product does not have a default path, call `ListLaunc
    hPaths` to disambiguate between paths.  Otherwise, `ListLaunchPaths` is not required, and the output
    of ProductViewSummary can be used directly with `DescribeProvisioningParameters`.
    """
    has_default_path: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Product ID. For example, `prod-dnigbtea24ste`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the product.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Owner of the product.
    """
    owner: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block for provisioning artifact (i.e., version) parameters. Detailed below.
    """
    provisioning_artifact_parameters: ProvisioningArtifactParameters = core.attr(
        ProvisioningArtifactParameters
    )

    """
    Status of the product.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Support information about the product.
    """
    support_description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Contact email for product support.
    """
    support_email: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Contact URL for product support.
    """
    support_url: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Tags to apply to the product. If configured with a provider [`default_tags` configuration
    block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration
    block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Required) Type of product. Valid values are `CLOUD_FORMATION_TEMPLATE`, `MARKETPLACE`.
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        owner: str | core.StringOut,
        provisioning_artifact_parameters: ProvisioningArtifactParameters,
        type: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        distributor: str | core.StringOut | None = None,
        support_description: str | core.StringOut | None = None,
        support_email: str | core.StringOut | None = None,
        support_url: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Product.Args(
                name=name,
                owner=owner,
                provisioning_artifact_parameters=provisioning_artifact_parameters,
                type=type,
                accept_language=accept_language,
                description=description,
                distributor=distributor,
                support_description=support_description,
                support_email=support_email,
                support_url=support_url,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        distributor: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        owner: str | core.StringOut = core.arg()

        provisioning_artifact_parameters: ProvisioningArtifactParameters = core.arg()

        support_description: str | core.StringOut | None = core.arg(default=None)

        support_email: str | core.StringOut | None = core.arg(default=None)

        support_url: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
