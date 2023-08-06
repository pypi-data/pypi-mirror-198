import terrascript.core as core


@core.resource(type="aws_worklink_website_certificate_authority_association", namespace="worklink")
class WebsiteCertificateAuthorityAssociation(core.Resource):
    """
    (Required, ForceNew) The root certificate of the Certificate Authority.
    """

    certificate: str | core.StringOut = core.attr(str)

    """
    (Optional, ForceNew) The certificate name to display.
    """
    display_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required, ForceNew) The ARN of the fleet.
    """
    fleet_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A unique identifier for the Certificate Authority.
    """
    website_ca_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate: str | core.StringOut,
        fleet_arn: str | core.StringOut,
        display_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=WebsiteCertificateAuthorityAssociation.Args(
                certificate=certificate,
                fleet_arn=fleet_arn,
                display_name=display_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate: str | core.StringOut = core.arg()

        display_name: str | core.StringOut | None = core.arg(default=None)

        fleet_arn: str | core.StringOut = core.arg()
