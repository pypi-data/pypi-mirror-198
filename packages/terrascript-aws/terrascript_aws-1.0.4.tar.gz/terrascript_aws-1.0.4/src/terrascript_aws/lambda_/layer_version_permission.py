import terrascript.core as core


@core.resource(type="aws_lambda_layer_version_permission", namespace="lambda_")
class LayerVersionPermission(core.Resource):
    """
    (Required) Action, which will be allowed. `lambda:GetLayerVersion` value is suggested by AWS documan
    tation.
    """

    action: str | core.StringOut = core.attr(str)

    """
    The `layer_name` and `version_number`, separated by a comma (`,`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    layer_name: str | core.StringOut = core.attr(str)

    """
    (Optional) An identifier of AWS Organization, which should be able to use your Lambda Layer. `princi
    pal` should be equal to `*` if `organization_id` provided.
    """
    organization_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    Full Lambda Layer Permission policy.
    """
    policy: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) AWS account ID which should be able to use your Lambda Layer. `*` can be used here, if yo
    u want to share your Lambda Layer widely.
    """
    principal: str | core.StringOut = core.attr(str)

    """
    A unique identifier for the current revision of the policy.
    """
    revision_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of Lambda Layer Permission, for example `dev-account` - human readable note abou
    t what is this permission for.
    """
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
