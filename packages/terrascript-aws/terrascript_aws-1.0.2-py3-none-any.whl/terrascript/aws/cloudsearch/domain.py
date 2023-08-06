import terrascript.core as core


@core.schema
class EndpointOptions(core.Schema):

    enforce_https: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    tls_security_policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        enforce_https: bool | core.BoolOut | None = None,
        tls_security_policy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EndpointOptions.Args(
                enforce_https=enforce_https,
                tls_security_policy=tls_security_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enforce_https: bool | core.BoolOut | None = core.arg(default=None)

        tls_security_policy: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ScalingParameters(core.Schema):

    desired_instance_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    desired_partition_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    desired_replication_count: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        desired_instance_type: str | core.StringOut | None = None,
        desired_partition_count: int | core.IntOut | None = None,
        desired_replication_count: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ScalingParameters.Args(
                desired_instance_type=desired_instance_type,
                desired_partition_count=desired_partition_count,
                desired_replication_count=desired_replication_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        desired_instance_type: str | core.StringOut | None = core.arg(default=None)

        desired_partition_count: int | core.IntOut | None = core.arg(default=None)

        desired_replication_count: int | core.IntOut | None = core.arg(default=None)


@core.schema
class IndexField(core.Schema):

    analysis_scheme: str | core.StringOut | None = core.attr(str, default=None)

    default_value: str | core.StringOut | None = core.attr(str, default=None)

    facet: bool | core.BoolOut | None = core.attr(bool, default=None)

    highlight: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut = core.attr(str)

    return_: bool | core.BoolOut | None = core.attr(bool, default=None, alias="return")

    search: bool | core.BoolOut | None = core.attr(bool, default=None)

    sort: bool | core.BoolOut | None = core.attr(bool, default=None)

    source_fields: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
        analysis_scheme: str | core.StringOut | None = None,
        default_value: str | core.StringOut | None = None,
        facet: bool | core.BoolOut | None = None,
        highlight: bool | core.BoolOut | None = None,
        return_: bool | core.BoolOut | None = None,
        search: bool | core.BoolOut | None = None,
        sort: bool | core.BoolOut | None = None,
        source_fields: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=IndexField.Args(
                name=name,
                type=type,
                analysis_scheme=analysis_scheme,
                default_value=default_value,
                facet=facet,
                highlight=highlight,
                return_=return_,
                search=search,
                sort=sort,
                source_fields=source_fields,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        analysis_scheme: str | core.StringOut | None = core.arg(default=None)

        default_value: str | core.StringOut | None = core.arg(default=None)

        facet: bool | core.BoolOut | None = core.arg(default=None)

        highlight: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        return_: bool | core.BoolOut | None = core.arg(default=None)

        search: bool | core.BoolOut | None = core.arg(default=None)

        sort: bool | core.BoolOut | None = core.arg(default=None)

        source_fields: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_cloudsearch_domain", namespace="aws_cloudsearch")
class Domain(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    document_service_endpoint: str | core.StringOut = core.attr(str, computed=True)

    domain_id: str | core.StringOut = core.attr(str, computed=True)

    endpoint_options: EndpointOptions | None = core.attr(
        EndpointOptions, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    index_field: list[IndexField] | core.ArrayOut[IndexField] | None = core.attr(
        IndexField, default=None, kind=core.Kind.array
    )

    multi_az: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    scaling_parameters: ScalingParameters | None = core.attr(
        ScalingParameters, default=None, computed=True
    )

    search_service_endpoint: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        endpoint_options: EndpointOptions | None = None,
        index_field: list[IndexField] | core.ArrayOut[IndexField] | None = None,
        multi_az: bool | core.BoolOut | None = None,
        scaling_parameters: ScalingParameters | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Domain.Args(
                name=name,
                endpoint_options=endpoint_options,
                index_field=index_field,
                multi_az=multi_az,
                scaling_parameters=scaling_parameters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        endpoint_options: EndpointOptions | None = core.arg(default=None)

        index_field: list[IndexField] | core.ArrayOut[IndexField] | None = core.arg(default=None)

        multi_az: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        scaling_parameters: ScalingParameters | None = core.arg(default=None)
