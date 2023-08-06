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


@core.resource(type="aws_worklink_fleet", namespace="aws_worklink")
class Fleet(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    audit_stream_arn: str | core.StringOut | None = core.attr(str, default=None)

    company_code: str | core.StringOut = core.attr(str, computed=True)

    created_time: str | core.StringOut = core.attr(str, computed=True)

    device_ca_certificate: str | core.StringOut | None = core.attr(str, default=None)

    display_name: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_provider: IdentityProvider | None = core.attr(IdentityProvider, default=None)

    last_updated_time: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    network: Network | None = core.attr(Network, default=None)

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
