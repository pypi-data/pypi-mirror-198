import terrascript.core as core


@core.resource(type="aws_directory_service_shared_directory_accepter", namespace="ds")
class DirectoryServiceSharedDirectoryAccepter(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    method: str | core.StringOut = core.attr(str, computed=True)

    notes: str | core.StringOut = core.attr(str, computed=True)

    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    owner_directory_id: str | core.StringOut = core.attr(str, computed=True)

    shared_directory_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        shared_directory_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceSharedDirectoryAccepter.Args(
                shared_directory_id=shared_directory_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        shared_directory_id: str | core.StringOut = core.arg()
