import terrascript.core as core


@core.data(
    type="aws_serverlessapplicationrepository_application",
    namespace="aws_serverlessapplicationrepository",
)
class DsApplication(core.Data):

    application_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    required_capabilities: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    semantic_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    source_code_url: str | core.StringOut = core.attr(str, computed=True)

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
