import terrascript.core as core


@core.resource(type="aws_iam_signing_certificate", namespace="iam")
class SigningCertificate(core.Resource):

    certificate_body: str | core.StringOut = core.attr(str)

    """
    The ID for the signing certificate.
    """
    certificate_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The `certificate_id:user_name`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut | None = core.attr(str, default=None)

    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_body: str | core.StringOut,
        user_name: str | core.StringOut,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SigningCertificate.Args(
                certificate_body=certificate_body,
                user_name=user_name,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_body: str | core.StringOut = core.arg()

        status: str | core.StringOut | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()
