import terrascript.core as core


@core.resource(type="aws_directory_service_log_subscription", namespace="ds")
class DirectoryServiceLogSubscription(core.Resource):
    """
    (Required) The id of directory.
    """

    directory_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the cloudwatch log group to which the logs should be published. The log group sho
    uld be already created and the directory service principal should be provided with required permissi
    on to create stream and publish logs. Changing this value would delete the current subscription and
    create a new one. A directory can only have one log subscription at a time.
    """
    log_group_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: str | core.StringOut,
        log_group_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceLogSubscription.Args(
                directory_id=directory_id,
                log_group_name=log_group_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_id: str | core.StringOut = core.arg()

        log_group_name: str | core.StringOut = core.arg()
