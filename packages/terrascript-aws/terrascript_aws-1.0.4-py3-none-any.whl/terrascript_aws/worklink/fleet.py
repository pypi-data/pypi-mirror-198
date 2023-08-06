import terrascript.core as core


@core.schema
class Network(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=Network.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class IdentityProvider(core.Schema):

    saml_metadata: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        saml_metadata: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=IdentityProvider.Args(
                saml_metadata=saml_metadata,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        saml_metadata: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_worklink_fleet", namespace="worklink")
class Fleet(core.Resource):
    """
    The ARN of the created WorkLink Fleet.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN of the Amazon Kinesis data stream that receives the audit events. Kinesis data st
    ream name must begin with `"AmazonWorkLink-"`.
    """
    audit_stream_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The identifier used by users to sign in to the Amazon WorkLink app.
    """
    company_code: str | core.StringOut = core.attr(str, computed=True)

    """
    The time that the fleet was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The certificate chain, including intermediate certificates and the root certificate autho
    rity certificate used to issue device certificates.
    """
    device_ca_certificate: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the fleet.
    """
    display_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN of the created WorkLink Fleet.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Provide this to allow manage the identity provider configuration for the fleet. Fields do
    cumented below.
    """
    identity_provider: IdentityProvider | None = core.attr(IdentityProvider, default=None)

    """
    The time that the fleet was last updated.
    """
    last_updated_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A region-unique name for the AMI.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Provide this to allow manage the company network configuration for the fleet. Fields docu
    mented below.
    """
    network: Network | None = core.attr(Network, default=None)

    """
    (Optional) The option to optimize for better performance by routing traffic through the closest AWS
    Region to users, which may be outside of your home Region. Defaults to `true`.
    """
    optimize_for_end_user_location: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        audit_stream_arn: str | core.StringOut | None = None,
        device_ca_certificate: str | core.StringOut | None = None,
        display_name: str | core.StringOut | None = None,
        identity_provider: IdentityProvider | None = None,
        network: Network | None = None,
        optimize_for_end_user_location: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Fleet.Args(
                name=name,
                audit_stream_arn=audit_stream_arn,
                device_ca_certificate=device_ca_certificate,
                display_name=display_name,
                identity_provider=identity_provider,
                network=network,
                optimize_for_end_user_location=optimize_for_end_user_location,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        audit_stream_arn: str | core.StringOut | None = core.arg(default=None)

        device_ca_certificate: str | core.StringOut | None = core.arg(default=None)

        display_name: str | core.StringOut | None = core.arg(default=None)

        identity_provider: IdentityProvider | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        network: Network | None = core.arg(default=None)

        optimize_for_end_user_location: bool | core.BoolOut | None = core.arg(default=None)
