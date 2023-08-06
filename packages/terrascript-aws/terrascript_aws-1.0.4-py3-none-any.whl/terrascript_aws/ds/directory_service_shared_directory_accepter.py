import terrascript.core as core


@core.resource(type="aws_directory_service_shared_directory_accepter", namespace="ds")
class DirectoryServiceSharedDirectoryAccepter(core.Resource):
    """
    Identifier of the shared directory.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Method used when sharing a directory (i.e., `ORGANIZATIONS` or `HANDSHAKE`).
    """
    method: str | core.StringOut = core.attr(str, computed=True)

    """
    Message sent by the directory owner to the directory consumer to help the directory consumer adminis
    trator determine whether to approve or reject the share invitation.
    """
    notes: str | core.StringOut = core.attr(str, computed=True)

    """
    Account identifier of the directory owner.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the Managed Microsoft AD directory from the perspective of the directory owner.
    """
    owner_directory_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Identifier of the directory that is stored in the directory consumer account that corresp
    onds to the shared directory in the owner account.
    """
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
