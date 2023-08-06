import terrascript.core as core


@core.resource(type="aws_servicecatalog_provisioning_artifact", namespace="aws_servicecatalog")
class ProvisioningArtifact(core.Resource):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    active: bool | core.BoolOut | None = core.attr(bool, default=None)

    created_time: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    disable_template_validation: bool | core.BoolOut | None = core.attr(bool, default=None)

    guidance: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    product_id: str | core.StringOut = core.attr(str)

    template_physical_id: str | core.StringOut | None = core.attr(str, default=None)

    template_url: str | core.StringOut | None = core.attr(str, default=None)

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
