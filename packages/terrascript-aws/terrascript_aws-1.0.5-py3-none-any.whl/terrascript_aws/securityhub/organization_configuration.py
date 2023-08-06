import terrascript.core as core


@core.resource(type="aws_securityhub_organization_configuration", namespace="securityhub")
class OrganizationConfiguration(core.Resource):

    auto_enable: bool | core.BoolOut = core.attr(bool)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        auto_enable: bool | core.BoolOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationConfiguration.Args(
                auto_enable=auto_enable,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_enable: bool | core.BoolOut = core.arg()
