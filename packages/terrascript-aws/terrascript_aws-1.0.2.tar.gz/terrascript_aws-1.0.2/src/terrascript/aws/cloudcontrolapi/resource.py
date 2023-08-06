import terrascript.core as core


@core.resource(type="aws_cloudcontrolapi_resource", namespace="aws_cloudcontrolapi")
class Resource(core.Resource):

    desired_state: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    properties: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    schema: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    type_name: str | core.StringOut = core.attr(str)

    type_version_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        desired_state: str | core.StringOut,
        type_name: str | core.StringOut,
        role_arn: str | core.StringOut | None = None,
        schema: str | core.StringOut | None = None,
        type_version_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Resource.Args(
                desired_state=desired_state,
                type_name=type_name,
                role_arn=role_arn,
                schema=schema,
                type_version_id=type_version_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        desired_state: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)

        schema: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut = core.arg()

        type_version_id: str | core.StringOut | None = core.arg(default=None)
