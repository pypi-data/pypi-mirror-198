import terrascript.core as core


@core.data(type="aws_iam_server_certificate", namespace="aws_iam")
class DsServerCertificate(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_body: str | core.StringOut = core.attr(str, computed=True)

    certificate_chain: str | core.StringOut = core.attr(str, computed=True)

    expiration_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    latest: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    path: str | core.StringOut = core.attr(str, computed=True)

    path_prefix: str | core.StringOut | None = core.attr(str, default=None)

    upload_date: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        latest: bool | core.BoolOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        path_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServerCertificate.Args(
                latest=latest,
                name=name,
                name_prefix=name_prefix,
                path_prefix=path_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        latest: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        path_prefix: str | core.StringOut | None = core.arg(default=None)
