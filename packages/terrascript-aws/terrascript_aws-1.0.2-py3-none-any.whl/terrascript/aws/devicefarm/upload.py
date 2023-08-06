import terrascript.core as core


@core.resource(type="aws_devicefarm_upload", namespace="aws_devicefarm")
class Upload(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    category: str | core.StringOut = core.attr(str, computed=True)

    content_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    metadata: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    project_arn: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        project_arn: str | core.StringOut,
        type: str | core.StringOut,
        content_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Upload.Args(
                name=name,
                project_arn=project_arn,
                type=type,
                content_type=content_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_type: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        project_arn: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()
