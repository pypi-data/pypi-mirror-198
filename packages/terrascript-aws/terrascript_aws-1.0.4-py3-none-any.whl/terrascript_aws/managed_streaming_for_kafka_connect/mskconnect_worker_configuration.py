import terrascript.core as core


@core.resource(
    type="aws_mskconnect_worker_configuration", namespace="managed_streaming_for_kafka_connect"
)
class MskconnectWorkerConfiguration(core.Resource):
    """
    the Amazon Resource Name (ARN) of the worker configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A summary description of the worker configuration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    an ID of the latest successfully created revision of the worker configuration.
    """
    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The name of the worker configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Contents of connect-distributed.properties file. The value can be either base64 encoded o
    r in raw format.
    """
    properties_file_content: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        properties_file_content: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskconnectWorkerConfiguration.Args(
                name=name,
                properties_file_content=properties_file_content,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        properties_file_content: str | core.StringOut = core.arg()
