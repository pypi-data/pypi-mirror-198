import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        types: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=EndpointConfiguration.Args(
                types=types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        types: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_api_gateway_domain_name", namespace="aws_api_gateway")
class DsDomainName(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_name: str | core.StringOut = core.attr(str, computed=True)

    certificate_upload_date: str | core.StringOut = core.attr(str, computed=True)

    cloudfront_domain_name: str | core.StringOut = core.attr(str, computed=True)

    cloudfront_zone_id: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut = core.attr(str)

    endpoint_configuration: list[EndpointConfiguration] | core.ArrayOut[
        EndpointConfiguration
    ] = core.attr(EndpointConfiguration, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    regional_certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    regional_certificate_name: str | core.StringOut = core.attr(str, computed=True)

    regional_domain_name: str | core.StringOut = core.attr(str, computed=True)

    regional_zone_id: str | core.StringOut = core.attr(str, computed=True)

    security_policy: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDomainName.Args(
                domain_name=domain_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
