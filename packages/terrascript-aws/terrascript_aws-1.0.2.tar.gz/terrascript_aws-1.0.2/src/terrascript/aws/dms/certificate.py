import terrascript.core as core


@core.resource(type="aws_dms_certificate", namespace="aws_dms")
class Certificate(core.Resource):

    certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_id: str | core.StringOut = core.attr(str)

    certificate_pem: str | core.StringOut | None = core.attr(str, default=None)

    certificate_wallet: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_id: str | core.StringOut,
        certificate_pem: str | core.StringOut | None = None,
        certificate_wallet: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                certificate_id=certificate_id,
                certificate_pem=certificate_pem,
                certificate_wallet=certificate_wallet,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_id: str | core.StringOut = core.arg()

        certificate_pem: str | core.StringOut | None = core.arg(default=None)

        certificate_wallet: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
