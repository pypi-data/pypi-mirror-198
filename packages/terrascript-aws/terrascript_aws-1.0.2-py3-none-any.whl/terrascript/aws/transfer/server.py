import terrascript.core as core


@core.schema
class EndpointDetails(core.Schema):

    address_allocation_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_endpoint_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    vpc_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        address_allocation_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        vpc_endpoint_id: str | core.StringOut | None = None,
        vpc_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EndpointDetails.Args(
                address_allocation_ids=address_allocation_ids,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_allocation_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        vpc_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class OnUpload(core.Schema):

    execution_role: str | core.StringOut = core.attr(str)

    workflow_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        execution_role: str | core.StringOut,
        workflow_id: str | core.StringOut,
    ):
        super().__init__(
            args=OnUpload.Args(
                execution_role=execution_role,
                workflow_id=workflow_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        execution_role: str | core.StringOut = core.arg()

        workflow_id: str | core.StringOut = core.arg()


@core.schema
class WorkflowDetails(core.Schema):

    on_upload: OnUpload | None = core.attr(OnUpload, default=None)

    def __init__(
        self,
        *,
        on_upload: OnUpload | None = None,
    ):
        super().__init__(
            args=WorkflowDetails.Args(
                on_upload=on_upload,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_upload: OnUpload | None = core.arg(default=None)


@core.resource(type="aws_transfer_server", namespace="aws_transfer")
class Server(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate: str | core.StringOut | None = core.attr(str, default=None)

    directory_id: str | core.StringOut | None = core.attr(str, default=None)

    domain: str | core.StringOut | None = core.attr(str, default=None)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    endpoint_details: EndpointDetails | None = core.attr(EndpointDetails, default=None)

    endpoint_type: str | core.StringOut | None = core.attr(str, default=None)

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    function: str | core.StringOut | None = core.attr(str, default=None)

    host_key: str | core.StringOut | None = core.attr(str, default=None)

    host_key_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_provider_type: str | core.StringOut | None = core.attr(str, default=None)

    invocation_role: str | core.StringOut | None = core.attr(str, default=None)

    logging_role: str | core.StringOut | None = core.attr(str, default=None)

    post_authentication_login_banner: str | core.StringOut | None = core.attr(str, default=None)

    pre_authentication_login_banner: str | core.StringOut | None = core.attr(str, default=None)

    protocols: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_policy_name: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: str | core.StringOut | None = core.attr(str, default=None)

    workflow_details: WorkflowDetails | None = core.attr(WorkflowDetails, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate: str | core.StringOut | None = None,
        directory_id: str | core.StringOut | None = None,
        domain: str | core.StringOut | None = None,
        endpoint_details: EndpointDetails | None = None,
        endpoint_type: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        function: str | core.StringOut | None = None,
        host_key: str | core.StringOut | None = None,
        identity_provider_type: str | core.StringOut | None = None,
        invocation_role: str | core.StringOut | None = None,
        logging_role: str | core.StringOut | None = None,
        post_authentication_login_banner: str | core.StringOut | None = None,
        pre_authentication_login_banner: str | core.StringOut | None = None,
        protocols: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_policy_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        url: str | core.StringOut | None = None,
        workflow_details: WorkflowDetails | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Server.Args(
                certificate=certificate,
                directory_id=directory_id,
                domain=domain,
                endpoint_details=endpoint_details,
                endpoint_type=endpoint_type,
                force_destroy=force_destroy,
                function=function,
                host_key=host_key,
                identity_provider_type=identity_provider_type,
                invocation_role=invocation_role,
                logging_role=logging_role,
                post_authentication_login_banner=post_authentication_login_banner,
                pre_authentication_login_banner=pre_authentication_login_banner,
                protocols=protocols,
                security_policy_name=security_policy_name,
                tags=tags,
                tags_all=tags_all,
                url=url,
                workflow_details=workflow_details,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate: str | core.StringOut | None = core.arg(default=None)

        directory_id: str | core.StringOut | None = core.arg(default=None)

        domain: str | core.StringOut | None = core.arg(default=None)

        endpoint_details: EndpointDetails | None = core.arg(default=None)

        endpoint_type: str | core.StringOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        function: str | core.StringOut | None = core.arg(default=None)

        host_key: str | core.StringOut | None = core.arg(default=None)

        identity_provider_type: str | core.StringOut | None = core.arg(default=None)

        invocation_role: str | core.StringOut | None = core.arg(default=None)

        logging_role: str | core.StringOut | None = core.arg(default=None)

        post_authentication_login_banner: str | core.StringOut | None = core.arg(default=None)

        pre_authentication_login_banner: str | core.StringOut | None = core.arg(default=None)

        protocols: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        security_policy_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        url: str | core.StringOut | None = core.arg(default=None)

        workflow_details: WorkflowDetails | None = core.arg(default=None)
