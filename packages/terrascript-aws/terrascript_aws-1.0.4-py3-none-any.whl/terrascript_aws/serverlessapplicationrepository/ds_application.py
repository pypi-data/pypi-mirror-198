import terrascript.core as core


@core.data(
    type="aws_serverlessapplicationrepository_application",
    namespace="serverlessapplicationrepository",
)
class DsApplication(core.Data):
    """
    (Required) The ARN of the application.
    """

    application_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the application.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of capabilities describing the permissions needed to deploy the application.
    """
    required_capabilities: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The requested version of the application. By default, retrieves the latest version.
    """
    semantic_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A URL pointing to the source code of the application version.
    """
    source_code_url: str | core.StringOut = core.attr(str, computed=True)

    """
    A URL pointing to the Cloud Formation template for the application version.
    """
    template_url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        application_id: str | core.StringOut,
        semantic_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsApplication.Args(
                application_id=application_id,
                semantic_version=semantic_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_id: str | core.StringOut = core.arg()

        semantic_version: str | core.StringOut | None = core.arg(default=None)
