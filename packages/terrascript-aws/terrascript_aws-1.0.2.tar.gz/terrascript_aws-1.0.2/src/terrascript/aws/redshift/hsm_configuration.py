import terrascript.core as core


@core.resource(type="aws_redshift_hsm_configuration", namespace="aws_redshift")
class HsmConfiguration(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str)

    hsm_configuration_identifier: str | core.StringOut = core.attr(str)

    hsm_ip_address: str | core.StringOut = core.attr(str)

    hsm_partition_name: str | core.StringOut = core.attr(str)

    hsm_partition_password: str | core.StringOut = core.attr(str)

    hsm_server_public_certificate: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
        description: str | core.StringOut,
        hsm_configuration_identifier: str | core.StringOut,
        hsm_ip_address: str | core.StringOut,
        hsm_partition_name: str | core.StringOut,
        hsm_partition_password: str | core.StringOut,
        hsm_server_public_certificate: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=HsmConfiguration.Args(
                description=description,
                hsm_configuration_identifier=hsm_configuration_identifier,
                hsm_ip_address=hsm_ip_address,
                hsm_partition_name=hsm_partition_name,
                hsm_partition_password=hsm_partition_password,
                hsm_server_public_certificate=hsm_server_public_certificate,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut = core.arg()

        hsm_configuration_identifier: str | core.StringOut = core.arg()

        hsm_ip_address: str | core.StringOut = core.arg()

        hsm_partition_name: str | core.StringOut = core.arg()

        hsm_partition_password: str | core.StringOut = core.arg()

        hsm_server_public_certificate: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
