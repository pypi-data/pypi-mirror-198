import terrascript.core as core


@core.data(type="aws_codecommit_repository", namespace="codecommit")
class DsRepository(core.Data):
    """
    The ARN of the repository
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The URL to use for cloning the repository over HTTPS.
    """
    clone_url_http: str | core.StringOut = core.attr(str, computed=True)

    """
    The URL to use for cloning the repository over SSH.
    """
    clone_url_ssh: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the repository
    """
    repository_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for the repository. This needs to be less than 100 characters.
    """
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
