import terrascript.core as core


@core.resource(type="aws_servicecatalog_provisioning_artifact", namespace="servicecatalog")
class ProvisioningArtifact(core.Resource):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). The default
    value is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether the product version is active. Inactive provisioning artifacts are invisible to e
    nd users. End users cannot launch or update a provisioned product from an inactive provisioning arti
    fact. Default is `true`.
    """
    active: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Time when the provisioning artifact was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the provisioning artifact (i.e., version), including how it differs from t
    he previous provisioning artifact.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Whether AWS Service Catalog stops validating the specified provisioning artifact template
    even if it is invalid.
    """
    disable_template_validation: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Information set by the administrator to provide guidance to end users about which provisi
    oning artifacts to use. Valid values are `DEFAULT` and `DEPRECATED`. The default is `DEFAULT`. Users
    are able to make updates to a provisioned product of a deprecated version but cannot launch new pro
    visioned products using a deprecated version.
    """
    guidance: str | core.StringOut | None = core.attr(str, default=None)

    """
    Provisioning Artifact identifier and product identifier separated by a colon.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Name of the provisioning artifact (for example, `v1`, `v2beta`). No spaces are allowed.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Identifier of the product.
    """
    product_id: str | core.StringOut = core.attr(str)

    """
    (Required if `template_url` is not provided) Template source as the physical ID of the resource that
    contains the template. Currently only supports CloudFormation stack ARN. Specify the physical ID as
    arn:[partition]:cloudformation:[region]:[account ID]:stack/[stack name]/[resource ID]`.
    """
    template_physical_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required if `template_physical_id` is not provided) Template source as URL of the CloudFormation te
    mplate in Amazon S3.
    """
    template_url: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Type of provisioning artifact. Valid values: `CLOUD_FORMATION_TEMPLATE`, `MARKETPLACE_AMI
    , `MARKETPLACE_CAR` (Marketplace Clusters and AWS Resources).
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        product_id: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        active: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        disable_template_validation: bool | core.BoolOut | None = None,
        guidance: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        template_physical_id: str | core.StringOut | None = None,
        template_url: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProvisioningArtifact.Args(
                product_id=product_id,
                accept_language=accept_language,
                active=active,
                description=description,
                disable_template_validation=disable_template_validation,
                guidance=guidance,
                name=name,
                template_physical_id=template_physical_id,
                template_url=template_url,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        active: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        disable_template_validation: bool | core.BoolOut | None = core.arg(default=None)

        guidance: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        product_id: str | core.StringOut = core.arg()

        template_physical_id: str | core.StringOut | None = core.arg(default=None)

        template_url: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
