import terrascript.core as core


@core.resource(type="aws_iot_certificate", namespace="aws_iot")
class Certificate(core.Resource):

    active: bool | core.BoolOut = core.attr(bool)

    arn: str | core.StringOut = core.attr(str, computed=True)

    ca_pem: str | core.StringOut | None = core.attr(str, default=None)

    certificate_pem: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    csr: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    private_key: str | core.StringOut = core.attr(str, computed=True)

    public_key: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        active: bool | core.BoolOut,
        ca_pem: str | core.StringOut | None = None,
        certificate_pem: str | core.StringOut | None = None,
        csr: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                active=active,
                ca_pem=ca_pem,
                certificate_pem=certificate_pem,
                csr=csr,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        active: bool | core.BoolOut = core.arg()

        ca_pem: str | core.StringOut | None = core.arg(default=None)

        certificate_pem: str | core.StringOut | None = core.arg(default=None)

        csr: str | core.StringOut | None = core.arg(default=None)
