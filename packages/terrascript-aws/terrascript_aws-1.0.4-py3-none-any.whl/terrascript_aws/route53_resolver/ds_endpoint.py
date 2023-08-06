import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_route53_resolver_endpoint", namespace="route53_resolver")
class DsEndpoint(core.Data):
    """
    The computed ARN of the Route53 Resolver Endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The direction of the queries to or from the Resolver Endpoint .
    """
    direction: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more name/value pairs to use as filters. There are
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of IPaddresses that have been associated with the Resolver Endpoint.
    """
    ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the Route53 Resolver Endpoint.
    """
    resolver_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The current status of the Resolver Endpoint.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the Host VPC that the Resolver Endpoint resides in.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        resolver_endpoint_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEndpoint.Args(
                filter=filter,
                resolver_endpoint_id=resolver_endpoint_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        resolver_endpoint_id: str | core.StringOut | None = core.arg(default=None)
