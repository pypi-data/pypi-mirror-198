import terrascript.core as core


@core.schema
class ProvisioningParameter(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProvisioningParameter.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ServiceCatalogProvisioningDetails(core.Schema):

    path_id: str | core.StringOut | None = core.attr(str, default=None)

    product_id: str | core.StringOut = core.attr(str)

    provisioning_artifact_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    provisioning_parameter: list[ProvisioningParameter] | core.ArrayOut[
        ProvisioningParameter
    ] | None = core.attr(ProvisioningParameter, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        product_id: str | core.StringOut,
        path_id: str | core.StringOut | None = None,
        provisioning_artifact_id: str | core.StringOut | None = None,
        provisioning_parameter: list[ProvisioningParameter]
        | core.ArrayOut[ProvisioningParameter]
        | None = None,
    ):
        super().__init__(
            args=ServiceCatalogProvisioningDetails.Args(
                product_id=product_id,
                path_id=path_id,
                provisioning_artifact_id=provisioning_artifact_id,
                provisioning_parameter=provisioning_parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path_id: str | core.StringOut | None = core.arg(default=None)

        product_id: str | core.StringOut = core.arg()

        provisioning_artifact_id: str | core.StringOut | None = core.arg(default=None)

        provisioning_parameter: list[ProvisioningParameter] | core.ArrayOut[
            ProvisioningParameter
        ] | None = core.arg(default=None)


@core.resource(type="aws_sagemaker_project", namespace="sagemaker")
class Project(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    project_description: str | core.StringOut | None = core.attr(str, default=None)

    project_id: str | core.StringOut = core.attr(str, computed=True)

    project_name: str | core.StringOut = core.attr(str)

    service_catalog_provisioning_details: ServiceCatalogProvisioningDetails = core.attr(
        ServiceCatalogProvisioningDetails
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        project_name: str | core.StringOut,
        service_catalog_provisioning_details: ServiceCatalogProvisioningDetails,
        project_description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Project.Args(
                project_name=project_name,
                service_catalog_provisioning_details=service_catalog_provisioning_details,
                project_description=project_description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        project_description: str | core.StringOut | None = core.arg(default=None)

        project_name: str | core.StringOut = core.arg()

        service_catalog_provisioning_details: ServiceCatalogProvisioningDetails = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
