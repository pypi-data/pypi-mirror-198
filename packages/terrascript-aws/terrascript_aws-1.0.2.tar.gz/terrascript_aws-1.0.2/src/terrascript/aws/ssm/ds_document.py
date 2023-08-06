import terrascript.core as core


@core.data(type="aws_ssm_document", namespace="aws_ssm")
class DsDocument(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    content: str | core.StringOut = core.attr(str, computed=True)

    document_format: str | core.StringOut | None = core.attr(str, default=None)

    document_type: str | core.StringOut = core.attr(str, computed=True)

    document_version: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        document_format: str | core.StringOut | None = None,
        document_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDocument.Args(
                name=name,
                document_format=document_format,
                document_version=document_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        document_format: str | core.StringOut | None = core.arg(default=None)

        document_version: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
