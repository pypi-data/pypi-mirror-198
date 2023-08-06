import terrascript.core as core


@core.resource(type="aws_lambda_layer_version_permission", namespace="aws_lambda_")
class LayerVersionPermission(core.Resource):

    action: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    layer_name: str | core.StringOut = core.attr(str)

    organization_id: str | core.StringOut | None = core.attr(str, default=None)

    policy: str | core.StringOut = core.attr(str, computed=True)

    principal: str | core.StringOut = core.attr(str)

    revision_id: str | core.StringOut = core.attr(str, computed=True)

    statement_id: str | core.StringOut = core.attr(str)

    version_number: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        action: str | core.StringOut,
        layer_name: str | core.StringOut,
        principal: str | core.StringOut,
        statement_id: str | core.StringOut,
        version_number: int | core.IntOut,
        organization_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LayerVersionPermission.Args(
                action=action,
                layer_name=layer_name,
                principal=principal,
                statement_id=statement_id,
                version_number=version_number,
                organization_id=organization_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: str | core.StringOut = core.arg()

        layer_name: str | core.StringOut = core.arg()

        organization_id: str | core.StringOut | None = core.arg(default=None)

        principal: str | core.StringOut = core.arg()

        statement_id: str | core.StringOut = core.arg()

        version_number: int | core.IntOut = core.arg()
