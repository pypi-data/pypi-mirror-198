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


@core.resource(type="aws_transfer_server", namespace="transfer")
class Server(core.Resource):
    """
    Amazon Resource Name (ARN) of Transfer Server
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate. This is
    required when `protocols` is set to `FTPS`
    """
    certificate: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The directory service ID of the directory service you want to connect to with an `identit
    y_provider_type` of `AWS_DIRECTORY_SERVICE`.
    """
    directory_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The domain of the storage system that is used for file transfers. Valid values are: `S3`
    and `EFS`. The default value is `S3`.
    """
    domain: str | core.StringOut | None = core.attr(str, default=None)

    """
    The endpoint of the Transfer Server (e.g., `s-12345678.server.transfer.REGION.amazonaws.com`)
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The virtual private cloud (VPC) endpoint settings that you want to configure for your SFT
    P server. Fields documented below.
    """
    endpoint_details: EndpointDetails | None = core.attr(EndpointDetails, default=None)

    """
    (Optional) The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC`
    (or `VPC_ENDPOINT`), your SFTP server isn't accessible over the public internet. If you want to con
    nect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
    """
    endpoint_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A boolean that indicates all users associated with the server should be deleted so that t
    he Server can be destroyed without error. The default value is `false`. This option only applies to
    servers configured with a `SERVICE_MANAGED` `identity_provider_type`.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The ARN for a lambda function to use for the Identity provider.
    """
    function: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) RSA private key (e.g., as generated by the `ssh-keygen -N "" -m PEM -f my-new-server-key`
    command).
    """
    host_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    This value contains the message-digest algorithm (MD5) hash of the server's host key. This value is
    equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
    """
    host_key_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The mode of authentication enabled for this service. The default value is `SERVICE_MANAGE
    D`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` ind
    icates that user authentication requires a call to an API Gateway endpoint URL provided by you to in
    tegrate an identity provider of your choice. Using `AWS_DIRECTORY_SERVICE` will allow for authentica
    tion against AWS Managed Active Directory or Microsoft Active Directory in your on-premises environm
    ent, or in AWS using AD Connectors. Use the `AWS_LAMBDA` value to directly use a Lambda function as
    your identity provider. If you choose this value, you must specify the ARN for the lambda function i
    n the `function` argument.
    """
    identity_provider_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an
    identity_provider_type` of `API_GATEWAY`.
    """
    invocation_role: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP user
    s’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
    """
    logging_role: str | core.StringOut | None = core.attr(str, default=None)

    post_authentication_login_banner: str | core.StringOut | None = core.attr(str, default=None)

    pre_authentication_login_banner: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the file transfer protocol or protocols over which your file transfer protocol
    client can connect to your server's endpoint. This defaults to `SFTP` . The available protocols are:
    """
    protocols: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Specifies the name of the security policy that is attached to the server. Possible values
    are `TransferSecurityPolicy-2018-11`, `TransferSecurityPolicy-2020-06`, `TransferSecurityPolicy-FIP
    S-2020-06` and `TransferSecurityPolicy-2022-03`. Default value is: `TransferSecurityPolicy-2018-11`.
    """
    security_policy_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) - URL of the service endpoint used to authenticate users with an `identity_provider_type`
    of `API_GATEWAY`.
    """
    url: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the workflow details. See Workflow Details below.
    """
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
