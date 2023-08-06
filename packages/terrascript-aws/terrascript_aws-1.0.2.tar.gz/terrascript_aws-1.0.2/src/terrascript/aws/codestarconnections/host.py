import terrascript.core as core


@core.schema
class VpcConfiguration(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tls_certificate: str | core.StringOut | None = core.attr(str, default=None)

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
        tls_certificate: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=VpcConfiguration.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
                tls_certificate=tls_certificate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tls_certificate: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()


@core.resource(type="aws_codestarconnections_host", namespace="aws_codestarconnections")
class Host(core.Resource):
    """
    The CodeStar Host ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The CodeStar Host ARN.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the host to be created. The name must be unique in the calling AWS account.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The endpoint of the infrastructure to be represented by the host after it is created.
    """
    provider_endpoint: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the external provider where your third-party code repository is configured.
    """
    provider_type: str | core.StringOut = core.attr(str)

    """
    The CodeStar Host status. Possible values are `PENDING`, `AVAILABLE`, `VPC_CONFIG_DELETING`, `VPC_CO
    NFIG_INITIALIZING`, and `VPC_CONFIG_FAILED_INITIALIZATION`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The VPC configuration to be provisioned for the host. A VPC must be configured, and the i
    nfrastructure to be represented by the host must already be connected to the VPC.
    """
    vpc_configuration: VpcConfiguration | None = core.attr(VpcConfiguration, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        provider_endpoint: str | core.StringOut,
        provider_type: str | core.StringOut,
        vpc_configuration: VpcConfiguration | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Host.Args(
                name=name,
                provider_endpoint=provider_endpoint,
                provider_type=provider_type,
                vpc_configuration=vpc_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        provider_endpoint: str | core.StringOut = core.arg()

        provider_type: str | core.StringOut = core.arg()

        vpc_configuration: VpcConfiguration | None = core.arg(default=None)
