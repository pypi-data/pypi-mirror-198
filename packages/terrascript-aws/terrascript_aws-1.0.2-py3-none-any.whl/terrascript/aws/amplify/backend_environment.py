import terrascript.core as core


@core.resource(type="aws_amplify_backend_environment", namespace="aws_amplify")
class BackendEnvironment(core.Resource):

    app_id: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    deployment_artifacts: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    environment_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    stack_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        app_id: str | core.StringOut,
        environment_name: str | core.StringOut,
        deployment_artifacts: str | core.StringOut | None = None,
        stack_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BackendEnvironment.Args(
                app_id=app_id,
                environment_name=environment_name,
                deployment_artifacts=deployment_artifacts,
                stack_name=stack_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_id: str | core.StringOut = core.arg()

        deployment_artifacts: str | core.StringOut | None = core.arg(default=None)

        environment_name: str | core.StringOut = core.arg()

        stack_name: str | core.StringOut | None = core.arg(default=None)
