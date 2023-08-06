import terrascript.core as core


@core.data(type="aws_codecommit_repository", namespace="aws_codecommit")
class DsRepository(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    clone_url_http: str | core.StringOut = core.attr(str, computed=True)

    clone_url_ssh: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    repository_id: str | core.StringOut = core.attr(str, computed=True)

    repository_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        repository_name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsRepository.Args(
                repository_name=repository_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_name: str | core.StringOut = core.arg()
