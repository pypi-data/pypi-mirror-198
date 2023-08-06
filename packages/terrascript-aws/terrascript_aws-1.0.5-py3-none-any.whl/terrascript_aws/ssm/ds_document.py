import terrascript.core as core


@core.data(type="aws_ssm_document", namespace="ssm")
class DsDocument(core.Data):
    """
    The ARN of the document. If the document is an AWS managed document, this value will be set to the n
    ame of the document instead.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The contents of the document.
    """
    content: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns the document in the specified format. The document format can be either `JSON`, `
    YAML` and `TEXT`. JSON is the default format.
    """
    document_format: str | core.StringOut | None = core.attr(str, default=None)

    """
    The type of the document.
    """
    document_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The document version for which you want information.
    """
    document_version: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Systems Manager document.
    """
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
