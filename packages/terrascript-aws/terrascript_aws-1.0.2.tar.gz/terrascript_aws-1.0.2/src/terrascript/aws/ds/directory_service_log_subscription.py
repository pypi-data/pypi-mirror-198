import terrascript.core as core


@core.resource(type="aws_directory_service_log_subscription", namespace="aws_ds")
class DirectoryServiceLogSubscription(core.Resource):

    directory_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
