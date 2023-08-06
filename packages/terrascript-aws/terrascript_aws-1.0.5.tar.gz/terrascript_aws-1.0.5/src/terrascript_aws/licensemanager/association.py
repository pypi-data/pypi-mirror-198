import terrascript.core as core


@core.resource(type="aws_licensemanager_association", namespace="licensemanager")
class Association(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    license_configuration_arn: str | core.StringOut = core.attr(str)

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        license_configuration_arn: str | core.StringOut,
        resource_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Association.Args(
                license_configuration_arn=license_configuration_arn,
                resource_arn=resource_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        license_configuration_arn: str | core.StringOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()
